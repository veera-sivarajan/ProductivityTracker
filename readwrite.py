def write(data_list):
	with open('data.txt', 'a') as f:
		for d in data_list:
			f.write(' '.join(str(s) for s in d) + '\n')

def read():
	with open('data.txt', 'r') as f:
		lis = f.read().splitlines()
	return lis
