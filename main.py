#Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = (" ")

for i in range (1, nr_letters + 1):
  random_char = random.choice(letters)
  password += random_char


for i in range(1, nr_symbols + 1):
  random_symbol = random.choice(symbols)
  password += random_symbol


for i in range (1, nr_numbers + 1):
  random_number = random.choice(numbers)
  password += random_number

print(password)


# OR            OR               OR              OR


password = []

for char in range (1, nr_letters + 1):
  password.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password += random.choice(symbols)


for i in range (1, nr_numbers + 1):
  password += random.choice(numbers)

random.shuffle(password)

strong_password = ""

for char in password:
  strong_password += char

print(f"Your password is: {strong_password}")