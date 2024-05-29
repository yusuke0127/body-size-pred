import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class AgeGroupTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, age_column='age', group_column_name='age_group'):
        self.age_column = age_column
        self.group_column_name = group_column_name
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Define age bins and labels for the groups
        bins = [0, 12, 18, 35, 65, np.inf]
        labels = ['Child', 'Teen', 'Young Adult', 'Adult', 'Senior']
        # Assuming X is a DataFrame
        X = X.copy()  # Avoid changing the original dataset
        X[self.group_column_name] = pd.cut(X[self.age_column], bins=bins, labels=labels, right=False)
        return X


class BMICalculator(BaseEstimator, TransformerMixin):
    def __init__(self, height_column, weight_column, bmi_column='BMI'):
        self.height_column = height_column
        self.weight_column = weight_column
        self.bmi_column = bmi_column
    
    def fit(self, X, y=None):
        return self  # Nothing else to do
    
    def transform(self, X):
        # Ensure X is a DataFrame to simplify column access
        X = pd.DataFrame(X)
        
        # Calculate BMI = weight (kg) / (height (m))^2
        # Assuming height is in meters and weight is in kg
        X[self.bmi_column] = X[self.weight_column] / (X[self.height_column] / 1000) ** 2
        
        return X


class BMICategoryTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, bmi_column='BMI', category_column_name='bmi_category'):
        self.bmi_column = bmi_column
        self.category_column_name = category_column_name
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Define BMI categories based on standard BMI thresholds
        bins = [0, 18.5, 25, 30, np.inf]
        labels = ['Underweight', 'Normal weight', 'Overweight', 'Obese']
        # Assuming X is a DataFrame
        X = X.copy()  # To avoid changing the original dataset
        X[self.category_column_name] = pd.cut(X[self.bmi_column], bins=bins, labels=labels, right=False)
        return X


class HeightToWeightRatio(BaseEstimator, TransformerMixin):
    def __init__(self, height_column='height', weight_column='weight', ratio_column_name='height_to_weight_ratio'):
        self.height_column = height_column
        self.weight_column = weight_column
        self.ratio_column_name = ratio_column_name
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Assuming X is a DataFrame for simplicity
        height = X[self.height_column]
        weight = X[self.weight_column]
        # Calculate the height-to-weight ratio
        X[self.ratio_column_name] = height / weight
        return X
