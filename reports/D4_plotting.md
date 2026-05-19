# Deliverable 4 - Plotting

## 1. Plot 1 - Original data

File: `plots/plot_1_original_quality_distribution.png`

This chart shows the distribution of the original `quality` scores before transforming the target. It is useful because it shows which scores are common and which scores are rare. We can observe that middle scores are the most frequent, while extreme scores are less frequent.

## 2. Plot 2 - Feature-engineered data

File: `plots/plot_2_engineered_quality_group_distribution.png`

This chart shows the distribution of `quality_group`, the final target used for classification. It is useful for understanding the imbalance between `low quality`, `medium quality`, and `high quality`. We can observe that the classes are not perfectly balanced, which supports the use of macro F1-score.

## 3. Plot 3 - Model performance

File: `plots/plot_3_model_performance_macro_f1.png`

This chart compares the three models using the main metric, macro F1-score. The values come directly from `results/model_metrics.csv`.

Results used:

| model | accuracy | precision_macro | recall_macro | f1_macro |
| --- | --- | --- | --- | --- |
| Logistic Regression | 0.582 | 0.585 | 0.539 | 0.550 |
| Random Forest | 0.732 | 0.748 | 0.712 | 0.726 |
| SVM | 0.627 | 0.637 | 0.576 | 0.589 |

This chart is useful for a simple model comparison. It shows that **Random Forest** is the best model in this first comparison, but this is still a POC result and not a final conclusion.
