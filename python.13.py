print("SHIVARAMAN COMPUTER MARK")
print("nehr stree puducherry")
print("______________________")
print("    BILL RECPIT      ")
print("  --------------      ")
no=int(input("Enter the item no:"))
name=(input("Enter the particular:"))
rate=int(input("Enter the rete:"))
qnty=int(input("Enter the quantity:"))
total=rate*qnty
print("Amount to be paid rs", total)
if(total>=100000):
    gst=total*10/100
    print("GST:",gst)
elif(total>=50000):
    gst=total*5/100
    print("GST:",gst)
elif(total>=20000):
    gst=total*3/100
    print("GST:",GST)
else:
    gst=total*2/100
    print("GST:",gst)
amt=total+gst
print("Amount to be paid",amt)
