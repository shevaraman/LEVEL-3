print("takshashila university")
print("ungur,tindivanam")
print("----------------")
print("STUDENT MARK LIST")
print("-----------------")
no=int(input("Enter the register no:"))
name=str(input("Enter the student name:"))
m1=int(input("Enter the python mark:"))
m2=int(input("Enter the DBMS mark:"))
m3=int(input("Enter the test automation mark:"))
total=m1+m2+m3
print("total mark:",total)
avg=total/3
print("average mark:",avg)
if (m1>=40,m2>=40,m3>40):
    print("result:pass")
else:
    print("result:fail")
if(total>=250):
    print("grade:0 grade")
elif(total>200):
    print("grade:A grade")
else:
    print("grade:B grade")
