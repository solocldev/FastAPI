# Importing necessary modules required

import speech_recognition as sr
import six
from google.cloud import translate_v2 as translate

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="banded-badge-359816-4f57409e22c9.json"

flag = 0
  
# A tuple containing all the language and
# codes of the language will be detcted
dic = {"english": "en", "spanish": "es", "french": "fr","hindi":"hi"}
  
# Capture Voice
# takes command through microphone
def takecommand():  
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='mr-IN')
        # print(f"The User said {query}\n")
    except Exception as e:
        print("say that again please.....")
        return "None"
    return query
 
    

    
  
# Input from user
# Make input to lowercase
# query = takecommand()
# while (query == "None"):
#     query = takecommand()
    
query = "nike red shoes"
translate_client = translate.Client()

text = query

if isinstance(text, six.binary_type):
    text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
# result = translate_client.translate(text, target_language="en")
# query = result["translatedText"]
# result = preprocess_query(query)
# print(result)
# print(result[0])
# transliterated_txt=translator.translate(result, dest='hi').pronunciation
# print(result," -> ",transliterated_txt)
# for word in result.split(" "):
#     print(word)
#     print(generate_queries(result,word))
# print(u"Text: {}".format(result["input"]))
# print(u"Translation: {}".format(result["translatedText"]))
# print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))


