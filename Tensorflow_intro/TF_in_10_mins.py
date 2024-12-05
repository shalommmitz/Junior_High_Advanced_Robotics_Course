#cell 0
# 0. Import Data

#cell 1
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler



#cell 2
df = pd.read_csv('Churn.csv')

#cell 3
X = pd.get_dummies(df.drop(['Churn', 'Customer ID'], axis=1))
y = df['Churn'].apply(lambda x: 1 if x=='Yes' else 0)

#cell 4
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

# Standardization
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# Normalization
minmax_scaler = MinMaxScaler()
X_train_norm = minmax_scaler.fit_transform(X_train)
X_test_norm = minmax_scaler.transform(X_test)


#cell 5
y_train.head()

#cell 6
# 1. Import Dependencies

#cell 7
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from sklearn.metrics import accuracy_score

#cell 8
# 2. Build and Compile Model

#cell 9
model = Sequential()
#model.add(Dense(units=32, activation='tanh', input_dim=len(X_train.columns)))
model.add(Dense(units=32, activation='relu', input_dim=len(X_train.columns)))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))


#cell 10
#model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#cell 11
# 3. Fit, Predict and Evaluate

#cell 12
#model.fit(X_train, y_train, epochs=800, batch_size=640)
model.fit(X_train_std, y_train, epochs=100, batch_size=640)

#cell 13
#y_hat = model.predict(X_test)
y_hat = model.predict(X_test_std)
y_hat = [0 if val < 0.5 else 1 for val in y_hat]

#cell 14
print("Accuracy score of test data:")
print(accuracy_score(y_test, y_hat))

#cell 15
# 4. Saving and Reloading

#cell 16
model.save('tfmodel.keras')

#cell 17
del model 

#cell 18
model = load_model('tfmodel.keras')

