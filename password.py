import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!','@','#','$','%','^','&','*','(',')','_','+']
numbers = ['1','2','3','4','5','6','7','8','9','0']
print("Welcome to Random password Generator...")
n_letters = int(input("How many letters you wish to have in your password ..: \n"))
n_symbols = int(input("How many symbols you wish to have in your password ..: \n"))
n_numbers = int(input("How many numbers you wish to have in your password ..: \n"))

#easy level
# password = ""
# for i in range(0,n_letters):
#     password += random.choice(letters)
# for i in range (0,n_symbols):
#         password += random.choice(symbols)
# for i in range (0, n_numbers):
#     password += random.choice(numbers)
#
# print(password)

#hard level
password_list = []
for i in range(0,n_letters):
    password_list.append(random.choice(letters))
for i in range (0,n_symbols):
        password_list.append(random.choice(symbols))
for i in range (0, n_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = "".join(password_list)
print(f"Your generated password is {password}")
