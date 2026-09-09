# Pipeline Run Anomaly Detection

Small ML-based observability demo for data engineering.

The model uses:

- row count
- runtime
- null percentage

to flag unusual pipeline runs with `IsolationForest`.

## Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python anomaly_detection.py
```

This is a learning example. In production, anomaly detection should complement deterministic data-quality rules, SLAs, alerts, and human investigation.
