"""
This module contains the knowledge base for the chatbot with normal, conversational replies.
"""

# Dictionary mapping keywords/intents to lists of possible responses
RESPONSES = {
    # Greetings & Closings
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you today?"],
    "hi": ["Hello!", "Hi!", "Hi there! What's on your mind?"],
    "hey": ["Hey!", "Hello!", "Hey! How's it going?"],
    "good morning": ["Good morning! Hope you have a great day!", "Morning! How can I assist you?"],
    "good afternoon": ["Good afternoon! How is your day going?", "Hello! Good afternoon!"],
    "good evening": ["Good evening! How can I help you tonight?", "Evening! Hope you're having a nice one."],
    "bye": ["Goodbye!", "Bye! Have a great day!", "See you later!", "Take care!"],
    "goodbye": ["Goodbye!", "Until next time!", "Have a wonderful day!"],
    "see you": ["See you soon!", "Catch you later!", "Goodbye for now!"],
    "night": ["Goodnight!", "Sleep well!", "See you in the morning!"],
    
    # Personal & Identity
    "who are you": ["I am a rule-based chatbot created for your task.", "I'm your python assistantbot!"],
    "what is your name": ["You can call me PythonBot.", "I go by PythonBot."],
    "how are you": ["I'm doing great, thank you for asking!", "I'm doing well, how about you?"],
    "how's it going": ["Everything is going smoothly!", "I'm doing well, how are things with you?"],
    "are you human": ["No, I am a computer program written in Python.", "I'm a chatbot, not a human."],
    "where do you live": ["I live inside your computer!", "I exist right here in the code."],
    "old are you": ["I was created recently for this project!", "Age doesn't really apply to a program like me."],
    "your creator": ["I was built using Python for this internship assignment.", "A programmer built me to help answer questions."],
    
    # Help & Capabilities
    "help": ["I can chat with you about various topics! Try saying hello, asking for a joke, or asking about the weather.", "I'm here to help! What do you need?"],
    "what can you do": ["I can answer simple questions, tell jokes, or just have a basic conversation.", "I am designed to respond to specific keywords you type."],
    "options": ["You can say hello, ask for a joke, talk about Python, or ask about the weather."],
    
    # Python & Programming
    "python": ["Python is a versatile and popular programming language!", "I love Python! It's what I am built with."],
    "programming": ["Programming is the art of writing instructions for computers.", "It is a great skill to learn!"],
    "code": ["Writing code is like solving an interesting puzzle.", "I am entirely made of code!"],
    "java": ["Java is a good language, but Python is often easier to read.", "Every programming language has its own uses."],
    "html": ["HTML is used for building the structure of websites.", "HTML is essential for web development."],
    
    # Fun & Entertainment
    "joke": ["Why did the programmer quit his job? Because he didn't get arrays (a raise)!", "Why do programmers wear glasses? Because they can't C#."],
    "funny": ["I try my best to have a good sense of humor!", "Glad you found that funny!"],
    "music": ["I can't listen to music, but I know it's great! What's your favorite genre?", "Music is wonderful. Do you have a favorite band?"],
    "movie": ["I can't watch movies, but sci-fi films sound interesting!", "What is your favorite movie?"],
    "game": ["Video games are a great way to relax and have fun.", "Do you enjoy playing video games?"],
    "book": ["Books are a fantastic source of knowledge and stories.", "What is the best book you have read recently?"],
    
    # Weather & Nature
    "weather": ["I can't check the live weather, but I hope it is nice outside!", "Make sure to check your local forecast before heading out!"],
    "rain": ["Rain is great for plants and nature.", "Make sure to grab an umbrella if it is raining!"],
    "sun": ["Sunny days are wonderful for spending time outdoors.", "Don't forget to enjoy the sunshine today!"],
    "snow": ["Snow looks beautiful, but make sure to stay warm!", "Snowy weather is perfect for a hot drink indoors."],
    "nature": ["Nature is amazing! It is always fascinating to learn about wildlife.", "The natural world is full of beautiful places."],
    
    # Food & Drink
    "food": ["I don't eat food, but pizza seems to be a popular favorite!", "What is your favorite meal?"],
    "pizza": ["Pizza is delicious! What toppings do you usually choose?", "You can never go wrong with a good pizza."],
    "coffee": ["Coffee is a favorite drink for many programmers!", "A lot of people rely on coffee to start their day."],
    "tea": ["Tea is very relaxing and soothing.", "Do you prefer green tea, black tea, or herbal tea?"],
    "water": ["Staying hydrated is very important for your health!", "Make sure to drink enough water today."],
    
    # Emotions & Feelings
    "happy": ["That is great to hear! I'm glad you're in a good mood.", "Awesome! Happiness makes everything better."],
    "sad": ["I'm sorry to hear that. I hope your day gets better soon.", "I'm here if you want to chat and clear your mind."],
    "angry": ["Take a deep breath. It is completely okay to feel annoyed sometimes.", "Try to relax and take a short break."],
    "tired": ["You should definitely get some rest!", "Make sure to get a good night's sleep tonight."],
    "bored": ["Let's chat! Or maybe you could work on a fun Python project.", "I can tell you a joke if you want to clear the boredom."],
    
    # Common Questions
    "why": ["That is an interesting question!", "Sometimes things are just the way they are."],
    "how": ["It usually depends on the specific situation.", "I can try to help you figure it out!"],
    "when": ["Timing is everything!", "You can check your system clock for the current time."],
    "where": ["Location matters!", "I am right here running inside your console terminal."],
    
    # Affirmation & Negation
    "yes": ["Great!", "I agree!", "Awesome!", "Exactly!"],
    "no": ["I understand.", "No problem.", "Alright, maybe next time.", "Okay."],
    "maybe": ["Take your time to think about it.", "It's completely fine to be undecided."],
    "thanks": ["You're very welcome!", "No problem at all!", "Happy to help!", "Anytime!"],
    "thank you": ["You're welcome!", "My pleasure!", "Glad I could assist you!"],
    
    # Miscellaneous
    "ok": ["Okay!", "Alright.", "Got it."],
    "cool": ["Yes, that is very cool!", "I agree, that's awesome."],
    "wow": ["It is impressive, isn't it?", "Glad you think so!"],
    "really": ["Yes, absolutely!", "That's correct."],
    "interesting": ["It really is fascinating!", "Tell me more about it."],
    "awesome": ["That's great!", "It really is excellent."],
    "great": ["Fantastic!", "Wonderful!", "That's excellent news!"],
    "good": ["Good to hear!", "That is nice."],
    "bad": ["I'm sorry to hear that.", "Hopefully, things look up soon."],
    "nice": ["It is nice, isn't it?", "Glad you think so."],
    "love": ["That is a very positive and kind sentiment!", "Spread the love!"],
    "hate": ["Let's try to focus on positive things instead.", "I'm sorry you feel that way."],
    "time": ["Time flies when you are busy!", "Check your computer's taskbar for the exact time!"],
    "date": ["You can see today's exact date on your computer's clock.", "Every day is a good day to practice coding!"],
    "math": ["Math is the core language of computer science!", "I love numbers! Simple calculations are easy for me."],
    "science": ["Science helps us discover how the universe works.", "Learning about scientific discoveries is always exciting."],
    "history": ["History is full of fascinating events that shape our world today.", "Learning about the past is always interesting."],
    "art": ["Art is a beautiful way for people to express creativity.", "Creativity makes the world a much better place."],
    "sport": ["Sports are fantastic for staying active and healthy.", "Do you follow any specific sports teams?"],
    "travel": ["Traveling is an excellent way to see new places and cultures.", "Where is your absolute dream travel destination?"],
    "family": ["Spending time with family is incredibly valuable.", "I hope your family is doing well!"],
    "friend": ["Friends make life much more enjoyable.", "Good friends are always important to have."]
}

import random

def get_response(user_input):
    """
    Checks the user input against predefined keywords 
    and returns a random matching response.
    """
    user_input = user_input.lower()  # Normalize input to lowercase
    
    # Check if any keyword exists in the user's message
    for keyword in RESPONSES:
        if keyword in user_input:
            return random.choice(RESPONSES[keyword])
            
    # Default fallback message if no keywords match
    return "I'm not sure I understand that. Can you rephrase?"
