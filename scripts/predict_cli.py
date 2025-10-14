
import joblib
import numpy as np
import sys
from pathlib import Path

def main(args):
    p = Path(__file__).parent.parent
    model = joblib.load(p / 'model' / 'diabetes_model.pkl')

    if len(args) == 8:
        arr = np.array([list(map(float, args))])
    else:
        print("Enter the features when prompted:")
        features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
        vals = []
        for f in features:
            v = input(f + ": ")
            vals.append(float(v))
        arr = np.array([vals])

    pred = model.predict(arr)[0]
    proba = model.predict_proba(arr)[0][1] if hasattr(model, 'predict_proba') else None
    print("Prediction (1 = Diabetes, 0 = No diabetes):", int(pred))
    if proba is not None:
        print(f"Probability of diabetes: {proba:.2f}")

if __name__== 'main':
    main(sys.argv[1:])