import requests


def get_base_data(data):

    username = data[0]
    turl = data[1]

    if turl[8:21] == 'challonge.com':
        subdomain = ''
    else:
        subdomain = turl[8:turl.index(".")]

    identifier = turl.split("/")[3]

    f = open('./key.txt', 'r')
    api_key = f.read()[9:len(f.read()) - 1]
    f.close()

    if subdomain == '':
        url = "https://" + username + ":" + api_key + "@api.challonge.com/v1/tournaments/" + identifier + "/participants"
    else:
        url = "https://" + username + ":" + api_key + "@api.challonge.com/v1/tournaments/" + subdomain + "-" + identifier + "/participants"

    return url


def creator(data):

    url = get_base_data(data)

    num_pools = int(data[2])

    get_all_url = url + ".json"

    response = requests.get(get_all_url).json()

    seeded_entrants = []
    pools = []

    # Append participants of response, write to input file, before the pools program runs

    f = open('./files/input.txt', 'w')
    for item in response:
        entrant = item['participant']["name"]
        seeded_entrants.append(entrant)
        f.write(entrant + '\n')

    f.close()


    count = len(seeded_entrants)

    # How many bye entrants to create perfectly split between X number of pools
    blank_slots = num_pools - (count % num_pools)

    for i in range(0, blank_slots):
        seeded_entrants.append("bye" + str(i))
    count = len(seeded_entrants)

    # Write to file, create pools
    f = open('./files/output.txt', 'w')
    for i in range(0, num_pools):
        index_list = []
        for j in range(i, count, num_pools):
            seeded_entrants_copy = seeded_entrants.copy()
            entrant = seeded_entrants_copy.pop(j)
            index_list.append(entrant)
            f.write(entrant + '\n')
        pools.extend(index_list)

    f.close()

    clear_url = url + "/clear.json"

    requests.delete(clear_url)

    # Bulk add contents into bracket

    bulk_add_url = url + "/bulk_add.json"

    data = {"participants[][name]": pools}

    requests.post(bulk_add_url, data=data)


def clear(data):
    url = get_base_data(data)
    clear_url = url + "/clear.json"
    requests.delete(clear_url)
