import pandas as pd
from sklearn.neighbors import KNeighborsClassifier #importing the classifier since it is a classification problem
from sklearn.preprocessing import LabelEncoder
import serial.tools.list_ports

dataset = pd.read_csv("C:/Users/rikes/OneDrive/Documents/ABC_Train.csv")
test_dataset = pd.read_csv("C:/Users/rikes/OneDrive/Documents/ABC_Test.csv")
test = pd.read_csv("C:/Users/rikes/OneDrive/Documents/new_ABC_test.csv")

# create training and testing data
X = dataset.iloc[ : , 0:11]
y = dataset.iloc[ : , 11]
test_X = test_dataset.iloc[ : , 0:11]
test_y = test_dataset.iloc[ : , 11]
X_train, y_train, X_test, y_test = (X, y, test_X, test_y)

#assigning a numerical value to the target alphabets
labelEncoder = LabelEncoder()
y_train = labelEncoder.fit_transform(y_train)
y_test = labelEncoder.fit_transform(y_test)

# Define the model: Init K-NN
classifier = KNeighborsClassifier(n_neighbors=37, p=3, metric='euclidean')
classifier.fit(X_train, y_train)

# predict the test set results
y_pred = labelEncoder.inverse_transform(classifier.predict(test))
print(y_pred)

serialInst = serial.Serial()    #creating an empty instance of the Serial
serialInst.baudrate = 9600      #defining the baud rate
serialInst.port = "COM3"        #connecting to the port COM3
serialInst.open()               #opening the connection

while True:                     #creating an infinite loop
    if serialInst.in_waiting:   #if there are data incoming then
        packet = serialInst.readline()  #read the incoming data
        # decode from byte string to unicode and strip the extra line and print the data from serial
        incoming_data = packet.decode('utf').rstrip('\n')
        with open("predict.txt", 'w') as f:
            f.write(incoming_data)
