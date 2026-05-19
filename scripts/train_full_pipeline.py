"""Train the full Random Forest pipeline used by the Streamlit demo."""

from __future__ import annotations

import sys
from pathlib import Path

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
sys.path.append(str(SRC_DIR))

from config import (  # noqa: E402
    CATEGORICAL_FEATURES,
    INPUT_FEATURES,
    NUMERIC_FEATURES,
    ORIGINAL_TARGET_COLUMN,
    RANDOM_FOREST_FULL_PIPELINE_FILE,
    RANDOM_STATE,
    TARGET_COLUMN,
    TEST_SIZE,
)
from data import build_combined_dataset  # noqa: E402
from model_io import load_model, save_model  # noqa: E402


def make_one_hot_encoder() -> OneHotEncoder:
    """Create a OneHotEncoder compatible with several sklearn versions."""
    try:
        return OneHotEncoder(handle_unknown="ignore", sparse_output=False)
    except TypeError:
        return OneHotEncoder(handle_unknown="ignore", sparse=False)


def main() -> None:
    """Train and save a raw-input prediction pipeline."""
    wine = build_combined_dataset(save=True)

    X = wine[INPUT_FEATURES]
    y = wine[TARGET_COLUMN]

    if ORIGINAL_TARGET_COLUMN in X.columns or TARGET_COLUMN in X.columns:
        raise ValueError("Target leakage detected in input features.")

    X_train, _, y_train, _ = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y,
    )

    numeric_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )
    categorical_pipeline = Pipeline(steps=[("encoder", make_one_hot_encoder())])

    preprocessing = ColumnTransformer(
        transformers=[
            ("num", numeric_pipeline, NUMERIC_FEATURES),
            ("cat", categorical_pipeline, CATEGORICAL_FEATURES),
        ]
    )

    full_pipeline = Pipeline(
        steps=[
            ("preprocessing", preprocessing),
            ("model", RandomForestClassifier(n_estimators=200, random_state=RANDOM_STATE)),
        ]
    )

    full_pipeline.fit(X_train, y_train)

    save_model(full_pipeline, RANDOM_FOREST_FULL_PIPELINE_FILE)
    loaded_model = load_model(RANDOM_FOREST_FULL_PIPELINE_FILE)
    if not hasattr(loaded_model, "predict"):
        raise TypeError("Saved pipeline does not expose a predict method.")
    print(f"Saved full pipeline to: {RANDOM_FOREST_FULL_PIPELINE_FILE}")


if __name__ == "__main__":
    main()
