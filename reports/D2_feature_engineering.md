# Deliverable 2 - Feature Engineering

## 1. Goal of feature engineering

The goal of feature engineering is to transform the raw data into data that is ready for model training. In this project, the transformations stay simple so the result remains understandable.

## 2. Raw data preparation

The two CSV files are loaded with `pd.read_csv(..., sep=";")`, because the separator is a semicolon.

Then:

- `wine_type = red` is added to the red wine file;
- `wine_type = white` is added to the white wine file;
- the two datasets are merged;
- the target variable `quality_group` is created from `quality`;
- `quality` is removed from the features to avoid target leakage.

Mapping used:

- `low quality`: `quality <= 5`;
- `medium quality`: `quality == 6`;
- `high quality`: `quality >= 7`.

## 3. Engineered dataset variant

Variant A - Classification-ready dataset

- target: `quality_group`;
- numerical features: median imputation and standardization;
- categorical feature: one-hot encoding of `wine_type`;
- train/test split performed before preprocessing;
- preprocessing fitted only on the training set.

## 4. Retained transformations

| Transformation | Kept? | Reason | Expected effect |
|---|---|---|---|
| Add `wine_type` | Yes | Red and white wines have different profiles. | The model can use this difference. |
| Merge red and white wines | Yes | This gives a larger dataset. | More data for training. |
| Create `quality_group` | Yes | Classification is easier to explain. | More readable target: low, medium, high. |
| Train/test split before preprocessing | Yes | Avoids data leakage. | More honest evaluation. |
| Median imputation | Yes | Robust even with few or no missing values. | Dataset compatible with sklearn. |
| Standardization | Yes | Useful for Logistic Regression and SVM. | Numerical variables become comparable. |
| One-hot encoding of `wine_type` | Yes | Avoids creating a false order between red and white. | The categorical variable can be used by the models. |

## 5. Rejected or postponed alternatives

| Alternative | Rejected/Postponed | Reason |
|---|---|---|
| PCA | Rejected | There are few features and it reduces interpretability. |
| Polynomial features | Rejected | The complexity is unnecessary for a first version. |
| Log transform | Postponed | Could be tested later if some variables are very skewed. |
| Target encoding | Rejected | Unnecessary because `wine_type` has only two classes. |
| Ordinal encoding of `wine_type` | Rejected | It would create a false order between red and white. |
| Text vectorization | Rejected | There is no text in the features. |
| Date-time decomposition | Rejected | There are no dates in the dataset. |

## 6. Expected effect on later modeling

The transformed dataset is compatible with sklearn. Numerical variables become comparable thanks to standardization, which helps Logistic Regression and SVM. Random Forest can also use this version, even though scaling is less necessary for that model. Adding `wine_type` allows the model to distinguish between red and white wines while keeping the interpretation relatively simple.

## 7. Leakage prevention

Leakage prevention is important in this step:

- the train/test split is done before any transformation;
- preprocessing is fitted only on `X_train`;
- the same preprocessing is then applied to `X_train` and `X_test`;
- `quality` and `quality_group` are never used as input features.
