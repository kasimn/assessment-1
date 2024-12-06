mark = int(input("enter the studen's mark: "))

if mark >=70:
     grade= "A"
elif mark >=60:
     grade= "B"
elif mark >=50:
     grade= "C"
elif mark >=40:
     grade= "D"
elif mark >=30:
     grade= "E"
elif mark >=20:
     grade= "F"
else:
    grade="U"

print(f" print the student's mark {grade}")
