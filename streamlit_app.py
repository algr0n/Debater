import streamlit as st
import random

# Set up the Streamlit app
st.title("AI Debates")

# Sidebar for debate setup
st.sidebar.header("Debate Controls")

# Options for topics and participants
topics = ["AI Ethics", "Climate Change", "Healthcare Policy"]
participants = ["AI Model 1", "AI Model 2"]

selected_topic = st.sidebar.selectbox("Select Debate Topic", topics)
selected_participant_1 = st.sidebar.selectbox("Select Participant 1", participants)
selected_participant_2 = st.sidebar.selectbox("Select Participant 2", participants)

# Initialize debate state
if 'debate_state' not in st.session_state:
    st.session_state.debate_state = None

# Debate functionality
if st.sidebar.button("Start Debate"):
    st.session_state.debate_state = {"topic": selected_topic, "turn": 0, "scores": {selected_participant_1: 0, selected_participant_2: 0}}
    st.success("Debate started between {} and {} on topic: {}".format(selected_participant_1, selected_participant_2, selected_topic))

if st.session_state.debate_state:
    # Display the current turn
    if st.session_state.debate_state['turn'] < 10:
        current_turn = st.session_state.debate_state['turn']
        st.markdown(f"### Turn {current_turn + 1}")
        st.text(f"Debater {participants[current_turn % 2]} to speak:")
        st.text_area("Argument", "Enter argument here...")
        # Button to submit argument
        if st.button("Submit Argument"):
            # Randomly award points for simplicity
            if random.random() > 0.5:
                st.session_state.debate_state['scores'][selected_participant_1] += 1
            else:
                st.session_state.debate_state['scores'][selected_participant_2] += 1
            st.session_state.debate_state['turn'] += 1
    else:
        st.success("Debate completed!")
        st.write("Final Scores:")
        st.write(st.session_state.debate_state['scores'])
        st.balloons()

# Display leaderboard based on random performance analytics
st.sidebar.header("Performance Analytics")
if st.sidebar.button("Show Leaderboard"):
    leaderboard = {"AI Model 1": random.randint(0, 10), "AI Model 2": random.randint(0, 10)}
    st.sidebar.write("### Leaderboard")
    st.sidebar.write(leaderboard)