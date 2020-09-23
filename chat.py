# This will give you access to the random module or library.
# choice() will randomly return an element in a list.
# Read more: https://pynative.com/python-random-choice/

from random import choice

#combine functions and conditionals to get a response from the bot
def get_day_bot_response(user_response):

#add some bot responses to this list
#bot_response_happy = ["omg! great!", "Keep smiling!", "I love to see you happy!"]
    bot_response_Monday = ["SPD class with the ", "Sleeping in "]
    bot_response_Tuesday = ["CS class and lunch ", "Web class till 6 then dinner"]

    if user_response == "Monday":
        return choice(bot_response_Monday)

    elif user_response == "Tuesday":
        return choice(bot_response_Tuesday)

    elif user_response == "Wednesday":
        return choice(bot_response_Wednesday)

    elif user_response == "Thursday":
        return choice(bot_response_Thursday)

    elif user_response == "Friday":
        return choice(bot_response_Friday)

    elif user_response == "Saturday":
        return choice(bot_response_Saturday)

    elif user_response == "Sunday":
        return choice(bot_response_Sunday)

    else:
        return "I hope your day gets better"




print("Welcome to a day in my week bot")
print("Please enter a day, Mon-Sun to find out what I am doing")

user_response = ""
#TODO: we want to keep repeating until the user enters "done" what should we put here?
while True:
user_response = input("How are you feeling today?: ")

# Quits program when user responds with 'done'
if user_response == 'done':
    break


bot_response = get_day_bot_response(user_response)
print(bot_response)

