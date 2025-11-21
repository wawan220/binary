import modul_binary_conv
import modul_körperberechnen

mbc=modul_binary_conv
mkb=modul_körperberechnen

##print(mbc.umrechnen_in_dezmal(input("bitte binär eingeben: \n> ")))
##print(mbc.umrechen_in_binary(int(input("bitte Dezimal eingeben: \n> "))))
##
##eingabe=input("gebe eine binärzahl ein: ")
##print(mbc.umrechnen_in_dezmal(eingabe))
##print(mbc.umrechen_in_binary(int(input("bitte Dezimal eingeben: \n> "))))


print(mkb.flaeche_berechen(float(input("gebe länge")),
                           float(input("gebe breite : "))))

print("-----------------------------")

print(mkb.volumen_berechnen(float(input("gebe länge")),
                            float(input("gebe breite : ")), 
                            float(input("gebe höhe : "))
                            ))
