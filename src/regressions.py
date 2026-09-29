"""Illustrative event-level regressions used in the research design."""
from __future__ import annotations
import pandas as pd
import statsmodels.formula.api as smf


def car_regression(df: pd.DataFrame):
    """CAR on tone, pause ratio, firm controls, and industry effects."""
    formula = "CAR ~ TONE + PAUSE + SIZE + BM + COVER + C(industry)"
    return smf.ols(formula, data=df).fit(cov_type="HC1")


def volume_regression(df: pd.DataFrame):
    """Change in log volume on acoustic measures."""
    formula = "delta_log_volume ~ TONE + PAUSE + ENERGY"
    return smf.ols(formula, data=df).fit(cov_type="HC1")
