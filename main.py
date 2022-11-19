import requests, random

koo_post = input("Paste the post link: ").replace("/","")[-36:]

api_url = f'https://www.kooapp.com/apiV1/ku/{koo_post}/rekoo_users?limit=1&offset=0'
response = requests.get(api_url).json()
items = response["numItems"]
if(items == 0):
    print("The post doesn't exist or doesn't have Re-Koos, make sure you put the correct link")
    exit()

participants = []

for i in range(0,items,50):
    api_url = f'https://www.kooapp.com/apiV1/ku/{koo_post}/rekoo_users?limit=50&offset={str(i)}'
    response = requests.get(api_url).json()
    for e in response["likers"]:
        participants.append({"userHandle": e["userHandle"], "name": e["name"],})

print(f'Amount of Re-Koos: {str(items)}\n')
while(True):
    draw = input("Draw someone ?(Y/N)")
    if(draw.upper() == "Y"):
        winner = participants[random.randrange(len(participants))]
        print(f'The winner is: {winner["name"]} (@{winner["userHandle"]})')
    elif(draw.upper() == "N"):
        break
    else:
        print("choose between (Y/N)")
