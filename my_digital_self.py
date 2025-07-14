name = input("What is your name? ")
age = int(input("What is your age? "))
GPA = float(input("What is your GPA? "))
student = input("Are you currently a student? ")

if student == "yes":
    print("Wow! that's awesome")
else:
    print("Are you a college student?")
    
print("")

name = input("What is your name? ")
color = input("What is your favorite color? ")
hobby = input("What is your favorite hobby? ")
print("")

print(f"Hi {name}! It's cool that you like the color {color} and enjoy {hobby}.")