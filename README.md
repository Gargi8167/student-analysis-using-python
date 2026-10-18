# Real Data-Student-Analysis-Project
Statistical analysis of student lifestyle, learning habits, career-domain preferences, skill development, and career readiness using Python, Pandas, and NumPy.
# Student Lifestyle & Learning Habits Analysis

A Python-based statistical analysis of student lifestyles, self-learning habits, skill development, and career-domain preferences using survey data.

## Overview

This project analyzes survey responses from 33 students to explore their learning patterns, daily routines, technical skills, and career interests. It uses descriptive statistics and group-wise comparisons to identify trends and provide actionable insights.

## Objectives

- Analyze self-learning and domain-specific practice hours.
- Study sleep patterns and entertainment habits.
- Explore career-domain preferences and skill ratings.
- Compare learning trends across academic years and branches.
- Summarize findings to support better learning and career planning.

## Tools & Technologies

- **Python**
- **Pandas** — data cleaning and analysis
- **NumPy** — statistical calculations
- **Matplotlib** — imported for plotting

## Methodology

1. Inspect and clean the survey dataset.
2. Remove personal identifiers from the analysis dataset.
3. Calculate descriptive statistics, percentiles, variance, standard deviation, and interquartile range (IQR).
4. Group responses by academic year, branch, gender, and career domain.
5. Export statistical summaries as CSV files.

## Key Findings

- AI/ML was the most preferred career domain in the survey.
- Second-year students showed the highest reported average daily self-learning time.
- Most respondents reported around 7–7.5 hours of sleep per day.
- Many students reported limited time for domain-specific practice and project development.


## Project Outputs

The analysis generates CSV files containing:

- Descriptive statistics and important statistical measures
- Percentiles and coefficient of variation
- Practice-frequency summaries
- Branch-wise and year-wise comparisons
- Career-domain, career-clarity, and gender summaries
- Domain-wise skill and practice analysis
- Cleaned student survey data

## How to Run

1. Clone or download this repository.
2. Install the required libraries:

   ```bash
   pip install pandas numpy matplotlib
   ```

3. Place the survey CSV file in the project directory.
4. Run `Student_Analysis.py` using Python.

**Note:** The input CSV filename and column names must match those referenced in the script.

## Limitations

- The analysis is based on a small survey sample.
- Results describe the collected data and do not establish causation.
- The project focuses on statistical analysis rather than predictive modelling.


