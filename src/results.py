import pandas as pd

from src.config import CLASSIFICATION_REPORTS_FILE, MODEL_METRICS_FILE


def write_metrics(rows) -> pd.DataFrame:
    """
    Write model metrics to results/model_metrics.csv and return a DataFrame.
    """
    metrics_df = pd.DataFrame(rows)
    MODEL_METRICS_FILE.parent.mkdir(parents=True, exist_ok=True)
    metrics_df.to_csv(MODEL_METRICS_FILE, index=False)
    return metrics_df


def write_classification_reports(text: str) -> None:
    """
    Write classification reports to results/classification_reports.txt.
    """
    CLASSIFICATION_REPORTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    CLASSIFICATION_REPORTS_FILE.write_text(text, encoding="utf-8")

