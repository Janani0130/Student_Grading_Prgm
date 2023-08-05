sub1 = int(input("Enter your First subject mark: "))
sub2 = int(input("Enter your Second subject mark: "))
sub3 = int(input("Enter your Third subject mark: "))
sub4 = int(input("Enter your Fourth subject mark: "))
sub5 = int(input("Enter your Fifth subject mark: "))
avg = (sub1+sub2+sub3+sub4+sub5)/5
print("The average mark of all 5 subject is:",avg)
if(avg>=101):
    print("It's a Invalid Mark.")
elif(avg>=90 and avg<=100):
    print("Grade: A+")
elif(avg>=80 and avg<90):
    print("Grade: A")
elif(avg>=70 and avg<80):
    print("Grade: B")
elif(avg>=60 and avg<70):
    print("Grade: C")
elif(avg>=50 and avg<60):
    print("Grade: D")
else:
    print("Grade: Fail")




