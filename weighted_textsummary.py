import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation
from collections import Counter
import pprint

paragraph = 'The Taj Mahal is a beautiful monument built in 1631 by an Emperor named Shah Jahan in memory of his wife Mumtaz Mahal. It is situated on the banks of river Yamuna at Agra. It looks beautiful in the moonlight. The Taj Mahal is made up of white marble. In front of the monument, there is a beautiful garden known as the Charbagh. Inside the monument, there are two tombs. These tombs are of Shah Jahan and his wife Mumtaz Mahal. The Taj Mahal is considered as one of the Seven Wonders of the World. Many tourists come to see this beautiful structure from different parts of the world.'



#Splitting paragraph into sentences using periods.
split_para = paragraph[:-1].split('.')

#Converting to lower case and removing punctuation
table = str.maketrans('','',punctuation)
sentences = [sentence.translate(table) for sentence in split_para]


#Removing stop words
stop_words = stopwords.words('english')
filtered_sentences = [words.strip() for words in sentences if words not in stop_words]

#Tokenzing the words
tokens = word_tokenize(' '.join(filtered_sentences))

#Collections of --> Words : Occurance
c = Counter(tokens)
most_freq = c.most_common()[0][1] # -> Highest frequency (int)


# List of weighted frequency of words
weighted_freq_dict = {k:v/most_freq for k,v in c.most_common()}


# Totaling scores from each word in a sentence
sentence_score = {}
for sentence in filtered_sentences:
    score = 0
    sentence = sentence.strip()
    temp_list = sentence.split(' ')
    for word in temp_list:
        freq = weighted_freq_dict[word]
        score += freq
    sentence_score[sentence + '.'] = score


sentence_score_sorted = list({k: v for k, v in sorted(sentence_score.items(),key=lambda item : item[1], reverse=True)})

#Degree of Summarization
deg_of_sum = 3

summary = ''.join(sentence_score_sorted[0:deg_of_sum])
print(summary)
