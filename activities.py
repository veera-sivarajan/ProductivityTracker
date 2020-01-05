from datetime import datetime
from check import *
from convertlist import *
from readwrite import *

date_today = datetime.now() 
date = int(str(date_today)[8:10])
#No. of activites = 12
#No. of active hours in a day = 16.5hrs 5am - 9:30pm
data_list = list()

activities_time = {
    "Studying" : 3,
    "Assignments" : 3,
    "Coding" : 2,
    "Running" : 1,
    "Reading" : 1,
    "Table Tennis" : 3,
    "Breakfast": 0.5,
    "Lunch" : 0.5,
    "Dinner" : 1,
    "Misc:" : 1.5
}
points = 0
for activity in activities_time:
    if check(activity):
        points += check_time(activities_time[activity])

x, y = (date, points)
data_list.append(tuple((x, y)))
write(data_list)
lis = read()
readdata = list()
x_list, y_list = convertlist(lis)	
print(x_list, y_list)



