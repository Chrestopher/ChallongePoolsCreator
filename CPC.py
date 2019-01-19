import requests
import json


#FILL THESE IN FIRST
api_key = ''   #From Challonge Developer API
username = ''  #Account Username
subdomain = '' #Subdomain (ex: rocnysmash)
tournament_url = ''  #url for the tournament, after challonge.com/{url}


if __name__ == '__main__':

    url = "https://" + username + ":" + api_key + "@api.challonge.com/v1/tournaments/" + subdomain + "-" + tournament_url + "/participants.json"
    response = requests.get(url).json()

    seeded_entrants = []

    for item in response:
        seeded_entrants.append(item['participant']["name"])
        f = open('files/input.txt', 'w')
        for line in seeded_entrants:
            f.write(line + '\n')




