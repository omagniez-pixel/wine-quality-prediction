# Deliverable 3 - Model Selection

## 1. Business objective reminder

The objective is to help a producer, distributor, or laboratory quickly estimate the probable quality of a wine based on its physicochemical characteristics.

## 2. ML task

The task is multiclass classification.

- Target: `quality_group`.
- Classes: `low quality`, `medium quality`, `high quality`.

## 3. Main evaluation metric

The main metric is the macro F1-score.

The secondary metrics are accuracy, precision_macro, and recall_macro.

This choice is appropriate because the classes are imbalanced. Accuracy alone can hide poor performance on less frequent classes, especially `high quality`.

## 4. Selected models

### Model 1 - Logistic Regression

Role: simple and interpretable baseline.

Expected strengths: simple, fast, easy to explain, and a good reference model.

Expected weaknesses: may poorly capture non-linear relationships, depends on scaling, and may be limited if the classes do not separate well linearly.

Fit with the business objective: useful for having a first simple and explainable estimate.

Fit with the metric: serves as a baseline to compare macro F1-score.

### Model 2 - Random Forest Classifier

Role: flexible non-linear model.

Expected strengths: suitable for tabular data, can capture interactions between chemical variables, and is fairly robust.

Expected weaknesses: less interpretable than a linear model, can be heavier, and may overfit if poorly configured.

Fit with the business objective: can improve prediction if quality depends on complex relationships between variables.

Fit with the metric: may better balance predictions between classes if the patterns are non-linear.

### Model 3 - SVM Classifier

Role: model based on class separation.

Expected strengths: useful for testing a different logic, can work well with standardized variables, and may help if the classes are separable in a transformed space.

Expected weaknesses: less interpretable, sensitive to parameters, and can be slower on large datasets.

Fit with the business objective: provides a comparison between a simple model, a tree-based model, and a margin-based model.

Fit with the metric: it is compared using the same macro F1-score as the other models.

## 5. Fair evaluation protocol

The three models are compared with the same dataset, the same target, the same train/test split, the same basic preprocessing, the same metrics, the same final test set, no data leakage, and a simple comparable configuration.

## 6. Simple model results

The models were trained in `notebooks/03_deliverable_3_model_selection_training.ipynb`. The results were saved in `results/model_metrics.csv`.

| model | accuracy | precision_macro | recall_macro | f1_macro |
| --- | --- | --- | --- | --- |
| Logistic Regression | 0.582 | 0.585 | 0.539 | 0.550 |
| Random Forest | 0.732 | 0.748 | 0.712 | 0.726 |
| SVM | 0.627 | 0.637 | 0.576 | 0.589 |

The best macro F1-score in this test is obtained by **Random Forest** with a score of **0.726**. This result should be interpreted as a first POC comparison, not as a final model. Performance could still be improved later with more validation and limited tuning.
