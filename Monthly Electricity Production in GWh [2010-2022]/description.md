# About Dataset
The data was collected from the website of the International Energy Agency (IEA), specifically from their Monthly Electricity Statistics tool available at iea.org/data-and-statistics/data-tools/monthly-electricity-statistics

If you're interested in how the data was collected, you can check: github.com/ccan23/iea_electricity_generation_data_scraper

The data includes information about energy production in various countries on a monthly basis from 2010 to 2022. The energy production is measured in gigawatt-hours (GWh) and covers a range of energy products including hydro, wind, solar, geothermal, nuclear, fossil fuels, and others.

## Countries:
Argentina, Australia, Austria, Belgium, Brazil, Bulgaria, Canada, Chile, Colombia, Costa Rica, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, IEA Total, Iceland, India, Ireland, Italy, Japan, Korea, Latvia, Lithuania, Luxembourg, Malta, Mexico, Netherlands, New Zealand, North Macedonia, Norway, OECD Americas, OECD Asia Oceania, OECD Europe, OECD Total, People's Republic of China, Poland, Portugal, Republic of Turkiye, Romania, Serbia, Slovak Republic, Slovenia, Spain, Sweden, Switzerland, United Kingdom, United States

## Products:
Hydro, Wind, Solar, Geothermal, Other renewables, Nuclear, Total combustible fuels, Coal, Oil, Natural gas, Combustible renewables, Other combustible non-renewables, Not specified, Net electricity production, Total imports, Total exports, Electricity supplied, Used for pumped storage, Distribution losses, Final consumption, Electricity trade, Renewables, Non-renewables, Others, Other renewables aggregated, Low carbon, Fossil fuels

The dataset columns include:

**COUNTRY**: Name of the country

**CODE_TIME**: A code that represents the month and year (e.g., JAN2010 for January 2010)

**TIME**: The month and year in a more human-readable format (e.g., January 2010)

**YEAR**: The year of the data point

**MONTH**: The month of the data point as a number (1-12)

**MONTH_NAME**: The month of the data point as a string (e.g., January)

**PRODUCT**: The type of energy product (e.g., Hydro, Wind, Solar)

**VALUE**: The amount of electricity generated in gigawatt-hours (GWh)

**DISPLAY_ORDER**: The order in which the products should be displayed

**yearToDate**: The amount of electricity generated for the current year up to the current month in GWh

**previousYearToDate**: The amount of electricity generated for the previous year up to the current month in GWh

**share**: The share of the product in the total electricity generation for the country in decimal format
