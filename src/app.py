import sys
from pathlib import Path
from typing import Optional

import pandas as pd

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.config import (
    COMBINED_WITH_TARGET_FILE,
    INPUT_FEATURES,
    MODEL_METRICS_FILE,
    PLOT_MODEL_PERFORMANCE_MACRO_F1,
    PLOT_ORIGINAL_QUALITY_DISTRIBUTION,
    PLOT_QUALITY_GROUP_DISTRIBUTION,
    RANDOM_FOREST_FULL_PIPELINE_FILE,
)
from src.model_io import load_model


def _load_metrics_table() -> Optional[pd.DataFrame]:
    if MODEL_METRICS_FILE.exists():
        return pd.read_csv(MODEL_METRICS_FILE)
    return None


def _build_input_dataframe(values: dict) -> pd.DataFrame:
    return pd.DataFrame([values], columns=INPUT_FEATURES)


def build_app() -> None:
    """
    Build the Streamlit mock-up app.
    """
    import streamlit as st

    st.set_page_config(page_title="Wine Quality Prediction", layout="wide")

    st.title("Wine Quality Prediction")
    st.caption("DAT0424 student machine learning proof of concept")

    tabs = st.tabs(["Overview", "Prediction mock-up", "Model story", "Next steps"])

    with tabs[0]:
        st.header("Project overview")
        st.write(
            "The objective is to predict a wine quality group from physicochemical "
            "wine characteristics and wine_type."
        )
        st.info(
            "This Streamlit application is a student project dashboard. It is not a "
            "production-certified wine quality system."
        )

        st.subheader("Dataset summary")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Red wine rows", "1,599")
        col2.metric("White wine rows", "4,898")
        col3.metric("Total rows", "6,497")
        col4.metric("Missing values", "0")

        st.markdown(
            """
            Target mapping:
            - low quality: quality <= 5
            - medium quality: quality == 6
            - high quality: quality >= 7
            """
        )

        if COMBINED_WITH_TARGET_FILE.exists():
            st.caption(f"Combined dataset available: {COMBINED_WITH_TARGET_FILE.name}")

    with tabs[1]:
        st.header("Prediction mock-up")
        st.write(
            "Enter wine characteristics below. If the full prediction pipeline has been "
            "trained and saved, the app can use it for a real POC prediction."
        )

        left, right = st.columns(2)
        with left:
            fixed_acidity = st.number_input("fixed acidity", min_value=0.0, value=7.0, step=0.1)
            volatile_acidity = st.number_input("volatile acidity", min_value=0.0, value=0.30, step=0.01)
            citric_acid = st.number_input("citric acid", min_value=0.0, value=0.30, step=0.01)
            residual_sugar = st.number_input("residual sugar", min_value=0.0, value=5.0, step=0.1)
            chlorides = st.number_input("chlorides", min_value=0.0, value=0.05, step=0.001, format="%.3f")
            free_so2 = st.number_input("free sulfur dioxide", min_value=0.0, value=30.0, step=1.0)
        with right:
            total_so2 = st.number_input("total sulfur dioxide", min_value=0.0, value=115.0, step=1.0)
            density = st.number_input("density", min_value=0.0, value=0.995, step=0.001, format="%.3f")
            ph = st.number_input("pH", min_value=0.0, value=3.20, step=0.01)
            sulphates = st.number_input("sulphates", min_value=0.0, value=0.50, step=0.01)
            alcohol = st.number_input("alcohol", min_value=0.0, value=10.5, step=0.1)
            wine_type = st.selectbox("wine_type", ["white", "red"])

        input_values = {
            "fixed acidity": fixed_acidity,
            "volatile acidity": volatile_acidity,
            "citric acid": citric_acid,
            "residual sugar": residual_sugar,
            "chlorides": chlorides,
            "free sulfur dioxide": free_so2,
            "total sulfur dioxide": total_so2,
            "density": density,
            "pH": ph,
            "sulphates": sulphates,
            "alcohol": alcohol,
            "wine_type": wine_type,
        }

        if st.button("Predict"):
            if RANDOM_FOREST_FULL_PIPELINE_FILE.exists():
                pipeline = load_model(RANDOM_FOREST_FULL_PIPELINE_FILE)
                input_df = _build_input_dataframe(input_values)
                prediction = pipeline.predict(input_df)[0]
                st.success(f"Predicted quality group: {prediction}")
                st.caption(
                    "This is a student POC prediction from the saved Random Forest full pipeline, "
                    "not a production-certified result."
                )
                if hasattr(pipeline, "predict_proba"):
                    probabilities = pipeline.predict_proba(input_df)[0]
                    classes = list(pipeline.classes_)
                    probability_df = pd.DataFrame(
                        {"quality_group": classes, "probability": probabilities}
                    )
                    st.dataframe(probability_df, use_container_width=True)
            else:
                st.warning(
                    "The full prediction pipeline is not available yet. The app can display "
                    "the dashboard and results, but cannot generate a real prediction."
                )

    with tabs[2]:
        st.header("Model story")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("Logistic Regression")
            st.write("A simple model used as a clear and easy-to-explain baseline.")
        with col2:
            st.subheader("Random Forest")
            st.write("The best model in this first POC comparison, based on macro F1-score.")
        with col3:
            st.subheader("SVM")
            st.write("A margin-based classifier tested with standardized variables.")

        st.subheader("Model results")
        metrics_df = _load_metrics_table()
        if metrics_df is not None:
            st.dataframe(metrics_df, use_container_width=True)
        else:
            st.info("Model metrics file is not available yet.")

        st.subheader("Project visualizations")
        plot_cols = st.columns(3)
        plot_paths = [
            (PLOT_ORIGINAL_QUALITY_DISTRIBUTION, "Original quality distribution"),
            (PLOT_QUALITY_GROUP_DISTRIBUTION, "Quality group distribution"),
            (PLOT_MODEL_PERFORMANCE_MACRO_F1, "Macro F1-score comparison"),
        ]
        for column, (plot_path, caption) in zip(plot_cols, plot_paths):
            with column:
                if plot_path.exists():
                    st.image(str(plot_path), caption=caption)
                else:
                    st.info(f"{caption} plot is not available yet.")

    with tabs[3]:
        st.header("Next steps")
        st.info(
            "This Streamlit app is currently a mock-up dashboard. It shows the intended "
            "user journey and project structure, but it is not a final production app."
        )

        prototype_col, future_col = st.columns(2)
        with prototype_col:
            st.subheader("Current prototype")
            st.markdown(
                """
                - simple input form;
                - project overview;
                - model story;
                - metrics table and plots;
                - real prediction only if the full pipeline has been trained.
                """
            )
        with future_col:
            st.subheader("Future app")
            st.markdown(
                """
                - load the trained preprocessing pipeline;
                - load the selected model;
                - transform user inputs;
                - generate a real prediction;
                - display the predicted quality group;
                - optionally display prediction probabilities;
                - display model performance metrics;
                - keep the graphs available for interpretation.
                """
            )

        st.divider()
        st.subheader("Dashboard role")
        st.markdown(
            """
            The dashboard should help a non-technical user understand:
            - what the project does;
            - what information the model uses;
            - what quality group is predicted;
            - how well the models performed;
            - what the limits of the prediction are.
            """
        )

        st.info(
            "The next development step would be to connect the trained preprocessing "
            "pipeline and the selected model, so that user inputs can be transformed "
            "and used to generate real predictions."
        )

        st.divider()
        st.subheader("Limitations")
        st.markdown(
            """
            - The model is not final.
            - Tuning is limited.
            - Wine quality is partly subjective.
            - The dataset does not include region, price, grape variety, vintage, or brand.
            - Predictions should be interpreted as a student POC result.
            """
        )


if __name__ == "__main__":
    build_app()
