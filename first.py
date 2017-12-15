# with open("nopage.txt","r") as f:
#     wordlist = [r.split()[0] if r is not '\n' else '\n' for r in f]

# print("\n".join(wordlist))
# with open("wordsOE.txt", "w") as d_file:
#     d_file.write("\n".join(wordlist))

#import nltk
# nltk.download()

# from nltk.corpus import brown
# print(brown.words())

# import os, os.path
# path = os.path.expanduser('~/nltk_data')
# if not os.path.exists(path):
# 	os.mkdir(path)

# print(os.path.exists(path))

# import nltk.data
# print(path in nltk.data.path)

# import nltk.data
# l = nltk.data.load('/Users/lucasrosenblatt/nltk_data/corpora/oldenglish/wordsOE.txt', format='raw')
# print(l)

# from nltk.corpus.reader import WordListCorpusReader
# reader = WordListCorpusReader('/Users/lucasrosenblatt/nltk_data/corpora/yceo', ['wordlist'])
# print(reader.raw())

#print(nltk.corpus.reader.yceo.fileids())
# from nltk.corpus.reader import TaggedCorpusReader
# reader = TaggedCorpusReader('/Users/lucasrosenblatt/nltk_data/corpora/oldenglish', 'taggedOEnp.pos')
# print(reader.tagged_paras())
with open("taggedOEnpnouns.pos","r") as f:
    wordlist = [r if '/nn' in r or if '/fw' in r or if '/ls' in r else '\n' for r in f]

print("\n".join(wordlist))
with open("taggedOEnpnounsDone.txt", "w") as d_file:
    d_file.write("\n".join(wordlist))
# import nltk
# with open('JudithPlainText.txt', 'r') as myfile:
#     judith=myfile.read()
# tokens = nltk.word_tokenize(judith)
# import pickle
# tagger = pickle.load(open("/Users/lucasrosenblatt/nltk_data/taggers/oldenglish_aubt.pickle",'rb'))
# t = tagger.tag(tokens)
# words = [word + ' (' + tag + ') ' for (word,tag) in t]
# print("".join(words))
