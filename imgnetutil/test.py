import imgnetutils

info = imgnetutils.ImageNetInfo()
info.load('urls 3.txt')
info.mapWnids('words.txt')
info.downloadImages()
