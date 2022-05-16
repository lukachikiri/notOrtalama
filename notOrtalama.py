not1=int(input("Birinci Sınav Giriniz: "))
not2=int(input("İkinci Sınav Giriniz: "))
ortalama=(not1+not2)/2
print("Ortalamanız: %s" %(ortalama))
if(ortalama>=80):   
    print("Harf Notunuz: AA")
elif(ortalama>=71):   
    print("Harf Notunuz: BA")
elif(ortalama>=63):   
    print("Harf Notunuz: BB")
elif(ortalama>=55):
    print("Harf Notunuz: CB")
elif(ortalama>=50):   
    print("Harf Notunuz: CC")
elif(ortalama>=45):
    print("Harf Notunuz: DC")
elif(ortalama>=35):
    print("Harf Notunuz: DD")
else:
    print("Harf Notunuz: FF")