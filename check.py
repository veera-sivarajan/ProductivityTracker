def check(activity):
    result = False
    print("Completed " + activity + "?:")
    response = input()
    if response == 'Y':
        result = True
    return result


