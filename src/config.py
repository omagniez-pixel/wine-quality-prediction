from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODELS_DIR = PROJECT_ROOT / "models"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
PLOTS_DIR = PROJECT_ROOT / "plots"
RESULTS_DIR = PROJECT_ROOT / "results"
REPORTS_DIR = PROJECT_ROOT / "reports"
SCREENSHOTS_DIR = PROJECT_ROOT / "screenshots"
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
TESTS_DIR = PROJECT_ROOT / "tests"

for folder in [
    SRC_DIR,
    DATA_DIR,
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    MODELS_DIR,
    NOTEBOOKS_DIR,
    PLOTS_DIR,
    RESULTS_DIR,
    REPORTS_DIR,
    SCREENSHOTS_DIR,
    SCRIPTS_DIR,
    TESTS_DIR,
]:
    folder.mkdir(parents=True, exist_ok=True)

RED_WINE_FILE = RAW_DATA_DIR / "winequality-red.csv"
WHITE_WINE_FILE = RAW_DATA_DIR / "winequality-white.csv"
WINE_NAMES_FILE = RAW_DATA_DIR / "winequality.names"

X_TRAIN_ENGINEERED_FILE = PROCESSED_DATA_DIR / "X_train_engineered.csv"
X_TEST_ENGINEERED_FILE = PROCESSED_DATA_DIR / "X_test_engineered.csv"
Y_TRAIN_FILE = PROCESSED_DATA_DIR / "y_train.csv"
Y_TEST_FILE = PROCESSED_DATA_DIR / "y_test.csv"
COMBINED_WITH_TARGET_FILE = PROCESSED_DATA_DIR / "wine_quality_combined_with_target.csv"

LOGISTIC_REGRESSION_MODEL_FILE = MODELS_DIR / "logistic_regression_model.joblib"
RANDOM_FOREST_MODEL_FILE = MODELS_DIR / "random_forest_model.joblib"
SVM_MODEL_FILE = MODELS_DIR / "svm_model.joblib"
RANDOM_FOREST_FULL_PIPELINE_FILE = MODELS_DIR / "random_forest_full_pipeline.joblib"

MODEL_METRICS_FILE = RESULTS_DIR / "model_metrics.csv"
CLASSIFICATION_REPORTS_FILE = RESULTS_DIR / "classification_reports.txt"

PLOT_ORIGINAL_QUALITY_DISTRIBUTION = PLOTS_DIR / "plot_1_original_quality_distribution.png"
PLOT_QUALITY_GROUP_DISTRIBUTION = PLOTS_DIR / "plot_2_engineered_quality_group_distribution.png"
PLOT_MODEL_PERFORMANCE_MACRO_F1 = PLOTS_DIR / "plot_3_model_performance_macro_f1.png"

RANDOM_STATE = 42
TEST_SIZE = 0.2
TARGET_COLUMN = "quality_group"
ORIGINAL_TARGET_COLUMN = "quality"

NUMERIC_FEATURES = [
    "fixed acidity",
    "volatile acidity",
    "citric acid",
    "residual sugar",
    "chlorides",
    "free sulfur dioxide",
    "total sulfur dioxide",
    "density",
    "pH",
    "sulphates",
    "alcohol",
]
CATEGORICAL_FEATURES = ["wine_type"]
INPUT_FEATURES = NUMERIC_FEATURES + CATEGORICAL_FEATURES

MODELS = {
    "Logistic Regression": {
        "display_name": "Logistic Regression",
        "description": "Simple baseline model.",
        "path": LOGISTIC_REGRESSION_MODEL_FILE,
    },
    "Random Forest": {
        "display_name": "Random Forest",
        "description": "Flexible tree-based model for tabular data.",
        "path": RANDOM_FOREST_MODEL_FILE,
    },
    "SVM": {
        "display_name": "SVM",
        "description": "Margin-based classifier using standardized features.",
        "path": SVM_MODEL_FILE,
    },
}

