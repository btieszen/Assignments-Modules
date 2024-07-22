#Task1
#1. Python Modules and Data Handling Assignment
#Task 1: Your Mood Today -
# Problem Statement: Create a Python program using a custom module that asks the user how they are feeling today 
# and responds with a custom message based on the mood entered


import mood_responses

def main():
    while True:
        
        mood = input("How are you feeling today(Sad,Happy,Tired)? ").lower()
      
        if mood =="sad":
            
            print(mood_responses.mood_response_sad(mood))
        elif mood =="happy":
            
            print(mood_responses.mood_response_happy(mood))
        elif mood =="tired":
            
            print(mood_responses.mood_response_tired(mood))
        else: 
            print(" I sometimes feel ",(mood)," too")
            
main()
    


