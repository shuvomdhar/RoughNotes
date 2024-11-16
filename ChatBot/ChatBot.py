# Simple Chatbot Using Rule-Based Logic
# Create a rule-based chatbot using Python that can respond to simple queries.

import datetime
import requests

def get_weather(city_name):
    try:
        # Format the city name for use in the URL
        city = city_name.replace(" ", "+")
        url = f"https://wttr.in/{city}?format=%l:+%c+%t\n"

        # Make a GET request to fetch the weather data
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            print(response.text)
        else:
            print("Could not fetch weather data. Please try again.")

    except Exception as e:
        print("An error occurred:", e)

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"

    elif "how are you" in user_input:
        return "I'm just a bot, but thanks for asking! How can I help you?"

    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."
    
    elif "date" in user_input:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        return f"Today’s date is {current_date}."
    
    elif "thank you" in user_input:
        return f"You are most welcome :)"

    elif "weather" in user_input:
        city = input("Enter the Name of City -> ")
        get_weather(city)
        return "Have a Nice Day:)"

    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day."

    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase?"


print("Chatbot: Hello! Type 'bye' to exit the chat.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit"]:
        print("Chatbot: Goodbye! Have a great day.")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
