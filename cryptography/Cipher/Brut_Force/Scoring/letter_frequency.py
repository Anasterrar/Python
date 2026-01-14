FREQ = {
    "French": {
        'a': 8.13,'b':0.93,'c':3.15,'d':3.55,'e':15.10,'f':0.96,
        'g':0.97,'h':1.08,'i':6.94,'j':0.71,'k':0.16,'l':5.68,
        'm':3.23,'n':6.42,'o':5.27,'p':3.03,'q':0.89,'r':6.43,
        's':7.91,'t':7.11,'u':6.05,'v':1.83,'w':0.04,'x':0.42,
        'y':0.19,'z':0.21
    },
    "English": {
        'a':8.12,'b':1.49,'c':2.71,'d':4.32,'e':12.02,'f':2.30,
        'g':2.03,'h':5.92,'i':7.31,'j':0.10,'k':0.69,'l':3.98,
        'm':2.61,'n':6.95,'o':7.68,'p':1.82,'q':0.11,'r':6.02,
        's':6.28,'t':9.10,'u':2.88,'v':1.11,'w':2.09,'x':0.17,
        'y':2.11,'z':0.07
    }
}

def frequency_score(text):
    text = ''.join(c for c in text.lower() if c.isalpha())
    if not text:
        return float("inf")

    scores = {}

    for lang in FREQ:
        score = 0
        for letter in FREQ[lang]:
            freq = text.count(letter) / len(text) * 100
            score += abs(freq - FREQ[lang][letter])
        scores[lang] = score

    return scores
