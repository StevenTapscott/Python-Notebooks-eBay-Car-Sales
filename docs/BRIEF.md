# Project 5: eBay Car Sales Data

The eBay Kleinanzeigen dataset is messy in the way real data always is: column names in German, outlier prices in the millions, registration years in the future, and inconsistent formatting throughout. Cleaning it properly, and being transparent about your decisions, is the whole project.

## Skills You'll Practice

- pandas
- data cleaning
- outlier detection
- string manipulation
- exploratory data analysis (EDA)

## Dataset

**eBay Kleinanzeigen Car Sales** (Kaggle)

## Step-by-Step Instructions

### 1. Load the Data

- Import the dataset into pandas.
- Inspect column names.
- Review data types.
- Explore missing values and overall structure.

### 2. Clean Column Names

- Standardize column names.
- Convert names to snake_case.
- Improve consistency and readability.

### 3. Handle Outliers

Identify and address unrealistic values in:

- Price
- Mileage

Examples may include:

- Vehicles listed for €0
- Multi-million euro listings
- Impossible mileage values

Document all cleaning decisions and justify why records were removed or retained.

### 4. Explore Relationships

Analyze how vehicle price relates to:

- Brand
- Mileage
- Vehicle age

Use summary statistics and visualizations to identify patterns.

### 5. Brand Value Analysis

Calculate average prices by brand.

Investigate:

- Which brands retain value best
- Which brands depreciate most heavily
- Premium versus budget brand performance

### 6. Create Visualizations

Summarize findings using charts and graphs.

Potential visualizations:

- Average price by brand
- Mileage versus price
- Vehicle age versus price
- Price distributions

## Take It Further

Build a simple price estimator.

Given:

- Brand
- Mileage
- Vehicle age

Estimate the expected price range.

This does not need to be a machine learning model.

A grouped average lookup table is sufficient and transforms the project from a standard EDA exercise into an interactive analytical tool.

## Why Employers Care

Data cleaning is widely reported as accounting for **60–80% of real-world data science work**.

A project that demonstrates:

- Transparent cleaning decisions
- Outlier detection methodology
- Data quality assessment
- Documentation of assumptions

shows the type of rigorous, audit-ready thinking that analytics and data science teams value.

## Learning Resources

### Dataquest Guided Project

**Exploring eBay Car Sales Data**

Provides a structured walkthrough of:

- Data cleaning
- Data transformation
- Exploratory analysis

### Preview Video

A free walkthrough video is available for previewing the overall project approach before starting.

### Recommended Course

**Introduction to Pandas and NumPy for Data Analysis (Dataquest)**

Key topics covered:

- Data cleaning techniques
- Pandas workflows
- Data transformation methods
- Exploratory analysis fundamentals

## Portfolio Value

This project demonstrates:

- Real-world data cleaning
- Data quality assessment
- Exploratory data analysis
- Business-focused insights
- Analytical communication
- Practical pandas proficiency

It is an excellent beginner-to-intermediate portfolio project because it mirrors the messy, imperfect datasets analysts encounter in professional environments.
