import requests
from time import sleep
try:
    response = requests.get('.https://.sdfsvsrvvs')
except BaseException as e:
    print(f"something went wrong: {e.args}")
#skips and provides the detailed error


#time_to_sleep = input("time to sleep: ")
#sleep(time_to_sleep)
try:
    a = int(input("first: "))
    b = int(input("second: "))
    res = (a/b)
    print(res)
except ZeroDivisionError:
    print("b cant be 0")
#condition for except - for example - if the error is zerodivision - print b cant be zero
