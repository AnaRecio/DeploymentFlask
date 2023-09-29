#!/usr/bin/env python
# coding: utf-8

# In[18]:


import Model
from flask import Flask, render_template, request


# In[19]:


app = Flask(__name__,template_folder="templates")

@app.route('/home')
def home():
    return render_template('home.html')


# In[21]:


@app.route('/classify',methods=['GET'])
def classify_type():
    try:
        a = request.args.get('Pregnancies') 
        b = request.args.get('Glucose') 
        c = request.args.get('BPressure')
        d = request.args.get('SkinThick') 
        e = request.args.get('Insuline') 
        f = request.args.get('BMI')
        g = request.args.get('Pedigree') 
        h = request.args.get('Age')

        output = Model.classify(a, b, c, d, e, f, g, h)

        return render_template('outcome.html', output=output)
    except:
        return 'Error'
    
if(__name__=='__main__'):
    app.run(debug=True)


# In[ ]






