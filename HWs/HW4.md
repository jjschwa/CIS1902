---
layout: page
title: HW4 - Data Science Part 2
nav_exclude: true
---

**If you're reading this before class on Wednesday, 3/18, it may not be complete and is subject to changes.**

# HW4 - Predicting NYC Property Values Part 2
Due Date: Wednesday, April 1st

This homework _picks up from HW3: Part 1_. You should make a copy of that file, rename it to `hw4.ipynb`, and add cells as appropriate under your existing code.

## Part 2 - Predicting Property Prices

Now that we have some ideas about what parameters are important, let's fit a regression model to predict property prices. Here's a general outline of your job:

1. Feature engineering & selection.
2. Train your model.
3. Explore different models and features to see what gives the best results.
4. Plot your results!

### Feature Engineering & Feature Selection

Think about what you think would be the most informative features to train on. In class, we used both logic from our intuition about what would be informative as well as plotting the correlations of the variables. 

Additionally, you may think of some more features that may be informative to the model. Don't simply include all features to your model, this might result in some terribly long training times. Ideally, your model shouldn't take longer than about 30 seconds to train. For reference, the best model we have found took only about 9 seconds to train.

A warning: do NOT include any features that are derived from price! For example, if we include `price_per_sqft` and `gross_square_feet`, then our model will easily figure out the price and have basically zero error. Since our goal is to determine the price, we should only provide features that are disjoint from it.

### Picking a Model

Once you've got an idea of which features are important, let's train our model! You should be doing the following:

1. Slice your dataset to include the features you want.
2. Split your dataset into a training set and labels, and testing set and labels.
3. Fit the model!
4. Test the model to determine it's accuracy. 

**You will not be graded on how optimal the model is, simply if you've correctly trained one.** Kudos will be given to the best tuned model :)) 

Here's some models that you might want to try from scikit, but feel free to use anything you want! We encourage you to explore what's out there and to practice reading documentation to learn more.

* [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
* [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)
* [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html)

Once you pick features and train your model, experiment with different model types to see how performance changes.

For reference, we were able to get:

* Log MSE ≈ 26
* R² ≈ 0.64


You may find these useful to quickly compare your models.

`from sklearn.metrics import mean_squared_error, r2_score`

`print("Log of Mean Squared Error:", np.log(mean_squared_error(y_pred, y_test)))`

`print("R^2 value:", r2_score(y_pred, y_test))`

Some tips:

* Start with as few features as possible, then slowly add more. Otherwise, your model might take too long to train! In the real world, you might actually want to do the opposite since you might have some beefy machines and more data typically means better fits.
* Use a fixed random state in your models, e.g. `random_state=2`, so results are reproducible.
* Lower MSE is better.
* R² closer to 1 is better.
* R² above 0.7 is typically strong in practice.


### Visualization

Now visualize your predictions.

Use Matplotlib to generate a scatter plot:

- X-axis: Predicted property value
- Y-axis: True property value

If the prediction were perfect, all points would lie on the line y = x. Include the line y = x in a different color so you can visually assess how far predictions deviate.

Add:
- X label
- Y label
- Title

Because of outliers, you will likely want to cap your graph at around $2.5 million. Use set_xlim and set_ylim to do this.

### Model Comparison and Reflection
After training at least two different models:
1. Create a small comparison table that includes:
    - Model name
    - Log(MSE)
    - R²
2. Answer the following:
    - Which model performed best?
    - Was the most complex model necessarily the best?
    - How did adding or removing features affect performance?
    - If you had to deploy one model in a real-world setting, which would you choose and why?

This problem is intended to help you think critically about model selection rather than just training one model and stopping there.

### Cross-Validation

A single train/test split may not fully represent how well your model performs.

Use 5-fold cross-validation on your best model.

Compute:
- The R² score for each fold
- The average R² across all folds

Then answer:
- What is the average cross-validated R²?
- How does it compare to your original test R²?
- What does cross-validation tell us about model stability?
- Why might relying on only one train/test split be misleading?

#### Extra Credit
Visualize your results in another meaningful way using Matplotlib.
Examples:
- Residual plot (prediction error vs predicted value)
- Histogram of prediction errors
- Borough-specific prediction error comparison
- Error vs square footage plot

### Deep Learning

Please answer the following questions in your notebook:

1. A single-layer perceptron is very similar to linear regression because when there are no hidden layers, it simply computes a weighted sum of the input features (plus a bias), resulting in a linear relationship between the inputs and the output.
    - In the context of this dataset, what does this mean about the type of relationships it can model between features (eg., square footage, borough) and price?
2. Give at least one example of a relationship in this dataset that might be nonlinear (ie., not well modeled by a straight line). You should answer this based on your real-world intuition about the relationships of the features in the dataset, what you learned about the relationships in previous parts, or informal visualizations (don't feel like you need to plot it out, but rather try to picture the graph).
3. Neural networks use hidden layers and activation functions.
    a. Give an example of an activation function and its pros and cons.
    b. How would these components help model the relationship you described in question 2?
4. Suppose you train a neural network on this dataset.
    a. Give one reason it might perform better than linear regression
    b. Give one reason it might perform worse or be less practical
5. Would a CNN be a good choice for this property dataset? Why or why not?

Include a short explanation of what your visualization shows.

# Submission
Submit your completed `hw4.ipynb` notebook and the `hw4.py` file.
Make sure:
- All code runs without errors
- All questions are answered
- All plots are labeled
- Explanations are clear and concise
