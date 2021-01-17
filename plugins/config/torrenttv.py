# -*- coding: utf-8 -*-

'''
ttv.run Playlist Downloader Plugin configuration file
'''

# Insert your ttv.run playlist URL here
url = ''

# TV Guide URL
tvgurl = 'http://api.ttv.run/ttv.xmltv.xml.gz'

# Shift the TV Guide time to the specified number of hours
tvgshift = 0

# Download playlist every N minutes to prevent
# torrent-tv tracker forgetting us.
#
# 0 = disabled
updateevery = 0

# Channel logos mapping
logobase = 'http://ttv.run/uploads/'
logomap = {
    u'1 HD': logobase + 'FtLnmUwjG18XJFEKYvLKjwUq1gwHVZ.png',
    u'1 Балтийский Музыкальный': logobase + 'wLtopqioazWFEqSAGxC1D8ybC0KvHq.png',
    u'1+1': logobase + 'omm2Xc8xSVIT6Od6ca4QqMrEXw3jaK.png',
    u'100% News': logobase + '9yEWvPmTcFS8lyQ5NjJ7vbYOa3bx1W.png',
    u'112 Украина HD': logobase + '0AUjU7DOzZcpizC4UR19vDZqqthSe0.png',
    u'112 Украина': logobase + '0AUjU7DOzZcpizC4UR19vDZqqthSe0.png',
    u'2+2': logobase + 'XHXBC3ghvhh100BNXylSgJLx5FVQgD.png',
    u'24 Док': logobase + 'H1UXBai10DjYfScfv1sNAILV9EPDer.png',
    u'24 Украина': logobase + 'XfKEdfsy4S1zbE8n2tB1tNNe9IkrRP.png',
    u'2x2 (+2)': logobase + 'hTpJUV15GSTxZ5kJQGLcn42kCzKyEH.png',
    u'2x2': logobase + 'hTpJUV15GSTxZ5kJQGLcn42kCzKyEH.png',
    u'360 градусов HD': logobase + 'K4tiqb5ajIgmxqh8X5moJuDjN7q5hx.png',
    u'360 градусов': logobase + 'K4tiqb5ajIgmxqh8X5moJuDjN7q5hx.png',
    u'365 Дней': logobase + '0IZrVwoxtmjtgnWu5Dj4Hb8FRc8NIX.png',
    u'43 Канал HD': logobase + '1mNoU1QXmcmK48eVTlnADtsEBmA2sN.png',
    u'49 канал': logobase + 'liRZcIcNbzQTngm8CIkcnw7gLJfeIJ.png',
    u'5 канал (Украина)': logobase + '9La0uS6S8rMKr0BOh6vSCQLNiCqN7N.png',
    u'8 канал': logobase + 'wKPUJjcpZIfI5zBSZwNayOlv63zRNV.png',
    u'9 волна': logobase + '8zDeTSBhsmJDbXo9dxHA1c9mDOP9sP.png',
    u'A-One UA': logobase + '8rEKNCXhKeWnUvGhWCsrb2RN5FMqJi.png',
    u'A-One': logobase + 'buHzdmouswQyLnhzwqnPUHdS9BMHTw.png',
    u'AMC': logobase + 'rozrC8ZPYA1YGajyow35doeVcaQzpa.png',
    u'ATR': logobase + 'uggqxQxxDTuz1P1mY4PZdlRcAKow3F.png',
    u'Al Jazeera English': logobase + 'B1AC3jl0CY8u4qxO0aIEHVMFQFvBUu.png',
    u'Amazing Life': logobase + 'w8TNEcKxT64e1cJuN1b1DXvV1IumE0.png',
    u'Amedia 1': logobase + 'jT3vAEOG5jTd2t8GcC797Bw5W0kSl9.png',
    u'Amedia 2': logobase + 'fAvxTQbWu0DAcMkqej0m73KohAcQJw.png',
    u'Amedia Premium HD (SD)': logobase + 'ornzQpk6WCW6xk0lyBhlwqH8u2QyU7.png',
    u'Amedia Premium HD': logobase + 'ornzQpk6WCW6xk0lyBhlwqH8u2QyU7.png',
    u'Ani': logobase + 'vui1cRrE05CZv1N9Qb20jJ6mTFOJue.png',
    u'Animal Planet': logobase + '45.png',
    u'Animаl Planеt HD': logobase + '9HZGan5rQItVQOfnB91FGqyJXjoqYV.png',
    u'Armenia 1': logobase + 'YST19D8Vt4g7ck1MquvppzKy8Oa27D.png',
    u'Armenia TV Satellite': logobase + 'M4UAMT6cEyL3zuim9fzy38vZRkIfKq.png',
    u'Az TV': logobase + 'FB2qxgNm8xTU6YiR2fY1jH4PIRR2SF.png',
    u'B4U Music UK': logobase + 'LlfDsq3FEU2D4P3lmj25fvl6zQnvNM.png',
    u'BBC One': logobase + 'ofuDCyM7MgzwFbzG2pyavFu6xeRHwp.png',
    u'BBC Two': logobase + 'o7LyIuTJT2C7wJG77Zx5cZhBYP2L8B.png',
    u'BBC World News': logobase + '8cSYWwvq6BAzcGDjJODvCGQYGJ2c4S.png',
    u'BT Sport 1': logobase + 'RNwudSF1Lys88WmIXhiS43g2urfknl.png',
    u'BT Sport 2': logobase + 'NdEFtAJBS9EtR2rSEUZ1ZF15tQzH6y.png',
    u'BT Sport ESPN': logobase + 'NA9uK6s2dqxbRAuhguG80gO03mGUOl.png',
    u'BT Sport Europe': logobase + 'e3dk71TnjMRLy1A1FjvWnuwLDP3rM0.png',
    u'BTV 1 HD': logobase + 's9FERVp6FKtSyMB0N4g17aaKLdxGl5.png',
    u'Bein Sports 1 HD France': logobase + 'iFvQJFlFSlOnL7VN1KZ2qo5DD6lNgU.png',
    u'Bein Sports 2 HD France': logobase + 'eYy8eQWvjK2lUBRCPXldM7DgOanhVZ.png',
    u'Bloomberg': logobase + 'OTsoNZRT8xjXz5nnTICPCQRvNLjBal.png',
    u'Boomerang': logobase + 'tsP2U3zkp5o8B0TD6luRLg0leS9FvM.png',
    u'Boxnation': logobase + '8mECbEuuVmoMl17GPq6hV8X7LDMlu5.png',
    u'Brazzers TV Europe': logobase + 'OmVBp3Kz4Lx722dq2e1OxE26QSxrDA.png',
    u'Bridge TV': logobase + 'dPhBiaViIznwjeWU3pTbIXFmS3iJkU.png',
    u'Brodilo TV HD': logobase + '0pLPWiGqZjDe2O4vbPd8QL0qGsA9lq.png',
    u'Business': logobase + 'wvwXc2x8Bjev90GD6LO6t7TL2aKW1h.png',
    u'C More Tennis': logobase + 'ql4qy7gHN4GtWhcqfd97HqXUs8HXI9.png',
    u'CBS Drama': logobase + '1Mcq9jbl7qPeXpT0bbPTnf8aM3f7dq.png',
    u'CCTV 4': logobase + 'PsrMNDhKrEgCJA5lAR9UUtBlOI4uJg.png',
    u'CCTV News': logobase + 'TyWVFvKwV3lOYYXWVJSj8HMu5AodJr.png',
    u'CNL': logobase + 'wwQ6u4lFXyaUDJLu2JOh6mtbkIz0Nf.png',
    u'CNN International': logobase + 'lIwbRbM3ve4ixhFXp75Oap9nzcO71G.png',
    u'CT 1': logobase + 'sgPGofRHRzOlNb6dBsk5QGiCdzJewS.png',
    u'CT 2': logobase + 'dFDWTyqFwS3roF7Jb3JGZIfm1htuUv.png',
    u'CT Decko': logobase + 'iZ4GvLdo9Gt4NiVLCuiRYtF8rtgYmi.png',
    u'Canal+ Deportes 2': logobase + '4EUoskZorTXBkMxeR8ykSpyQOErvgu.png',
    u'Canal+ Deportes': logobase + 'qoi5H4OujPPtCC1JJO1ozeyFLPqPk6.png',
    u'Canal+ Futbol': logobase + '1En2KRyo8ywbMPWjiiri7TcEXJbqcE.png',
    u'Canal+ Liga': logobase + '6GyapitmDBshZmCxXPJsQWJGhkcooJ.png',
    u'Candy': logobase + 'YW8BJnImniuR7l1U85Khw31mX2XO0S.png',
    u'Candyman': logobase + '8pCxUJ8TBWfvWCrIPN4a4Jimsv9onx.png',
    u'Cartoon Network': logobase + 'NTNQLLri3Hh9iqYjW7VEkFYJsTLjk9.png',
    u'CentoXCento TV': logobase + 'dPuPlqJtkLMRy7NmOhyHDfL0PJqYj4.png',
    u'Cinemax 1': logobase + 'iVIDTNBhrsd8S7OUexIOE9lJJ0BGZU.png',
    u'Cinemax 2': logobase + 'XLVuXXOFFSfsOVKEsFxarjmvLeA5WK.png',
    u'Da Vinci Learning': logobase + 'Yl6p1IDDkZxxiUa3p2JxI66mIlOPns.png',
    u'Dange TV': logobase + 'ofmgiZlRmwOZtTaYtUtfErZS3ODDDM.png',
    u'Deluxe Music': logobase + '3VnQoAyJh3RZM88USPszL1TZIE5t0u.png',
    u'Deutsche Welle': logobase + 'RnqBDfde1HP4OkZhXWlKB1xkHi6Io9.png',
    u'Diema Sport BG': logobase + 'AA2hWbb0gyhc7nYtjWXJH9ZrB3D5EM.png',
    u'Digi Sport 1': logobase + 'gk0ajzoQjMHlBKM298kWjcfNy1P8ec.png',
    u'Digi Sport 2': logobase + 'x1HMd7tDoprxuZvq90Uj2Gb1eEOhTm.png',
    u'Discovepy Science': logobase + 'GAaO3EfDwMuHAIelG4gYW6TDEYbLnS.png',
    u'Discovery Channel HD': logobase + 'SmWnYlOvkJn8GzttT2UY0vmo8PYfMg.png',
    u'Discovery Channel': logobase + 'oKx1ImWVRT3AK3DHYWUVc71JZUkwu5.png',
    u'Disney Channel': logobase + 'JxEjTeXwExjnxutQGKJBmMI85tpNqK.png',
    u'Dobro TV': logobase + 'tcHbtjkY9gYD4VqipgwLP2BYxgdrZb.png',
    u'Dorcel': logobase + '9bzeA3zNtESvDVsiMyDlcrTAngs2af.png',
    u'Dro TV HD': logobase + 'iV5n6aGpDLVpReaJz71u0XrIyAHTcG.png',
    u'Dunya TV AZ': logobase + 'C9oEtk1vVd0yApuKTUve53ADQUhNFj.png',
    u'English Club TV': logobase + 'Hf5RUQ91cEGtHoaK3GK6VIZlJ8Leql.png',
    u'Enter Film': logobase + '8FPA5SCEIj35fBO8yrULnefW4NzIzk.png',
    u'EroXXX HD': logobase + 'VxkJjYZQqK3OcevhRKsz2L3OFiaEwt.png',
    u'Eska Best Music TV HD': logobase + 'wI3e672FQZpD8yr8aIV8Q2fL15zENv.png',
    u'Eska Music Vox TV OldsCool HD': logobase + '7LW3s6C3D3yeciqTY0CKXpEmL3Tb3w.png',
    u'Eska Party TV HD': logobase + 'MaX9is65hlDpRDwgOikGE2RqMRxn8G.png',
    u'Eska Rock TV HD': logobase + 'VU2POxFhYCM4XhFAtOp8Y4sdlbu32M.png',
    u'Eska TV': logobase + '1KX19DgurgoaSKNTTpjXCeSQr1epwv.png',
    u'Eska Wawa TV HD': logobase + 'r9d697qox4MFgypnVqeILYWKcfbwNc.png',
    u'EuroNews': logobase + 'Vb3fP5gUK0q40WuzYeUhMT7RQmDg27.png',
    u'Europa Plus TV': logobase + 'PkatgpdmA4ArsgSG5shu0ZCQQ5RgMx.png',
    u'Eurosport 2 British': logobase + 'syqFtqcYUfxX6t2wcfSGKNbKQ7vGgN.png',
    u'Eurosport British': logobase + 'sKWbooLWxKfwjge6dMOTWi35gQvcG8.png',
    u'Eurosport HD': logobase + 'DpFTzUEA3y67Z6ObTPF4xH0XLNRAZm.png',
    u'Eurosport': logobase + 'QA9jgUaQRrE4vMno04eM3aUrklXOce.png',
    u'Eurospоrt 2 North-East HD': logobase + '0tv5hm546AKIySs7cpj30LlCOcY0Mj.png',
    u'Eurospоrt 2 North-East': logobase + 'qYbdkVFDkhGqTAjXlRtIj2Fg45bmrm.png',
    u'Eurospоrt 2': logobase + 'qYbdkVFDkhGqTAjXlRtIj2Fg45bmrm.png',
    u'Exotica TV': logobase + 'K5hm3mURkkDaSc7RI5RDti5edynMGl.png',
    u'Extreme Sports': logobase + '21FhIqWK82JDPNuLTEIC9hSO2EHfks.png',
    u'F+ BG': logobase + 'DJZlMhUwCNcVypOBoytE7QQnKtMepM.png',
    u'Fashion One HD': logobase + 'iPs2ptiBXm8h0KSnRmyqu45texHNig.png',
    u'Fashion TV': logobase + 'PSjqabjhYIBqcS8hUA8WNrZEjV4zZY.png',
    u'Fine Living': logobase + '22I1fK1aMCUgeYUCV0K3vwmlJKELZD.png',
    u'Food Network': logobase + 'W68LEGlOOMPtN0qoGXvdkWhHBjKet6.png',
    u'Fox Life': logobase + 'rkksGUl3DstQSEyT26Q07hNCEwyNnd.png',
    u'Fox Sports 2': logobase + '6huWEAg1M7y9bKk21UkIyJ3yw1RRHO.png',
    u'Fox': logobase + 'XGC77wQNeEyaJ2z2mDipyIPsoF0xc1.png',
    u'France 24': logobase + 'pViXgcMjLnB5WyOoQJ7sBxhHo5fTSB.png',
    u'Fоx HD': logobase + 'Pl8S60EJ52htHxi1gAw1SS1y8i1p3z.png',
    u'Fоx Life HD': logobase + 'Vou521VpOGAGqhp4HUfiG7BSbKNSk6.png',
    u'Galaxy TV': logobase + 'pU2NsRP9CVtEgQuDTi9jcTYV8iAD4a.png',
    u'GlobalStar TV': logobase + 'Y4kNxgbAnPGCt753P73NzCIbcNz5lD.png',
    u'Gulli': logobase + '2IynBdmw3mmdXt01r8DXKxeor7STnw.png',
    u'HD Life (SD)': logobase + 'jUteUS0xRGdvLyBVqNjowEUDkOjT0t.png',
    u'HD Life': logobase + 'jUteUS0xRGdvLyBVqNjowEUDkOjT0t.png',
    u'HD Media': logobase + 'woAI3zcytfbyiX0LBRToKzErJNy1qF.png',
    u'HD Кино 2': logobase + '8zMANTj9xekiWSig7DHFVSb1HlzJdw.png',
    u'HD Кино': logobase + 'iHVs7YvUVlUvMTnlma7GMpX5p0Tpy1.png',
    u'HD Спорт': logobase + 'dgBOid0Zm2uOU5zvI0ZBAKqUD3n0fE.png',
    u'HardLife TV': logobase + 'fHPc5oaRdIzKpHTqBFnHA4O2LVf91D.png',
    u'History Channel HD': logobase + 'VFgU260pmiIyPxCzD3f8R7Yc6DXClH.png',
    u'History Channel': logobase + '9cVifexiWW0qWDhhpnLNVydoZkeRqZ.png',
    u'Hot': logobase + 'OjgEHQGo84KMtVReLDbO2zDGF4r2Jt.png',
    u'Hustler HD': logobase + 'LBz8ia8AASewVuLjMs5v4MDiVYfsJO.png',
    u'Hustler TV': logobase + 'wgAR4TI1xdd2LAtnbkpvFAfnnn5Uru.png',
    u'ICG TV': logobase + 'seGXEcBUOeAmwcn2KezmYYuEwTOH8J.png',
    u'ICTV': logobase + 'YuNtYxhj9vqgTU9kVuz9imhqviY4PZ.png',
    u'IQ HD': logobase + 'tkCaOFZ7Xf1TmIzhazLXZlcWfJa8Od.png',
    u'Info TV LT': logobase + 'Sv42hVuB4nb2y04ggrhadg9FYZI3Kw.png',
    u'InterAz': logobase + 'rdntbmpYEYtyRbW3nGa1FUNZPXF53O.png',
    u'Inva Media TV': logobase + 'mGWpCUkls40liFDUVrxhaIAFwYXZSt.png',
    u'Investigation Discovery Europe': logobase + 'QvF9d3DYyndsYsyfjC8aWeSzy6hpns.png',
    u'Jahonnamo': logobase + 'OqNuJdvRTdBh5NeydnpmCfMnTJs9XZ.png',
    u'JimJam': logobase + 'BPDFCK5SQF3mXu5MsDNSdtvz4Gjawo.png',
    u'Jurnal TV': logobase + 'qNBTlT1Dtnl0X87LipDLE7uJ0pgLj2.png',
    u'Lale': logobase + '99AZ5VwFy9yZrgsdZ6kIxcoYqwSyUH.png',
    u'Lider TV': logobase + 'LByLhdeQ30Ln5pSZRYSpoLpXQS5Ytr.png',
    u'Life78': logobase + 'ZloJoTx0yurBDfEtB6V91vRuF8mxB4.png',
    u'LifeNews HD': logobase + 'Mvurp6cp7Sq2fV3tnFBwPtJy7Ifm1i.png',
    u'LifeNews': logobase + 'K8dBCUNz1BSwbgUYYU04i2qJpQKLMc.png',
    u'Liuks': logobase + 'niAMFUABvOhd1M42fmveGQcATd8lK7.png',
    u'MGM HD': logobase + 'o4K0lgc2D1GkuFwMC3Cdg1uK6fMrG4.png',
    u'MTV Adria': logobase + 'CiM7BJh1M8SscxNfX5bLhTsizFHubP.png',
    u'MTV Dance': logobase + 'ZXKNRw6Ai8u4lY0wxeycQwj2dIkm66.png',
    u'MTV Hits': logobase + 'iLJhuLh9kFLQkG4ERvLGSjSgMfNiM4.png',
    u'MTV Live HD': logobase + 'WjyYXtYHhG5COxGab7luHb1bmvAioA.png',
    u'MTV Rocks': logobase + 'SEwn7rL2FxPcf5Ol9KRKedIwXlpsAP.png',
    u'MTV Россия': logobase + 'P5ijp2sRQsKVZkOJwjdqIVgYdJzhpZ.png',
    u'Maxxi-TV': logobase + 'uqyYr07PPk2OuEdnNrbkMHVlGZCJp5.png',
    u'Mezzo Live HD': logobase + 'lGOtRiUoGyJUMCtAtUwevBerpQORD4.png',
    u'Mi Lady': logobase + 'Fd556PD2ffD6zdVUiX0dvVfBJavBNd.png',
    u'Motors TV': logobase + '5t2PirCczEeIqzonCtgbmgpbyOZO5q.png',
    u'Motorsport': logobase + '7fAmhbXY4MwyRxACHpWPIaNqNiW6Y8.png',
    u'Movistar F1': logobase + 'no1c6DhrTCZVqnq9N4Z4SZ2dKx3DyU.png',
    u'Movistar MotoGP': logobase + 'nvj6jOmluzhKXuUoXWePwrccFE3DO2.png',
    u'Music Box RU': logobase + 'zaHCW7nPCyGRnqHDkenCIXo7d6vR7v.png',
    u'Music Box TV': logobase + 'fvt4pris0lwnVhSyUrh8QlyzWBhbgz.png',
    u'Music Box UA': logobase + '8T7Rnct8q2VHhRm0BcGFxCjxuYEArc.png',
    u'Music Box UK': logobase + 'KUbeGDe2HthXSDa8OqMhia0nhTSL61.png',
    u'Music InTV': logobase + 'QTJnJokXeUpNksMV5cp0TiE9lyUesQ.png',
    u'NHK World TV': logobase + 'JJ8Sh9c7zA3PaXlK1ZaNjy3GgWQFh2.png',
    u'Nat Geo Wild HD': logobase + 'YYa1wyNA9prFK1APZ2ZSHGirPpm8kY.png',
    u'Nat Geo Wild': logobase + 'ciHIDUuHEnkEuPghbcqkDQx4vadle3.png',
    u'National Geographic HD': logobase + 'hK1waimMq9eAp0ugM19moSoQvUeve5.png',
    u'National Geographic': logobase + 'i6STSw6Hg1wWP18yBAOyKoKpSMeKLu.png',
    u'Nautical Channel': logobase + 't3fIrxEyf2vpizbuznXFKet6yOpEfh.png',
    u'News One': logobase + 'WmOw8mtP3YhXptHbvayITx0TNJdB5Z.png',
    u'Nick Jr.': logobase + 'D87kJ3fIWIm5wKi5qxm24nbuPQv0U8.png',
    u'Nickelodeon HD': logobase + 'CFYx7Bd1aDSgkqjMLLQjFE6xe3u1E0.png',
    u'Nickelodeon': logobase + 'j66xpaZbfiYIgQxv76QAPckPVjmLNs.png',
    u'Nova Cinema': logobase + 'cgxxcQ2S8E2XMoSMlF5pLdQ9ySJD0e.png',
    u'Nova Cz': logobase + 'Z3wXiyZqhbm9uRZDAJcVuaQjoESQtr.png',
    u'Nova Sport BG': logobase + 'BZNQubMesUUPrPyQdhdUEICSjkoaXf.png',
    u'Nova Sport': logobase + '8npwMe6SAEgj5nMBCoVPCemX9fKOvI.png',
    u'Nuart TV': logobase + 'aqMIuUixqLQYmJITPnOGtFkRPuTqKa.png',
    u'O-TV': logobase + 'UlIt4rE3FZs7IQmPN3tsGS6fqY5F1D.png',
    u'O-la-la': logobase + '7ddvb8Tivq7yuEgffrKildHi2BQcCE.png',
    u'ORF Sport +': logobase + 'JQlgjMTC1udkBdrHMiKd2UIV2sJlvw.png',
    u'Ocean-TV': logobase + 'cvBAngU16nJU1bEzxAEcMPiPvf7fVT.png',
    u'Outdoor Channel': logobase + 'SuxFoocUmay5G8jtfJaHL1yIbAT5Hr.png',
    u'Paramount Comedy HD': logobase + 'AvH8i4NV780Q7PcHi5KkxnCDU0Y0yl.png',
    u'Paramount Comedy': logobase + '5EtvAWXB7VK1Yw82yvO28sY28dU4ZC.png',
    u'Pingviniukas LT': logobase + '8X45gGlJq2Vx2jUts3EhYESzpwjmPo.png',
    u'Pink O TV': logobase + 'aI99kH6bHY5Qt2ph4W1Nh0wxdzd1p8.png',
    u'Playboy TV': logobase + 'lIWBxmt5GDl9tg4KsQNtA0CuZWdOHH.png',
    u'Polonia 1': logobase + '3fzUyCBgUoJ6zqc92KSXh9g9utJEuO.png',
    u'Polsat Sport Extra HD': logobase + 'AdIBJziuh63ffasA6KeDMAKV9DPBqL.png',
    u'Polsat Sport HD': logobase + 'zAC1zjpeHrGa3vb5nPLvvNJ8SooQes.png',
    u'Polsat Sport News': logobase + 'WhGmGGlQXEvepTfPBd3u1to4ekbtDN.png',
    u'Premier Sports': logobase + 'dIKsh48t49lFlDcKPhHKsvYsKaOfNS.png',
    u'Pro Все': logobase + 'F8P8nU4YKStbVP2CQD1iaTkcDBzaJn.png',
    u'QTV': logobase + 'PahwxLR2J1qfVSGGr54hdPeUD5vpsy.png',
    u'RMC TV': logobase + '3CiAgachWg7ohgoU1Gilcm73hXhT41.png',
    u'RTVi': logobase + 'QBnba0xrWtpPWLL4yKDRixaCRQAmaP.png',
    u'RU TV': logobase + '161.png',
    u'Redlight HD': logobase + '5tFZcJtKAZRbXtKGDuLe8FZ3lK9LI5.png',
    u'Retro Music TV': logobase + 'zVS9G1oine56udlAK30gNut16iJ9Ft.png',
    u'Ru Music': logobase + 'sAVGvLHkObOsYWh36zLIDjxTCWANlo.png',
    u'Rusong TV': logobase + '186WxZMn3PGQyMlWsItM9JkSS4Tt29.png',
    u'Russia Today Arabic': logobase + 'OPbYfpQc4ShP8JmgPeiavUroY98H8L.png',
    u'Russia Today Doc HD': logobase + 'b8QePfFi6zsCDS7hfTeFWES5UN4SAk.png',
    u'Russia Today Doc Rus': logobase + 'VOYx5PIhDPrWiZIcCYpm1xrDSQZnsN.png',
    u'Russia Today Espanol': logobase + 'zkPwjfFbktNO8EYDaHlYhwAeT88dmY.png',
    u'Russia Today HD': logobase + 'rL14fwCe8q10mKTchOwLkfwQVki9XK.png',
    u'Russia Today': logobase + 'rL14fwCe8q10mKTchOwLkfwQVki9XK.png',
    u'Russian Travel Guide HD': logobase + 'g4MDyw0yqXWkIar8eH0cgCz4xhiKON.png',
    u'Russian Travel Guide': logobase + 'IeaOjwR6Q9eJjGZr0LYk2tpchM3ITZ.png',
    u'SET HD': logobase + 'sX1unYoKj8JR7m8lbtkmPCClRrjAZ9.png',
    u'SET': logobase + 'tKzOKIcOQYrFl1VL8B0QqERFXCAYfU.png',
    u'STV': logobase + 'DbKEKL5gUOFHiruYRjY2H9gTLOV5mu.png',
    u'Satisfaction HD': logobase + 'isdNgbfGENuaDPSMzsz8WMjBzc1rah.png',
    u'Setanta Sports + HD': logobase + 'jW7pJhmebW2fZsXUTvDuRQLahgiLlU.png',
    u'Setanta Sports Eurasia HD': logobase + '1wgHdJP76TCItF14FxDwBtak8tmxRv.png',
    u'Sextosenso': logobase + 'HXMvFMLO9weHUcolVmmMKpz98T0K4K.png',
    u'Shant TV': logobase + 'IgJpH1JzyjI55Ki2G2Ybz6jzOkwG0T.png',
    u'Shop 24': logobase + 'bCuxLyvoTk8l5cBRSyKFXjWjYucvlu.png',
    u'Sky Sports 1': logobase + 'pzVzAnJJ90768a73nJXWFAni9yYPT3.png',
    u'Sky Sports 3': logobase + 'UAUhQNqNqyEgXdUoeffjssUZ262Lsx.png',
    u'Sky Sports 4': logobase + 'qqJzEqYys67VAtSt59keaQaJdM4LUg.png',
    u'Sky Sports 5': logobase + 'yFt8HuKsDvuLii304FlhbEIPZ3gTvi.png',
    u'Sky Sports F1': logobase + 'J9T7KUE84YobHuNThXN6Hl9UG21tD9.png',
    u'Slagr TV': logobase + 'MGCm4Mz8Ggf7xrG9CpfB5QUUOcmfEq.png',
    u'Sony Sci-Fi': logobase + 'zLWEgf9BbxBr1TR2Qj2NxVQBuPecEP.png',
    u'Sony Turbo': logobase + 'CaPjVaQrpyN138TarQ7CYBqBOz0ZF7.png',
    u'Sport 1 Cz': logobase + 'kCLlfkFz3Ba3BL9Jc9ZPgUKXh2piyv.png',
    u'Sport 1 LT': logobase + 'nRFc87aOV1vRnjEqmQZUneZe4HiCqn.png',
    u'Sport 1 Select': logobase + '899pteevSriMFxe4omDA4G6l9i0czY.png',
    u'Sport 1 Voetbal HD': logobase + '0WEqpl3cqObcLs2J0l5DDhVPZalvXx.png',
    u'Sport 2 Cz': logobase + 'YLmEjnczWQGJcZC0SxRcH4ifPcwYlx.png',
    u'Sport Klub 1 HD': logobase + 'cLQ3uuWhQqxCQk5RUDwA9x7bLUHBwn.png',
    u'Sport Klub 2 HD': logobase + 'LiIua5Nyy8xdHFYhwgrwbcajbKz6fH.png',
    u'Sport Klub 3 HD': logobase + 'UkUGpf3hamDPGPtkqximS96rrts4jx.png',
    u'Sport TV 1': logobase + '7u5sbYjzJdQopdQ6bAH7GLDUsPWnXc.png',
    u'Sport TV 2': logobase + 'u6T8L5PPYKHCbBATjdzjLpTC8zzCdV.png',
    u'Sport TV 3': logobase + 'dYTM6Oqhaqw18FI6uYPS5yhjCmc1nZ.png',
    u'Sport TV 4': logobase + 'YfFhr0OCmbN8vHUuGCLp488dxGpKVw.png',
    u'Sport TV 5': logobase + 'YyzfJTMsBcmTKptLzxZcAcLKFj52LT.png',
    u'Super Tennis HD': logobase + 'mjQW91VJdjIEhADvOO2s6OiKNeUdUK.png',
    u'TGirls TV': logobase + 'FufZ2heFswzvAbRkTQZs8UJBYGsxuG.png',
    u'TLC HD': logobase + 'gT4olUY9nFJbGRCdwd7hHJp1NJ5eJr.png',
    u'TLC': logobase + 'gT4olUY9nFJbGRCdwd7hHJp1NJ5eJr.png',
    u'TV 1000 Action East': logobase + 'GblbxkDGXZyW5oWt9W8wuERQAiZ7ZT.png',
    u'TV 1000 Русское кино': logobase + 'ch5DX6f8hxDnmyzrjotUoKHNGzcw9P.png',
    u'TV 1000': logobase + 'WJMEvVafVakrm7BUMy1lzku7VQCx25.png',
    u'TV Bakhoristan': logobase + 'LoXaN929SQC5r5aQ3JETDXwG6VlPMk.png',
    u'TV Plus BG': logobase + 'cxxTbCRSZsh4l1CNpZ4mYychepxUGw.png',
    u'TV Safina': logobase + 'mJUmNhJbQqcr2NPppAryEJqDPBJGV0.png',
    u'TV Sale': logobase + 'hs0YdiUTlpRtb3wTiP4cXboX0H9oTN.png',
    u'TV Smichov': logobase + 'hqgkCNoqMXiAgNU6uedqUNIR7Z0ox5.png',
    u'TV XXI (TV21)': logobase + 'TKchoTWZFRMmGDBok08zoEFJ8mJJCe.png',
    u'TV1000 Comedy HD': logobase + 'ygGiR2hkQLySH6khdo8GV9CyMJ8dXi.png',
    u'TV1000 Megahit HD': logobase + 'lVPY7WCjn1WM6NL6tfLFy8iGA4yk3Z.png',
    u'TV1000 Premium HD': logobase + 'raoDrpin8VKmi522LZWzSF0fLRO04m.png',
    u'TV2 Sport HD': logobase + 'iL3TM972YPxOxajyfbuNcKGPFrVvTg.png',
    u'TV4 Sport HD': logobase + 'm8tNJfJGN7cYZtUWBggz3PMVB28clK.png',
    u'TV5 Monde Europe': logobase + 'ko7rbRBnyK1iINkLOA2adRvgVOEgUK.png',
    u'TV6 LT': logobase + 'SKskx67yBUvbTdMIIZjH1Z4EcB8nYX.png',
    u'TVT 1': logobase + 'CKKdhDfmno9O52tMfWptiAQT0IBWV8.png',
    u'Teledeporte': logobase + '57r0Kq1rFB6vcMeldfWDvp438Jz5qT.png',
    u'Teletravel HD': logobase + '4ZlASq3oDpOjXfhwluOzY74sy9elaE.png',
    u'TiJi': logobase + 'mD3GW0E7rdPwc4stjk7xrLI2gZn4Hq.png',
    u'Tonis': logobase + '38BRA5jO6LAsQ6rv1NC3FMJ6KALp8z.png',
    u'Top Shop': logobase + 'uD257Lhw7Ko2YD1reC0nRqW7lpy93D.png',
    u'Topsong TV': logobase + 'DsJRpcbI6rgjONbQftC5nHt1XMAXYQ.png',
    u'Torrent TV - Android': logobase + 'wf43FCQBGnvSrknDmSJXTOtbVWgOiP.png',
    u'Travel + adventure HD': logobase + 'b1HifWKMyefmDDvaDAJTwNNTaD8LF4.png',
    u'Travel + adventure': logobase + 'b1HifWKMyefmDDvaDAJTwNNTaD8LF4.png',
    u'Travel Channel HD': logobase + 'zfnAGLCvIu1fx9hfrITAZMoo9HYww4.png',
    u'UBR': logobase + 'F6EzmjkOBVB0gmn1kQX6itv5VvFml5.png',
    u'Ukraine Today': logobase + '3AVq6O577A7uw9uZ7fxIvpvE3CxdtW.png',
    u'VH1 Classic': logobase + 'FhxUFQ2Bsfom4vb8Ce41gFObAbh1Vh.png',
    u'VH1': logobase + '58.png',
    u'VIVA DE': logobase + 'HagNMshKtJ7zKnk9fdmBLhITjoWdrJ.png',
    u'Venus': logobase + 'R2ug0cuB3SmBBA6LK1uoNbEV66u39v.png',
    u'Viasat Explore': logobase + 'uCqpsdKP0ialUUYxUk2fXshYdYfxzW.png',
    u'Viasat Fotboll': logobase + '0JLqj3qwFoT1Y61scCyUdWioV5U6hx.png',
    u'Viasat History': logobase + 'MWGbB8wJp5Gm4vbPHl0ktohDDjMKdr.png',
    u'Viasat Hockey': logobase + 'CuAbCRGdf3Z1FGFiwErTbHZ3lAMJzr.png',
    u'Viasat Motor': logobase + 'RuYtGxEpqJ5DG7WxGCMWNDXosRdh59.png',
    u'Viasat Nature East': logobase + 'yimDcPvajJcUKQm9bY15cDdp3rJFcp.png',
    u'Viasat Nature-History HD': logobase + 'pSP6zxmuO4PU6xa6KRlZ9L8vvVM2Dy.png',
    u'Viasat Sport Baltic': logobase + 'ZIITckvF1w5u1MlubmhoG45HxPgcZZ.png',
    u'Viasat Sport HD': logobase + 'prAZKkny3W1HGM03lP0EhzcMmTPZdi.png',
    u'Viasat Sport Sverige': logobase + 'prAZKkny3W1HGM03lP0EhzcMmTPZdi.png',
    u'Viasat Sport': logobase + 'prAZKkny3W1HGM03lP0EhzcMmTPZdi.png',
    u'Viasat TV3 Sport 1': logobase + 'LUsZ9yjy6izQJHd2z2Hf7uBZ4UyUcM.png',
    u'Vip TV HD': logobase + 'VXNvw8nbJhjRncTmxkuglf8htUxN2N.png',
    u'WedTV (Свадебный)': logobase + 'u93ysJkZEp1NzeG7jTbVgB7nKhDTqH.png',
    u'World Fashion': logobase + '2YI4sT9YkGezrw9vZPn0uIRhZ7E2BV.png',
    u'WowGirls': logobase + 'phiImbBi8hRs3LqmOOpLVsPqQkD2Hc.png',
    u'XXL': logobase + '6nJtj85PlL0MxB8RDkM3toyGND3Anc.png',
    u'ZDF': logobase + '5SH5FeZiITw27CPxscjksZp272u7He.png',
    u'Zee TV': logobase + '1HooaeEhMSvpKmWv6nneZxnTmG5r6Q.png',
    u'Zoom': logobase + 'SyisYhg411o7z9kXci4vfpLq4KBZZ4.png',
    u'bTV BG': logobase + 'xiNqovHjloSoVzrVieKo6saLQTUnJ7.png',
    u'nSport + HD': logobase + 'JSpj8Lq758dRJzBaTEjM8nbSfnLf9M.png',
    u'АРМ ТВ': logobase + 'OgrdBlfYISfcpr0XO0ImEyelCMjUVx.png',
    u'Авто плюс': logobase + 'WkRxjy6fJEBJ5NZiaGn2j05eqfFfQq.png',
    u'Беларусь 24': logobase + 'GxA1KJP5YwpWc38BoPEmLwQH6uDeEz.png',
    u'Беларусь 5': logobase + 'aMU4HXJN11Bo9WissbPW4rhe06vAql.png',
    u'Белсат ТВ': logobase + '9VYuUQxx1ss7ieu2upENtlibyamBP0.png',
    u'Бигуди': logobase + 'JvcMdB5e6KVBpbXT12ulzmDqenheRx.png',
    u'Бобер': logobase + '2Edln8vEbg7UUSVUo7lIJPR780OWAR.png',
    u'Боец': logobase + 'pmkJgRqsuZDzuN4c6v6jZaBVKCN3K3.png',
    u'Бойцовский клуб': logobase + 'oo4RN3hUUjuVbtegW8Q5QE0bT6GwwD.png',
    u'ВТВ': logobase + 'svsUD6TinXyv3B1q5sZf3fI9ebmpaF.png',
    u'Вместе РФ': logobase + 'qa50GYekwBWym7KtoJdzrWHWqN8TeU.png',
    u'Вопросы и ответы': logobase + 'xbV8M35FkvpieQ3TUEL8fhwU8MzjmQ.png',
    u'Время': logobase + 'F44yKDJQLsX0llpZ2wupg8V5vHx5fF.png',
    u'Громадське ТБ HD': logobase + 'Ovkd9TiVv3nLcKPwQS2wkJ85KyYCMQ.png',
    u'Детский мир': logobase + '00Vf3rPABNnbNQ6Rv0dnfcg3JsJelA.png',
    u'Детский': logobase + 'jk8kody2p38CKdj5KGXWMwRLjgFIlG.png',
    u'Джус ТВ': logobase + 'qVNFoyUAOJSDvN9tHhf9j2AP7x4VkV.png',
    u'Дождь HD': logobase + '381.png',
    u'Дождь': logobase + '381.png',
    u'Дом кино International': logobase + '69MqZE2YHJNewQkqRbJea33WuRkKgo.png',
    u'Дом кино': logobase + 'jlC78Fy13KWjQUN6l3FtbsRLZDvc0x.png',
    u'Домашний (+4)': logobase + 'LRMaRyPCroUq4dVcRhwKJKVuhvdvUZ.png',
    u'Домашний': logobase + 'qmqrH2E2EX11qitbIvq0CYsxQjsHGm.png',
    u'Драйв ТВ': logobase + 'pmmgMKcRbxeYkjVUVr4IAWM0UuZHO4.png',
    u'Еврокино': logobase + '34mszCG0j0Vf6kFcMrLPnFEA8UPdu6.png',
    u'Еда HD': logobase + 'ojUD1jhpv7HBOLmubpEBOsANkpYNtk.png',
    u'Еда ТВ': logobase + 'TWdAdMXfMSylb2mQ4efFnOAYosymNC.png',
    u'Еспресо ТВ': logobase + 'lOwm890F5URuR5Ej7IacerzECPIDt4.png',
    u'Живая Планета': logobase + 'xgKSMwqBdEyXnbVgb8LtNXSMiaPcOx.png',
    u'Живи': logobase + 'cOluSjslxxs3JZtSVO8c15xh7h8SDU.png',
    u'Загородная жизнь': logobase + 'cGGo8HRkVhy66UXKXZ4tH5HyUaaxJA.png',
    u'Звезда (+4)': logobase + '01VqCLfVy5OsMBN1qXjxOTp5NKT4QS.png',
    u'Звезда': logobase + '0HLRrFHt2QIkbJpLc1fy0RVe7hqCEC.png',
    u'Здоровое ТВ': logobase + '2LgJcyMnjJpMAhUqX3rdQ4ChOmbuTo.png',
    u'Зоо ТВ': logobase + 'RtAhntWPlKQs6CIYAb72piNF9EsN3E.png',
    u'Зоопарк': logobase + '1Ugpb5T1THFcFpn19Mnua21KxHkjct.png',
    u'Иллюзион+': logobase + 'XOO3bLrAAvCj45nIsxsGCppY14bY1n.png',
    u'Индия': logobase + 'XVWyHt5bFFcZNzmysBSjuVdGBGl45D.png',
    u'Интер': logobase + '3SP67FapzyZqMVZTPiJIcN09KRkTeu.png',
    u'Интер+': logobase + 'QEdaDBbqr13CCfwKQAP77UZYPQIPn0.png',
    u'Искушение': logobase + 'p3WsIen84SZK76zTMWnslNgUjsqsMZ.png',
    u'История': logobase + 'PNRaeOUFzOPFtrclFBBRTckj6Lvo0u.png',
    u'К1': logobase + 'mk2mYb28HFIxkFIiMNQWmKUdn1Y8hD.png',
    u'К2': logobase + 'IjG76jf8k8HTNLooNpUiEXtkPfA2rG.png',
    u'КХЛ HD': logobase + 'kRN7BwVtcdaXrU4Mdg24qhFAxjx9oZ.png',
    u'КХЛ ТВ': logobase + '216.png',
    u'Карусель': logobase + 'S233D4b6eq7KOXfdyi4dY2GokKeltg.png',
    u'Киевская Русь': logobase + 'C1AZimW2NnNA17H1uJLxxePUMTPQZ7.png',
    u'Кино ТВ': logobase + 'KkITMDICqC1erWdSqyOqoccqde2wHC.png',
    u'Кино премиум HD': logobase + 'p580CRZ8bBS6dw3plMWhhxXSzQ59uS.png',
    u'Кинопоказ': logobase + 'v0JEbxExcFI8dVEzCkpZUoktgiS9t7.png',
    u'Кинорейс 1': logobase + 'q3N266MTLCzzNVXy3q330VIVgTp93L.png',
    u'Кинорейс 2': logobase + 'RO9ac4e18hSAsPhquZ9JzyTHo5oqMK.png',
    u'Комедия ТВ': logobase + 'L2MEpT2YePoDvmKRjYy6yyt5ssH1m4.png',
    u'Красная линия': logobase + 'I43S6jd5noclar0LlPJnyY8adonmUV.png',
    u'Кто есть кто': logobase + 'MwNkO3fXd6KefRdiGlOdOQ5q0Zu7kS.png',
    u'Кубань 24 Орбита': logobase + 'FauvJxsKmI5a1fR62uSH9hJfHs5TCr.png',
    u'Кубань 24': logobase + 'CAAqiN96tQzFDdtz3vjrrgeIjAKqNq.png',
    u'Культура Украина': logobase + 'pyKdve4YhoChQFGSha8J0FBWBf302a.png',
    u'Кухня ТВ': logobase + 'G0WbVMphlP9oJ6KvHRfx0xDfhrF9Re.png',
    u'Ля-минор': logobase + '8FJA3xMMHcrZuGifHViyVQLjVIem5u.png',
    u'М1': logobase + 'ezvu2ugYMGnZ968LlnjPw7VjqWIPeM.png',
    u'М2': logobase + 'U4s78hznNz7mFYZQICkxN7J0HTtlCP.png',
    u'Малятко ТВ': logobase + 'kjYF9vS2IDTMehpzC7WWfjnZ4NVpuk.png',
    u'Мама': logobase + 'nw9fROQIjjKSDp8Wjkjl1Wt0n0xHxd.png',
    u'Марс ТВ': logobase + 'KnDO2ZAW1Xlahhp1ysdlDUPCQI3Jix.png',
    u'Матч ТВ HD': logobase + 'MXyy9Uud7oDuH8JqVisjsD0csgAHnQ.png',
    u'Матч ТВ': logobase + 'hQDOuQjUVczvUU2ocLE0tkC1siCqpo.png',
    u'Мега': logobase + 'IXY7dRFoq0qCqn4UbY47iP36vVZ6ck.png',
    u'Мир (+3)': logobase + 'QxOYkz6f80IdhmC4RSHI1cMd32CqYZ.png',
    u'Мир 24': logobase + 'auv6717gJOWi0A2VoeDQaCsx9G1NOj.png',
    u'Мир HD': logobase + 'Oq6h2IicTagHENQu1mFkjLk5rChMnr.png',
    u'Мир': logobase + 'Oq6h2IicTagHENQu1mFkjLk5rChMnr.png',
    u'Многосерийное ТВ': logobase + '4TMYdVpZYXafyIumuB5d7PrjFnslyT.png',
    u'Москва 24': logobase + 'dZcmoqRoZLhCBh8BE4RnbQivuDY6hH.png',
    u'Москва Доверие': logobase + '9oPazhJQrGZcSN64ZOS3WjLwGmQIZy.png',
    u'Моя планета': logobase + 'Qa41eifERrD77xQsmpRGbeTq95Ldlv.png',
    u'Мужское кино': logobase + 'PUDb8m2JFLndsPvb56tdH0V4RW0kZc.png',
    u'Мужской': logobase + '6YbhuWNqPKQWWsUGbBnSbAbm7IGssX.png',
    u'Муз ТВ': logobase + 'gttVvZmkAklbl2i0Mqy1MCzSCn7WiY.png',
    u'Музыка Первого': logobase + 'fD2Hnsq5BPMGvobLDMPZP049yNhBYt.png',
    u'Мульт': logobase + 'ZVzHvGF8mZ6RTsSh6aWsPbF1FBLjyp.png',
    u'Мультимания': logobase + '132.png',
    u'НЛО ТВ': logobase + '2VGhYruaQo19G1NLGoOiTrwmPxef7d.png',
    u'НСТ': logobase + 'fKYzdlWRz68qd9mRZnWuxMY73EyaSz.png',
    u'НТВ (+4)': logobase + 'B5GA1cfgmn8EsxrdwfNUIrEbdqarXf.png',
    u'НТВ (+7)': logobase + 'B5GA1cfgmn8EsxrdwfNUIrEbdqarXf.png',
    u'НТВ HD': logobase + 'zdJ3ye6d3UWl5a56zm6LjqYH6ziSOs.png',
    u'НТВ': logobase + 'B5GA1cfgmn8EsxrdwfNUIrEbdqarXf.png',
    u'НТВ+ 3D': logobase + 'qvuG0JySlHPlEH9A7G4xMNjBqOB35h.png',
    u'НТВ+ Баскетбол': logobase + 'bIWuyv7DJ65D5hIANkeo9SyIHGUXtn.png',
    u'НТВ+ Кино Союз': logobase + 'F3RiiQtowA2YoHw73iEzcMLZwfDiSx.png',
    u'НТВ+ Кино плюс': logobase + 'cnz8ZMypP2HV6phwv3rkSVQ7CgJExi.png',
    u'НТВ+ Киноклуб': logobase + 'nRnksgRuhojvbFDqh5KZ30XJQ4iyFO.png',
    u'НТВ+ Наше кино': logobase + 'UXJcZjVdZVIzciVHgGT3e6XxdRaBsD.png',
    u'НТВ+ Премьера': logobase + 'lDiI54Y3LjIAOg5VV0adicP3OJrdgo.png',
    u'НТВ+ Спорт плюс': logobase + '222.png',
    u'НТВ+ Спорт': logobase + '2WCUNhvAYk7RJUCcbt4N8xvOxWGlbx.png',
    u'НТВ+ Теннис': logobase + 'SdtlGA6I7WvjOpHsbabE4C9DP7JvJ7.png',
    u'НТВ+ Футбол 1 HD': logobase + '5gVddUBrGBIvdTx0cpRgCMJwVgphJz.png',
    u'НТВ+ Футбол 1': logobase + 'EQQJV8zgnv5MCfa5VBcvOm1GsLWovM.png',
    u'НТВ+ Футбол 2 HD': logobase + '8X1dxETwOup3Qton0J35BoW5glu5UG.png',
    u'НТВ+ Футбол 2': logobase + 'hD6OLNWbxyDtqE5VlVxCaoNeEoYpFb.png',
    u'НТВ+ Футбол 3 HD': logobase + 'eC4IeAxFTXXMsVfQaQHPtAN7LvosGd.png',
    u'НТВ+ Футбол 3': logobase + '4B2emgwWQ7kgFJwdoh0zNxDguh4Fh3.png',
    u'НТН (Украина)': logobase + 'LpQE1Odb1EoH5dJ90gWjItVyEYBXsw.png',
    u'НТРК "ИРТА"': logobase + 'd8zPTPLcK87xhBnGVFhgkuwFBY2TnK.png',
    u'Нано ТВ': logobase + 'QuURIfJUmXegxsHMYqMivVwxizbfKd.png',
    u'Наука 2.0': logobase + 'ypWbqYqKApM8cnDK1FibvQgpmgEay9.png',
    u'Наше любимое кино': logobase + 'LSR5M6VxB0YDwv6803zrGFkq7vGQ3J.png',
    u'Ника ТВ': logobase + 'pb3d3rBN4qW7ggzsosbAZXflfIv0Ty.png',
    u'Новороссия ТВ': logobase + 'zUchDq13UVJRmlwAl3feV8cgKHYSyE.png',
    u'Новый канал': logobase + 'k7YdHhVpFZPIkBMXS2P2O2TkZSPf0y.png',
    u'Ностальгия': logobase + 'tIfiXoDaXoZevuGu9pZJSvX8unv1xl.png',
    u'Ночной клуб': logobase + 'nXifSdkxHJVKI4SKtgtBQmCSHXtgOt.png',
    u'ОТР': logobase + 'CqxKorK72v3ULbWkB3ZOhdte0duYZa.png',
    u'Оплот 2': logobase + 'EqwpuUgrI6Wl6JVDK2fLtXkNaqOXeU.png',
    u'Оплот ТВ': logobase + 'gvofGxTug45qSt1vsX0BPzQxGTrwTr.png',
    u'Оружие': logobase + 'CyDUCmYXK8WS2kXCX5kiAOFejnlwoP.png',
    u'Остросюжетное HD': logobase + 'mxF7CZsqsDRMMK4pN8ekdccEgvEsZC.png',
    u'Охотник и рыболов': logobase + 'Ws2ddPI0b5Ie7PymoPUsboVlz9lYMS.png',
    u'Парк развлечений': logobase + 'beyfqyeacrFG0PrOeKUQhzQ4bV6Q5d.png',
    u'Первый автомобильный (Украина)': logobase + 'oZTXrmNOxeJIVSbnuxqbiuAL3voXYa.png',
    u'Первый городской (Киров)': logobase + 'sxUNuJVQpUjRMmASa5TvwlGykSBAkY.png',
    u'Первый городской Одесса': logobase + 'vBOI3YTA4FDLD0c7BHHjq476p9GMCZ.png',
    u'Первый деловой': logobase + 'a1Qf3MpxC9FPD68Tj8vtUTNK8P25xr.png',
    u'Первый канал (+4)': logobase + 'nHJycH0CkOhPeZ9DmB47iSMWP5HyWz.png',
    u'Первый канал (+6)': logobase + 'xEhi4YWxLlIcHq33Y44NrYvyHRArwa.png',
    u'Первый канал (Европа)': logobase + 'WimZD6efLd6QotrPP9uiJeF7t50nFv.png',
    u'Первый канал (СНГ)': logobase + 'WimZD6efLd6QotrPP9uiJeF7t50nFv.png',
    u'Первый канал HD': logobase + 'VxAFWzh1y88c8Aqa17TsxD2IO5pqoi.png',
    u'Первый канал': logobase + 'WimZD6efLd6QotrPP9uiJeF7t50nFv.png',
    u'Первый музыкальный HD': logobase + 'YxKl6Jqi6fmlUJjYGPnBhWhntKzI65.png',
    u'Первый музыкальный UHD': logobase + 'YxKl6Jqi6fmlUJjYGPnBhWhntKzI65.png',
    u'Первый музыкальный Россия HD': logobase + 'h7EDhdGypKmtfEP98O052SLlXUCcXt.png',
    u'Первый музыкальный Россия': logobase + 'MkX2WG1zhZ2KcYFdL0xWH1T4xkO7UW.png',
    u'Первый музыкальный канал': logobase + 'gYpYhzD3akuKSFpRmkh2p36pXnqHoW.png',
    u'Первый национальный (Украина)': logobase + '8yGRnEG4pNYMLFDVekA2yeOAX1lGZ2.png',
    u'Первый образовательный': logobase + '1kXxtStMuodaPU09H3rla3ry3QA2Wr.png',
    u'Перец (+4)': logobase + '28.png',
    u'Перец': logobase + '28.png',
    u'Пиксель ТВ': logobase + 'BdCXB7wPZMNvlWzB5xEFzmsYUXcfXW.png',
    u'ПлюсПлюс': logobase + '6gVIy7RMokFO61iVawgwbthe5mhgqm.png',
    u'Право ТВ': logobase + 'jqV4vr8830fm6lYlX9F7w3tRvcrRra.png',
    u'Просвещение': logobase + 'Fpx3Vqqk2VNcXl4YjsfO53XscWadvF.png',
    u'Психология 21': logobase + 'AyLAdiqcKu5X8ykdLf2bO9HsxMlJdO.png',
    u'Пятница (+2)': logobase + '0fafj6PSIWdqtBdgwYTl9M06SDU2wA.png',
    u'Пятница (+4)': logobase + 'fF9FYWNiHFfuR1ZrkaboYHwi1O37TJ.png',
    u'Пятница (+7)': logobase + '0fafj6PSIWdqtBdgwYTl9M06SDU2wA.png',
    u'Пятница': logobase + '0fafj6PSIWdqtBdgwYTl9M06SDU2wA.png',
    u'Пятый канал (+4)': logobase + 'tUE3C0hSxn7AxGHhST36CWi6HgJbIi.png',
    u'Пятый канал': logobase + 'nIUDYY41OO4Xo0ntGpGv2rfpOR5ngt.png',
    u'РБК': logobase + 'JUMDXZxxB3UiVpMpU8t0aCpbVzxTmP.png',
    u'РЕН ТВ (+2)': logobase + 'xwSFxBlid4YhPjZl8ibcIeTlzP0VVS.png',
    u'РЕН ТВ (+4) (резерв)': logobase + '2Z3hcLqC0pQC9gLkuZSl5WkHfS5HYb.png',
    u'РЕН ТВ (+4)': logobase + 'BE7n1y2cjisjflpQuMdC9P3c79rWb7.png',
    u'РЕН ТВ': logobase + 'LJvkfB2kYaDzij1Y13Fy6syUCkP5Y6.png',
    u'РИА Новости': logobase + 'DixgG6tVZzcVHO2LPQEx3QrtfoVah3.png',
    u'Рада Украина': logobase + 'hBFJBYNiqZUom0ooVtNEJKliZwfioO.png',
    u'Радость моя': logobase + 'VRylZFYgFq7AL0FWcbf5JVOX3desn3.png',
    u'Ретро ТВ': logobase + 'axrNIB7372SHIRwqT0jBbfyvjSoZ7I.png',
    u'Россия 1 (+4)': logobase + 'DL17FIS3R8m6eWTwFvdDYualmxvkGV.png',
    u'Россия 1': logobase + 'UUrfoqi6NQcc9gRLnCc8ODZJ2T3ShE.png',
    u'Россия 24': logobase + 'LWfGV6eICPYL7psaBfw2dOgGrOtHFS.png',
    u'Россия HD': logobase + 'ghvqmVpPWqn9x6POAm9UJBvXFzTrqN.png',
    u'Россия К (+4)': logobase + 'lzLdqpUZ8iHL9JEV7vQGG1gSlyswfB.png',
    u'Россия К': logobase + 'W9pWrec1BOJTmj8okrFeyM44wcpyd4.png',
    u'Россия РТР (Украина)': logobase + '5o9OWeEw90hM5ouECuTLwj5QP8MwU3.png',
    u'Русская ночь': logobase + '9Sh9bJuj6js5AJsypAd6UvwnsIB25R.png',
    u'Русский бестселлер': logobase + 'b5JXaosgmcanh9EVJg52yBefvdLQF7.png',
    u'Русский детектив': logobase + '7I7VjbsFMIkZdoSbHFXiKEVZKNUbOM.png',
    u'Русский иллюзион': logobase + 'E9Imfr8aHN5midPVpNhJ3fo49FHbQE.png',
    u'Русский роман': logobase + '2smriIFxtj7Ojh4jyZq0K1XrT98XjS.png',
    u'Русский экстрим': logobase + 'upndVpIdjY3vb5vrituof5UcKISNcQ.png',
    u'Рыжий': logobase + 'wfBSy60qHaPSKPpTfrNv9Q167iHIPu.png',
    u'СТБ': logobase + 'saZlIDrdaXWoiQa8sfZp2bEAeH0kXk.png',
    u'СТРК HD': logobase + 'xOmVS1kQFIHeAwqtJbBfrbE75Quj2a.png',
    u'СТС (+4)': logobase + 'Tl0KbPAKgErgJHEw9yo3VMoc35EWZt.png',
    u'СТС Love': logobase + 'iciJHbEmJ1hHXAMhzC9cRWhmh9gH0L.png',
    u'СТС': logobase + 'is620Pu6DreVLLnpHkpcXXZC9PI2Hi.png',
    u'Санкт-Петербург': logobase + 'sb81YtPOvlHidztMnC5tZPSKkb1uMI.png',
    u'Сарафан ТВ': logobase + 'LsYzwEOUspoxkY2hrTSy9zKqvpWlY8.png',
    u'Совершенно секретно': logobase + 'BZJQEpa6Y4KL9tQjPHAIxbodw0KAyN.png',
    u'Сонце': logobase + 'TJXJVeoBFRMFrUgzpPW4dunJL6XSzn.png',
    u'Союз': logobase + 'YpsuBorUwulPHW3nI8O6nKETnEVB83.png',
    u'Спас ТВ': logobase + 'pAFeyS1iCV4BybnpnnwjoKm0y0zvaA.png',
    u'Спорт 1 (Украина)': logobase + 'XqwvMS8Hn0mOpbh79esrIqELTsvo5b.png',
    u'Спорт 1 HD': logobase + 'cqsjEb2YlMBsTNJPvKmkxmAWLkfNmp.png',
    u'Спорт 1': logobase + 'UNqCK5IiCxetsHsN7eMApPOzhaM9v0.png',
    u'Спорт 2 (Украина)': logobase + 'q0PokCXx6jtCHEPMvE42I0pD3ZNY0o.png',
    u'Спорт': logobase + 'InpgSRB4SoFzJSAOkLpGCMayuYTtVm.png',
    u'Страна': logobase + '5G27bahViND43dD1VlkaKlQRsYOqwL.png',
    u'ТБН': logobase + 'r9O7HmwQbFR4oKMH9yKAogE8xBzwz4.png',
    u'ТВ 3 (+2)': logobase + '427.png',
    u'ТВ 3': logobase + '427.png',
    u'ТВ2-ТВ': logobase + 'fFl6h6QUwFKoI3N4lqEyhNLdACGkNq.png',
    u'ТВЦ (+4)': logobase + 'dR7hMBOIq0MDGMkydFuksHGLNIWz7U.png',
    u'ТВЦ': logobase + 'QEpQTskZ9hcfI0rgD8osHVYSv58pde.png',
    u'ТДК': logobase + 'eSrHE6Gws4U6JxhFXA3mQ4iDVc0SwS.png',
    u'ТЕТ': logobase + 'jp0YxRwXOyMWgVfDAyQaXNwle90sV3.png',
    u'ТНВ-Планета': logobase + 'vBMv8AtIpDhBGQLjPoxkko3baWMFac.png',
    u'ТНВ-Татарстан': logobase + 'kMdYm3qFLgK52EV0ymvRBB43peSrj9.png',
    u'ТНТ (+4)': logobase + 'eU71rcMDW3T6Ra5K7Ahh16wGf1gPvr.png',
    u'ТНТ (+7)': logobase + 'Vtt1KKIpLY4LTQGnV03sdBYyX3hyWR.png',
    u'ТНТ Comedy': logobase + 'IihdBuOBtjIeeUli9g5jR0196S9Ryk.png',
    u'ТНТ': logobase + 'Vtt1KKIpLY4LTQGnV03sdBYyX3hyWR.png',
    u'ТРК Киев': logobase + 'qW0p5z3De7COmSxTmvJ4ZA2wOuSJjg.png',
    u'ТРК Украина': logobase + '0co3dwhFDhoCVeTbfMV8ASYFYxSrWM.png',
    u'ТРО Союза': logobase + 'xAXy9iMyJ4wa2wmugJvbZuDIzc9pVz.png',
    u'Теледом HD': logobase + 'XviuCfRo0T4WFTOhFaC978AwZ1a3Ge.png',
    u'Телекафе': logobase + 'fYRFV5oY197jXcyModfWVs0AlrCOIs.png',
    u'Телепутешествия': logobase + 'fz4bqwLySJAQkUN7l2EPKNqyvilfRD.png',
    u'Техно 24': logobase + 'JbUGHLuuZa3WQbjtbzUo0cDZkGnLRK.png',
    u'Тонус ТВ': logobase + 'bE8WfReOerYTIbqPOo6VD2ajrFdOBT.png',
    u'Трофей': logobase + 'pOZb3d5BA6OkYL7qpTS4AUiihdLgZ5.png',
    u'Улыбка ребенка': logobase + 'P8aPFN50uJWJHkrqFGb7wgzfaTHUOO.png',
    u'Унiан': logobase + 'fhpFrTDoI9xx7UlK65KAjAbdTGehLL.png',
    u'Усадьба': logobase + '5yIxLQzQyZnH5EJcwpSGb28QuRTSFH.png',
    u'Успех': logobase + 'RLcfsouYRxTNrQT97AOPIYfSneJyB6.png',
    u'Феникс+ Кино': logobase + 'idiNkkBsxLwxWCF2VZrc9LQEevKh0d.png',
    u'Футбол 1 (Украина)': logobase + 'AMKtYwcgSAX5mTcPdhQDe4he18Jz7S.png',
    u'Футбол 1 HD (Украина)': logobase + 'hZaWPKLVxTqUWZk0LTmLi1K1WUzX85.png',
    u'Футбол 2 (Украина)': logobase + 'PUXTI9mKcs49JnEENkh95KoKqt9VNg.png',
    u'Футбол 2 HD (Украина)': logobase + 'TTvGrBoRM07MHY4q6bSwfzVuDKEGTi.png',
    u'Футбол': logobase + '472.png',
    u'ЧГТРК Грозный': logobase + 'LqDNdQj6nf4MraZztT6ZnACn7yOJpV.png',
    u'Шансон ТВ': logobase + 'VY0TyCCkKOj5b8BhBJjT020sQoxL9F.png',
    u'Эгоист ТВ': logobase + 'moG8uExVh4nw3MN7dmGFdysJHBWLk6.png',
    u'Ю (+2)': logobase + 'YvnG7hXCwMmHnakp2KkCbqeCigHcuK.png',
    u'Ю (+7)': logobase + 'lS7OcLo9fsdDFdDFDvdlM3OE3Uu8Tj.png',
    u'Ю': logobase + 'YvnG7hXCwMmHnakp2KkCbqeCigHcuK.png',
    u'Юмор ТВ': logobase + '6VFA1SVxeFHUsGaKPbNxWZREDkGeZw.png',
    u'Ямал Регион': logobase + 'xapccCaMjlT6JEAkZmk27wzCXlEU2m.png'
}