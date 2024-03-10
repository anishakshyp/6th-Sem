#6.
marks = float(input("Enter the marks: "))

if marks >= 90:
  grade = 'A+'
elif marks >= 80:
  if marks >= 70:
    grade = 'A'
  else:
    grade = 'B+'
elif marks >= 60:
  if marks >= 50:
    grade = 'B'
  else:
    grade = 'C+'
elif marks >= 40:
  grade = 'C'
else:
  grade = 'F'

print("Grade:", grade)