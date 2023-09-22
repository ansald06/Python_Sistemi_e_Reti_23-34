def main():
    a=1
    print(f"il valore di a è {a}")
    nome=input("come ti chiami? ")
    anni=int(input("quanti anni hai?"))
    anno_corrente=int(input("in quale anno siamo? "))
    print(f"il tuo nome è {nome} e hai {anni} anni")
    print(f"sei nato nel {anno_corrente-anni}")

if __name__=="__main__":
    main()