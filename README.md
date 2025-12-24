# Crypto Microstructure: The Predictability Gap

This research investigates the divergence between directional price predictability and volatility persistence in high-frequency crypto markets (1-minute intervals).

## 📈 Key Findings
- **The Predictability Gap**: Directional price movement is near-random, with baseline models (Logistic Regression/Random Forest) struggling to exceed **50.5% accuracy**.
- **Structural Memory**: Unlike direction, volatility exhibits high persistence. Our Ridge Regression models achieved an **Out-of-Sample R² of 0.274** for BTC and **0.221** for ETH.
- **Microstructure Signal**: High autocorrelation (~0.35) in absolute returns at early lags suggests that volatility is a latent state with significant tradable memory.

## 📊 Visual Evidence
Detailed ACF (Autocorrelation Function) plots and performance tables are located in the `results/` directory. These plots provide visual confirmation of volatility clustering, which serves as the primary feature for our predictive models.

## 🛠 Project Structure
- **src/models/**: Implementation of Ridge Regression and Random Forest architectures.
- **src/preprocessing/**: Feature engineering for volatility and return distributions.
- **results/tables/**: Comparative metrics (^2$, RMSE, Accuracy) across BTC, ETH, SOL, and DOGE.
- **diagnostics/**: Scripts for testing stationarity and autocorrelation.

---
**Author:** Souparneya Chakrabarti
