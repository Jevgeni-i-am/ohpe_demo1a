luku = 0
print("Luku on", luku)
syotto = str(input("Anna operaatio(tyhjä lopettaa): "))
operaatio = syotto[0]
operaation_luku = int(syotto[1:])

# Testataan muuttujaat
print("SYÖTTÖ", type(syotto), syotto)
print("OPERAATIO:", type(operaatio), operaatio)
print("OPERAATION LUKU:", type(operaation_luku),  operaation_luku)
# Testi loppuu

while syotto:

    if operaatio == '+':
        luku = luku+operaation_luku
        print("FOUND  +   ! Luku on: ", luku)

    elif operaatio == '-':
        luku = luku-operaation_luku
        print("FOUND  -   ! Luku on: ", luku)
    elif operaatio == '*':
        luku = luku*operaation_luku
        print("FOUND  *   ! Luku on: ", luku)
    elif operaatio == '/':
        luku = luku/operaation_luku
        print("FOUND  /   ! Luku on: ", luku)

    elif syotto == "":
        print("LOPETETAAN. SYÖTETTY TYHJÄ")
        break
print("Kiitos ja moi!")
