import requests
import sys

# FILL THESE IN FIRST

# From Challonge: Developer API Key
api_key = ''

# Account Username
username = ''

# Subdomain (ex: rocnysmash)
subdomain = ''

# url for the tournament, after challonge.com/{url}
tournament_url = sys.argv[1]

if __name__ == '__main__':

    print("Challonge settings: ")
    print("2 Stage - Double Elim")
    print("Set number of entrants in each pool to total entrants/8 rounded up ex: 75 entrants 75/8 =9.xxx round up to 10")

    if subdomain == '':
        url = "https://" + username + ":" + api_key + "@api.challonge.com/v1/tournaments/" + tournament_url + "/participants"
    else:
        url = "https://" + username + ":" + api_key + "@api.challonge.com/v1/tournaments/" + subdomain + "-" + tournament_url + "/participants"

    get_all_url = url + ".json"

    response = requests.get(get_all_url).json()

    seeded_entrants = []
    pools = []

    # Append participants of response, write to input file, before the pools program runs

    f = open('files/input.txt', 'w')
    for item in response:
        entrant = item['participant']["name"]
        seeded_entrants.append(entrant)
        f.write(entrant + '\n')

    f.close()

    # Determine how many bye entrants challonge needs to even up pools

    count = len(seeded_entrants)

    # How many bye entrants to create perfectly split between 8 pools
    blank_slots = 8 - (count % 8)

    for i in range(0, blank_slots):
        seeded_entrants.append("bye" + str(i))
    count = len(seeded_entrants)

    # Write to file, create pool
    f = open('files/output.txt', 'w')
    for i in range(0, 8):
        index_list = []
        for j in range(i, count, 8):
            seeded_entrants_copy = seeded_entrants.copy()
            entrant = seeded_entrants_copy.pop(j)
            index_list.append(entrant)
            f.write(entrant + '\n')
        pools.extend(index_list)

    f.close()

    clear_url = url + "/clear.json"

    response = requests.delete(clear_url)

    # Bulk add contents into bracket

    bulk_add_url = url + "/bulk_add.json"

    data = {"participants[][name]": pools}

    response = requests.post(bulk_add_url, data=data)
