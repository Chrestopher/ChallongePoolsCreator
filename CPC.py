import requests
import json
'pools for top 16'

if __name__ == '__main__':
    api_key = 'oa1peEFUK2kTFLFL4EvDEenwVdgEQIJW0am6NbQ1'
    url = "https://chresssb:" + api_key + "@api.challonge.com/v1/tournaments/rocnysmash-tpg30s4/participants.json"
    headers = {
        'api-key': api_key
    }
    response = requests.get(url, headers=headers)
    response = response.json()
    print(response)

    seeded_entrants = []

    for item in response:
        seeded_entrants.append(item['participant']["name"])
        f = open('files/input.txt', 'w')
        for line in seeded_entrants:
            f.write(line + '\n')




