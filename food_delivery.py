pile=int(input())
riba=int(input())
veg=int(input())
dostavka=2.50
cena_pile=pile*10.35
cena_riba=riba*12.40
cena_veg=veg*8.15
obshta_cena=cena_pile+cena_riba+cena_veg
desert=0.20*obshta_cena
finalna_cena=obshta_cena+desert+dostavka
print(f"{finalna_cena}")