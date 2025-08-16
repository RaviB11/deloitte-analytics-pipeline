# End-to-End Manufacturing Quality Analytics Pipeline

### Business Problem
This project was designed to solve a common business problem in manufacturing: a lack of timely and actionable insights into production quality. The goal was to build an automated pipeline and an interactive dashboard to help managers identify defect trends and perform root cause analysis.

### Solution
The solution is an end-to-end analytics pipeline that consists of three main components:

#### 1. ETL Data Pipeline
A batch ETL (Extract, Transform, Load) pipeline was built using **Python** and the **Pandas** library. The pipeline automatically ingests raw production data, cleans it, and prepares it for analysis.

* **Key Transformations:** Renaming columns for clarity, creating new business-logic features (`Defect_Status`), and converting units (Kelvin to Celsius).

* **To run the pipeline:** Execute the `etl_pipeline.py` script.

#### 2. Business Intelligence Dashboard
The processed data from the pipeline is used as the source for an interactive dashboard built in **Power BI**. This dashboard visualizes key performance indicators (KPIs) and allows users to drill down into the data.

* **View the Dashboard Walkthrough:** [**Click here to see the PDF Walkthrough**](./Ravi_Bisht_Deloitte_Project_Dashboard_Walkthrough.pdf) 

#### 3. Documentation
This project is fully documented to ensure clarity and maintainability, a key requirement in a consulting environment.

### Technologies Used
- **Data Engineering:** Python, Pandas
- **Visualization:** Power BI
- **Version Control & Documentation:** Git, GitHub

