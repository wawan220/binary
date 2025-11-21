import modul_binary_conv

mbc=modul_binary_conv

print(mbc.umrechnen_in_dezmal(input("bitte binär eingeben: \n> ")))
print(mbc.umrechen_in_binary(int(input("bitte Dezimal eingeben: \n> "))))

eingabe=input("gebe eine binärzahl ein: ")
print(mbc.umrechnen_in_dezmal(eingabe))
print(mbc.umrechen_in_binary(int(input("bitte Dezimal eingeben: \n> "))))
