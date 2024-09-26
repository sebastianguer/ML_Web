#from utils import db_connect
#engine = db_connect()

# your code here

import numpy as np
import flask
import pickle
import requests
from flask import Flask, render_template, request


app = Flask(__name__)

model=pickle.load(open('models/model_xgb.pkl','rb'))

dictionary = {"0":'Not Approved', "1":'Approved'}


@app.route('/',methods=['GET','POST'])


def index():
    if request.method == 'POST':
        AttendanceRate = float(request.form['AttendanceRate'])
        StudyHoursPerWeek = float(request.form['StudyHoursPerWeek'])
        PreviousGrade = float(request.form['PreviousGrade'])
        ExtracurricularActivities = float(request.form['ExtracurricularActivities'])

        data=[[AttendanceRate,StudyHoursPerWeek,StudyHoursPerWeek,PreviousGrade,ExtracurricularActivities]]
        prediction = str(model.predict(data)[0])
        pred_dict=dictionary[prediction]
    else:
        pred_dict=None

    return render_template('index.html',prediction=pred_dict)

