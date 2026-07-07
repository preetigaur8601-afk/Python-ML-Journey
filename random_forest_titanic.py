import pandas as pd
import zipfile
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

with zipfile.ZipFile('/content/titanic.zip', 'r') as z:
    z.extractall('/content/')

df = pd.read_csv('/content/train.csv')

df['Age'] = df['Age'].fillna(df['Age'].mean())
df = df.drop('Cabin', axis=1)
df = df.dropna()
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

X = df[['Pclass', 'Age', 'Fare', 'Sex']]
y = df['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))
