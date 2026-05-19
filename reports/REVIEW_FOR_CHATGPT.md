# Review Summary for ChatGPT

## 1. Project overview

Student DAT0424 project using the Wine Quality Dataset. The objective is to predict `quality_group` (`low quality`, `medium quality`, `high quality`) from physicochemical variables and `wine_type`. The original CSV files use the `;` separator and were copied into `data/raw/` without modifying the originals.

## 2. Deliverable 1 summary

Deliverable 1 presents the dataset, variables, simple EDA, business objective, ML context, metrics, and limitations.

Main files:

- `reports/D1_project_proposal.md`
- `notebooks/01_deliverable_1_project_proposal_eda.ipynb`

Important points: 1599 red wine rows, 4898 white wine rows, 6497 rows in total, 0 missing values detected.

## 3. Deliverable 2 summary

Deliverable 2 prepares the data for classification.

Files created:

- `data/processed/wine_quality_combined_with_target.csv`
- `data/processed/X_train_engineered.csv`
- `data/processed/X_test_engineered.csv`
- `data/processed/y_train.csv`
- `data/processed/y_test.csv`
- `reports/D2_feature_engineering.md`
- `notebooks/02_deliverable_2_feature_engineering.ipynb`

Retained transformations: add `wine_type`, merge red/white wines, create `quality_group`, split before preprocessing, median imputation, standardization, and one-hot encoding.

Rejected or postponed transformations: PCA, polynomial features, log transform, target encoding, ordinal encoding, text vectorization, and date-time decomposition.

## 4. Deliverable 3 summary

Exactly three models were trained: Logistic Regression, Random Forest Classifier, and SVM Classifier.

Main metric: macro F1-score.

Protocol: same dataset, same split, same target, same metrics, no data leakage, and no heavy tuning.

Results obtained:

| model | accuracy | precision_macro | recall_macro | f1_macro |
| --- | --- | --- | --- | --- |
| Logistic Regression | 0.582 | 0.585 | 0.539 | 0.550 |
| Random Forest | 0.732 | 0.748 | 0.712 | 0.726 |
| SVM | 0.627 | 0.637 | 0.576 | 0.589 |

Files:

- `results/model_metrics.csv`
- `results/classification_reports.txt`
- `models/logistic_regression_model.joblib`
- `models/random_forest_model.joblib`
- `models/svm_model.joblib`
- `reports/D3_model_selection.md`
- `notebooks/03_deliverable_3_model_selection_training.ipynb`

## 5. Deliverable 4 summary

Three main plots were created:

- `plots/plot_1_original_quality_distribution.png`: distribution of original `quality` scores.
- `plots/plot_2_engineered_quality_group_distribution.png`: distribution of the final target `quality_group`.
- `plots/plot_3_model_performance_macro_f1.png`: macro F1-score comparison for the three models using real metrics.

Files:

- `reports/D4_plotting.md`
- `reports/D4_plotting.pdf`
- `notebooks/04_deliverable_4_plotting.ipynb`

## 6. Deliverable 5 summary

The Streamlit mock-up contains a project overview, simulated input form, mocked prediction, presentation of the three models, display of the macro F1 chart if available, and a plan to replace the mock-up with real predictions.

Files:

- `src/app.py`
- `reports/D5_streamlit_mockup.md`
- `reports/D5_streamlit_mockup.pdf`
- `notebooks/05_deliverable_5_streamlit_mockup_notes.ipynb`

Screenshots generated automatically with Playwright:

- `screenshots/streamlit_mockup_home.png`
- `screenshots/streamlit_mockup_prediction.png`
- `screenshots/streamlit_mockup_model_story.png`

## 7. Files created or modified

- `.DS_Store`
- `README.md`
- `data/processed/X_test_engineered.csv`
- `data/processed/X_train_engineered.csv`
- `data/processed/wine_quality_combined_with_target.csv`
- `data/processed/y_test.csv`
- `data/processed/y_train.csv`
- `data/raw/winequality-red.csv`
- `data/raw/winequality-white.csv`
- `data/raw/winequality.names`
- `models/logistic_regression_model.joblib`
- `models/random_forest_model.joblib`
- `models/svm_model.joblib`
- `notebooks/01_deliverable_1_project_proposal_eda.ipynb`
- `notebooks/02_deliverable_2_feature_engineering.ipynb`
- `notebooks/03_deliverable_3_model_selection_training.ipynb`
- `notebooks/04_deliverable_4_plotting.ipynb`
- `notebooks/05_deliverable_5_streamlit_mockup_notes.ipynb`
- `plots/plot_1_original_quality_distribution.png`
- `plots/plot_2_engineered_quality_group_distribution.png`
- `plots/plot_3_model_performance_macro_f1.png`
- `reports/CHECKLIST.md`
- `reports/D1_project_proposal.md`
- `reports/D2_feature_engineering.md`
- `reports/D3_model_selection.md`
- `reports/D4_plotting.md`
- `reports/D4_plotting.pdf`
- `reports/D5_streamlit_mockup.md`
- `reports/D5_streamlit_mockup.pdf`
- `reports/FILES_CREATED.md`
- `reports/REVIEW_FOR_CHATGPT.md`
- `requirements.txt`
- `results/classification_reports.txt`
- `results/model_metrics.csv`
- `screenshots/streamlit_mockup_home.png`
- `screenshots/streamlit_mockup_model_story.png`
- `screenshots/streamlit_mockup_prediction.png`
- `src/app.py`
- `src/data.py`
- `src/metrics.py`

## 8. Commands run

- `python3 - generated and corrected project artifacts`
- `pd.read_csv(..., sep=";") for the two CSV files`
- `train_test_split(test_size=0.2, random_state=42, stratify=y)`
- `trained LogisticRegression, RandomForestClassifier, and SVC`
- `saved metrics, models, and plots`
- `executed notebooks with nbclient`
- `python3 -m pip install streamlit`
- `python3 -m pip install playwright && python3 -m playwright install chromium`
- `python3 -m streamlit run src/app.py --server.headless true --server.port 8501 --server.address 127.0.0.1`
- `captured screenshots with Playwright`
- `translated reports, README, notebook notes, and Streamlit text to English`
- `generated D4 and D5 PDF files with matplotlib`

## 9. Known limitations

- The model is not final.
- Tuning is intentionally limited.
- The Streamlit mock-up is not connected to a real prediction backend.
- Results could be improved later with more complete validation.
- The screenshots were generated automatically in this environment, but they can be retaken manually if the layout changes.

## 10. Checklist

- [x] D1 includes dataset, features, EDA, business objective, ML context, metric, risks
- [x] D2 includes engineered dataset, retained transformations, rejected alternatives, expected modeling effect
- [x] D3 includes exactly 3 models, strengths, weaknesses, business fit, metric fit
- [x] D4 includes exactly 3 required plots
- [x] D5 includes Streamlit mock-up and replacement plan
- [x] No invented model results
- [x] No target leakage
- [x] Reports are written in student-level English
