# Regression on the tabular data
This problem is a part of Quantum test task. Other problems can be found at the [main repo](https://github.com/nktntp/quantum-test-task).

## Project objective
Given a dataset that contains $53$ anonymized features and a target column. The task is to build a model that predicts a target based on the proposed features. We will use __RMSE__ as a target metric.

## Technologies
- Python3
- Pandas
- Scikit-learn 

## Project Description

During the analysis, it was noticed that all the features do not have a linear correlation with the the target. 

![correlation matrix](https://github.com/nktntp/quantum-test-task/blob/master/task3/img/correlation-matrix.png)

Therefore, we can conclude that it makes sense to consider only nonlinear models. For this task, a model based on XGBoost was chosen.
The result __RMSE__ on the test data is $\approx 0.0322$.

