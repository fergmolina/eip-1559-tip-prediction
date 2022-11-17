# Mechanism Design and the Ethereum Blockchain Transaction Fee Market

In this repo you will finde the full analysis made in the ___"Mechanism Design and the Ethereum Blockchain Transaction Fee Market"___ study. The full analysis paper will be published in this README.

## Data
The data can be downloaded using the scripts in the datasets folder. Each script create a different csv file and must be executed in the following order:
- dataset_hourly.py
- dataset_hourly_validation.py
- dataset_threshold.py
- dataset_validation_threshold.py
- eth_price.py
- eth_price_validation.py
- bsc.py
- bsc_validation.py
- polygon.py
- polygon_validation.py
- nfts.py
- defillama.py – This is the only script that needs 3 csv that are manually downloaded and already in the dataset folder (chain-dataset-BSC.csv, chain-dataset-Ethereum.csv and chain-dataset-Polygon.csv)
- Fear and Index information are also a csv that was manually downloaded and are in the dataset folder. No script is needed to be executed.

Once all the csv files are in the dataset folder you should execute step by step the following scripts located in the root folder of the project:
- final_dataset.ipynb
- dataset_validation.ipynb 


## Code
The code for this project is licensed under BSD 3-Clause ”New” or ”Revised” License. It has the following structure: 

* datasets: contains all the scripts to create all the datasets that are used in this study. All the csv files created using these scripts should be stored in this folder.
* exploratory_analysis: contains all the scripts that are used to create the insights and graphics of exploratory analysis chapter
* root: in the root of the repository it’s stored all the notebooks used to create the models of this study.
    - ARIMA.ipynb
    - Lasso.ipynb
    - Random_Forest.ipynb
    - XGBoost.ipynb


