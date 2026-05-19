import pickle
from pathlib import Path

import joblib


def load_model(model_path: Path):
    """
    Load a saved model from .joblib, .pkl, or .pickle.
    """
    model_path = Path(model_path)
    if model_path.suffix == ".joblib":
        return joblib.load(model_path)
    if model_path.suffix in {".pkl", ".pickle"}:
        with model_path.open("rb") as file:
            return pickle.load(file)
    raise ValueError(f"Unsupported model file extension: {model_path.suffix}")


def save_model(model, model_path: Path) -> None:
    """
    Save a model to .joblib, .pkl, or .pickle.
    """
    model_path = Path(model_path)
    model_path.parent.mkdir(parents=True, exist_ok=True)
    if model_path.suffix == ".joblib":
        joblib.dump(model, model_path)
        return
    if model_path.suffix in {".pkl", ".pickle"}:
        with model_path.open("wb") as file:
            pickle.dump(model, file)
        return
    raise ValueError(f"Unsupported model file extension: {model_path.suffix}")

