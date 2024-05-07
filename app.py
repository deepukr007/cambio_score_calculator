import streamlit as st
import pandas as pd

class Player:
    def __init__(self, name):
        self.name = name
        self.scores = []
        self.cumulative_score = 0

    def add_score(self, score):
        self.scores.append(score)
        self.cumulative_score += score


st.title("Cambio Score Calculator")

num_of_players = st.sidebar.number_input("Number of Players", min_value=0, max_value=10, step=1)


if st.session_state.get("players") is None:
    st.session_state["players"] = []



player_names = []
for i in range(num_of_players):
    player_name = st.sidebar.text_input(f"Player {i+1} Name")
    player_names.append(player_name)


    
scores = []

if st.sidebar.button("Start Game"):
    st.session_state["players"] = [Player(name) for name in player_names]
    st.balloons()

if len(st.session_state.get("players")) > 0 :
    for player in st.session_state["players"]:
        score = st.number_input(f"Enter score for {player.name}", key=player.name , value=None, placeholder="Type a number...")
        scores.append(score)
      
    if st.button("Next Round"):
        for player in st.session_state["players"]:
            player.add_score(scores.pop(0))

    data = []
    for player in st.session_state["players"]:
        data.append([player.name] + player.scores + [player.cumulative_score])
    df = pd.DataFrame(data, columns=['Player'] + [f'Round {i+1}' for i in range(len(st.session_state["players"][0].scores))] + ['Cumulative score'])
    st.table(df)