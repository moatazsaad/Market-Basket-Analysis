1- This project focuses on market basket analysis using the Apriori algorithm. Market basket analysis is a data mining technique used to uncover associations between items purchased together in transactions. The goal is to identify patterns in customer purchasing behavior to optimize product placement, promotions, and marketing strategies.

2- The dataset used in this project is the "Online Retail" dataset, which contains transaction records from an online retail store. Initially, the dataset is loaded and preprocessed. A sample of 40,000 rows is taken for analysis.

3- The main steps of the analysis include:

- Data Preprocessing: The dataset is cleaned, and extra spaces in the description column are removed.

- Market Basket Analysis for Sweden: Transactions for the country of Sweden are extracted and encoded into a binary format suitable for Apriori analysis. The Apriori algorithm is applied to identify frequent itemsets, which represent items frequently purchased together. Association rules are generated to uncover relationships between items, based on metrics such as support, confidence, and lift.

- Insights and Recommendations: The association rules are interpreted to extract actionable insights for business decisions. High lift values indicate positive associations between items, suggesting opportunities for promotion, cross-selling, bundling, and targeted marketing campaigns. Specific recommendations are provided for leveraging these insights to improve sales and customer satisfaction.

- Streamlit Web Application: A Streamlit web application is developed to interactively explore the association rules analysis. Users can select a country from the dataset and view top association rules, products to promote, and cross-selling opportunities tailored to the selected country.

- The project demonstrates how market basket analysis can be applied to real-world retail datasets to derive valuable insights and inform business strategies for increasing revenue and customer engagement.

4- The provided Streamlit web application allows users to dynamically explore association rules for different countries, empowering businesses to make data-driven decisions based on customer purchasing patterns.
- You can interact with the deployed application on the cloud by visiting the following link:
(https://market-hhlqxt4hzmxuob6kflxdbt.streamlit.app/)
- If Streamlit is down, you can still run the Streamlit app locally, execute the following command in the last cell of the notebook:
!streamlit run streamlit_app.py
