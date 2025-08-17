# County-Level Climate Analysis Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://climatedasboard-m8jnmrjrd6ltxhgnbet8x3.streamlit.app/)

## Overview

This repository contains an interactive web application for performing detailed climate trend analysis on county-level data for the United States. The initial implementation focuses on the Standardized Precipitation Index (SPI).

The project is architected as a fully self-contained, automated system. It integrates a data pipeline that automatically fetches, processes, and updates the application's data on a monthly schedule using GitHub Actions.

## Live Application

The live, interactive dashboard is deployed on Streamlit Cloud and is available at the following URL:
**[https://climatedasboard-m8jnmrjrd6ltxhgnbet8x3.streamlit.app/](https://climatedasboard-m8jnmrjrd6ltxhgnbet8x3.streamlit.app/)**

---

## Features

*   **County-Specific Analysis:** Users can input any 5-digit US County FIPS code to load and analyze data for that specific geography.
*   **Comprehensive Analysis Suite:** The application provides a suite of standard time-series analyses:
    *   **Trend Analysis:** Visualization of long-term trends using a 12-month rolling average.
    *   **Anomaly Detection:** Identification of statistical anomalies (defined as >2 standard deviations from the rolling mean).
    *   **Seasonal Decomposition:** Decomposition of the time series into observed, trend, seasonal, and residual components.
    *   **Autocorrelation Analysis:** Generation of ACF and PACF plots to inspect the data's correlation structure.
    *   **Forecasting:** Predictive 24-month forecasting using an ARIMA model.
*   **Automated Data Refresh:** The underlying dataset is automatically updated monthly via a GitHub Actions workflow.

---

## System Architecture and Workflow

This project is designed as a single, self-sustaining repository ("monorepo") that handles both the data pipeline and the user-facing application. It utilizes **Git LFS** to manage large data files and **GitHub Actions** for full automation.

The workflow is as follows:

1.  **Scheduled Trigger:** A GitHub Actions workflow is scheduled to run on the first day of every month.
2.  **Data Pipeline Execution:** The workflow executes a series of scripts within a cloud-based runner:
    *   `download_script.py`: Fetches the latest raw data from the source (CDC).
    *   `parse_precipitation_index.py`: Cleans and processes the raw data into a standardized format.
    *   The processed data is then converted into the efficient Parquet format (`spi_data.parquet`).
3.  **Data Versioning and Update:** The workflow commits the new Parquet data file back to the repository. Git LFS handles the storage of this large file.
4.  **Continuous Deployment:** Streamlit Cloud detects the new commit in the repository and automatically redeploys the application, making the fresh data immediately available to users.

---

## Local Development

To run this application on a local machine, follow these steps.

### Prerequisites
*   Git
*   Git LFS (`sudo apt-get install git-lfs`)
*   Python 3.8+ and `pip`

### Installation
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/vishalworkdatacommon/climate_dasboard.git
    cd climate_dasboard
    ```

2.  **Pull LFS data:**
    Download the large data files tracked by Git LFS.
    ```bash
    git lfs pull
    ```

3.  **Set up a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application
Launch the Streamlit application with the following command:
```bash
streamlit run app.py
```
The application will open in your default web browser.