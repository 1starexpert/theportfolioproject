import streamlit as st

import pandas as pd


st.title("Decisision!!!!")

st.write("""

I have just woke up and had a sudden idea on what I want my first personal
project to be. I want to create my own Legend Tracker for Clash of Clans.
Legend Trackers already exist, but they tend to be inaccurate at times.

""")

expander = st.expander("Why Do We Need Legends Trackers?")
expander.write("""
Many people above 5000 trophies (the elo system in Clash of Clans) are constantly looking for ways to get 
better at the game. They want to climb the leaderboards of Legends League for the fame or maybe 
make some shady money on the side (see "Dark Side of Legends League).

Seeing this, many pro players see a business opportunity. Many will offer to sell their trade secrets in 
return for x amount of money. 

Clash of Clans can essentially broken down into two core aspects: Offense and Defense. Attack
the bases of other players, while defending your own from attacks. The quickest way to
get better at the game is to improve one's Offense and Defense.

This is where coaching and subscription services come in sold by pro players come in.

For offense, Pro players will offer to coach lower level players on their attacks. These
guys usually charge anywhere from 30-50 bucks an hour.

On defense, for 30 bucks a month, they will share the base layouts that they are using for
the month.

To ensure that the guys who are selling their services are not scammers, Legend Trackers
are critical. These tools allow players to track the offense and defense logs of others,
ensuring that they are not being scammed by some random joe who just bought a high ranking
account and is posing as pro. 

""")

st.subheader("Darkside of Legends League?")

st.write("""

For many, Legends League is understood to be essentially Clash's
"ranked" mode. It's the most competitive league/division in the game.
One needs to have above 5000 trophies (Clash's elo system) in order to enter.

However, to the top .01% of Legends League players, Legends League is
essentially a business. At times, it can even get quite shady.

Officially, people can make money from playing Clash of Clans in two ways:

1) Official tournaments, such as the World Championships with a prize pool
of one million dollars.

2) Content creation such as Youtube and Twitch.

This is pretty standard for most video games.

However, there is an even shadier side, one tends to be frowned upon
by the developers of the game.

Unofficially, there are three main ways people make money:

1) "Clan Mercenaries:" These are high trophy players that Clan leaders
would pay to join their clan for the month. This is done to boost their Clan
Ranking on the leaderboards and help their clan gain recognition to attract
more players. 


2) Name changes. Players in the top 5-10 of the World leaderboards
are given money to change their name temporarily for the month.

This can be anywhere from 200 to 1000 dollars per account. Remember many of
these guys are playing like 10+ accounts.

3) "Pilotting." High level players are paid to play the accounts of other
players, helping them finish higher in the World rankings at the end of every
month. Funny story, Elon Musk has been exposed for doing this with his
Diablo account.

""")




