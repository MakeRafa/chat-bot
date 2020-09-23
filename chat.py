
from random import choice


def get_day_bot_response(user_response):


#bot_response_day = ["jibber jabber about said day"]
    bot_response_Monday = ["SPD class while barely awake", "Napping or gaming it"]

    bot_response_Tuesday = ["CS class and lunch ", "Web class till 6 then dinner"]

    bot_response_Wednesday = ["SPD class ", "Doing HW all day"]

    bot_response_Thursday = ["CS class and lunch ", "Web class till 6 then dinner"]

    bot_response_Friday = ["Sleeping in because no A.M. class ", "EC while eating dinner"]

    bot_response_Saturday = ["Saturdays are for the boys"]

    bot_response_Sunday = ["Waking up after 11am", "Doing all the HW that is due "]


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
        return "My schedule is elite"




print("Welcome to a day in my week bot")
print("Choose any day to get an insight of my schedule")

user_response = ""

while True:
    user_response = input("Pick a day Monday-Sunday: ")
    if user_response == "done":
        break

    bot_response = get_day_bot_response(user_response)
    print(bot_response)