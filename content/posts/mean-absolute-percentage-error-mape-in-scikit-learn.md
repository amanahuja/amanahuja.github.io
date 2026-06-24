---
title: "Mean absolute percentage error (MAPE) in Scikit-learn"
date: 2013-06-26
author: "Aman Ahuja"
series:
  - pafnuty-blog
tags:
  - algorithm
  - coding
  - data
  - error
  - machine learning
  - mean absolute percentage error
  - numpy
  - python
  - regression analysis
  - scikit-learn
  - scipy
categories:
  - CHANGETHISCATEGORY
layout: single
draft: false
---

*Originally published on my old blog, [Pafnuty blog](https://pafnuty.wordpress.com/2013/06/26/mean-absolute-percentage-error-mape-in-scikit-learn/). Reposted here as an effort to [consolidate writing](/posts/consolidating-my-writing/) into one place. The original publication date was: June 26, 2013.*

---

On [CrossValidated](http://stats.stackexchange.com/), the [StackExchange](http://stackexchange.com/) for statistics, someone asks:
> How can we calculate the Mean absolute percentage error (MAPE) of our predictions using Python and scikit-learn?

[Mean Absolute Percentage Error (MAPE)](http://en.wikipedia.org/wiki/Mean_absolute_percentage_error) is an metric used to determine the success of a [regression analysis](http://en.wikipedia.org/wiki/Regression_analysis "Regression analysis"). Read my answer on CV here:

<http://stats.stackexchange.com/questions/58391/mean-absolute-percentage-error-mape-in-scikit-learn/62511#62511>

**Cross posting my answer here:**
As noted (for example, [in Wikipedia](http://en.wikipedia.org/wiki/Mean_absolute_percentage_error)), MAPE can be problematic. Most pointedly, it can cause division-by-zero errors. My guess is that this is why it is not included in the sklearn metrics.
However, it is simple to implement.
[gist https://gist.github.com/amanahuja/6315882]
Use like any other metric...:
[code language="python"]
> y\_true = [3, -0.5, 2, 7]; y\_pred = [2.5, -0.3, 2, 8]
> mean\_absolute\_percentage\_error(y\_true, y\_pred)
Out[19]: 17.738095238095237
[/code]
(Note that I'm multiplying by 100 and returning a percentage.)
... but with caution:
[code language="python"]
> y\_true = [3, 0.0, 2, 7]; y\_pred = [2.5, -0.3, 2, 8]
> #Note the zero in y\_true
> mean\_absolute\_percentage\_error(y\_true, y\_pred)
-c:8: RuntimeWarning: divide by zero encountered in divide
Out[21]: inf
[/code]
