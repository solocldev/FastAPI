import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.corpus import wordnet as wn
from spellCorrector import *
import yake
from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer, RegexpStemmer
from translate import *

def synonymsCreator(word):
	synonyms = []
	for syn in wn.synsets(word):
		for i in syn.lemmas():
			synonyms.append(i.name())
	return synonyms


def keywords_extraction(query):
    kw_extractor = yake.KeywordExtractor()
    result = []
    language = "en"
    max_ngram_size = 3
    deduplication_threshold = 0.9
    numOfKeywords = 20
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(query)
    for kw in keywords:
        result.append(kw[0])
    return result

def pos_tags(query):
    tokens = nltk.word_tokenize(query)
    tag = nltk.pos_tag(tokens)
    return tag

def generate_queries(query,word):
    query = query.lower()
    words = query.split(" ")
    new_query = ""
    new_queries = []
    for word in words:
        synonyms = synonymsCreator(word)
        if len(synonyms) == 0:
            break
        else:
           for synonym in synonyms:
            new_query = query.replace(word, synonym)
            new_queries.append(new_query)
    return new_queries

def preprocess_query(query,source_language,destination_language):
    print(query)
    for i in query:
        if(32 <= ord(i) <= 47  or 58 <= ord(i) <= 64 or 123 <= ord(i) <= 126 ): #32–47 / 58–64 / 91–96 / 123–126
            query.replace(i,"")
    words = word_tokenize(query)
    # porter = PorterStemmer()
    # list=[]
    # for token in word_tokenize(query):
    #     list.append(porter.stem(token))
    # query = "".join(list)
    stopword = stopwords.words('english')
    punc = list(punctuation)
    y = []
    for i in words:
        if i not in stopword and i not in punc:
            y.append(i)
            y.append(" ")
    query = "".join(y)
    try:
        keywords = keywords_extraction(query)
        query = keywords[0]
    except:
        query = query.lower()
    # new_query = []
    # for i in query:
    #     new_query.append(get_word(i))
    # return new_query
    dest_lang = dic[str(destination_language).lower()]
    result = translate_client.translate(query, target_language=dest_lang)
    result = result["translatedText"]
    return query,result

# result = preprocess_query("nike red shoes under rs 5000")
# print(result)
# for word in result.split(" "):
#     print(word)
#     print(generate_queries(result,word))