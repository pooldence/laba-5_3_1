import math
import random
alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ.,/;[]{}!@#$%^&?*()"
S = (10*60*24*7 * 5/7) / math.pow(10, -6)
dlinaAlf = len(alphabet)
dlina = 0
while math.pow(dlinaAlf, dlina) <= S:
    dlina += 1
password=''
for i in range(dlina):
    password=password+alphabet[random.randint(0, dlinaAlf-1)]
print("Сгенерированный пароль: \n",password)
print("Взлом пароля возможен за : ",(dlinaAlf**dlina* math.pow(10, -6))/(10*60*24 * 7))
