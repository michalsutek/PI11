while True:
    n = int(input("Zadaj n: "))
    print("Prvočísla:", end=" ")
    for cislo in range(2, n + 1):
        prvocilo = True
        for delitel in range(2, cislo // 2 + 1):
            if cislo % delitel == 0:
                prvocilo = False
                break
        if prvocilo:
            print(cislo, end=" ")
    print()
    if n == 0:
        break

