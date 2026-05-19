# Deliverable 1 - Project Proposal

## 1. Dataset to be used

This project uses the Wine Quality Dataset. It contains two data files:

- `winequality-red.csv`, for red wines;
- `winequality-white.csv`, for white wines.

The file `winequality.names` documents the columns and gives context about the dataset. The data is public, already structured in a tabular format, and suitable for a student machine learning project.

## 2. Available features and short description

- `fixed acidity`: fixed acidity of the wine.
- `volatile acidity`: volatile acidity, which can be linked to wine defects when it is high.
- `citric acid`: amount of citric acid.
- `residual sugar`: sugar remaining after fermentation.
- `chlorides`: amount of salts/chlorides.
- `free sulfur dioxide`: free sulfur dioxide.
- `total sulfur dioxide`: total sulfur dioxide.
- `density`: density of the wine.
- `pH`: acidity level on the pH scale.
- `sulphates`: amount of sulphates.
- `alcohol`: alcohol level.
- `wine_type`: wine type added in this project (`red` or `white`).
- `quality` / `quality_group`: original score and transformed target for classification.

## 3. Initial EDA

The initial EDA was done in `notebooks/01_deliverable_1_project_proposal_eda.ipynb`.

Main observations:

- number of red wine rows: 1599;
- number of white wine rows: 4898;
- total number of rows after merging: 6497;
- number of columns after adding `wine_type` and `quality_group`: 14;
- total number of missing values detected: 0;
- the data is tabular;
- there are no time variables;
- the variables are mainly continuous;
- one categorical variable was created: `wine_type`;
- the target `quality` was transformed into `quality_group` for classification;
- the distribution is imbalanced, especially because some scores and the `high quality` group are less frequent.

Distribution of `quality`:

```text
quality
3      30
4     216
5    2138
6    2836
7    1079
8     193
9       5
```

Distribution of `quality_group`:

```text
quality_group
low quality       2384
medium quality    2836
high quality      1277
```

## 4. Business objective

The business objective is to help a producer, distributor, or laboratory quickly estimate the probable quality of a wine based on its physicochemical characteristics.

This can help to:

- prioritize batches for analysis;
- detect wines that may be low quality;
- identify wines that may be higher quality;
- provide a first estimate before a more expensive sensory analysis.

## 5. ML context

The machine learning task is multiclass classification.

- Target: `quality_group`.
- Classes: `low quality`, `medium quality`, `high quality`.
- Input features: physicochemical measurements and `wine_type`.

## 6. Cost function or main evaluation objective

The main metric is the macro F1-score.

The secondary metrics are:

- accuracy;
- precision_macro;
- recall_macro;
- confusion matrix if useful.

This choice is justified because the classes may be imbalanced. Accuracy alone can give a result that looks too positive if the model mostly predicts the majority class. Macro F1-score gives more balanced importance to the three classes.

## 7. Main risks, assumptions, limitations

- Wine quality remains partly subjective.
- The dataset does not include price, exact region, grape variety, vintage, or brand.
- The model may not generalize to all wines.
- The classes are imbalanced.
- Some chemical variables may be correlated.
- The dataset is suitable for a student POC, but it is not enough for a real business decision without additional validation.
