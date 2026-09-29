"""Acoustic feature utilities matching the paper's conceptual workflow."""
from __future__ import annotations
import numpy as np


def rms_energy(signal: np.ndarray) -> float:
    """Root-mean-square amplitude of a one-dimensional audio signal."""
    x = np.asarray(signal, dtype=float)
    return float(np.sqrt(np.mean(np.square(x))))


def pause_ratio(signal: np.ndarray, threshold: float = 0.01) -> float:
    """Share of samples whose absolute amplitude is below a silence threshold."""
    x = np.asarray(signal, dtype=float)
    if x.size == 0:
        return float("nan")
    return float(np.mean(np.abs(x) < threshold))


def standardize(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    sd = x.std(ddof=0)
    if sd == 0:
        return np.zeros_like(x)
    return (x - x.mean()) / sd


def tone_index(pitch: np.ndarray, energy: np.ndarray) -> np.ndarray:
    """Simple standardized composite illustrating the paper's tone concept.

    The paper defines TONE using the first principal component of standardized
    pitch and energy. This helper returns an equal-weight standardized composite
    for transparent demonstration; use PCA for exact replication.
    """
    return (standardize(pitch) + standardize(energy)) / np.sqrt(2.0)
