age = int(input("Enter your age: "))

if age < 18:
    print("You're a minor.")
elif age >= 18 and age < 60:
    print("You're an adult.")
else:
    print("You're a senior citizen.")
#code 2nd example
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A 🎉")
elif marks >= 75:
    print("Grade: B 👍")
elif marks >= 60:
    print("Grade: C 🙂")
elif marks >= 40:
    print("Grade: D 😐")
else:
    print("Grade: F 😢")
