# Data Science Project

## Introduction
This repository contains two data analysis projects:
1. **NSF Article Summaries Analysis**: This dataset includes several article summaries, one per file, provided by the National Science Foundation (NSF). The goal is to build a text classification model based on topics using natural language processing (NLP) techniques.
2. **Birmingham City Council Purchase Card Transactions Analysis**: This dataset contains purchase card transaction records from the Birmingham City Council. The objective is to perform exploratory data analysis (EDA).

NSF data is available at the following URL, which will download a 2020.zip file: [NSF Data](https://www.nsf.gov/awardsearch/download?DownloadFileName=2020&All=true).
Transaction data is retrieved from the following URL using a web scraper: [Birmingham City Council Transactions](https://www.cityobservatory.birmingham.gov.uk/@birmingham-city-council/purchase-card-transactions).

## Project Structure
```
project/
│
├── README.md
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── requirements_scraping.txt
├── notebooks/
├── scripts/
│   ├── pipeline_webscrap.py
│   ├── pipeline_nlp.py
|
├── data/
└── 
```

- **`data` folder**: Stores the extracted data and some files generated during the project execution.
  - `2020.zip`: Compressed file containing the article summaries provided by the NSF.
  - `Forecast Data/`: Folder where transaction data downloaded from the Birmingham City Council URL will be stored.

- **`notebooks` folder**: Contains all the notebooks used for data visualization and exploration.

- **`scripts` folder**: Contains the necessary scripts for data extraction.
  - `pipeline_nlp.py`: Script to process NSF data.
  - `pipeline_web_scraper.py`: Script to obtain transaction data from the Birmingham City Council.

- **`.gitignore` file**: Specifies which files and folders should be ignored by Git.

- **`docker-compose.yml` file**: Defines and runs multi-container Docker applications, used to create the web scraper container.

- **`Dockerfile`**: Contains instructions to build the Docker image that mounts a Firefox browser and its necessary drivers to execute the web scraper.

- **`README.md` file**: This file, provides a detailed description of the project, installation instructions, and usage guidelines.

- **`requirements_scraping.txt` file**: Lists the specific requirements needed for the Docker container of the web scraper.

- **`requirements.txt` file**: Lists all the dependencies needed for the project.

# Prerequisites

To run the project, you need to have the following tools and libraries installed:

1. **Python**: Ensure Python is installed. You can download it from [here](https://www.python.org/downloads/).
2. **Virtual Environment**: It is recommended to create a virtual environment to manage the project dependencies.
3. **Requirements.txt**: All necessary libraries for the project are listed in the `requirements.txt` file. You can install them by running:
   ```bash
   pip install -r requirements.txt
   ```
4. **Docker**: Docker is needed to mount a container that will be used for web scraping the Birmingham City Council data. You can download Docker from [here](https://www.docker.com/get-started).

## Installation

1. **Clone the Repository**:
    ```sh
    git clone url_repo
    cd your_project
    ```

2. **Create a Virtual Environment and Install Dependencies**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `source venv/Scripts/activate`
    pip install -r requirements.txt
    ```

# Project Execution

## Data Acquisition and Collection

The project is divided into two main parts, each with its own data acquisition script. The scripts are located within the `scripts` folder of each project.

### 1. NLP Pipeline (NSF Data)
This script processes the article summaries provided by the NSF.

**Steps:**
1. **Unzip Files**: The `2020.zip` file contains numerous XML files.
2. **Process XML Files**: The XML files are processed to extract the most relevant information.
3. **Generate a CSV**: All extracted information is consolidated into a CSV file for further analysis.

**Execution:**
```bash
python scripts/pipeline_nlp.py
```

**Notes:**
- Ensure the `2020.zip` file downloaded from the URL is located in the project's main folder, as the script will use it.
- The script will generate a CSV file with the processed data, extracting the most relevant information for subsequent analysis.

### 2. Web Scraper Pipeline (Birmingham City Council Data)
This script uses Docker to run a web scraper that obtains historical purchase card transaction data from the Birmingham City Council.

**Steps:**
1. **Mount the Docker Container**: The container contains all the necessary drivers to run the web scraper.
2. **Run the Web Scraper**: The web scraper accesses the URL where the data is located and downloads it.
3. **Store the Data**: The downloaded files are stored in the `Forecast Data` folder.

**Execution:**
```bash
python scrpipts/pipeline_webscraper.py
```

**Notes:**
- Ensure Docker is installed and running correctly.
- The downloaded XLS files will be saved in the `Forecast Data` folder within `data`.

### Directories and Files
- `scripts/pipeline_nlp.py`: Script to process NSF data.
- `scripts/pipeline_web_scraper.py`: Script to obtain transaction data from the Birmingham City Council.
- `2020.zip`: Compressed file containing NSF data.
- `data/Forecast Data/`: Folder where the downloaded transaction data will be stored.