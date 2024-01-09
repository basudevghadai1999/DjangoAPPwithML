from django.shortcuts import render
from django.http import HttpResponse
from joblib import load

# Assuming you have a DataFrame df containing your data
model = load('modelview\model.joblib')

# Create your views here.

def callnew(request):
    return render(request,'auth-sign-in.html')


def secall(request):
    sepatl_length = float(request.GET['inputone'])
    sepatl_width = float(request.GET['inputtwo'])
    petal_length = float(request.GET['inputthree'])
    petal_width = float(request.GET['inputfour'])

    y_pred = model.predict([[sepatl_length,sepatl_width,petal_length,petal_width]])
    print('inputone ',y_pred[0])
    name = y_pred[0]
    if y_pred[0] ==0:
        y_pred = ' setosa'
    elif y_pred[0]==1:
        y_pred = 'verscicolor'
    else:
        y_pred = 'Virginica'

    return render(request,'sec.html',{'predict':y_pred})
