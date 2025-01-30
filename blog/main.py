from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
import numpy as np
import joblib
import random
from io import BytesIO
import os

app = FastAPI()

# Load the trained model and scaler
try:
    model_path = os.path.join(os.path.dirname(__file__), 'isolation_forest.pkl')
    model, scaler = joblib.load(model_path)
except FileNotFoundError:
    raise Exception("Model file not found! Train and save the model first.")

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    """
    Upload an Excel or CSV file for anomaly detection.
    """

    # Read the file contents
    contents = await file.read()
    if not contents:
        raise HTTPException(status_code=400, detail="Uploaded file is empty!")

    file.file.seek(0)  # Reset file pointer

    # Load data (CSV or Excel)
    try:
        if file.filename.endswith(".csv"):
            try:
                df = pd.read_csv(BytesIO(contents), encoding="utf-8")
            except UnicodeDecodeError:
                df = pd.read_csv(BytesIO(contents), encoding="latin1")
        elif file.filename.endswith((".xlsx", ".xls")):
            df = pd.read_excel(BytesIO(contents))
        else:
            raise HTTPException(status_code=400, detail="Unsupported file format! Upload CSV or Excel.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading file: {str(e)}")

    if df.empty:
        raise HTTPException(status_code=400, detail="File contains no data!")

    # ✅ Handle categorical values ('DK' → Random int)
    for column in df.columns:
        if df[column].dtype == 'object':
            mask = df[column] == 'DK'
            df.loc[mask, column] = [random.randint(1, 5) for _ in range(mask.sum())]

    # ✅ Attempt to convert columns to numeric, but handle exceptions for non-numeric columns
    for column in df.columns:
        try:
            # If a column can't be converted to numeric, it will remain as an object or datetime
            df[column] = pd.to_numeric(df[column], errors='coerce')  # Use 'coerce' to replace errors with NaN
        except (ValueError, TypeError):
            pass

    # ✅ Drop any columns with non-numeric data (like Date or other text columns)
    df = df.select_dtypes(include=[np.number])

    # ✅ Fill missing values
    df.fillna(df.mean(), inplace=True)

    # ✅ Scale data
    try:
        scaled_data = scaler.transform(df)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error during scaling: {str(e)}")

    # ✅ Predict anomalies
    anomaly_labels = model.predict(scaled_data)
    anomaly_labels = np.where(anomaly_labels == 1, 0, 1)  # Convert to binary

    # ✅ Compute metrics
    total_samples = len(df)
    anomaly_count = np.sum(anomaly_labels)
    anomaly_percentage = round((anomaly_count / total_samples) * 100, 2)

    return {
        "total_samples": total_samples,
        "anomaly_count": int(anomaly_count),
        "anomaly_percentage": anomaly_percentage,
    }
