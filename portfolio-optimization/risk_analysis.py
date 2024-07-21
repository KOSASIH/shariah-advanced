import numpy as np

def analyze_risk(portfolio_weights, covariance_matrix):
    portfolio_risk = np.sqrt(np.dot(portfolio_weights.T, np.dot(covariance_matrix, portfolio_weights)))
    return portfolio_risk
