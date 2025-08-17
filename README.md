# County-Level Climate Analysis Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://YOUR_STREAMLIT_APP_URL_HERE)

An interactive web application for performing detailed climate trend analysis on county-level data for the United States, starting with the Standardized Precipitation Index (SPI).

This repository is a fully self-contained, automated system. It includes a live data pipeline that automatically fetches the latest data, processes it, and updates the application.

## 🚀 Live Application

You can access the live, interactive dashboard here:
**[https://YOUR_STREAMLIT_APP_URL_HERE](https://YOUR_STREAMLIT_APP_URL_HERE)**
*(Note: Replace this URL with your actual Streamlit Cloud URL after deployment.)*

---

## ✨ Features

*   **Interactive County Selection:** Enter any 5-digit US County FIPS code to load its specific data.
*   **Multi-Analysis Suite:** Perform a variety of time-series analyses on the selected county's data:
    *   **Trend Analysis:** Visualize the long-term trend with a 12-month rolling average.
    *   **Anomaly Detection:** Identify months with unusually high or low SPI values (more than 2 standard deviations from the mean).
    *   **Seasonal Decomposition:** Break down the time series into its observed, trend, seasonal, and residual components.
    *   **Autocorrelation:** Analyze the ACF and PACF plots to understand the data's correlation structure.
    *   **Forecasting:** Generate a 24-month forecast using a predictive ARIMA model.
*   **Fully Automated:** The underlying data is automatically refreshed on a monthly schedule.

---

## ⚙️ Overall Workflow & Architecture

This project is designed as a single, self-sustaining repository that handles both the data pipeline and the user-facing application. It uses **Git LFS** to manage large data files and **GitHub Actions** for full automation.

The architecture can be understood as two parts that work together within this repository:

1.  **The Automated Data Factory (The Pipeline):** A background process that automatically creates the final data product.
2.  **The Live Application (The Storefront):** The Streamlit app that users interact with.

Here is a diagram of the complete, end-to-end workflow:

```
+------------------------------------------------------+
| 1. GITHUB ACTIONS (The Robot)                        |
| (Triggered automatically on the 1st of every month)  |
+------------------------------------------------------+
                         |
                         ▼
+------------------------------------------------------+
| 2. RUNS PIPELINE SCRIPTS (The Factory)               |
|    - download_script.py  (Fetches new raw data)      |
|    - parse_precipitation_index.py (Cleans the data)  |
|    - Converts the clean data to spi_data.parquet     |
+------------------------------------------------------+
                         |
                         ▼
+------------------------------------------------------+
| 3. PUSHES NEW DATA (The Robot restocks the shelf)    |
|    - Commits the new spi_data.parquet file           |
|    - Pushes the commit to the repository via Git LFS |
+------------------------------------------------------+
                         |
                         ▼
+------------------------------------------------------+
| 4. STREAMLIT CLOUD (The Storefront)                  |
|    - Automatically detects the new commit            |
|    - Redeploys the app with the fresh data file      |
|    - Users see the latest data on their next visit   |
+------------------------------------------------------+
```

---

## 📂 Repository Structure

```
climate_dasboard/
├── .github/
│   └── workflows/
│       └── update_data.yml   # The instruction manual for the GitHub Actions robot
├── .gitattributes            # Configures which files are handled by Git LFS
├── .gitignore                # Tells Git which files to ignore (e.g., cache files)
├── app.py                    # The main Streamlit application code (the "Storefront")
├── download_script.py        # Pipeline script to download raw data
├── parse_precipitation_index.py  # Pipeline script to clean raw data
├── import_configs.json       # Configuration for the pipeline
├── index/                    # Contains the raw input data for the pipeline
├── spi_data.parquet          # The final, clean data file used by the app (managed by LFS)
└── requirements.txt          # A list of all Python libraries required
```

---

## 🛠️ Getting Started & Local Development

To run this application on your own machine, follow these steps.

### Prerequisites
*   Git
*   Git LFS (`sudo apt-get install git-lfs`)
*   Python 3.8+ and `pip`

### Installation & Setup
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/vishalworkdatacommon/climate_dasboard.git
    cd climate_dasboard
    ```

2.  **Pull the large data files:**
    After cloning, you need to pull the data files being tracked by Git LFS.
    ```bash
    git lfs pull
    ```

3.  **Create and activate a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application Locally
To launch the Streamlit web application, run the following command in your terminal:
```bash
streamlit run app.py
```
This will open the application in your default web browser.
