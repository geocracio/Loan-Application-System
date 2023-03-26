import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from joblib import dump


target_variable = "Risk_Flag"
data = pd.read_csv("./data/Training Data.csv")
data.rename(columns={"Married/Single": "MaritalStatus"}, inplace=True)
num_cols = ['Income', 'Age', 'Experience', 'CURRENT_JOB_YRS', 'CURRENT_HOUSE_YRS']
cat_cols = ['MaritalStatus', 'House_Ownership', 'Car_Ownership', 'Profession']
data = data[num_cols + cat_cols + [target_variable]].copy()

X_train, X_test, y_train, y_test = train_test_split(
    data.drop(columns=target_variable),
    data[target_variable],
    test_size=0.25,
    random_state=66)

num_pipeline = Pipeline(steps=[
    ('impute', SimpleImputer(strategy='mean')),
    ('scale', MinMaxScaler())
])
cat_pipeline = Pipeline(steps=[
    ('impute', SimpleImputer(strategy='most_frequent')),
    ('one-hot', OneHotEncoder(handle_unknown='ignore', sparse=False))
])
col_trans = ColumnTransformer(transformers=[
    ('num_pipeline', num_pipeline, num_cols),
    ('cat_pipeline', cat_pipeline, cat_cols)
],
    remainder='drop',
    n_jobs=-1)
clf = XGBClassifier()
clf_pipeline = Pipeline(steps=[
    ('col_trans', col_trans),
    ('model', clf)
])

clf_pipeline.fit(X_train, y_train)
preds = clf_pipeline.predict(X_test)
probs = clf_pipeline.predict_proba(X_test)[:, 1]
accuracy = clf_pipeline.score(X_test, y_test)
print(f"Model Accuracy: {accuracy}")

roc_auc = roc_auc_score(y_test, probs)
gini = np.abs((roc_auc * 2) - 1)
print(f"Model Gini: {gini}")

# dump(clf, 'assets/clf.joblib')
dump(clf_pipeline, 'assets/pipeline.joblib')

import sklearn
print('The scikit-learn version is {}.'.format(sklearn.__version__))

# %%
# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from xgboost import XGBClassifier
# from sklearn.metrics import roc_auc_score, accuracy_score, precision_score, recall_score, f1_score
# from sklearn.impute import SimpleImputer
# from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
# from sklearn.pipeline import Pipeline
# from sklearn.compose import ColumnTransformer
# from joblib import dump
#
# def load_data(path, target_variable):
#     """
#     Load data from a CSV file and split into features and target variable.
#     """
#     data = pd.read_csv(path)
#     X = data.drop(columns=target_variable)
#     y = data[target_variable]
#     return X, y
#
# def preprocess_data(X, num_cols, cat_cols):
#     """
#     Preprocess the data by imputing missing values and scaling numeric data.
#     """
#     num_pipeline = Pipeline(steps=[
#         ('impute', SimpleImputer(strategy='median')),
#         ('scale', MinMaxScaler())
#     ])
#     cat_pipeline = Pipeline(steps=[
#         ('impute', SimpleImputer(strategy='most_frequent')),
#         ('one-hot', OneHotEncoder(handle_unknown='ignore', sparse=False))
#     ])
#     col_trans = ColumnTransformer(transformers=[
#         ('num_pipeline', num_pipeline, num_cols),
#         ('cat_pipeline', cat_pipeline, cat_cols)
#     ],
#         remainder='drop',
#         n_jobs=-1)
#     X_processed = col_trans.fit_transform(X)
#     return X_processed, col_trans
#
# def train_model(X_train, y_train, classifier):
#     """
#     Train a machine learning model on the training data.
#     """
#     clf_pipeline = Pipeline(steps=[
#         ('model', classifier)
#     ])
#     clf_pipeline.fit(X_train, y_train)
#     return clf_pipeline
#
# def evaluate_model(clf_pipeline, X_test, y_test):
#     """
#     Evaluate the performance of the machine learning model on the test data.
#     """
#     preds = clf_pipeline.predict(X_test)
#     probs = clf_pipeline.predict_proba(X_test)[:, 1]
#     accuracy = accuracy_score(y_test, preds)
#     precision = precision_score(y_test, preds)
#     recall = recall_score(y_test, preds)
#     f1 = f1_score(y_test, preds)
#     roc_auc = roc_auc_score(y_test, probs)
#     gini = np.abs((roc_auc * 2) - 1)
#     print(f"Model Accuracy: {accuracy}")
#     print(f"Model Precision: {precision}")
#     print(f"Model Recall: {recall}")
#     print(f"Model F1-score: {f1}")
#     print(f"Model ROC AUC: {roc_auc}")
#     print(f"Model Gini: {gini}")
#
# def save_model(clf, pipeline_filename, model_filename):
#     """
#     Save the machine learning model and pipeline to disk.
#     """
#     dump(clf, model_filename)
#     dump(clf['model'], pipeline_filename)
#
# # Load data
# target_variable = "Risk_Flag"
# X, y = load_data("./data/Training Data.csv", target_variable)
#
# # Split data into train and test sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=66)
#
# # Define numeric and categorical columns
# num_cols = ['Income', 'Age', 'Experience', 'CURRENT_JOB_YRS', 'CURRENT_HOUSE_YRS']
# cat_cols = ['Married/Single', 'House_Ownership', 'Car_Ownership', 'Profession']
#
# # Preprocess data
# X_train_processed, col_trans = preprocess_data(X_train, num_cols,