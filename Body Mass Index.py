H=input("Enter your height in m pls:")
W=input("Enter your weight in kg pls:")

height=float(H)
weight=int(W)

bmi=weight/(height*height)
#bmi=int(BMI)
print("your body mass index is:", bmi)

if bmi<18.5:
    print("underweight")
elif 18.5<=bmi<24.9:
    print("Normal")
elif 24.9<=bmi<29.9:
    print("overweight")
elif 29.9<=bmi:
    print("very overweight go workout buddy")
    
    
    
