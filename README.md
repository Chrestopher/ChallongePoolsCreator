# ChallongePoolsCreator

**Backstory**:
When running large tournaments on challonge, it is inefficient as a tournament organizer to manage and traverse the brackets. A solution to this is using 2 stage tournaments (or pools system). Challonge has this setting when creating a new tournament, but the way they create the pools defys the seeding and competitive integrity of the seed. For example, Challonge takes the top 10 seeds and puts them into one pool where 2 make it out to the final bracket. Seeding is a prediction of placement so the top 10 must be spread out into each individual pool. This program takes a 2 stage tournament and seeds it accordingly to make even seeding throughout all pools. This program is designed for small local scenes who are approaching a large amount of entrants where running pools would be more efficient.


**Challonge Setup**:

Create a tournament in challonge with these settings:

**Initialize type of tournament**

Game Info -> Type ->  Two Stage Tournament — groups compete separately, winners proceed to a final stage (e.g. World Cup)

**Group Stage Setup**

Game Info -> Group Stage -> Single Elimination, Double Elimination, Round Robin (Can be anything)

Game Info -> Group Stage -> participants compete in each group

This setting must be calculated to obtain correct results for pools. entrants per pool = roundup(total entrants / number of pools)

For example: 76 entrants, I want 8 pools. 76 / 8 = 9.5 -> 9.5 roundup = 10

Game Info -> Group Stage -> participants advance from each group

**Final Stage Setup**

Game Info -> Final Stage -> Single Elimination, Double Elimination, Round Robin, Swiss (Can be anything, recommend using double elim)


**Program Setup**:

Place your API Key in keys.txt
The API Key can be found on your challonge account at this address (https://challonge.com/settings/developer)

Run the executable file and provide the required inputs


