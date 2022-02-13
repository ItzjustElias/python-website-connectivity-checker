import urllib.request
import time

from pygame.key import start_text_input

user_input = input("Give me a website > ")
rules = ("\nonly use https/http urls")


def connect(host=user_input):
    if user_input.startswith(("http", "https")):
        try:
            urllib.request.urlopen(host) #Python 3.x
            return True
        except:
            return False
    else:
        print(rules)
    exit()
# test
print( "connected🟢" if connect() else "could not connect!🔴" )

