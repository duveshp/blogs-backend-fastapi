import joblib
import numpy as np
import os
import pandas as pd

# Load the trained Isolation Forest model
model_path = os.path.join(os.path.dirname(__file__), 'isolation_forest_model.pkl')
model = joblib.load(model_path)

FEATURE_NAMES = [
    'T_Q019_Q026_1', 'T_Q019_Q026_2', 'T_Q019_Q026_3',
    'T_Q019_Q026_4', 'T_Q019_Q026_5', 'T_Q019_Q026_6',
    'T_Q019_Q026_7', 'T_Q019_Q026_8'
]

def detect_anomaly(df):
    """
    Detects if the given data is an anomaly using the Isolation Forest model.
    
    Args:
        features (list): A list of numerical feature values.
        
    Returns:
        dict: {"anomaly": True} if anomaly detected, otherwise {"anomaly": False}
    """
    # Convert input data into numpy array for prediction
    # feature_array = np.array(features).reshape(1, -1)  # Ensure correct shape
    df = df[FEATURE_NAMES]

    # Make prediction (-1 = anomaly, 1 = normal)
    predictions = model.predict(df)[0]

    print("inside detect::",predictions)
    
    # Return result as dictionary
    return {"anomaly": predictions == -1}  # Anomaly (-1) = True
