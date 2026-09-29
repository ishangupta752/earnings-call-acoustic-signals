"""Fama-French five-factor expected-return helpers."""
from __future__ import annotations
import pandas as pd
import statsmodels.api as sm

FACTORS = ["MKT_RF", "SMB", "HML", "RMW", "CMA"]


def fit_five_factor(estimation: pd.DataFrame):
    """Fit excess return on the Fama-French five factors."""
    X = sm.add_constant(estimation[FACTORS])
    return sm.OLS(estimation["excess_return"], X, missing="drop").fit()


def abnormal_returns(event: pd.DataFrame, model) -> pd.Series:
    """Realized excess return minus model-implied excess return."""
    X = sm.add_constant(event[FACTORS], has_constant="add")
    expected = model.predict(X)
    return event["excess_return"] - expected


def cumulative_abnormal_return(ar: pd.Series) -> float:
    return float(ar.sum())
