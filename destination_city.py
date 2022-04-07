
#!/usr/bin/env python3
   
import random
   
vacation_cities = {
           "Spring": ["Miami", "Myrtle Beach", "New Orleans", "Los Angeles"],
           "Summer": ["New York", "Chicago", "Denver"],
           "Fall": ["Atlanta", "Houston"],
           "Winter": ["Aspen"]
 }
 
vacation_cities["Winter"].append("Toronto")
print("New winter location added:", vacation_cities["Winter"][1])
def destination_find():
 curr_season = ""
 choice = ""
 while curr_season == "" or choice == "" :
  curr_season = input("What season is it?").capitalize()
 
 if curr_season in ["Fall"]:
  choice = vacation_cities["Fall"][random.randint(0, len(vacation_cities["Fall"]) -1)]
  print(f"Your next fall vacation destination is {choice}")
  
 elif curr_season in ["Spring"]:
  choice = vacation_cities["Spring"][random.randint(0, len(vacation_cities["Spring"]) -1)]
  print(f"Your next spring vacation destination is {choice}")
  
 elif curr_season == "Winter":
  choice = vacation_cities["Winter"][random.randint(0, len(vacation_cities["Winter"]) -1)]
  print(f"Your next winter vacation destination is {choice}")
 
 elif curr_season == "Summer":
  choice = vacation_cities["Summer"][random.randint(0, len(vacation_cities["Summer"]) -1)]
  print(f"Your next summer vacation destination is {choice}")
  
 else:
  print("Enter valid season")
 
destination_find()
