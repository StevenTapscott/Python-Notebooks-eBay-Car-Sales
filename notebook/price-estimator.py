
import pandas as pd

price_estimator = pd.read_csv(
    "output/price_estimator.csv"
)

def estimated_price(
        brand,
        milegae_band,
        age_band
):
    
    result = price_estimator[
        (price_estimator['brand'] == brand)
        & (price_estimator['mileage_band'] == milegae_band)
        & (price_estimator['age_band'] == age_band)
        ]
    
    if result.empty:
        print("No results found")
    else:
        print(f"Estimated Price €{result.iloc[0]['price']:,.0f}")

#For this section, select the car brand (can range from Audi, Porsche etc.).
#milege_band consist of 0-50k, 50k-100k, 100-150k, 150k.
#age_band consist of 0-5 years, 6-10 years, 11-15 years, 16-20 years, 21-40 years, and 40+ years.
estimated_price(
    "porsche",
    "50k-100k",
    "40+"
)