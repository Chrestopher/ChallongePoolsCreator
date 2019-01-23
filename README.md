# ChallongePoolsCreator

**Backstory**:
When running large tournaments on challonge, it is inefficient as a tournament organizer to manage and traverse the brackets. A solution to this is using 2 stage tournaments (or pools system). Challonge has this setting when creating a new tournament, but the way they create the pools defys the seeding and competitive integrity of the seed. For example, Challonge takes the top 10 seeds and puts them into one pool where 2 make it out to the final bracket. Seeding is a prediction of placement so the top 10 must be spread out into each individual pool. This program takes a 2 stage tournament and seeds it accordingly to make even seeding throughout all pools. This program is designed for small local scenes who are approaching a large amount of entrants where running pools would be more efficient.


**Instructions**:
1. In CPC.py, fill in the fields at the top and then run.

python CPC.py (tournament_id) (number of pools) (pool survivors)

Ex: python CPC.py adnkfla 5 1
this would seed the tournament to have 5 pools and 1 entrant per pool make it to the final bracket

Pools will be in output.txt

