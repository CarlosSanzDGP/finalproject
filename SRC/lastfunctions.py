


from numpy import loadtxt
from keras.models import load_model
from PIL import Image
import tensorflow as tf
import numpy as np
from sklearn.preprocessing import OneHotEncoder


# load model
model = load_model('model.cars_colours')
# summarize model.
model.summary()

def CCCP(path):
    pic=Image.open(path)
    pic=pic.resize((64,64))
    pic=np.expand_dims(np.array(pic),0)
    pic=tf.keras.utils.normalize(pic,axis=1) 
    pred= model.predict(pic)
    enc = OneHotEncoder()
    labels=[["black"],["green"], ["red"], ["white"]]
    enc.fit(labels)  
    c = enc.inverse_transform(pred)
    prob = max(pred[0])
    resp = c[0,0],prob
    return resp




import random
def car_c (*resp):
    dic={'black':["the black sheep you are","my soul","Black Lives Matter", "Michael Jackson... I mean, the young Michael Jackson", "Back to Black by AC/DC"],
          'white':["the White Stripes", "the Pope", "Barry's surname", "the white russian I'll have this evening"],
          'red':["red,red wine", "Trotsky and Pablo Iglesias", "the Communism", "little red riding hood"],
          'green':["Hulk", "Green day", "the Green Lantern, the worst script ever", "Pere-grin"]
        }
    
    return f'The color of the car of the picture is {resp[0]}, like {random.choice(dic[resp[0]])}, with a probability of {round(resp[1]*100,2)}%.'


