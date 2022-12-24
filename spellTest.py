from spellcheck import *
from pprint import pprint
import pytest


r = Spellcheck()
test_string = """नमस्कार, महिला दिवस की शुभकामनाएं। आज सबसे ज्यादा महिला सशक्तिकरण की बातें होंगी।"""


output = r.call(test_string)

def test_spell():
    out = {'Data': ['ंनमस्कार, महिला दिवस की शुभकामनाएं । ',
  ' आज सबसे ज्यादा महिला सशक्तिकरण की बातें होंगी । '],
 'Spell_check': {0: ['ंनमस्कार,', 'शुभकामनाएं'], 1: ['सशक्तिकरण']},
 'Spell_reco': {'ंनमस्कार,': ['नमस्कार', 'नमस्कारं'],
  'शुभकामनाएं': ['शुभकामना', 'शुभकामनाएँ', 'शुभकामनाओं'],
  'सशक्तिकरण': []}}
    temp_1 = all([i in output for i in out])
    return temp_1
print(output)