import joblib
import numpy as np
import os

# Load the trained Isolation Forest model
model_path = os.path.join(os.path.dirname(__file__), 'isolation_forest_model.pkl')

model = joblib.load(model_path)

def detect_anomaly():
    """
    Detects if the given data is an anomaly using the Isolation Forest model.
    Returns:
        -1: Anomaly
        1: Normal
    """
    # Convert input data into numpy array for prediction
    #data = np.array(features).reshape(1, -1)  # Ensure correct shape
    prediction = model.predict()
    
    # Return result as dictionary
    return {"anomaly": prediction[0] == -1}  # Anomaly (-1) = True
