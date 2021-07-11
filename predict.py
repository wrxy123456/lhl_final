import pickle
import pandas as pd
import preprocess as pre
from flask import Flask, jsonify, request, render_template
from gensim.corpora import Dictionary

app = Flask(__name__)

model = pickle.load(open('data/model.p','rb'))

df = pd.read_csv('data/tags.csv')
df['Votes for this tag'] = df['Votes for this tag'].apply(lambda x: int(x.replace(',','')))


old_tags = df.sort_values('Votes for this tag',ascending=False)['Tag'].head(70)
bad_tags = ['Building', 'Difficult', 'Physics', 'Dark', 'Mature', 'Classic', 'Space', 'Funny']
new_tags = [st.lower() for st in list(old_tags) if not st in bad_tags]


best_tags = {1:'Action', 2:'Adventure', 3:'Anime',  6:'Puzzle',  7:'Simulation', 8: 'Great Soundtrack', 9: 'RPG', 11: 'Space', 12: 'Casual', 13: ['Fantasy', 'RPG'],
             14: 'Card Game', 15: 'Simulation', 19: ['Fantasy','RPG'], 21: 'Adventure', 23: 'Strategy'}


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method== 'POST':
        inp = request.form['Input']
        tags = []
        must_tags = []
        o = pre.preprocess(inp)
        dictionary = pickle.load(open('data/dictionary.p','rb'))
        corpus = dictionary.doc2bow(o)
        
        for word in o:
            if(word in new_tags and not word in must_tags):
                must_tags.append((word))
                
        top_topics = model.get_document_topics(corpus,minimum_probability=0.1)

        for topic in top_topics:
            t = best_tags.get(topic[0])
            if(t != None):
                if(not type(t) == list):
                    tags.append((t, topic[1]))
                else:
                    for x in t:
                        tags.append((x, topic[1]))
                        
                        
        output1 = "Popular Tags: " + ','.join(must_tags).title()
        output2 = sorted(tags, key = lambda tup : tup[1], reverse=True)
        output2 = [', '.join(map(str, x)) for x in output2]
        output2 = "Recommended Tags: " + ', '.join(output2)
        return render_template('index.html',Output1=output1,Output2=output2)

if __name__ == '__main__':
    app.run(debug=True, port='5555',host='0.0.0.0')