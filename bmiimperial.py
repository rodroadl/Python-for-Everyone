#bmimetric
weight_in_pounds = float(input("please enter weight in pounds: "))
height_in_inches = float(input("please enter height in inches: "))
weight = weight_in_pounds * 0.453592
height = height_in_inches * 0.0254

bmi = weight / height**2
print("BMI is:", bmi)