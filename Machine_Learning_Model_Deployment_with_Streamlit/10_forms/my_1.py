import streamlit as st

choice = ["choice1", "choice2", "choice3"]

# Creating the form with a unique identifier
with st.form("dinner_form"):
    # Form fields
    appetizer = st.selectbox("Appetizers", options=choice)
    main_course = st.selectbox("Main Course", options=choice)
    dessert = st.selectbox("Dessert", options=choice)
    wine = st.checkbox("Are You Bringing Your Own Wine?")
    date = st.date_input("On What Date Are You Coming?")
    visit_time = st.time_input("At what time are you coming?")
    allergies = st.text_area(
        "Any allergies?", placeholder="Leave us a note for allergies")

    # Submit button inside the form
    submit_button = st.form_submit_button(label="Submit")

# Check if the form is submitted
if submit_button:
    st.write(f"Appetizer: {appetizer}")
    st.write(f"Main Course: {main_course}")
    st.write(f"Dessert: {dessert}")
    st.write(f"Bringing Wine: {wine}")
    st.write(f"Arrival Date: {date}")
    st.write(f"Visit Time: {visit_time}")
    st.write(f"allergies: {allergies}")
