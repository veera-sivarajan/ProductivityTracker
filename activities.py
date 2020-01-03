from check import *
activities_list = ["Studying(3)", "Completing Assignments", "Coding", "Running", "Reading", "Playing Table Tennis", "Waking up early", "Socializing", "Writing Diary", "Talking with parents", "Attend all classes", "Clean room"]

#No. of activites = 12
#No. of active hours in a day = 16.5hrs 5am - 9:30pm

activities_dict = {
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
for activity in activities_dict:
    if check(activity):
        points += activities_dict[activity]

print("Today's score: " + str(points))
    
    
