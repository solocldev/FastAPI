import requests
import json
import streamlit as st

# Define the title
st.title("Query Processing")

languaes = ["English","Hindi","Spanish","French"]
col1,col2= st.columns(2)
with col1:
    source_language = st.selectbox("Source languages",languaes,key=1)
with col2:
    destination_language = st.selectbox("Destination languages",languaes,key=2)
 
query = st.text_input('Enter query: ')
input = {"q":query,"source_language":source_language, "destination_language":destination_language}
if st.button("submit"):
    res = requests.post('http://localhost:8000/query',data = json.dumps(input))
    results = (res.text).split(",")
    preprocess_query = results[0]
    transliterated_txt = results[1]
    st.subheader(f"Processed Query is  {preprocess_query} and the transiliterated text is {transliterated_txt}")


# st.header("1. Record your own voice")

# filename = st.text_input("Choose a filename: ")

# if st.button(f"Click to Record"):
#     if filename == "":
#         st.warning("Choose a filename.")
#     else:
#         record_state = st.text("Recording...")
#         duration = 5  # seconds
#         fs = 48000
#         myrecording = record(duration, fs)
#         record_state.text(f"Saving sample as {filename}.mp3")

#         path_myrecording = f"./samples/{filename}.mp3"

#         save_record(path_myrecording, myrecording, fs)
#         record_state.text(f"Done! Saved sample as {filename}.mp3")

#         st.audio(read_audio(path_myrecording))

#         fig = create_spectrogram(path_myrecording)
#         st.pyplot(fig)