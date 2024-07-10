from flask import Flask,render_template,url_for,request
import pandas as pd
import joblib


app=Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/prediction',methods=['GET','POST'])
def prediction():
    if request.method=='POST':
        age=request.form['age']
        gender=request.form['gender']
        travel_type=request.form['travel_type']
        class_type=request.form['class_type']
        distance=request.form['distance']
        inflight_entertainment=request.form['inflight_entertainment']
        baggage_handling=request.form['baggage_handling']
        cleanliness=request.form['cleanliness']
        customer_type=request.form['customer_type']
        departure_delay=request.form['departure_delay']
        arrival_delay=request.form['arrival_delay']
        
        a=0
        b=0
        c=0
        d=0
        e=0
        if gender=="Male":
            a=1
        if customer_type=="Disloyal":
            b=1    
        if travel_type=="Personal Travel":
            c=1
        if class_type=="Eco":
            d=1
        if class_type=="Eco-Plus":
            e=1        


        
        dt=[[age,distance,inflight_entertainment,baggage_handling,cleanliness,departure_delay,arrival_delay,a,b,c,d,e]]
        df=pd.DataFrame(dt)
        lg=joblib.load("Logistic_Regression.lb")
        pred=lg.predict(df)

        if pred==[1]:
            return "Satisfied"
        
        else:
            return "Not Stisfied"

if __name__=="__main__":
    app.run(debug=True)