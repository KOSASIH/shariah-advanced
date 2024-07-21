import cvxpy as cp
import numpy as np

def optimize_portfolio(risk_tolerance, expected_returns, covariance_matrix):
    n = len(expected_returns)
    weights = cp.Variable(n)
    portfolio_return = cp.sum(expected_returns * weights)
    portfolio_risk = cp.quad_form(weights, covariance_matrix)
    problem = cp.Problem(cp.Maximize(portfolio_return), [cp.sum(weights) == 1, weights >= 0, portfolio_risk <= risk_tolerance])
    problem.solve()
    return weights.value
