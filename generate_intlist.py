from random import randint

for i in range(9999):
	x = randint(0,999999999)
	print(f'{x}')
	with open('intlist.txt','a') as f:
		f.write(f'{x}\n')
		f.close()
