# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 08:26:17 2026

@author: gargi
"""
#importing libraraies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#loading csv
df = pd.read_csv(r"C:\Student_Analysis\Student_Analysis Final - Form responses 1.csv")

#checking load data
df.head()

#checking number of responses and variable
df.shape

#column names
df.columns

#checking data type
df.dtypes

#complete overview
df.info()

#checking missing values
df.isnull().sum()

missing_values = df.isnull().sum()
missing_values[missing_values > 0]

#checking for duplicates
df.duplicated().sum()

#check rating column
for column in df.columns:
    if df[column].dtype != "object":
        print("\n", column)
        print(df[column].unique())

#checking min and max values
df.describe().T

#dropping unwanted columns
clean_df = df.copy()
print(clean_df.columns.tolist())
clean_df = clean_df.drop(
    columns=["Name of the Student", "Phone Number"]
)

#checking missing values again
clean_df.isnull().sum()
missing = clean_df.isnull().sum()
missing[missing > 0]

#check for negative value
numeric_cols = clean_df.select_dtypes(include=np.number).columns
for column in numeric_cols:
    if (clean_df[column] < 0).any():
        print("Negative values found in:", column)

#saving cleaned csv
clean_df.to_csv("Student_Analysis_Cleaned.csv", index=False)

#save status check
import os
print(os.path.exists("Student_Analysis_Cleaned.csv"))

#checking new cleaned file
clean_df.shape
clean_df.head()

#data cleaning summary

print("DATA CLEANING SUMMARY")
print("-" * 40)

print("Original number of responses:", df.shape[0])
print("Original number of columns:", df.shape[1])

print("Missing values in raw data:", df.isnull().sum().sum())

print("Duplicate rows in raw data:", df.duplicated().sum())

print("Final number of responses:", clean_df.shape[0])
print("Final number of columns:", clean_df.shape[1])

print("\nColumns in cleaned dataset:")
print(clean_df.columns.tolist())

#summary report
cleaning_summary = pd.DataFrame({
    "Item": [
        "Original Responses",
        "Original Columns",
        "Missing Values",
        "Duplicate Rows",
        "Final Responses",
        "Final Columns"
    ],
    "Value": [
        df.shape[0],
        df.shape[1],
        df.isnull().sum().sum(),
        df.duplicated().sum(),
        clean_df.shape[0],
        clean_df.shape[1]
    ]
})

cleaning_summary

#descriptive stats
import pandas as pd
import numpy as np

clean_df = pd.read_csv("Student_Analysis_Cleaned.csv")

print("Dataset loaded successfully!")
print("Shape:", clean_df.shape)

#variables to analyze
print(clean_df.columns.tolist())

#identify numerical variables
numerical_columns = clean_df.select_dtypes(include=np.number).columns
print("NUMERICAL VARIABLES:")
for i, column in enumerate(numerical_columns, start=1):
    print(i, ":", column)
    
#checking how many numerical variables we have
print("\nTotal numerical variables:", len(numerical_columns))

#mean
mean_values = clean_df[numerical_columns].mean()
print("MEAN OF NUMERICAL VARIABLES:")
print(mean_values)

#extending mean to 2 decimal places
mean_values = mean_values.round(2)
print("MEAN:")
print(mean_values)

#median
median_values = clean_df[numerical_columns].median()
print("MEDIAN OF NUMERICAL VARIABLES:")
print(median_values.round(2))

#mode
mode_values = clean_df[numerical_columns].mode().iloc[0]
print("MODE OF NUMERICAL VARIABLES:")
print(mode_values)

#range,variance,standarad deviation
#Range
range_values = clean_df[numerical_columns].max() - clean_df[numerical_columns].min()

# Variance
variance_values = clean_df[numerical_columns].var()

# Standard Deviation
std_values = clean_df[numerical_columns].std()

print("RANGE:")
print(range_values.round(2))

print("\nVARIANCE:")
print(variance_values.round(2))

print("\nSTANDARD DEVIATION:")
print(std_values.round(2))

#quartile,percentile,iqr
# First Quartile (Q1) = 25th percentile
Q1 = clean_df[numerical_columns].quantile(0.25)

# Second Quartile (Q2) = 50th percentile / Median
Q2 = clean_df[numerical_columns].quantile(0.50)

# Third Quartile (Q3) = 75th percentile
Q3 = clean_df[numerical_columns].quantile(0.75)

# Interquartile Range
IQR = Q3 - Q1

print("Q1 (25th Percentile):")
print(Q1.round(2))

print("\nQ2 (50th Percentile / Median):")
print(Q2.round(2))

print("\nQ3 (75th Percentile):")
print(Q3.round(2))

print("\nIQR:")
print(IQR.round(2))

#few more percentiles
percentiles = clean_df[numerical_columns].quantile(
    [0.10, 0.25, 0.50, 0.75, 0.90]
)
print("PERCENTILES:")
print(percentiles.round(2))

#descriptive statistics table

descriptive_stats = pd.DataFrame({
    "Mean": mean_values,
    "Median": median_values,
    "Mode": mode_values,
    "Range": range_values,
    "Variance": variance_values,
    "Standard Deviation": std_values,
    "Q1": Q1,
    "Q3": Q3,
    "IQR": IQR
})

descriptive_stats = descriptive_stats.round(2)

descriptive_stats

#saving this table
descriptive_stats.to_csv(
    "Descriptive_Statistics.csv"
)

#selecting important variables
print("All numerical columns:")
for i, column in enumerate(numerical_columns, start=1):
    print(i, ":", column)
    
#selecting variables we actually need - Key Variables
print(clean_df.columns.tolist())

key_variables = [
    "How many hours do you sleep per day?",
    
    "How many hours per day do you spend on mobile phones for non-academic purposes?",
    
    "How many hours per day do you spend on entertainment/social media/gaming? ",
    
    "How many hours per day do you spend on self-learning? ",
    
    "How many hours per week do you spend developing your career-domain skills? ",
    
    "How many hours per week do you spend on physical activity/sports/walking? ",
    
    "How many hours per week do you spend working on practical projects? ",
    
    "How would you rate your current skill level in your chosen domain? ",
    
    "How many domain-specific projects have you completed? ",
    
    "How many of these projects were developed independently by you? ",
    
    "How frequently do you practice your domain skills? ",
    
    "How many hours per week do you spend solving real-world/domain-specific problems? ",
    
    "How many domain-related courses/certifications have you completed? ",
    
    "How many internships or industry projects have you completed? ",
    
    "How confident are you in applying your domain knowledge to a real-world problem? ",
    
    "If you receive a new problem in your chosen domain, how confident are you that you can solve it independently? ",
    
    "How confident are you in explaining your project to an industry professional? ",
    
    "How confident are you about getting an internship/job in your chosen domain? "
]

print("Number of key variables:", len(key_variables))

#seperate dataset for key variables
key_df = clean_df[key_variables].copy()
print("Key analysis dataset shape:", key_df.shape)
key_df.head()

#final stat table
# ============================================================
#SELECT NUMERICAL KEY VARIABLES
# ============================================================

numerical_key_variables = [
    "How many hours do you sleep per day?",
    
    "How many hours per day do you spend on mobile phones for non-academic purposes?",
    
    "How many hours per day do you spend on entertainment/social media/gaming? ",
    
    "How many hours per day do you spend on self-learning? ",
    
    "How many hours per week do you spend developing your career-domain skills? ",
    
    "How many hours per week do you spend on physical activity/sports/walking? ",
    
    "How many hours per week do you spend working on practical projects? ",
    
    "How would you rate your current skill level in your chosen domain? ",
    
    "How many domain-specific projects have you completed? ",
    
    "How many of these projects were developed independently by you? ",
    
    "How many hours per week do you spend solving real-world/domain-specific problems? ",
    
    "How many domain-related courses/certifications have you completed? ",
    
    "How many internships or industry projects have you completed? ",
    
    "How confident are you in applying your domain knowledge to a real-world problem? ",
    
    "If you receive a new problem in your chosen domain, how confident are you that you can solve it independently? ",
    
    "How confident are you in explaining your project to an industry professional? ",
    
    "How confident are you about getting an internship/job in your chosen domain? "
]

key_df = clean_df[numerical_key_variables].copy()

print("Number of numerical key variables:", len(numerical_key_variables))
print("Shape:", key_df.shape)

# ============================================================
# PRACTICE FREQUENCY
# ============================================================

practice_frequency = clean_df[
    "How frequently do you practice your domain skills? "
]

print(practice_frequency.value_counts())

# ============================================================
# FINAL DESCRIPTIVE STATISTICS
# ============================================================

key_stats = pd.DataFrame({
    "Mean": key_df.mean(),
    "Median": key_df.median(),
    "Mode": key_df.mode().iloc[0],
    "Range": key_df.max() - key_df.min(),
    "Variance": key_df.var(),
    "Standard Deviation": key_df.std(),
    "Q1": key_df.quantile(0.25),
    "Q3": key_df.quantile(0.75),
    "IQR": key_df.quantile(0.75) - key_df.quantile(0.25)
})

key_stats = key_stats.round(2)

key_stats

#calculating freq and percentage
# ============================================================
# PRACTICE FREQUENCY ANALYSIS
# ============================================================

practice_counts = clean_df[
    "How frequently do you practice your domain skills? "
].value_counts()

print("PRACTICE FREQUENCY:")
print(practice_counts)

practice_percentages = (
    clean_df[
        "How frequently do you practice your domain skills? "
    ]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

print("PRACTICE FREQUENCY PERCENTAGES:")
print(practice_percentages)

practice_summary = pd.DataFrame({
    "Frequency": practice_counts,
    "Percentage": practice_percentages
})

practice_summary

practice_summary.to_csv("Practice_Frequency_Summary.csv")

#percentile analysis
key_percentiles = key_df.quantile(
    [0.10, 0.25, 0.50, 0.75, 0.90]
).round(2)

# Give meaningful names to percentile rows
key_percentiles.index = [
    "10th Percentile",
    "25th Percentile (Q1)",
    "50th Percentile (Median)",
    "75th Percentile (Q3)",
    "90th Percentile"
]

key_percentiles.to_csv("Member2_Percentiles.csv")

#important variable summary

important_variables = [
    "How many hours do you sleep per day?",
    "How many hours per day do you spend on self-learning? ",
    "How many hours per week do you spend developing your career-domain skills? ",
    "How many hours per week do you spend working on practical projects? ",
    "How would you rate your current skill level in your chosen domain? ",
    "How many domain-specific projects have you completed? ",
    "How many of these projects were developed independently by you? ",
    "How many hours per week do you spend solving real-world/domain-specific problems? ",
    "How confident are you in applying your domain knowledge to a real-world problem? ",
    "If you receive a new problem in your chosen domain, how confident are you that you can solve it independently? ",
    "How confident are you in explaining your project to an industry professional? ",
    "How confident are you about getting an internship/job in your chosen domain? "
]

important_stats = key_stats.loc[important_variables]

important_stats

print("Percentile table saved successfully!")

key_percentiles

important_stats.to_csv("Member2_Important_Statistics.csv")

print("Important statistics table saved successfully!")

#compare mean and median
mean_median_comparison = pd.DataFrame({
    "Mean": key_df.mean(),
    "Median": key_df.median()
})

mean_median_comparison["Difference"] = (
    mean_median_comparison["Mean"]
    - mean_median_comparison["Median"]
)

mean_median_comparison = mean_median_comparison.round(2)

mean_median_comparison

#identifying variables where mean and median differ noticably
noticeable_difference = mean_median_comparison[
    mean_median_comparison["Difference"].abs() > 0.5
]

noticeable_difference

#OUTLIER DETECTION USING IQR

Q1_outlier = key_df.quantile(0.25)
Q3_outlier = key_df.quantile(0.75)

IQR_outlier = Q3_outlier - Q1_outlier

lower_limit = Q1_outlier - 1.5 * IQR_outlier
upper_limit = Q3_outlier + 1.5 * IQR_outlier

outlier_summary = pd.DataFrame({
    "Q1": Q1_outlier,
    "Q3": Q3_outlier,
    "IQR": IQR_outlier,
    "Lower Limit": lower_limit,
    "Upper Limit": upper_limit
}).round(2)

outlier_summary

#Count outliers in each variable

outlier_counts = {}

for column in key_df.columns:
    outliers = key_df[
        (key_df[column] < lower_limit[column]) |
        (key_df[column] > upper_limit[column])
    ]
    
    outlier_counts[column] = len(outliers)

outlier_counts = pd.Series(outlier_counts).sort_values(ascending=False)

print("OUTLIER COUNT BY VARIABLE:")
print(outlier_counts)

#show variables having outliers
outlier_counts[outlier_counts > 0]

#final summary
final_summary = pd.DataFrame({
    "Mean": key_df.mean(),
    "Median": key_df.median(),
    "Mode": key_df.mode().iloc[0],
    "Standard Deviation": key_df.std(),
    "Q1": key_df.quantile(0.25),
    "Q3": key_df.quantile(0.75),
    "IQR": key_df.quantile(0.75) - key_df.quantile(0.25)
})

final_summary = final_summary.round(2)

#summary table
final_summary = pd.DataFrame({
    "Mean": key_df.mean(),
    "Median": key_df.median(),
    "Mode": key_df.mode().iloc[0],
    "Standard Deviation": key_df.std(),
    "Q1": key_df.quantile(0.25),
    "Q3": key_df.quantile(0.75),
    "IQR": key_df.quantile(0.75) - key_df.quantile(0.25)
})

final_summary = final_summary.round(2)

final_summary

final_summary

final_summary.to_csv("Member2_Final_Summary.csv")

#stastical interpretation

for column in important_variables:
    mean = key_df[column].mean()
    median = key_df[column].median()
    std = key_df[column].std()
    
    print("\nVariable:", column)
    print("Mean:", round(mean, 2))
    print("Median:", round(median, 2))
    print("Standard Deviation:", round(std, 2))

print("Final Member 2 summary saved successfully!")

#highest and lowest mean value
mean_values = key_df.mean().sort_values(ascending=False)

print("HIGHEST MEAN VALUES:")
print(mean_values.head(5))

print("\nLOWEST MEAN VALUES:")
print(mean_values.tail(5))

#coefficient of variance
cv = (key_df.std() / key_df.mean()) * 100

cv_summary = pd.DataFrame({
    "Mean": key_df.mean(),
    "Standard Deviation": key_df.std(),
    "Coefficient of Variation (%)": cv
}).round(2)

cv_summary

cv_summary.to_csv("Member2_Coefficient_of_Variation.csv")

print("Coefficient of variation table saved successfully!")

#branch-wise student distribution
branch_counts = clean_df["Engineering Branch"].value_counts()

branch_percentages = (
    clean_df["Engineering Branch"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

branch_summary = pd.DataFrame({
    "Number of Students": branch_counts,
    "Percentage": branch_percentages
})

branch_summary

branch_summary.to_csv("Member2_Branch_Summary.csv")

print("Branch-wise summary saved successfully!")

#year wise student distribution
year_counts = clean_df["Year of study"].value_counts()

year_percentages = (
    clean_df["Year of study"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

year_summary = pd.DataFrame({
    "Number of Students": year_counts,
    "Percentage": year_percentages
})

year_summary

year_summary.to_csv("Member2_Year_Summary.csv")

print("Year-wise summary saved successfully!")

#career domain distribution

domain_column = "Which domain do you want to build your career in?"

domain_counts = clean_df[domain_column].value_counts()

domain_percentages = (
    clean_df[domain_column]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

domain_summary = pd.DataFrame({
    "Number of Students": domain_counts,
    "Percentage": domain_percentages
})

domain_summary

domain_summary.to_csv("Member2_Career_Domain_Summary.csv")

print("Career-domain summary saved successfully!")

#career domain clarity
clarity_column = "How clear are you about your chosen career domain?"

clarity_counts = clean_df[clarity_column].value_counts().sort_index()

clarity_percentages = (
    clean_df[clarity_column]
    .value_counts(normalize=True)
    .sort_index()
    .mul(100)
    .round(2)
)

clarity_summary = pd.DataFrame({
    "Number of Students": clarity_counts,
    "Percentage": clarity_percentages
})

clarity_summary

clarity_summary.to_csv("Member2_Career_Clarity_Summary.csv")

print("Career clarity summary saved successfully!")

#gender distribution

gender_counts = clean_df["Gender"].value_counts()

gender_percentages = (
    clean_df["Gender"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

gender_summary = pd.DataFrame({
    "Number of Students": gender_counts,
    "Percentage": gender_percentages
})

gender_summary

gender_summary.to_csv("Member2_Gender_Summary.csv")

print("Gender summary saved successfully!")

#domain wise skill and practice analysis

domain_skill_column = (
    "How would you rate your current skill level in your chosen domain? "
)

domain_practice_column = (
    "How many hours per week do you spend developing your career-domain skills? "
)

domain_analysis = clean_df.groupby(
    domain_column
).agg(
    Number_of_Students=(domain_column, "size"),
    Average_Skill=(domain_skill_column, "mean"),
    Average_Practice_Hours=(domain_practice_column, "mean")
)

domain_analysis = domain_analysis.round(2)

domain_analysis

domain_analysis.to_csv("Member2_Domain_Wise_Analysis.csv")

print("Domain-wise analysis saved successfully!")



# SELF-STUDY BY YEAR
import pandas as pd

# Load cleaned dataset
clean_df = pd.read_csv("Student_Analysis_Cleaned.csv")

self_study_column = "How many hours per day do you spend on self-learning? "

year_self_study = clean_df.groupby("Year of study")[
    self_study_column
].mean().sort_values(ascending=False)

print("Average Self-Study Hours by Year:")
print(year_self_study.round(2))

print("\nYear with highest average self-study:")
print(year_self_study.idxmax())

print("Average self-study hours per day:",
      round(year_self_study.max(), 2))


#Which branch studies the most
import pandas as pd

# Load cleaned dataset
clean_df = pd.read_csv("Student_Analysis_Cleaned.csv")

self_study_column = "How many hours per day do you spend on self-learning? "

branch_self_study = clean_df.groupby("Engineering Branch")[
    self_study_column
].mean().sort_values(ascending=False)

print("Average Self-Study Hours by Engineering Branch:")
print(branch_self_study.round(2))

print("\nBranch with highest average self-study:")
print(branch_self_study.idxmax())

print("Average self-study hours per day:",
      round(branch_self_study.max(), 2))