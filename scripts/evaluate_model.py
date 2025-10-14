# scripts/evaluate_model.py
import pandas as pd
import joblib
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def main():
    p = Path(__file__).parent.parent
    df = pd.read_csv(p / 'data' / 'diabetes_clean.csv')
    X = df.drop('Outcome', axis=1)
    y = df['Outcome']

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y)

    model = joblib.load(p / 'model' / 'diabetes_model.pkl')
    y_pred = model.predict(X_test)

    print(classification_report(y_test, y_pred))

    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6,4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix')
    out = p / 'model' / 'confusion_matrix.png'
    plt.savefig(out)
    print("Confusion matrix saved to:", out)

if __name__ == 'main':
    main()