# Monitoring and Alerts Assignment

## Overview

In this assignment, you'll be creating a monitoring system for a data engineering project. You'll be working with data from Google BigQuery (GBQ) that tracks various metrics related to data harvesting and processing activities on the Carbitrage project. The goal is to practice building a system that can provide meaningful insights and alerts based on the state of the data.

You will have two options for this assignment: either create a **Daily Monitoring Report** or implement an **Alert-Based Monitoring System**. The choice is yours, and each option will allow you to demonstrate your ability to effectively analyze data and build a notification system.

## Options

### 1. Daily Monitoring Report
Your task is to build a script that produces a daily snapshot of activity in the project. This report will be run daily (or maybe twice a day). You can use the notebook `monitoring.ipynb` to create and print a message similar to the sample provided, including key metrics about the data.

This option will allow you to practice regularly aggregating data and presenting it in a clear and informative way. Consider which metrics are most important to monitor over time.

### 2. Alert-Based Monitoring System
Instead of a daily report, you can create an alert system that triggers when certain thresholds are met or when anomalies are detected in the data. For instance, if the number of harvested pages drops below a certain threshold, an alert message should be generated.

This option focuses more on anomaly detection and requires setting up logic for when an alert should be triggered. You'll need to define meaningful thresholds for the metrics you're tracking.

## Provided Materials
- **Functions File (`student_functions.py`)**: This file contains several functions that query Google BigQuery tables and return basic counts. Use these functions to gather data for your monitoring or alert system.
- **Notebook (`gbq_student_notebook.ipynb`)**: This notebook will help you connect to Google BigQuery, use the functions provided, and build a simple monitoring message.

## Next Steps
1. **Review the provided functions** and understand how they retrieve data from GBQ.
2. **Choose an option** (Daily Monitoring or Alerts) and plan your approach to gather, analyze, and present the data.
3. **Implement your solution** in the provided notebook, using the functions to gather data and logic to build your report or alerts.

Feel free to experiment and add your own ideas to make the monitoring system more insightful. This assignment is meant to help you think critically about monitoring and alerting systems in a data engineering context. Good luck, and have fun!

