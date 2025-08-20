print("GOVERNMENT OF TAMILNADU")
print("_______________________")
print("     BALL RECEIPT      ")
print("-----------------------")
ebno=int(input("Enter the EB NO:"))
name=str(input("Enter the name:"))
pu=int(input("Enter the previous unit:"))
cu=int(input("Enter the current unit:"))
unit=cu-pu
print("unit consumed:",unit)
if (unit>=1000):
    ap=unit*10/100
    print("Amount to be paid:",ap)
elif(unit>=500):
    ap=unti*5/100
    print("Amount to be paid:",ap)
elif(unit>=100):
    ap=unit*2/100
    print("Amount to be paid:",ap)
else:
    print("Amount to be paid:,nil")
