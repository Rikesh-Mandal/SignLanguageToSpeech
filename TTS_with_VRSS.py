import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
import requests
import os
import time

#reading data from csv files
dataset = pd.read_csv("E:/Sign_Language_to_Speech/Datasets/Test_datasets/CSV_files/CSV_2/A-F_train.csv")
test_dataset = pd.read_csv("E:/Sign_Language_to_Speech/Datasets/Test_datasets/CSV_files/CSV_2/A-F_Y_train.csv")
test = pd.read_csv("E:/Sign_Language_to_Speech/Datasets/Test_datasets/CSV_files/CSV_2/A-F_test.csv")

# create training and testing data
X = dataset.iloc[ : , 0:11] #data from all the rows and from column at index 0 to 10
y = dataset.iloc[ : , 11] #data from all the rows and from column at index 11
test_X = test_dataset.iloc[ : , 0:11]
test_y = test_dataset.iloc[ : , 11]
X_train, y_train, X_test, y_test = (X, y, test_X, test_y) #defining the train and test dataset

# assigning a numerical value to the target alphabets
labelEncoder = LabelEncoder()
y_train = labelEncoder.fit_transform(y_train)
y_test = labelEncoder.fit_transform(y_test)

'''
Define the model: Init K-NN
n_neighbors defines the number of neighbors to take into consideration
p spicifies the power matrix for the Minkwoski distance metric 
p = 2 stands for Euclidean Distance metric and p = 1 is the Manhattan distance metric
'''
model = KNeighborsClassifier(n_neighbors=55, p=2, metric='euclidean')
model.fit(X_train, y_train) #providing the training data

# predict the test set results
#inverse_transform is used since the target variable were previously encoded using LabelEncoder
y_pred = labelEncoder.inverse_transform(model.predict(test))
print(y_pred)

# Connect to the voiceRss using the API key provided by VoiceRSS
API_KEY = "76109602f2ff4641b0f9c637a7e7511c"

text = y_pred #the text to be played
url = "http://api.voicerss.org/" #url of VoiceRSS
language = "en-us"
voice = "Mike"
voiceRate = "0"
params = {"key": API_KEY, "src": text, "hl": language, "v": voice, "r": voiceRate } #params that is requested to VoiceRSS
response = requests.get(url,params) #the get method used to connect to the url specified within the params variable

with open("output.mp3", "wb") as f: #open a file named output.mp3 in write binary mode
    f.write(response.content) #gets the response from VoiceRss and writes the content of the response to output.mp3

os.system("start output.mp3") #plays the save output file using a program chosen
time.sleep(5) #delays for 5 secs before closing the wmplayer
os.system("taskkill /IM wmplayer.exe") #kill the wmplayer, the /IM stands for image name, in this case the wmplayer.exe


