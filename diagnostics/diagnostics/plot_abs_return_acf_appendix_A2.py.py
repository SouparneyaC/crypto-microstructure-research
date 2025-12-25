import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf
import os

# Plot style (paper-ready)
plt.rcParams.update({
    "font.family": "Times New Roman",
    "font.size": 11,
    "axes.labelsize": 12,
    "axes.titlesize": 14,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11,
    "figure.dpi": 300,
})

# Paths
DATA_DIR = "dataset"
OUT_DIR = "figures"
os.makedirs(OUT_DIR, exist_ok=True)

ASSETS = {
    "BTC": "BTCUSDT.parquet",
    "ETH": "ETHUSDT.parquet",
    "SOL": "SOLUSDT.parquet",
    "DOGE": "DOGEUSDT.parquet",
}

MAX_LAG = 50

# Helper: mean ACF (lags 1..L)
def mean_acf(series, max_lag):
    acf_vals = acf(series, nlags=max_lag, fft=True)
    return np.mean(acf_vals[1:])  # exclude lag 0

# Compute statistics
mean_abs_acf = {}

for asset, file in ASSETS.items():
    df = pd.read_parquet(os.path.join(DATA_DIR, file))

    # Compute 1-minute returns from prices
    returns = df["close"].pct_change().dropna()
    abs_returns = returns.abs()

    mean_abs_acf[asset] = mean_acf(abs_returns, MAX_LAG)

# Plot (bar chart)
assets = list(mean_abs_acf.keys())
values = [mean_abs_acf[a] for a in assets]

fig, ax = plt.subplots(figsize=(6.5, 4.0))

bars = ax.bar(
    assets,
    values,
    color="white",
    edgecolor="black",
    linewidth=1.2
)

ax.set_ylabel("Mean ACF of |Returns| (lags 1–50)")
ax.set_title("Persistence of Absolute Returns Across Cryptocurrencies")

# Subtle grid for readability
ax.yaxis.grid(True, linestyle="--", linewidth=0.6, alpha=0.6)
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig(f"{OUT_DIR}/appendix_A2_abs_return_acf_bar.png", bbox_inches="tight")
plt.show()
