def convertlist(lis):
	returndata, x_list, y_list = list(), list(), list()
	for i in range(len(lis)):
		for j in range(len(lis[i])):
			if j == 0 or j == 2:
				returndata.append(int(lis[i][j]))
	for ind in range(len(returndata)):
		if ind % 2 == 0:
			x_list.append(returndata[ind])
		else:
			y_list.append(returndata[ind])
	return (x_list, y_list)

