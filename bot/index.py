# -*- coding: utf-8 -*-
#импорты зависимостей
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import re
import pickle
import requests
from fuzzywuzzy import fuzz
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers import Embedding, LeakyReLU
from keras.callbacks import ReduceLROnPlateau, EarlyStopping
from keras.optimizers import SGD
import numpy as np
import random
import matplotlib.pyplot as plt
import time
from keras.layers import LSTM, GRU
import rupostagger
from keras.models import load_model


texts = []
texts_2 = [] 
texts_labels = []

my_file = open(os.path.join(os.path.dirname(__file__), 'ru.conversations1.txt'), 'r', encoding='utf-8')
string_neobr = my_file.read()
my_file.close()



class Normal:
    def __init__(self):
        self.words = []

    def fix(self, text):
        d = []
        command = ""
        rate = 0
    
        for word in self.words:
            d.append(fuzz.ratio(text, word))
        
        command = self.words[d.index(max(d))]
        rate = fuzz.ratio(text, command)
        if rate < 70:
            sim = []
            for i in self.words:
                url = 'https://rusvectores.org/araneum_none_fasttextcbow_300_5_2018/' + text + '__' + i + '/api/similarity/'
                r = requests.get(url).content.decode().split("\t")[0]
                sim.append(r)
            resu = self.words[sim.index(max(sim))]
            return resu
        return command

    def normal2(self, inp):
        inp = inp.lower()
        reg = re.compile('[^a-zA-Zа-яА-Я ]')
        inp = reg.sub('', inp)
        inp = inp.split(' ')
        out = []
        for p in inp:
            out.append(p)
            
        out = ' '.join(out)
        print(get_vector(out, vectorizer))
        return get_vector(out, vectorizer)

    def normal3(self, inp):
        inp = inp.lower()
        reg = re.compile('[^a-zA-Zа-яА-Я ]')
        inp = reg.sub('', inp)
        inp = inp.split(' ')
        out = []
        for p in inp:
            out.append(p)
            
        out = ' '.join(out)
        return out

    def normal4(self, inp):
        inp = inp.lower()
        reg = re.compile('[^a-zA-Zа-яА-Я ]')
        inp = reg.sub('', inp)
        inp = inp.split(' ')
        out = []
        for p in inp:
            out.append(self.fix(p))
            
        out = ' '.join(out)
        return get_vector(out, vectorizer, vector=False)

    def normal(self, inp):
        inp = inp.lower()
        reg = re.compile('[^a-zA-Zа-яА-Я ]')
        inp = reg.sub('', inp)
        inp = inp.split(' ')
        out = []
        for p in inp:
            out.append(self.fix(p))
            
        out = ' '.join(out)
        return get_vector(out, vectorizer)
    
    def train(self, x):
        words_arr = []
        for i in x:
            i = self.normal3(i)
            words_arr = i.split(' ')
            for y in words_arr:
                self.words.append(y)

the_normalizer = Normal()

string = []
string = string_neobr.split('\n')
str = []
dialogs = []
ti = 0
maximum = 100000000000

pov = 0


for j in string:
    if j == "":
        continue
    else:
        new_str = ""
        for t in j:
            if t == "-":
                continue
            else:
                new_str = new_str + t
        str.append(new_str)
        ti += 1
        if ti == maximum:
            break

vn = []
ti = 0
for j in string:
    if j == "":
        dialogs.append(vn)
        vn = []
    else:
        new_str = ""
        for t in j:
            if t == "-":
                continue
            elif t == ":" and ti % 2 == 0:
                break
            else:
                new_str = new_str + t
        vn.append(new_str)
        ti += 1
        if ti == maximum:
            break

arr_str_types = []

for i in range(len(str)):
    if i % 2 == 0:
        arr_str_types.append(str[i].split(":")[1])
        texts.append(str[i].split(":")[0])
    else:
        texts_labels.append(str[i])


print(texts_labels)
vectorizer = TfidfVectorizer()
vectorizer.fit(texts)

def get_vector(s, vectorizerr, vector=True):
    if True: # для отступов
        if True: # для отступов
            if vector == False: # если вектор не запрашивался
                return r # возвращаем нормализованное слово
            words = []
            for i in s.split(" "):
                words.append(i) # доставание нормализованного слова из результата леммантизации
            documm = " ".join(words)
            return (vectorizerr.transform([documm]).toarray()[0]) # возврат из функции список итогового вектора документа


nu = 0
types = []
nn = 0
a = []
b = []
for u in arr_str_types:
    if not u in a:
        nn = nn + 1
        a.append(u)
        b.append(nn)
for u in arr_str_types:
    types.append(b[a.index(u)])


