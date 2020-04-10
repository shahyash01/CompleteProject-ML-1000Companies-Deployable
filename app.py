#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import math


# In[2]:




app=Flask(__name__,template_folder='template')
model = pickle.load(open('model.pkl', 'rb'))


# In[3]:


app=Flask(__name__,template_folder='template',static_folder='static')
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/index', methods=['GET', 'POST'])
@app.route('/')
def index():
    return render_template('index.html')




@app.route('/predict',methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    #state_list=['California','Florida','New_York']
    state={'California':[1,0,0],"Florida":[0,1,0],'New_York':[0,0,1]}
    s_name =state.get(int_features[3])
    int_features.pop()
    int_features.extend(s_name)
    print(int_features)
    final_features = [np.array(int_features).astype(float)]
    print(final_features)
    prediction = model.predict(final_features)
    prediction=np.round(prediction,2)
    return render_template('index.html', prediction_text='Profit Around $ {}'.format(prediction))


# In[4]:



if __name__ == "__main__":
app.run(debug=False)    

