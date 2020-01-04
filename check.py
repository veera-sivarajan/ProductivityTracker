

def check(activity):
    result = False
    print("Completed " + activity + "?:")
    response = input()
    if response == 'Y':
        result = True
    return result

def check_time(required_time):
    time_spent = float(input("Enter time spent:"))
    if time_spent >= required_time:
        return required_time
    else:
        return 0

