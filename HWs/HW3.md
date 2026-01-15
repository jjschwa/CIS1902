---
layout: page
title: HW3 - Data Science Part 1
nav_exclude: true
---

# HW3 - Predicting NYC Property Values Part 1
Due Date: 

[nyc-property-sales.csv](../HWs/nyc-property-sales.csv)

[nyc_properties.ipynb](../HWs/hw3.ipynb)

This dataset was taken from Kaggle.

In this assignment, we'll be working with a dataset of property sales within New York City boroughs from a 12-month period, roughly 2016-2017. This assignment has two parts:

1. First, we'll first clean the data and then answer some questions that will provide us with insight to formulate a predictive model for property prices.
2. We'll then use the insights from above to create a linear regression model to predict prices.

Attached you will find the dataset of NYC property sales (`nyc-property-sales.csv`). Information about the columns are described in the table below. Additionally, you will find a starter Python Notebook (`nyc_properties.ipynb`) with cells that have questions you should determine the answers to. Submit your completed notebook on Canvas.

| Column | Definition |
|--------|------------|
| borough | 1:Manhattan, 2:Bronx, 3:Brooklyn, 4:Queens, 5:Staten Island |
| neighborhood | Neighborhood Name |
| building_class_category | Categorization of buidling, i.e. walk-up, elevator building, condo, etc. |
| address | Street Address |
| apartment_number | Aparment number |
| zip_code | Zip Code |
| residential_units | Number of residential units in the building |
| commercial_units | Number of commercial units in the building |
| total_units | Total units (residential + commercial) in the building |
| land_square_feet | Square feet of the land the building is built on |
| gross_square_feet | The total area of all the floors of a building as measured from the exterior surfaces of the outside walls of the building, including the land area and space within any building or structure on the property. |
| year_built | Year building was built |
| sale_price | Amount of sale. Zero values indicate transfer of deeds, for example parent to child. |
| sale_date | Date of sale |

### Cleaning our Data

Do the following within a single cell of your notebook.

We'll need to clean our data to ensure that the columns are formatted the way we want. First, let's convert every column that we think should be a numeric value (hint: how did we do this for the duration column in the UFO lab?). These should be:

```text
residential_units
commercial_units
total_units
land_square_feet
gross_square_feet
year_built
sale_price
```

Our dataset includes _all_ propety sales
within the date range in NYC. So there's lot of things we probably don't care about, e.g. `36 OUTDOOR RECREATIONAL FACILITIES`.
Let's assume that we only want to learn about residential style properties from the perspective of someone looking for a home. Filter out any rows that do not fall under the following `building_class_category`:

```text
01 ONE FAMILY DWELLINGS
02 TWO FAMILY DWELLINGS
03 THREE FAMILY DWELLINGS
```

Next, let's drop some rows that don't make sense for our anaylsis.

1. Let's make sure that the sale was indeed for a home and not a commercial business. Specifically, further filter out any rows that have `residential_units` equal to 0.
2. Drop any rows that do not have a `sale_price` or are less than $65,000. Many sales occur with a nonsensically small dollar amount: $0 most commonly. Most of these sales are actually transfers of deeds between parties: for example, parents transferring ownership to their home to a child after moving out for retirement.
3. Drop any rows that do not have a `gross_square_feet` or `land_square_feet`, or have a value of 0.

As a checkpoint, you should now have a dataset with no null values and 24,416 rows.

### Gaining Insights from our Data

Next, we want to validate some hypothesis about the data we have. For example, it's highly likely that the borough and neighborhood drastically change the price of a property, but we should be sure that this is the case first. Answer each question in the corresponding cell of your notebook by printing them out.

1. Borough sensitivity: what are the average property prices per borough? What about the standard deviation of the average property prices per borough?
2. Square footage sensitivity: what is the average price per gross square foot per borough? What about the standard deviation?
3. Neighborhood sensitivity: what are the most expensive and least expensive neighborhoods in each borough?
4. Neighborhood sensitivity 2: what are the most expensive and least expensive neighborhoods in each borough _if we consider the per unit price_? That is, we instead average the price per residential unit of a building.
