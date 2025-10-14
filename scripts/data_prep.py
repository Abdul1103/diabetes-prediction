
import pandas as pd
import numpy as np


from pathlib import Path

def main():
    p = Path(__file__).parent.parent
    raw = p / 'data' / 'diabetes.csv'
    out = p / 'data' / 'diabetes_clean.csv'

    df = pd.read_csv(raw)
    # Replace zero-values which are invalid for these columns with median
    cols_zero = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    for c in cols_zero:
        df[c] = df[c].replace(0, np.nan)
        df[c].fillna(df[c].median(), inplace=True)

    df.to_csv(out, index=False)
    print(f"Cleaned data saved to: {out}")

if __name__ == 'main':
    main()