from sentence_transformers import SentenceTransformer,util
import nltk

model = SentenceTransformer('all-MiniLM-L6-v2')

vtorecognize =model.encode(['tell', 'speak', 'respond', 'give', 'say', 'answer'], convert_to_numpy=True)


def respondornot(noun, sentence):
    words1 = nltk.word_tokenize(sentence)
    results = nltk.pos_tag(words1)
    count1 = 0
    count2 = 0
    i = -1
    for word, tag in results:
        i=i+1
        if(tag == 'VBP' or tag == 'VB' or tag == 'VBD'):
            result2 =util.cos_sim( vtorecognize, model.encode(word, convert_to_numpy=True))

            for sim in result2:
                if (sim >=  .59):
                    count1 = 1
        if (tag == 'NNP' or tag == 'NN'):
            if(word == noun):
                count2 = 1
        if (tag == 'WRB' or tag == 'WP' or tag == 'WDT'):
            try:
                if(results[i+3][1] == 'NN' or results[i+4][1] == 'NN'):
                    count1 = 1
            except:
                continue

    if(count2 == 1 & count1 == 1):
        print("test")
        return 1
    else:
        print("fail")
        return 0

respondornot('max','    max can you respond')
        