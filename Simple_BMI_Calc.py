height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
result = weight / (height ** 2)
BMI = round(result)
new_BMI = str(BMI)
if BMI < 18.5:
    print("Your BMI is " + new_BMI + ", you are underweight.")
elif BMI <= 25:
    print("Your BMI is " + new_BMI + ", you have a normal weight.")
elif BMI <= 30:
    print("Your BMI is " + new_BMI + ", you are slightly overweight.")
elif BMI <= 35:
    print("Your BMI is " + new_BMI + ", you are obese.")
else:
    print("Your BMI is " + new_BMI + ", you are clinically obese.")
