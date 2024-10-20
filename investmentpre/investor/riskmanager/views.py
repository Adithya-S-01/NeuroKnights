from django.shortcuts import render
from joblib import load
from sklearn.preprocessing import StandardScaler
import numpy as np
model = load('../savedmodel/clf.joblib')
scaler = load('../savedmodel/scaler.pkl')
# Create your views here.
def risk_rate(request):
    return render(request, 'riskrate.html')
def formInfo(request):
    age=request.GET['age']
    gender=request.GET['gender']
    income=request.GET['income']
    credit_score=request.GET['credit_score']
    loan_amount=request.GET['loan_amount']
    years_at_job=request.GET['years_at_job']
    debt_income_ratio=request.GET['debt_income_ratio']
    asset_value=request.GET['asset_value']
    dependents=request.GET['dependents']
    if(gender.lower()=='male'):
        gender=0
    elif(gender.lower()=='female'):
        gender=1
    else:
        gender=2  
    data=[age,gender,income,credit_score,loan_amount,years_at_job,debt_income_ratio,asset_value,dependents]
    data = np.array(data).reshape(1, -1)
    data= scaler.transform(data)
    data=model.predict(data)
    if(data==0):
        result='low'
    elif(data==1):
        result='medium'
    else:
        result='high' 
    return render(request,'riskrateresult.html',{'name':result})

def gold(request):
    return render(request,'gold.html')