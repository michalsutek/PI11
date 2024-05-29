fmena = open('mena.txt', 'r', encoding='utf-8') # otvori subor mena.txt ma citanie r-citanie, w-zapis
# fmena = open('C:/dokumety/mena.txt', 'r')  absolutna cesta k suboru

while True:
    riadok = fmena.readline()
    if riadok == '':
        break
    print(riadok[:-1]) # [:-1] vypíše všetky znaky od nultého po preposledný


fmena.close() # zatvorenie suboru, vždy treba!!!!

