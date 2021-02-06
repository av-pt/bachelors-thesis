from nltk.corpus import brown
import phonetics

#a = [phonetics.nysiis(w) for w in brown.words()[:10000]]
#print(a[:5])

brown_words = brown.words()[:10]
l = []
for w in brown_words:
    try:
        l.append(phonetics.nysiis(w))
    except Exception:
        print(f'|{w}|')
print(l)
