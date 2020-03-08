from __future__ import division
import math
import numpy as np
from scipy.optimize import minimize

def neg_llh(theta, S):
    f, d = theta
    return -(S[0] * np.log(1. - f + f * np.exp(-d))
        + np.sum(S[1:]) * (np.log(f) - d)
        + np.sum(S[k] * (k * np.log(d) - np.log(math.factorial(k))) for k in range(1, len(S))))

def find_mle(S, guess):
    # NB: initial guess is important for convergence!
    if guess is None:
        guess = (1e-3, 0.5)
    return minimize(neg_llh, x0=guess, args=(S,), bounds=((0, 1), (0, None)))

def check_mle(f, d, S):
    if np.sum(S) == 0:
        return False
    x_bar = np.sum(S * np.arange(0, len(S))) / np.sum(S)
    return np.isclose(x_bar * (1 - np.exp(-d)), d * (1 - S[0] / np.sum(S))) \
       and np.isclose(f, x_bar / d)

def relative_error(a, b):
    return abs(a - b) / b

def estimate_parameters(counts, guess=None):
    result = find_mle(counts, guess)
    f, d = result.x
    return f, d, -neg_llh((f, d), counts), check_mle(f, d, counts)
