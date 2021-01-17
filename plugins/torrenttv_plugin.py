'''
ttv.run Playlist Downloader Plugin
http://ip:port/ttvplaylist
'''
import re
import logging
import urllib2
import time
import gevent
from modules.PluginInterface import AceProxyPlugin
from modules.PlaylistGenerator import PlaylistGenerator
import config.torrenttv as config


class Torrenttv(AceProxyPlugin):

    # ttvplaylist handler is obsolete
    handlers = ('torrenttv', 'ttvplaylist')

    logger = logging.getLogger('plugin_torrenttv')
    playlist = None
    playlisttime = None

    def __init__(self, AceConfig, AceStuff):
        if config.updateevery:
            self.downloadPlaylist()
            gevent.spawn(self.playlistTimedDownloader)

    def playlistTimedDownloader(self):
        while True:
            gevent.sleep(config.updateevery * 60)
            self.downloadPlaylist()

    def downloadPlaylist(self):
        try:
            Torrenttv.logger.debug('Trying to download playlist')
            req = urllib2.Request(config.url, headers={'User-Agent' : "Magic Browser"})
            Torrenttv.playlist = urllib2.urlopen(
                req, timeout=10).read()
            Torrenttv.playlisttime = int(time.time())
        except:
            Torrenttv.logger.error("Can't download playlist!")
            return False

        return True

    def handle(self, connection):
        # 30 minutes cache
        if not Torrenttv.playlist or (int(time.time()) - Torrenttv.playlisttime > 30 * 60):
            if not self.downloadPlaylist():
                connection.dieWithError()
                return

        hostport = connection.headers['Host']

        connection.send_response(200)
        connection.send_header('Content-Type', 'application/x-mpegurl')
        connection.end_headers()

        # Match playlist with regexp
        matches = re.finditer(r',(?P<name>\S.+) \((?P<group>.+)\)\n(?P<url>^.+$)',
                              Torrenttv.playlist, re.MULTILINE)
        
        add_ts = False
        try:
            if connection.splittedpath[2].lower() == 'ts':
                add_ts = True
        except:
            pass
                

        playlistgen = PlaylistGenerator()
        for match in matches:
            itemdict = match.groupdict()
            name = itemdict.get('name').decode('UTF-8')
            logo = config.logomap.get(name)
            if logo is not None:
                 itemdict['logo'] = logo
            playlistgen.addItem(itemdict)

        header = '#EXTM3U url-tvg="%s" tvg-shift=%d\n' %(config.tvgurl, config.tvgshift)
        connection.wfile.write(playlistgen.exportm3u(hostport, add_ts=add_ts, header=header))
