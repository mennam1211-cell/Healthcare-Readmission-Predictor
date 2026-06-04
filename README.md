#Patient 30-Day Readmission Risk Predictor

 Team Members
Menna tullah magdy el sabagh

# Project Description
This project focuses on a critical challenge in the healthcare industry: predicting whether a patient will be readmitted to a hospital within a 30-day window following their discharge. 

Using a dataset of 50,000 patient records, we built an end-to-end machine learning pipeline that handles data cleaning (removing duplicates and correcting impossible outlier ages), exploratory data analysis, and advanced feature engineering (creating dynamic clinical metrics like a Blood Pressure-to-BMI ratio). We leveraged `SelectKBest` for optimal feature selection and utilized a tuned `Random Forest Classifier` optimized via `GridSearchCV` to run predictions. Finally, the model was operationalized and deployed as an interactive, live web application interface using Streamlit Cloud.


#Critical Project Links
*  Project Demo Video:** [https://nileuniversity-my.sharepoint.com/:v:/g/personal/m_magdy2268_nu_edu_eg/IQDqLBMkU8iERZ739bgL5he_Adn_kA9c3RROJ8Q9GpjJMJw?e=xmMZQX]
*  Dataset Direct link https://nileuniversity-my.sharepoint.com/:f:/g/personal/m_magdy2268_nu_edu_eg/IgDkjvA_3YBiRofSCuslIn87Abh8pMhv5XUtvh6-q6E0urQ?e=bN3PFr] this also has all the data
* Live Web Application:** https://healthcare-readmission-predictor-sjw583yovyhrqm3pm3ovwb.streamlit.app/

---

## 🛠️ Required Libraries & Dependencies
This project requires Python 3.10+ along with the baseline libraries listed in our `requirements.txt` file:
* `streamlit` (For UI/UX construction)
* `pandas` & `numpy` (For structural data arrays and linear math operations)
* `scikit-learn` (For data transformations, feature selection, and algorithm modeling)
* `joblib` (For importing/exporting pickled asset pipelines)

---

## 🚀 How to Run This Project Locally

1. Clone the Repository
Open your computer terminal and google collab and download this workspace:
```bash
https://github.com/mennam1211-cell/Healthcare-Readmission-Predictor/new/main?filename=README.md
