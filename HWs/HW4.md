---
layout: page
title: HW4 - Data Science Part 2
nav_exclude: true
---

# HW4 - Predicting NYC Property Values Part 2
Due Date: 

This homework _picks up from HW3: Part 1_. You should make a copy of that file, rename it to `hw4.ipynb`, and add cells as appropriate under your existing code.

## Part 2 - Predicting Property Prices

Now that we have some ideas about what parameters are important, let's fit a regression model to predict property prices. Here's a general outline of your job:

1. Feature engineering & selection.
2. Train your model.
3. Explore different models and features to see what gives the best results.
4. Plot your results!

### Feature Engineer & Feature Selection

Think about what you think would be the most informative features to train on. Additionally, you may think of some more features that may be informative to the model. Don't simply include all features to your model, this might result in some terribly long training times. Ideally, your model shouldn't take longer than about 30 seconds to train. For reference, the best model I found took only about 9 seconds to train.

A warning: don't include any features that are derived from price! For example, if we include `price_per_sqft` and `gross_square_feet`, then our model will easily figure out the price and have basically zero error. Since our goal is to determine the price, we should only provide features that are disjoint from it.

### Picking a Model

Once you've got an idea of which features are important, let's train our model! You should be doing the following:

1. Slice your dataset to include the features you want.
2. Split your dataset into a training set and labels, and testing set and labels.
3. Fit the model!
4. Test the model to determine it's accuracy. There are two lines commented out that you may find useful.

**You will not be graded on how optimal the model is, simply if you've correctly trained one.** Kudos will be given to the best tuned model :) Here's some models that you might want to try from scikit, but feel free to use anything you want!

* [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
* [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)
* [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html)

Once you pick the features you think are important and train your mode, play around with some different types to see how well you can do! You won't be graded on how optimal the model is, but for reference, we were able to get a log MSE of about 26 and and R^2 of about 0.64

You may find these useful to quickly compare your models.

`from sklearn.metrics import mean_squared_error, r2_score`

`print("Log of Mean Squared Error:", np.log(mean_squared_error(y_pred, y_test)))`

`print("R^2 value:", r2_score(y_pred, y_test))`

Some tips:

* Start with as few features as possible, then slowly add more. Otherwise, your model might take too long to train! In the real world, you might actually want to do the opposite since you might have some beefy machines and more data typically means better fits.
* Use a fixed random state in your models, e.g. `random_state=2`. This will ensure that you can compare different feature sets.
* The provided lines will print out the (log of the) mean square error (MSE) and the R^2 value. In short, the lower the MSE the better, and the closer to 1 the R^2 the better. Typically, an R^2 value over 0.7 is fairly good in practice. For reference, I was able to pretty easily get an R^2 of 0.5 or so, but it took some effort to get to 0.64 or so.

### Visualization

Finally, let's visualize our predictions. Your goal is to use Matplotlib to generate a scatter plot. The x-axis should be your predicted property value and the y-axis should be the true value. Note that if our prediction was perfect, everything would simply be a point on the line y=x! In light of this, include the line defined by y=x in some other color. This way, we can visualize how far off our estimates are by seeing how far they lie from this line. Finally, add an x label, a y label, and a title to your plot.

Note, given some outliers, you probably will want to cap your graph at something like $2.5m, otherwise you probably won't see anything meaningful. Take a look at [`set_xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html) and [`set_ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html).

### Extra Credit

Visualize your results in any other meaningful way using Matplotlib. Plot something other than what we already plotted!