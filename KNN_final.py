import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
import pyttsx3


dataset = pd.read_csv("C:/Users/rikes/OneDrive/Documents/AB_Train.csv")
test_dataset = pd.read_csv("C:/Users/rikes/OneDrive/Documents/AB_Test2.csv")
test = pd.read_csv("C:/Users/rikes/OneDrive/Documents/new_test.csv")

# create training and testing data
X = dataset.iloc[ : , 0:11]
y = dataset.iloc[ : , 11]
test_X = test_dataset.iloc[ : , 0:11]
test_y = test_dataset.iloc[ : , 11]
X_train, y_train, X_test, y_test = (X, y, test_X, test_y)

labelEncoder = LabelEncoder()
y_train = labelEncoder.fit_transform(y_train)
y_test = labelEncoder.fit_transform(y_test)
y_train[697:705]  

# Define the model: Init K-NN
classifier = KNeighborsClassifier(n_neighbors=37, p=2, metric='euclidean')
classifier.fit(X_train, y_train)

# predict the test set results
y_pred = labelEncoder.inverse_transform(classifier.predict(test))
print(y_pred)

engine = pyttsx3.init()

# Set properties for the speech
engine.setProperty('rate', 100)  # Set the speaking rate (words per minute)
engine.setProperty('volume', 1)  # Set the volume (float between 0 and 1)


# Convert text to speech
engine.say(y_pred)
engine.runAndWait()

'''
# Evaluate model
cm = confusion_matrix(y_test, y_pred)
print(cm)
print(accuracy_score(y_test, y_pred))


# In[ ]:
'''



