import matplotlib.pyplot as plt
def plot(x, y):
	plt.xlabel('Date')
	plt.ylabel('Points')
	plt.title('Productivity Tracker')
	plt.scatter(x, y)
	plt.show()



