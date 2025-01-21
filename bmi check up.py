weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in Meter: "))

bmi = weight / (height**2)

print(f"Your BMI is {bmi}")

if bmi <= 18.4:
    print("You are underweight.")
    
elif bmi <= 24.9:
    print("You are healthy.")
    
elif bmi <= 29.9:
    print("You are over weight.")
    
elif bmi <= 34.9:
    print("You are obese.")
    
else:
    print("You are severely obese.")