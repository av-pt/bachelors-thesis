from converters import g2p, g2sc

hello = 'Hello World!'
print('Original: ' + hello)
print('IPA: ' + g2p(hello))
print('Dolgo: ' + g2sc(hello))