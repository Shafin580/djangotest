from django.shortcuts import render, redirect
from django.http import HttpResponse
import pyrebase
# Create your views here.

firebaseConfig = {
    'apiKey': "AIzaSyB2Djq9hBvhFQYjMtDGVYAkXUeHfAsjWVM",
    'authDomain': "djangotest-34f7a.firebaseapp.com",
    'databaseURL': "https://djangotest-34f7a-default-rtdb.firebaseio.com",
    'projectId': "djangotest-34f7a",
    'storageBucket': "djangotest-34f7a.appspot.com",
    'messagingSenderId': "61056256353",
    'appId': "1:61056256353:web:ea4816af3823ec3c801d20",
    'measurementId': "G-DX3S2ZMKQR"
  }

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

def index(request):

  pass

