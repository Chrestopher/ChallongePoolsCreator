import requests
import sys

#FILL THESE IN FIRST
api_key = ''   #From Challonge Developer API
username = ''  #Account Username
subdomain = 'rocnysmash' #Subdomain (ex: rocnysmash)
tournament_url = sys.argv[1]  #url for the tournament, after challonge.com/{url}



# For clearing entrants
# url = "https://" + username + ":" + api_key + "@api.challonge.com/v1/tournaments/apitestinglollmao/participants/clear.json"
# response = requests.delete(url)

if __name__ == '__main__':

    print("Challonge settings: ")
    print("Set number of entrants in each pool to total entrants/8 rounded up")


    url = "https://" + username + ":" + api_key + "@api.challonge.com/v1/tournaments/" + subdomain + "-" + tournament_url + "/participants.json"
    response = requests.get(url).json()

    seeded_entrants = []
    pools = []
    for item in response:
        seeded_entrants.append(item['participant']["name"])
        f = open('files/input.txt', 'w')

    count = len(seeded_entrants)

    blank_slots = 8 - (count % 8)
    for i in range(0, blank_slots):
        seeded_entrants.append("bye" + str(i))

    count = len(seeded_entrants)

    for i in range(0, 8):
        index_list = []
        for j in range(i, count, 8):
            seeded_entrants_copy = seeded_entrants.copy()
            #print(str(j+1) + ": " + seeded_entrants_copy[j])
            index_list.append(seeded_entrants_copy.pop(j))
        pools.extend(index_list)

    f = open('files/output.txt', 'w')
    for line in pools:
        f.write(line + '\n')

    print("Check files/output.txt for bulk add text")