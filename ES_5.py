#chiedo 2 numeri float deve stampare una stringa con i 2 numeri in ordine decrescente
a=float(input("inserisci un numero: "))
b=float(input("inserisci un numero: "))

if a>b:
    a, b=b, a
else:
    b, a= a, b

print(f"maggiore è {mag}")