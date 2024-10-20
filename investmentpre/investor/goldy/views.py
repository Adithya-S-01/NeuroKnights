from django.shortcuts import render
from joblib import load
import numpy as np
def golresult(request):
    model = load('../savedmodel/clf.joblib')
    spx = float(request.GET.get('spx', 0))  # Default to 0 if not provided
    uso = float(request.GET.get('uso', 0))  # Default to 0 if not provided
    slv = float(request.GET.get('slv', 0))  # Default to 0 if not provided
    eur_usd = float(request.GET.get('eur_usd', 0))  # Default to 0 if not provided

    # Create a data array including all features required by the model
    data = [11111,112122,121215,1123,1126,spx, uso, slv, eur_usd]  # Include all features here
    
    # Convert to a numpy array and reshape to 2D (1 sample, n features)
    data = np.array(data).reshape(1, -1)

    # Make a prediction using the model
    prediction = model.predict(data)

    # Render the result on the golresult.html page
    return render(request, 'golresult.html', {'name': prediction})
def goldy(request):
    return render(request, 'goldy.html')
