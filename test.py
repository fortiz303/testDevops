first_name = input('what is your name?')
print('hello', first_name)

if first_name == 'Craig':
	print(first_name, 'is learning Python by himself.')
elif first_name == 'Nick':
	print(first_name, 'is learning with the other folks')
else:
	age=int(input('how old are you? '))
	if age <= 6:
		print('Wow you are {}'.format(age))
	print('You should totally learn {}'.format(first_name))

first_name = input('what is your first name?')
print('hi {}'.format(first_name))
