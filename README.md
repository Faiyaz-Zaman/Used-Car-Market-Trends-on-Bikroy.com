# **UsedCarVisualization**

## **Problem Statement**

The goal of this project is to gather information on used cars in Bangladesh from [here](https://bikroy.com/en/ads/c/bangladesh/cars/used)
Later we used the scraped data to understand the following demographics and correlations using Tableau dashboard:

1.Market Insights: What is the scenario of used cars for sale across different cities?

2.Price-Mileage Relationship: Is there a significant relationship between a car's price and the mileage it has driven?

3.Brand Impact: Does the brand influence the price? Which brand commands the highest resale value?

4.Usage Patterns: After how much usage (in terms of mileage or years) do buyers typically sell their cars?

5.Top-Performing Models: Which car model stands out with the highest average price and the highest mileage driven when sold?

## **Findings**
1. Dhaka has the highest number of used cars for sale (192) with an average pricing of (Tk. 27,67,969)
2. Yes, there is a relation between them. As mileage increases price also decreases but the brand of the car is also a factor 
3. Yes, the brand affects their pricing.BMW has the highest selling value among all the other cars.
4. It depends on different brands, for example, Nissan users sell their car after 115,856 km, Cherry 26,100, etc. The rest of them are shown in the Tableau dashboard.
5. Nissan Teana cc 2400 2005 has an average mileage of 990000 km with an average price of 1080000.

You can visit the public dashboard [here](https://public.tableau.com/app/profile/faiyaz.zaman/viz/UsedCarVisualization/Dashboard1?publish=yes)
## Build From Sources
1. Clone the repo 
```bash
git clone: [https://github.com/Faiyaz-Zaman/tableauprojects.git](https://github.com/Faiyaz-Zaman/UsedCarVisualization.git)
```
2. Initialize and activate virtual env 
```bash
virtualenv --no-site-packages venv
source venv/bin/activate
```
3.Install dependencies
```bash
pip install -r requirements.txt
```
4.Check the scrapped data
```bash
https://github.com/Faiyaz-Zaman/UsedCarVisualization/blob/main/lastsecondhand_car_details.csv

```
5.Data Processing
```bash
I used Pandas to process the data, starting with converting the Price column, originally in string format (e.g., TK 12,333), into integers. I applied the same transformation to the Mileage Driven column. One major issue I encountered was inconsistency in city names—some entries had Dhaka Division while others had just Dhaka, which Tableau recognized as a separate location. To resolve this, I standardized the names to Dhaka.
```

