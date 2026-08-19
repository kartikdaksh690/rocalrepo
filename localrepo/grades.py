marks=float(input("Enter your marks: "))
if marks>100:
    print("Invalid marks. Please enter marks between 0 and 100.")
elif marks>=90:
    print("Grade A")
elif marks>=80:
    print("Grade B")
elif marks>=70:
    print("Grade C")
elif marks>=60:
    print("Grade D")
elif marks>=50:
    print("Grade E")
elif marks>=40:
    print("Grade F")
else:
    print("Fail")   
    print("You need to work hard to pass the exam.")     