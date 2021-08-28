#library 
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

# getting into data and analysis
df=pd.read_csv("ipl.csv")
# droping useless columns
df.drop(labels= ['mid', 'venue', 'batsman', 'bowler', ], axis=1, inplace=True)

#remove  other franchise which are not consistant
df.bat_team.replace('Deccan Chargers','Sunrisers Hyderabad',inplace=True)
df['bat_team'].replace('Delhi Daredevils','Delhi Capitals',inplace=True)
df.bowl_team.replace('Deccan Chargers','Sunrisers Hyderabad',inplace=True)
df.bowl_team.replace('Delhi Daredevils','Delhi Capitals',inplace=True)
df.head()
consistent_teams = ['Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals',
                    'Mumbai Indians', 'Kings XI Punjab', 'Royal Challengers Bangalore',
                    'Delhi Capitals', 'Sunrisers Hyderabad']
df = df[(df['bat_team'].isin(consistent_teams)) & (df['bowl_team'].isin(consistent_teams))

#removing first five over data
df = df[df['overs']>=5.0]

# making  variable for forcasting and splitting
df['date']=pd.to_datetime(df.date,format="%Y-%m-%d").dt.year

# making the dummy variables of 'bat_team', 'bowl_team'
new_df = pd.get_dummies(data=df, columns=['bat_team', 'bowl_team'])

#rearranging the columns
new_df = new_df[['date', 'bat_team_Chennai Super Kings', 'bat_team_Delhi Capitals', 'bat_team_Kings XI Punjab',
              'bat_team_Kolkata Knight Riders', 'bat_team_Mumbai Indians', 'bat_team_Rajasthan Royals',
              'bat_team_Royal Challengers Bangalore', 'bat_team_Sunrisers Hyderabad',
              'bowl_team_Chennai Super Kings', 'bowl_team_Delhi Capitals', 'bowl_team_Kings XI Punjab',
              'bowl_team_Kolkata Knight Riders', 'bowl_team_Mumbai Indians', 'bowl_team_Rajasthan Royals',
              'bowl_team_Royal Challengers Bangalore', 'bowl_team_Sunrisers Hyderabad',
              'overs', 'runs', 'wickets', 'runs_last_5', 'wickets_last_5','striker','non-striker', 'total']]

#splitting the data for forcasting        
X_train = new_df.drop(labels='total', axis=1)[new_df['date'] <= 2016]
X_test = new_df.drop(labels='total', axis=1)[new_df['date'] >= 2017]

# making deoendent variables
y_train = new_df[new_df['date'] <= 2016]['total'].values
y_test = new_df[new_df['date'] >= 2017]['total'].values

# dropping useless column
X_train.drop(labels='date', axis=True, inplace=True)
X_test.drop(labels='date', axis=True, inplace=True)
    
        
# building the final model
linear=LinearRegression()
linear.fit(X_train,y_train)
print(linear.score(X_test,y_test))

# saving the model
filename = 'linear.pkl'
pickle.dump(linear, open(filename, 'wb'))

