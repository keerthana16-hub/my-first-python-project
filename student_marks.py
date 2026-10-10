name = input("Enter your name: ")
marks = float(input("Enter your marks: "))

if marks >= 90:
    print("Excellent!")
elif marks >= 75:
    print("Very good!")
elif marks >= 35:
    print("You passed!")
else:
    print("You need to improve.")

print("Student:", name)
print("Marks:", marks)
