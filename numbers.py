for value in range(1,5):
 print(value)
'only prints 1-4'

for value in range(1,6):
 print(value)
'only prints 1-5'

numbers = list(range(1,6))
print (numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)
'prints numbers from 2 to 10 every other one'

for poop in list(range(2,11)):
	print (poop)


squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)
'1 x 1 x 1'
'1 x 2 x 2'
'1 x 3 x 3'

squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)

numbers = list(range(1,21))
min(numbers)

