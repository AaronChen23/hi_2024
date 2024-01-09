tall=input("請輸入你的身高(cm):")
weight=input("請輸入你的體重(kg):")

print("你的身高是:", tall, "cm")
print("你的體重是:", weight, "kg")
print("你的BMI是:", int(weight)/(int(tall)/100)**2)