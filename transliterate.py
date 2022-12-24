from googletrans import Translator 
# from hindiwsd import wsd

# my_input= ("I am very happy to be here with you today to receive the Nobel Prize for Peace.")

# print(my_input)

translator = Translator()

# sentences = ['The quick brown fox', 'jumps over', 'the lazy dog', "i am going home","how are you doing"]
# translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='hi')
# for sentence in sentences:
#     transliterated_txt=translator.translate(sentence, dest='hi').text
#     print(sentence," -> ",transliterated_txt)

# # for translation in translations:
# #     print("translation: ",translation.origin, ' -> ', translation.text)

# #print(wsd.preprocess_transliterate('aaj achha din hai'))

# transliterated_txt=translator.translate("gujrat mn chunav natija", dest='en').text
# print("gujrat mn chunav natija-> ",transliterated_txt)


def transliterate(query):
    return translator.translate(query, dest='hi').text

