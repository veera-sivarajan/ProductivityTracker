import matplotlib.pyplot as plt
def plot(x, y):
	plt.xlabel('Date')
	plt.ylabel('Points')
	plt.title('Productivity Tracker')
	plt.plot(x, y)
	plt.show()
