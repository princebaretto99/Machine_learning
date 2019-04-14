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

import pickle
model=pickle.dumps(clf)
pickle_out=pickle.loads(model)

age=int(input('Please enter your age: '))
sex=int(input('1: Male  0: Female: '))
cp_type = int(input('chest pain type||1:typical angina||2:atypical angina||3:non-anginal pain||4:asymptomatic: '))
rest_bp = int(input('Resting Blood Pressure: '))
chol=int(input('Serum Cholesterol: '))
fast_bs=int(input('Fasting Blood Sugar: '))
restecg= int(input('resting electrocardiographic results( Value 0: normal ,Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)'))
maxhr=int(input('Maximum Heart Rate: '))
exang=int(input('exercise induced angina(1:Yes,0:No): '))
oldpeak=float(input('Old Peak: '))
slope=int(input('the slope of the peak exercise ST segment 1:upsloping 2:Flat 3: downsloping: '))
ca=int(input('ca:  number of major vessels (0-3) colored by flourosopy: '))
thal=int(input('thal(3 = normal; 6 = fixed defect; 7 = reversable defect): '))

data1=[[age,sex,cp_type,rest_bp,chol,fast_bs,restecg,maxhr,exang,oldpeak,slope,ca,thal]]
df=pd.DataFrame(data1)

resultant=pickle_out.predict(df)

if resultant==1:
  print('You need to visit the doctor because you have a Heart Disease')
else:
  print('Dont Worry its just a minor chest pain!! Your Lucky ;)')
