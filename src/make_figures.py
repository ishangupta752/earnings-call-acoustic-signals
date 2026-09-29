from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
FIGURES.mkdir(exist_ok=True)

ret = pd.read_csv(RESULTS / "return_regression.csv")
plot = ret[ret["variable"].isin(["Tone Index", "Pause Ratio", "Size", "Book-to-Market"])]
fig, ax = plt.subplots(figsize=(8, 4.8))
ax.bar(plot["variable"], plot["coefficient"])
ax.axhline(0, linewidth=0.8)
ax.set_ylabel("Reported coefficient")
ax.set_title("Announcement-Period CAR Regression")
ax.tick_params(axis="x", rotation=20)
fig.tight_layout()
fig.savefig(FIGURES / "return_regression.png", dpi=180)
plt.close(fig)

rob = pd.read_csv(RESULTS / "robustness_results.csv")
fig, ax = plt.subplots(figsize=(8, 4.8))
ax.barh(rob["specification"], rob["tone_coefficient"])
ax.axvline(0, linewidth=0.8)
ax.set_xlabel("Reported tone coefficient")
ax.set_title("Tone Effect Across Robustness Specifications")
fig.tight_layout()
fig.savefig(FIGURES / "robustness_results.png", dpi=180)
plt.close(fig)
