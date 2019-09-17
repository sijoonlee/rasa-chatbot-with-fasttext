import spacy
nlp = spacy.load('../fasttext/wiki-news-300d-1M-subword')
doc1 = nlp(u"This is an apple")
doc2 = nlp(u"I like the orange")
print(doc1.similarity(doc2))
