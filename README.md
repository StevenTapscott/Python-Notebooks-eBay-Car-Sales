# eBay Car Sales Data Analysis

## Project Overview

This project explores a real-world dataset of used vehicle listings from eBay Kleinanzeigen. The dataset contains over 370,000 vehicle advertisements and includes information on vehicle prices, brands, mileage, registration years, fuel types, and other listing characteristics.

The objective of the project was to clean and prepare a messy real-world dataset, investigate factors influencing vehicle prices, identify patterns in depreciation, and develop a simple vehicle price estimator using historical listing data.

---

## Dataset Information

**Dataset:** eBay Kleinanzeigen Used Car Listings

### Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

### Dataset Size

| Stage | Records |
|---------|---------:|
| Original Dataset | 371,528 |
| After Cleaning | 357,683 |

---

## Project Objectives

The project aimed to:

- Clean and standardise raw vehicle listing data
- Investigate and remove unrealistic outliers
- Explore relationships between vehicle price, mileage, age, and brand
- Identify brands that retain value best
- Visualise key findings
- Develop a simple vehicle price estimator using historical data

---

## Data Cleaning and Preparation

### Column Standardisation

Original column names were converted from mixed camelCase formatting into a consistent snake_case convention.

| Original Column | Renamed Column |
|----------------|----------------|
| dateCrawled | date_crawled |
| offerType | offer_type |
| vehicleType | vehicle_type |
| yearOfRegistration | registration_year |
| powerPS | power_ps |
| fuelType | fuel_type |
| notRepairedDamage | unrepaired_damage |
| postalCode | postal_code |
| lastSeen | last_seen |

### Missing Value Assessment

Several columns contained missing values:

| Column | Missing Values |
|----------|--------------:|
| vehicle_type | Yes |
| gearbox | Yes |
| model | Yes |
| fuel_type | Yes |
| unrepaired_damage | Yes |

Missing values were investigated and retained where appropriate because they represented genuine gaps in user-submitted listing information.

### Outlier Investigation

#### Price Outliers

Price analysis revealed unrealistic values:

- Minimum Price: €0
- Maximum Price: €2.15 Billion

Inspection of extreme values identified numerous invalid listings including:

- €0 listings
- €9,999,999 listings
- €99,999,999 listings

These observations were removed to improve analytical accuracy.

#### Registration Year Outliers

Registration year analysis identified impossible values:

- Earliest Year: 1000
- Latest Year: 9999

Registration years greater than 2026 were considered invalid and removed.

Examples included:

- 5900
- 7000
- 8888
- 9999

---

## Exploratory Data Analysis

### Brand Value Analysis

Average vehicle prices were calculated by manufacturer.

#### Top Value-Retaining Brands

| Brand | Average Price (€) |
|---------|---------:|
| Porsche | 34,155 |
| Land Rover | 16,602 |
| Jaguar | 12,233 |
| Jeep | 11,131 |
| Mini | 9,973 |
| Audi | 8,969 |
| BMW | 8,355 |
| Mercedes-Benz | 8,332 |

#### Key Insight

Premium manufacturers consistently retained higher resale values than mass-market brands.

---

### Mileage Analysis

Vehicles were grouped into mileage bands:

- 0–50k km
- 50k–100k km
- 100k–150k km
- 150k+ km

#### Key Insight

Average vehicle prices declined as mileage increased, demonstrating the expected inverse relationship between mileage and market value.

---

### Vehicle Age Analysis

Vehicle age was calculated using the dataset collection year (2016):

```python
vehicle_age = 2016 - registration_year
```

Vehicles were grouped into:

- 0–5 Years
- 6–10 Years
- 11–15 Years
- 16–20 Years
- 21–40 Years
- 40+ Years

#### Key Insight

Vehicle prices generally declined with age.

However, vehicles older than 40 years displayed significantly higher average values than several younger age groups.

Further investigation revealed that this category contained many classic and collectible vehicles, including:

- Porsche
- Mercedes-Benz
- BMW
- Jaguar
- Volkswagen

This demonstrates that classic cars often appreciate in value rather than depreciate.

---

## Visualisations

Three primary visualisations were created:

### Top 15 Brands by Average Price

**Purpose:** Identify which manufacturers retain value best.

**Finding:** Porsche significantly outperformed all other brands.

### Average Price by Mileage Band

**Purpose:** Investigate the relationship between mileage and vehicle value.

**Finding:** Prices decreased as mileage increased.

### Average Price by Vehicle Age

**Purpose:** Examine depreciation trends.

**Finding:** Vehicle values generally declined with age, except for classic vehicles aged 40+ years.

---

## Vehicle Price Estimator

As an extension to the exploratory analysis, a simple vehicle price estimator was developed.

The estimator uses:

- Brand
- Mileage Band
- Age Band

to estimate an expected vehicle price using grouped historical averages.

### Example

```python
estimated_price(
    "audi",
    "50k-100k",
    "6-10"
)
```

### Output

```text
Estimated Price €16,704
```

This demonstrates how exploratory analysis can be transformed into a practical decision-support tool without requiring machine learning techniques.

---

## Key Findings

- Premium manufacturers retained significantly higher resale values than mass-market brands.
- Porsche recorded the highest average resale value in the dataset.
- Vehicle prices generally declined as mileage increased.
- Vehicle prices generally declined as vehicles aged.
- Classic vehicles older than 40 years often appreciated in value due to collector demand.
- Data cleaning and outlier management were critical to obtaining meaningful analytical results.
- Historical listing data can be used to create simple but effective vehicle price estimation tools.

---

## Skills Demonstrated

### Python

- Data manipulation
- Data cleaning
- Feature engineering
- Function development
- Aggregation and grouping

### Pandas

- DataFrame operations
- Missing value analysis
- GroupBy analysis
- Data transformation

### Data Analysis

- Exploratory Data Analysis (EDA)
- Outlier detection
- Data quality assessment
- Statistical summarisation

### Data Visualisation

- Bar charts
- Comparative analysis
- Insight communication

### Business Analytics

- Price trend analysis
- Depreciation analysis
- Value retention analysis
- Decision-support tool development

---

## Conclusion

This project demonstrates the end-to-end data analysis process, from cleaning a large real-world dataset through to generating actionable business insights. The analysis identified key drivers of vehicle value, highlighted the impact of mileage and age on resale prices, and showed how historical market data can be leveraged to build practical analytical tools.
