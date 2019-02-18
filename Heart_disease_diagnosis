!pip install -U -q PyDrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials
# Authenticate and create the PyDrive client.
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)
#put your file link below
link = 'https://drive.google.com/open?id=1R1s51AXWyTCEItbYEE2SXa0E8nFVQJqS'
fluff, id = link.split('=')

downloaded = drive.CreateFile({'id':id}) 
#put your file name below
downloaded.GetContentFile('hdata.xlsx')
#The data is taken from UCI repository and i have edited it a bit
import pandas as pd
data1=pd.read_excel('hdata.xlsx')

X=data1.drop('Result',axis=1)
y=data1.Result
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)

from sklearn import svm
clf=svm.SVC(kernel='linear',C=1000,gamma=3)
clf.fit(X_train,y_train)

prediction=clf.predict(X_test)

from sklearn.metrics import accuracy_score
score=accuracy_score(prediction,y_test)
print(score)
