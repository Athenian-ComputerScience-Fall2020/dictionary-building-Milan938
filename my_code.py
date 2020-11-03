# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  

team_list = {}

while True:
    print("Please follow the prompts to input your favorite sports team")
    print("Please input the city or state your favorite sports team is from")
    city = input()
    print("Next, please enter the name of this team")
    name = input()

    team_list.update({city: name})
    question = input("Would you like to stop? Enter Yes or No: ")
    if question == "Yes":
        break

   
print(team_list)

for key, value in team_list.items():
    print(key, value)