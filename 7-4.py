prompt = 'enter a series of pizza toppings'
prompt += '\ntype quit to end\n'
message = ""
topping = ""

while message != 'quit' :
 topping = input(message)
 print('Ill add', prompt, 'to your pizza')
 
 if message != 'quit':
	 print(message)


