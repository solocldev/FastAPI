import phonetics
import numpy as np

file1 = open(r"100k.txt", 'r')
Lines = file1.readlines()

code_buckets = [[] for _ in range(10)]
len_buckets = [[] for _ in range(10)]

for line in Lines:
    word = line.split("\t")[0].lower()
    code = phonetics.soundex(word)
    if len(code) < 10:
        code_buckets[len(code) - 1].append({
            "word": word,
            "code": code
        })
    else:
        code_buckets[9].append({
            "word": word,
            "code": code
        })
    if len(word) < 10:
        len_buckets[len(word) - 1].append({
            "word": word,
            "code": code
        })
    else:
        code_buckets[9].append({
            "word": word,
            "code": code
        })

def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros((size_x, size_y))
    for x in range(size_x):
        matrix[x, 0] = x
    for y in range(size_y):
        matrix[0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x - 1] == seq2[y - 1]:
                matrix[x, y] = min(
                    matrix[x - 1, y] + 1,
                    matrix[x - 1, y - 1],
                    matrix[x, y - 1] + 1
                )
            else:
                matrix[x, y] = min(
                    matrix[x - 1, y] + 1,
                    matrix[x - 1, y - 1] + 1,
                    matrix[x, y - 1] + 1
                )
    return (matrix[size_x - 1, size_y - 1])

def get_phonetic_candidates(query):
    relevant_buckets = [code_buckets[len(query) - 2], code_buckets[len(query) - 1], code_buckets[len(query)]]
    candidates = []
    for bucket in relevant_buckets:
        for candidate in bucket:
            query_code = phonetics.soundex(query)
            phonetic_distance = levenshtein(candidate['code'], query_code)
            if 1 >= phonetic_distance:
                edit_distance = levenshtein(candidate['word'], query)
                new_candidate = {
                    'word': candidate['word'],
                    'code': candidate['code'],
                    'phonetic_distance': phonetic_distance,
                    'edit_distance': edit_distance
                }
                candidates.append(new_candidate)
    return candidates


def get_edit_candidates(query):
    relevant_buckets = [len_buckets[len(query) - 2], len_buckets[len(query) - 1], len_buckets[len(query)]]
    candidates = []
    for bucket in relevant_buckets:
        for candidate in bucket:
            query_code = phonetics.soundex(query)
            edit_distance = levenshtein(candidate['word'], query)
            if 2 >= edit_distance:
                phonetic_distance = levenshtein(candidate['code'], query_code)
                new_candidate = {
                    'word': candidate['word'],
                    'code': candidate['code'],
                    'phonetic_distance': phonetic_distance,
                    'edit_distance': edit_distance
                }
                candidates.append(new_candidate)
    return candidates

query = 'sari'

def get_word(query):
    for i in get_phonetic_candidates(query):
        if(i["phonetic_distance"] == 0.0):
            return (i["word"])
    #for non-phonetic errors, we can potentiallu just use an existing inbuilt python library
   # if(get_phonetic_candidates(query)):
        #print(get_phonetic_candidates(query), get_edit_candidates(query))
# print(get_word(query))