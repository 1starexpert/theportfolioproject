import streamlit as st


st.title("Ground Zero:")

st.subheader("August 19, 2025")

st.write("""

After some planning, it's clear that this project won't be an easy one.
In order to track changes in a players legends trophies, I believe the
simplest way would be to constantly make api calls. Say every 30 seconds,
a python script would make a call of the supercell api to determine the
current trophy count of a player. When the trophy count increases,
it means that they gained trophies on offense. When the trophy count
decreases, it means that their village has been attacked and they have lost
trophies on defense.

All of this can probably be logged into a csv file somewhere. The main issue is,
this script would be running constantly. For a whole month. It'll have to
constantly run in the background of my computer. I find this to be inconvenient
as if my computer suddenly turns off or starts updating, the script would be
interrupted.

I've explored the idea of running this script on cloud computing softwares,
but those cost money. I'm not even sure how much computing power my script
will use, so the cost could quickly get out of hand.

Right now, the main issue is determining whether or not continuing this project
is feasible with the resources that I have.


""")

