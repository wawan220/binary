def umrechen_in_binary (dezimal):
    binary_output = ""
    while dezimal != 0:
        binary_output = str(dezimal % 2) + binary_output
        dezimal = dezimal // 2
    return binary_output

def umrechnen_in_dezmal(binary):
    dezimal_output=0
    anzahlstellen=len(binary)
    for i in range(anzahlstellen):
        if binary[anzahlstellen-1-i]=="1":
            dezimal_output+=2**i
    return dezimal_output

