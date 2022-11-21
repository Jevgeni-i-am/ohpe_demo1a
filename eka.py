"""
Tehtävä 1 (50 % )
Kirjoita editorilla ohjelma, joka kysyy käyttäjältä kolme lukua ja tulostaa luvuista pienimmän.
Ohjelman tulee siis toimia esim. seuraavasti:
Anna luku 1: 25
Anna luku 2: -123
Anna luku 3: 11
Pienin luku oli - 123.
Tallenna ohjelma nimellä eka.py.
Luo Gitlabiin julkinen tietovarasto, jonka nimi on ohpe_demo1a. Lähetä kirjoittamasi ohjelma tietovarastoon.
Jaa tietovaraston linkki ViLLEssä kierroksella Demo 1 olevaan tehtävään Tehtävä 1. Muista lähettää palautuksesi!
 """


list = []
round = 0

while True:
    luku = int(input("Anna luku: "))
    list.append(luku)
    round += 1
    if round == 3:
        list.sort()
        pienin = list[0]
        print(f'Pienin luku oli {pienin}')
        break
