
# Imports the Google Cloud client library
from google.cloud import speech
from queryhandler import *
import os

#Your credentials to google cloud
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"banded-badge-359816-4f57409e22c9.json"

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"

audio = speech.RecognitionAudio(uri=gcs_uri)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code="en-US",
)

# Detects speech in the audio file
response = client.recognize(config=config, audio=audio)

for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))
    print(preprocess_query(result.alternatives[0].transcript))