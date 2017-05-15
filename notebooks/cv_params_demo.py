from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.externals.joblib import hash
import pandas as pd
import numpy as np

def load_cv_split(split_idx):
    data = load_digits()
    splitted = train_test_split(data.data, data.target,
                                test_size=0.20,
                                random_state=split_idx)
    return split_idx, splitted

def evaluate_one(model_class, parameters, cv_split):
    split_idx, (X_train, X_val, y_train, y_val) = cv_split
    model = model_class(**parameters).fit(X_train, y_train)

    train_score = model.score(X_train, y_train)
    validation_score = model.score(X_val, y_val)

    results = {
        'train_score': train_score,
        'val_score': validation_score,
        'parameters': parameters,
        'parameters_hash': hash(parameters),
    }
    return results

import matplotlib.pyplot as plt

def plot_param_map(df, target, title):
    fig = plt.figure(figsize=(6, 5))
    plt.xlabel('log10(C)')
    plt.ylabel('log10(gamma)')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.scatter(np.log10(df['C']), np.log10(df['gamma']),
                c=target,
                marker='s', edgecolors='none',
                s=80, alpha=1, cmap='viridis')
    plt.colorbar()
    plt.title(title)
    return fig

def plot_results(results):
    results = pd.DataFrame.from_dict(results)

    mean_evaluations = results.groupby('parameters_hash').agg({
        'val_score': np.mean,
       # 'training_time': np.mean,
    }).reset_index()

    all_parameters = pd.DataFrame.from_dict(list(results['parameters']))
    all_parameters['parameters_hash'] = results['parameters_hash']

    evaluations = (
        mean_evaluations
        .merge(all_parameters)
        .drop(['parameters_hash'], axis=1)
    )
    top10 = evaluations.sort_values(
        by='val_score', ascending=False).head(10)

    fig = plot_param_map(evaluations, evaluations['val_score'],
                   'validation score')
