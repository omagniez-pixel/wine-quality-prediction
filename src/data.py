import pandas as pd

from src.config import (
    COMBINED_WITH_TARGET_FILE,
    RED_WINE_FILE,
    TARGET_COLUMN,
    WHITE_WINE_FILE,
    X_TEST_ENGINEERED_FILE,
    X_TRAIN_ENGINEERED_FILE,
    Y_TEST_FILE,
    Y_TRAIN_FILE,
)


def create_quality_group(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add the quality_group target column from the original quality score.
    """
    data = df.copy()

    def map_quality(value: int) -> str:
        if value <= 5:
            return "low quality"
        if value == 6:
            return "medium quality"
        return "high quality"

    data[TARGET_COLUMN] = data["quality"].apply(map_quality)
    return data


def load_raw_wine_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load raw red and white wine datasets with the correct separator.
    The original CSV files are only read, never modified.
    """
    red_wine = pd.read_csv(RED_WINE_FILE, sep=";")
    white_wine = pd.read_csv(WHITE_WINE_FILE, sep=";")
    red_wine["wine_type"] = "red"
    white_wine["wine_type"] = "white"
    return red_wine, white_wine


def build_combined_dataset(save: bool = False) -> pd.DataFrame:
    """
    Merge red and white wine data and add the quality_group target.
    """
    red_wine, white_wine = load_raw_wine_data()
    combined = pd.concat([red_wine, white_wine], ignore_index=True)
    combined = create_quality_group(combined)
    if save:
        combined.to_csv(COMBINED_WITH_TARGET_FILE, index=False)
    return combined


def load_dataset_split() -> tuple:
    """
    Load processed train/test split for the Wine Quality project.
    Returns X_train, X_test, y_train, y_test.
    """
    X_train = pd.read_csv(X_TRAIN_ENGINEERED_FILE)
    X_test = pd.read_csv(X_TEST_ENGINEERED_FILE)
    y_train = pd.read_csv(Y_TRAIN_FILE).squeeze("columns")
    y_test = pd.read_csv(Y_TEST_FILE).squeeze("columns")
    return X_train, X_test, y_train, y_test
