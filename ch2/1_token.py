import spacy
from utils.utils import *

# https://spacy.io/usage
# conda install -c conda-forge spacy
# python -m spacy download en_core_web_sm
# python -m spacy download ko_core_news_sm
nlp = spacy.load('en_core_web_sm')
text = "I really couldn't go out, because I had been busy preparing for a presentation"
doc = nlp(text.lower())

comment("토큰")
for token in doc :
    print(f"토큰={token} 기본형={token.lemma_} 품사={token.pos_}")
# 토큰=i 기본형=I 품사=PRON
# 토큰=really 기본형=really 품사=ADV
# 토큰=could 기본형=could 품사=AUX
# 토큰=n't 기본형=not 품사=PART
# 토큰=go 기본형=go 품사=VERB
# 토큰=out 기본형=out 품사=ADV
# 토큰=, 기본형=, 품사=PUNCT
# 토큰=because 기본형=because 품사=SCONJ
# 토큰=i 기본형=I 품사=PRON
# 토큰=had 기본형=have 품사=AUX
# 토큰=been 기본형=be 품사=AUX
# 토큰=busy 기본형=busy 품사=ADJ
# 토큰=preparing 기본형=prepare 품사=VERB
# 토큰=for 기본형=for 품사=ADP
# 토큰=a 기본형=a 품사=DET
# 토큰=presentation 기본형=presentation 품사=NOUN


comment("청크")
doc = nlp("Mary slapped the green witch")
for chunk in doc.noun_chunks :
    print(f"청크={chunk} 라벨={chunk.label_}")
# 청크=Mary 라벨=NP
# 청크=the green witch 라벨=NP