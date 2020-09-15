import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter


stop_words = set(stopwords.words('english'))



'''
So, keep working. Keep striving. Never give up. Fall down seven times, get up eight. Ease is a greater threat to progress than hardship. Ease is a greater threat to progress than hardship. So, keep moving, keep growing, keep learning. See you at work.
'''



string = ""

string = string.lower()

string_split = string.split('.')

token = word_tokenize(string)

char_to_remove = [',','.']

filtered_sentence = [i for i in token if i not in stop_words and i not in char_to_remove]


# Frequency of most occuring word
most_common = Counter(filtered_sentence).most_common(1)[0][1]

# Dictionary containing frequency of each word
filtered_sentence_dict = dict(Counter(filtered_sentence))

# Dictionary of frequency of each word divided by freq of most common word

for k,v in filtered_sentence_dict.items():
    filtered_sentence_dict[k] = v/most_common





sentence_score = {}
for i in range(len(string_split)):
    score = 0
    sentence = string_split[i].split(' ')
    for word in sentence:
        word = word.replace(',','')
        if word in filtered_sentence_dict.keys():
            score += filtered_sentence_dict[word]
        else:
            pass
    sentence_score[string_split[i]] = round(score,2)

sorted_sentence_score = {k:v for k,v in sorted(sentence_score.items(), key=lambda item: item[1], reverse = True)}

for i in range(len(list(sorted_sentence_score.items()))):
    if i != 3:
        print(list(sorted_sentence_score.items())[i][0].title() + '.')
    else:
        break
