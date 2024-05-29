fmena = open('mena.txt', 'r', encoding='utf-8')
fpriezviska = open('priezviska.txt', 'r', encoding='utf-8')
fmena_priezvska = open('mena_priezviska.txt', 'w', encoding='utf-8') # 'w' otvori subor na zapis. ak neexistuje, tak sa vytvori a ak existuje zmaze sa jeho obsah
for meno in fmena:
    priezvisko = fpriezviska.readline()
    print(f'{meno.strip()} {priezvisko.strip()}', file=fmena_priezvska)
    # fmena_priezvska.write(f'{meno.strip()} {priezvisko.strip()}\n')

fmena.close()
fpriezviska.close()
fmena_priezvska.close()

