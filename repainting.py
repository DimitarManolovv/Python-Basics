nailon=int(input())
boq=int(input())
razreditel=int(input())
chasove=int(input())
oshte_boq=boq*0.10
oshte_nailon=2
torbichki=0.40
suma_nailon=(nailon+oshte_nailon)*1.50
suma_boq=(boq+oshte_boq)*14.50
suma_razreditel=razreditel*5.00
suma_materiali=suma_nailon+suma_boq+suma_razreditel+torbichki
suma_maistori=(suma_materiali*0.30)*chasove
kraina_suma=suma_materiali+suma_maistori
print(f"{kraina_suma}")