the_normalizer.train(texts)
types2 = []
types2_lables = []
nn = 0
a1 = []
bb = []
for u in texts_labels:
    if not u in a1:
        nn = nn + 1
        a1.append(u)
        bb.append(nn)
for u in texts_labels:
    types2.append(bb[a1.index(u)])
    types2_lables.append(u)

text_clf = MLPClassifier(hidden_layer_sizes=(300, 200, 200, 200), learning_rate='adaptive', max_iter=3000)

for er in range(len(texts)):
    texts[er] = the_normalizer.normal2(texts[er])

text_clf.fit(texts, types)

pickle.dump(text_clf, open("model_neiroset_chatBot.pkl", 'wb'))

nnnnn = 0
d = []
a = []
for i in dialogs:
    m = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ggg = 0
    for j in i:
        ok2 = False
        for t in range(len(m) - 1):
            m[t] = m[t + 1]
        if nnnnn % 2 == 0:
            m[len(m) - 1] = text_clf.predict([the_normalizer.normal2(j)])
        elif not (ggg == len(j) - 1):
            ok2 = True
        n = []
        for t in range(len(m)):
            if t % 2 == 0:
                n.append(m[t])
        ok = False
        for k in n:
            if not k == 0:
                ok = True
        if ok == True:
            if ok2 == True:
                d.append(n)
                a.append(bb[a1.index(j)])
        ggg += 1
        nnnnn += 1


x = d
print(x)
y = []
mx = max(types2)
for yy in a:
    h = []
    for hh in range(mx + 1):
        if hh == yy:
            h.append(1)
            continue
        h.append(0)
    y.append(h)

print("sd1")
print(d)


model = Sequential()

model.add(Embedding(max(types) + 1, 100, mask_zero=True, input_length=len(x[0])))

model.add(Dense(80))
model.add(LeakyReLU(alpha=0.01))

model.add(Dense(80))
model.add(LeakyReLU(alpha=0.01))

model.add(GRU(16, return_sequences=True))

model.add(Dense(80))
model.add(LeakyReLU(alpha=0.01))

model.add(Dense(80))
model.add(LeakyReLU(alpha=0.01))

model.add(GRU(32))

model.add(Dense(80))
model.add(LeakyReLU(alpha=0.01))

model.add(Dense(len(y[0])))
model.add(Activation('softmax'))

sgd = SGD(lr=1, momentum=0.9)
model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy'])
model.summary()
#exit()
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.9, patience=2, min_lr=0.001)

history = model.fit(np.array(x), np.array(y), epochs=95, callbacks=[reduce_lr], validation_data=(np.array(x), np.array(y)))

model.save('model.h5')



#model = load_model("model.h5")
text_clf = pickle.load(open("model_neiroset_chatBot.pkl", 'rb'))

t1 = [0]
t2 = [0]
t3 = [0]
t4 = [0]
t5 = [0]
t6 = [0]
t7 = [0]
t8 = [0]
t9 = [0]
t10 = [0]
t11 = [0]
t12 = [0]

old_message = int(time.time())

token = 'af9d4693f0b0b1ff3e06406f2a1ef6a2a83fe760ab815debd8ec2a515f771786b300fbe1490401e3ded4c'
confirmation_token = '83117aee'
import vk
from flask import Flask, request, json
app = Flask(__name__)
def splitt(t, peer_id):
    if True: # для отступов
        inp = the_normalizer.normal(t) # нормализация текста

        print(inp)
        res = text_clf.predict([inp])
        result_arr = []
        if not inp == "": 
            t12 = res
        else:
            t12 = [0]
        m = np.array([t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12]).T
        print(m)
        predi = model.predict(m)
        otv = types2_lables[types2.index(predi[0].tolist().index(max(predi[0].tolist())))]
        for dc in texts_labels:
            if res == types[texts_labels.index(dc)]:
                result_arr.append(dc)

        print(otv)

        t1[0] = t2[0]
        t2[0] = t3[0]
        t3[0] = t4[0]
        t4[0] = t5[0]
        t5[0] = t6[0]
        t6[0] = t7[0]
        t7[0] = t8[0]
        t8[0] = t9[0]
        t9[0] = t10[0]
        t10[0] = t11[0]
        t11[0] = t12[0]
    return otv

@app.route('/', methods=['POST'])
def processing():
    # Распаковываем json из пришедшего POST-запроса
    data = json.loads(request.data)
    # Вконтакте в своих запросах всегда отправляет поле типа
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        session = vk.Session()
        api = vk.API(session, v=5.81)
        peer = data['object']['peer_id']

        result = splitt(data['object']['text'], data['object']['peer_id'])
        if not result == "":
            api.messages.send(access_token=token,peer_id=peer, message=result)
        # Сообщение о том, что обработка прошла успешно
        return 'ok'
		
if __name__ == '__main__':
    app.run(port=8080)