import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

train_df = pd.read_csv('titanic/train.csv')
test_df = pd.read_csv('titanic/test.csv')

train_df = train_df.drop(columns=['Cabin', 'PassengerId', 'Name', 'Ticket'])
test_df = test_df.drop(columns=['Cabin', 'Name', 'Ticket'])

train_df['Age'] = train_df['Age'].fillna(28.0)
train_df['Embarked'] = train_df['Embarked'].fillna('S')

test_df['Age'] = test_df['Age'].fillna(28.0)
test_df['Fare'] = test_df['Fare'].fillna(14.4542)
test_df['Embarked'] = test_df['Embarked'].fillna('S')

train_df['Embarked'] = train_df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
test_df['Embarked'] = test_df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
train_df['Sex'] = train_df['Sex'].map({'male': 0, 'female': 1})
test_df['Sex'] = test_df['Sex'].map({'male': 0, 'female': 1})

X_train = train_df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']].copy()
y_train = train_df['Survived']
X_test = test_df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']].copy()

scaler = StandardScaler()
X_train[['Age', 'Fare']] = scaler.fit_transform(X_train[['Age', 'Fare']])
X_test[['Age', 'Fare']] = scaler.transform(X_test[['Age', 'Fare']])

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

submission = pd.DataFrame({
    'PassengerId': test_df['PassengerId'],
    'Survived': y_pred
})

submission.to_csv('titanic_submission.csv', index=False)
print(submission.head())

custom_data = pd.DataFrame([{
    'Pclass': 1,
    'Sex': 0,
    'Age': 25,
    'SibSp': 0,
    'Parch': 0,
    'Fare': 71.2833,
    'Embarked': 0
}])

custom_data[['Age', 'Fare']] = custom_data[['Age', 'Fare']].astype(float)
custom_data[['Age', 'Fare']] = scaler.transform(custom_data[['Age', 'Fare']])

prediction = model.predict(custom_data)
probability = model.predict_proba(custom_data)

print(f'Custom prediction: {prediction}')
print(f'Custom probability: {probability}')
