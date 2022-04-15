# app.py

from re import S
from flask import Flask, render_template
from random import choice
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def base_page():
    emotions = {'mad': ['mad','hurt','hostile','angry','rage','hateful',
                    'critical','skeptical','irritated','furious',
                    'frustrated','selfish','jealous'],
                'scared': ['scared','rejected','confused','helpless',
                       'submissive','insecure','anxious','bewildered',
                       'discouraged','insignificant','weak','foolish',
                       'embarassed'],
                'joyful': ['excited','sexy','energetic','playful','creative',
                       'aware','daring','fascinating','stimulating','amused',
                       'extravagant','delightful'],
                'powerful': ['powerful','proud','respected','apprecaited','hopeful',
                         'important','faithful','cheerful','satisfied','valuable',
                         'worthwhile','intelligent','confident'],
                'peaceful': ['peaceful','content','thoughtful','intimate','loving',
                         'trusting','nurturing','pensive','relaxed','responsive',
                         'serene','sentimental','thankful'],
                'sad': ['sad','sleepy','bored','lonely','depressed','ashamed','guilty',
                    'bashful','stupid','miserable','inadequate','inferior','apathetic']
    }
    base_emotion = choice(list(emotions.keys()))
    emotion_name = choice(emotions[base_emotion])
    file_name= f'the_feeling_wheel_{base_emotion}.png'
    
    return render_template('index.html', emotion_name=emotion_name, file_name=file_name)

# We only need this for local development.
if __name__ == '__main__':
 app.run()
