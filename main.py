from random import randint

# генерується число 
random_number = randint(1, 100)

# цикл
while True:
	ans = int(input("Вкажіть число від 1 до 100"))
	if ans > random_number:
		print("Моє число менше")
	elif ans < random_number:
		print("Моє число більше")
	else:
		print("Вітаю ти вгадав це було", random_number)
		break
