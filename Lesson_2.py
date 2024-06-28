import random
symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = int(input("What is the length of your password: "))
password = ""
for i in range(length):
    password += random.choice(symbols)
print(password)

symbols_b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols_s = "qwertyuiopasdfghjklzxcvbnm"
length_w = int(input("How long is your nickname: "))
login = random.choice(symbols_b)
for i in range(length_w - 1):
    login += random.choice(symbols_s)
print(login)