
from flask import Flask,render_template,request
import pickle
import numpy as np


filename='linear.pkl'
linear=pickle.load(open(filename,'rb'))


app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    predict_array=list()
    if request.method=="POST":
         
        batting_team=str(request.form['batting-team'])
        if batting_team == 'Chennai Super Kings':
            predict_array = predict_array + [1,0,0,0,0,0,0,0]
        elif batting_team == 'Delhi Capitals':
            predict_array = predict_array + [0,1,0,0,0,0,0,0]
        elif batting_team == 'Kings XI Punjab':
            predict_array = predict_array + [0,0,1,0,0,0,0,0]
        elif batting_team == 'Kolkata Knight Riders':
            predict_array = predict_array + [0,0,0,1,0,0,0,0]
        elif batting_team == 'Mumbai Indians':
            predict_array = predict_array + [0,0,0,0,1,0,0,0]
        elif batting_team == 'Rajasthan Royals':
            predict_array = predict_array + [0,0,0,0,0,1,0,0]
        elif batting_team == 'Royal Challengers Bangalore':
            predict_array= predict_array + [0,0,0,0,0,0,1,0]
        elif batting_team == 'Sunrisers Hyderabad':
            predict_array= predict_array + [0,0,0,0,0,0,0,1]
        
        bowling_team=str(request.form['bowling-team'])
        if bowling_team == 'Chennai Super Kings':
            predict_array = predict_array + [1,0,0,0,0,0,0,0]
        elif bowling_team == 'Delhi Capitals':
            predict_array = predict_array + [0,1,0,0,0,0,0,0]
        elif bowling_team == 'Kings XI Punjab':
            predict_array = predict_array + [0,0,1,0,0,0,0,0]
        elif bowling_team == 'Kolkata Knight Riders':
            predict_array = predict_array + [0,0,0,1,0,0,0,0]
        elif bowling_team == 'Mumbai Indians':
            predict_array= predict_array + [0,0,0,0,1,0,0,0]
        elif bowling_team == 'Rajasthan Royals':
            predict_array = predict_array + [0,0,0,0,0,1,0,0]
        elif bowling_team == 'Royal Challengers Bangalore':
            predict_array = predict_array + [0,0,0,0,0,0,1,0]
        elif bowling_team == 'Sunrisers Hyderabad':
            predict_array = predict_array + [0,0,0,0,0,0,0,1]

        
        overs=float(request.form['overs'])
        run=int(request.form['runs'])
        wickets=int(request.form['wickets'])
        runs_in_prev5=int(request.form['runs_in_prev_5'])
        wickets_in_prev5=int(request.form['wickets_in_prev_5'])
        striker=int(request.form['striker'])
        non_striker=int(request.form['non-striker'])
        predict_array = predict_array + [overs, run, wickets, runs_in_prev5, wickets_in_prev5,striker,non_striker]

        
        data=np.array([predict_array])
        prediction=int(linear.predict(data)[0])
        
        return render_template("result.html",lower_limit=prediction-10,upper_limit=prediction+5)
    
if __name__=="__main__":
    app.run(debug=True)