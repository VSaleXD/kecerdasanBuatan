def BMI(weight, height):
    global bmi
    height = height / 100
    bmi = weight / (height ** 2)
    return bmi

def golongan():
    if(bmi < 18.5):
        return "Below normal weight"
    if(18.5 <= bmi < 25):
        return "Normal weight"
    if(25 <= bmi < 30):
        return "Overweight"
    if(30<= bmi < 35):
        return "Class I Obesity"
    if(35 <= bmi < 40):
        return "Class II Obesity"
    if(bmi >= 40):
        return "Class III Obesity"
    

def main():

    weight, height = input().split()
    weight = float(weight)
    height = float(height)
    BMI(weight, height)
    print(f"{golongan()}")

main()