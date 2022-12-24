import re
import pickle
import difflib 
from pprint import pprint
import pytest
from pathlib import Path

class Spellcheck():
    
    def __init__(self,):
        with open("wordlist.bin","rb") as f:
            self.spell_wordlist = pickle.load(f)
        
    def split_sentence(self,test_string):
        str_2 =  re.split("[\.\|\।]",test_string)
        return [i+" । " for i in str_2 if len(i.strip()) > 0 ]
    
    def spell_check(self,test_list):
        spell_check_list=[]
        for i,x in enumerate(test_list):
            for j in x.split():
                if j not in self.spell_wordlist:
                    if j.isnumeric() is False:
                        spell_check_list.append(j)
        return spell_check_list

    def spell_check_index(self,test_list):
        spell_check_index=[]
        for i,x in enumerate(test_list):
            for j in x.split():
                if j not in self.spell_wordlist:
                    if j.isnumeric() is False and not j.isalnum():
                        spell_check_index.append(i)
        return spell_check_index
        
    def calculation(self,test_list_1,test_list_2):
        index = test_list_1
        words = test_list_2
        d={}
        for y in range(len(index)):
            key = index[y]
            if key not in d:
                d[key] = []
            d[key].append(words[y])
        return d
    
    def recommend(self,test_list_1):
        reco = {}
        wd= test_list_1
        for j in self.spell_wordlist:
            for x in range(len(wd)):
                key = wd[x]
                if key not in reco:
                    reco[key] = []
                a = difflib.SequenceMatcher(None, wd[x], j).ratio()
                if(a > 0.8):
                    reco[key].append(j)
        return reco

    def call(self, test_string):
        dic = {}
        dic["Data"]=self.split_sentence(test_string)
        dic["Spell_check"]={}
        dic["Spell_reco"]={}
        dic["Spell_check"] = self.calculation(self.spell_check_index(dic["Data"]),self.spell_check(dic["Data"]))
        dic["Spell_reco"] = self.recommend(self.spell_check(dic["Data"]))
        return dic
        

r = Spellcheck()
test_string = """नमस्कार, महिला दवस की शुभकामनाएं। आज सबसे जयादा महिला सशक्तकरण की बात होंग।"""
test_string1 = "खेद क बात है, लेकिन वसा ही है।"
test_string2 = "माफ़ कीजए।"


output = r.call(test_string2)

print(output)
