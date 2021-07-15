# Basic Text Summarization with weighted frequency

1) Paragraph is split into sentences and punctuations removed
2) Remove stop words, these are words like 'The','You' and so on
3) Tokenize the words
4) Get a collection of words and their occurance
5) Now get their weights. The word frequency over the frequency of the most occuring word
6) Total up scores for each sentence.
