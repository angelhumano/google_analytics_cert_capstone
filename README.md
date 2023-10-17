# Google Data Analytics Certificate Capstone (Bellabeat Case Study)
By Gabriel Fernandez



## Project in brief
- mention problem
- tools
- insights



## Introduction

Welcome to my Google Analytics Certificate Capstone Project, centered around the Bellabeat case study (Case Study 2: How can a wellness company play it smart?). My objective is to analyze smart device fitness data for Bellabeat, a high-tech manufacturer of health-focused products for women, with a specific focus on the Bellabeat app.  

Through this case study, I will gain valuable insights into how consumers are using the Bellabeat app by performing data analysis. By following the data analysis process steps—Ask, Prepare, Process, Analyze, Share, and Act— I aim to unlock growth opportunities and provide high-level recommendations to guide Bellabeat's marketing strategy.

In this case study, I chose to use **R(RStudio and R Markdown)** for its versatility in completing all phases of data analysis and effectively documenting my findings. This certificate program also introduced me to other valuable tools, including Spreadsheets, SQL, and Tableau.

Visit the [Bellabeat website](https://bellabeat.com/) to learn the company that inspired this case study.

### Business problem

Bellabeat, a successful small company, has the potential to become a major player in the global smart device market. Urška Sršen, the visionary co-founder and Chief Creative Officer, believes that analyzing smart device data can lead to new growth avenues. As a part of the marketing analytics team, I have been tasked with analyzing smart device usage data for the Bellabeat app to guide marketing strategy based on user behavior insights.

Bellabeat offers smart wellness products and services, including:

- **Bellabeat App**: Tracks activity, sleep, stress, menstrual cycle, and mindfulness habits, providing insights for a healthier lifestyle.
- Leaf: A versatile wellness tracker worn as a bracelet, necklace, or clip, monitoring activity, sleep, and stress.
- Time: A smart wellness watch tracking activity, sleep, and stress, providing daily insights.
- Spring: A water bottle that monitors daily water intake to ensure proper hydration.
- Bellabeat Membership: A subscription-based program offering personalized guidance on nutrition, activity, sleep, health, beauty, and mindfulness.


### Data analysis process

I will follow a systematic data analysis process that I learned in the Google Analytics Certificate:

- **Ask**: Formulating pertinent questions to guide my analysis.
- **Prepare**: Gathering and organizing relevant data for analysis.
- **Process**: Cleaning and transforming data for accuracy.
- **Analyze**: Extracting valuable insights from the data.
- **Share**: Presenting my findings to the Bellabeat executive team.
- **Act**: Offering high-level recommendations for Bellabeat's marketing strategy.


![Example Image](images/data_analysis_process.png)

See original source :[Google Data Analytics Professional Certificate by Coursera](https://www.coursera.org/learn/foundations-data/supplement/Yo3Cn/the-data-analysis-process-and-this-program)



### Deliverables for each phase
1. A clear summary of the business task 
2. A description of all data sources used 
3. Documentation of any cleaning or manipulation of data 
4. A summary of your analysis 
5. Supporting visualizations and key findings 
6. Your top high-level content recommendations based on your analysis

## Ask 

**Deliverable 1**: Business task (The question or problem data analysis resolves for a business)

Analyze smart fitness device usage data to gain insight into how people already use them and help guide future marketing strategies for the Bellabeat App. Key stakeholders are Urška Sršen, Sando Mur, and the Bellabeat marketing analytics team.

## Prepare

**Deliverable 2**: Data source description

**Data**: Introducing the Fitbit Fitness Tracker Data

- Brief: Fitbit Fitness Tracker Data, collected via Amazon Mechanical Turk from 30 users in late 2016, offers minute-level physical activity, heart rate, and sleep monitoring. It is accessible on Kaggle.
- Access the data: [FitBit Fitness Tracker Data](https://www.kaggle.com/arashnic/fitbit)
- Contributor: Kaggle user [Möbius](https://www.kaggle.com/arashnic), a Data Scientist specializing in Healthcare.

**Bias and credibility concerns**

The data collection method through Amazon Mechanical Turk introduces potential biases, including sampling, selection, demographic, and incentive-driven biases. These biases may affect the generalizability of findings.

**Data quality checks (ROCCC)**

| Data Quality Check  | Assessment                                                                                   |
|---------------------|----------------------------------------------------------------------------------------------|
| Reliable            | Moderate; user-friendly but concerns about generalizability exist.                        |
| Original            | No; data collected from a third-party source through Amazon Mechanical Turk.               |
| Comprehensible      | Moderate; comprehensibility is affected by variations in participant numbers.              |
| Current             | Outdated; the data is from 2016, potentially affecting the relevance of findings.          |
| Cited               | Yes; data source is properly cited, ensuring transparency and attribution.                  |


**Licensing, privacy, security, and  accessibility**

| Data Aspect    | Assessment                                                       |
|----------------|-------------------------------------------------------------------|
| Licensing      | The data is under CC0 1.0 Universal Public Domain Dedication, allowing unrestricted use for commercial purposes. |
| Privacy        | No personally identifiable information is present in the data.   |
| Security       | I practiced this step, storing the original data in a password-protected MySQL database. |
| Accessibility  | The data is accessible on Kaggle for ease of access and sharing within the data analysis community. |


**Data integrity verification**

Data integrity was ensured through exploratory data analysis and cleaning processes, including column standardization, data type conversion, duplicate removal, zero-value observation removal, and comprehensive data assessment. See the guiding questions for this phase for more details.

**Relevance to analysis**

These datasets provide valuable insights for health and fitness analysis. However, potential biases and data quality concerns should be considered when interpreting the results. Additionally, the lack of gender information may limit its applicability, particularly for products targeted at women by companies like Bellabeat.

Note: During the completion of the capstone, I encountered difficulty in finding an alternative Fitbit dataset, highlighting the challenge of accessing proprietary data. However, during my research, I came across many research articles and analysis that can complement the insights gained from this project. You can find this in the appendix under supplementary analysis

## Process 






## Analyze



## Share 


## Act (Recommendations)




## Limitations

## Challenges

## Guiding questions for each phase

<details>
  <summary> Click here to see the guiding questions</summary>

### Ask (guiding questions)

**What is Bellabeat Mission?**

Bellabeat empowers women to reconnect with themselves, unleash their inner strengths and be what they were meant to be.

**Who are the stakeholders?**

- Urška Sršen: Bellabeat’s cofounder and Chief Creative Officer 
- Sando Mur: Mathematician and Bellabeat’s cofounder; key member of the Bellabeat executive team 
- Bellabeat marketing analytics team: A team of data analysts responsible for collecting, analyzing, and reporting data that helps guide Bellabeat’s marketing strategy. As a junior data analyst on this team for six months, I've been learning about Bellabeat's mission and business goals and how I can assist in achieving them.

**What is the problem that I am trying to solve?** 

- Analyze smart device usage data (in the market) in order to gain insight into how people are already using their smart devices
- Discover insights to unlock growth opportunities
  
**How can your insights drive business decisions?** 

- Trends can inform Bellabeat marketing strategy
- Usage can inspire product modification
- Insights could unlock new growth opportunities for the company

### Prepare (guiding questions)

**Where is your data stored?**

The original data is stored in my password-protected MySQL database on my local user account.

**How is the data organized? Is it in long or wide format?**

Most datasets are organized in a long format, but some redundant datasets are in a wide format. The datasets are in CSV files.

**Are there issues with bias or credibility in this data? Does your data ROCCC?**

Amazon Mechanical Turk (MTurk) facilitated the collection of Fitbit data for the Kaggle dataset. It served as the platform for outsourcing the task of gathering Fitbit data to a widely distributed workforce. Participants who shared their Fitbit data on MTurk may have earned compensation; usually, MTurk typically provides income-earning opportunities. The way these datasets were collected raised the following integrity concerns:

- Sampling bias: The data is derived from a non-random selection of 30 Fitbit users, making it an imperfect representation of the broader population.
- Selection bias: Data collected from Amazon Mechanical Turk (MTurk) depends on participants' voluntary choices, potentially resulting in a non-representative sample.
- Demographic bias: MTurk participants tend to be younger and more tech-savvy, which may limit the generalizability of findings across different age and gender groups.
- Incentive-driven bias: Some MTurk respondents may prioritize speed to maximize their earnings, potentially compromising the data's accuracy
  
Key data quality checks - ROCCC (Reliable, Original, Comprehensible, Current, and Cited):

- Reliable (Moderate): While the data receives a high usability rating of 10 on Kaggle, signifying its user-friendliness, its sourcing raises concerns about generalizability. As a result, any insights derived from this data should be approached with caution.
- Original (No): The data is not original; it was collected from a third-party source involving 30 Fitbit users through Amazon Mechanical Turk. While acquiring data directly from the source would be ideal, it's often not feasible, particularly with proprietary datasets like these.
- Comprehensible (Moderate): The data's comprehensibility is compromised by variations in participant numbers across datasets, potentially impacting the insights drawn from it. For instance, different participant counts across datasets may lead to difficulties in making accurate comparisons and drawing conclusions from the data.
- Current (Outdated): The data is not current, dating back to 2016. While it offers insights for that year, it might not accurately reflect recent trends, potentially impacting the relevance of current findings.
- Cited (Yes): Yes, the data source is cited, indicating transparency and proper attribution to the original data provider.

**How are you addressing licensing, privacy, security, and accessibility?** 

- Licensing: The data is under CC0 1.0 Universal (CC0 1.0) Public Domain Dedication, allowing unrestricted copying, modification, distribution, and use for commercial purposes without seeking permission.
- Privacy: No personally identifiable information is present in the data.
- Security: I practiced this step, storing the original data in a password-protected MySQL database.
- Accessibility: The data is also accessible on Kaggle, ensuring ease of access and sharing within the data analysis community.

**How did you verify the data’s integrity?**

I verified the integrity of the data by performing exploratory data analysis and data cleaning steps.  

**Are there any problems with the data?**

The data exhibits reliability, originality, comprehensibility, and currency issues. Furthermore, verifying data from its original source is not possible, underscoring the need for caution. Another issue I found with the data is the lack of gender information. This is relevant for Bellabeat,  a company producing products for women. If all the data comes from male participants, the insights might not be generalizable to the female users. This is another disadvantage of using Amazon Mechanical Turk to source fitness wearable data. 

**How does it help you answer your question?**

This information is crucial for me in interpreting and analyzing the dataset. It warns me about potential biases and issues, allowing me to approach any analysis or conclusions cautiously. It also highlights limitations, such as the lack of gender information, which could affect the generalizability of insights for a company like Bellabeat. 

## Process (guiding questions)

**What tools are you choosing and why?**

I explored all the tools from the Google Analytics certificate program, including Google Sheets, BigQuery, Tableau, and R. Also, I used MySQL because it gave me more flexibility than the free version of BigQuery.

- Google Sheets: Performed basic exploratory analysis
- BigQuery: Loaded all the datasets to BigQuery and practiced aggregations.
- Tableau: performed some exploratory data analysis.
- MySQL: I initially faced issues loading data using the MySQL Workbench UI. However, I persevered and discovered a faster and more efficient method: loading all the datasets through the terminal.

In the end, **I selected R in RStudio** for the Capstone project because it enabled transparent documentation of data analysis processes with R Notebooks, including data cleaning, transformation, and visualizations. Also, R Markdown made it easy to share my analysis on platforms such as Kaggle and GitHub, making the findings accessible to others interested in the work.

**Have you ensured your data’s integrity?** 
Data integrity was ensured through exploratory data analysis and cleaning processes, including column standardization, data type conversion, duplicate removal, zero-value observation removal, and comprehensive data assessment. See the guiding questions for this phase for more details.

**What steps have you taken to ensure that your data is clean?**

All data cleaning steps are documented in the project's R notebook. Please refer to the notebook for more details. The following are the most important steps I undertook:

- Checked for missing values.
- Changed column names to lowercase for consistency.
- Converted data types.
- Removed duplicates where necessary.
- Identified and removed observations with zero values in the "total_steps" column.
- Conducted an analysis of the distribution of IDs across datasets to identify potential discrepancies in data collection methods, completeness, or user engagement.
- Merged related datasets (hourly_calories, hourly_intensities, and hourly_steps) into a single dataset named "hourly_activity."
- Performed Exploratory Data Analysis (EDA) and summary statistics to better understand the data, detecting anomalies or inconsistencies.
- Identified data inconsistencies and alerted potential issues, such as discrepancies between "sedentary_minutes" and "total_minutes_asleep."
- Assessed data completeness by identifying users with missing activity data and observing declines in data reporting from some users during specific periods.

**How can you verify that your data is clean and ready to analyze?**

After cleaning and transforming the data, I conducted exploratory data analysis (EDA) on each cleaned dataset. I stored each dataset in a new object to preserve the original data. Additionally, I exported the clean datasets. The EDA encompassed:

- Univariate analysis for numerical variables
- Univariate analysis for categorical variables
- Bivariate analysis
- Summary statistics
  
**Have you documented your cleaning process so you can review and share those results?** 
I documented my data cleaning process in an R notebook, noting any issues before proceeding with each step. This detailed record makes it easy for me to review personally and allows for sharing of results with others. Also, I thoroughly documented all findings and insights under the "Observations" section in my notebook.




 
</details>

