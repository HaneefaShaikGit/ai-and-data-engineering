"""Detect unusual pipeline runs using IsolationForest."""

from pathlib import Path
import pandas as pd
from sklearn.ensemble import IsolationForest

DATA_PATH = Path(__file__).with_name("pipeline_runs.csv")

def main():
    df = pd.read_csv(DATA_PATH)
    features = ["row_count", "runtime_seconds", "null_percentage"]

    model = IsolationForest(contamination=0.08, random_state=42)
    df["anomaly_flag"] = model.fit_predict(df[features])
    df["status"] = df["anomaly_flag"].map({1: "NORMAL", -1: "ANOMALY"})

    print(df[["run_date", *features, "status"]].to_string(index=False))

if __name__ == "__main__":
    main()
