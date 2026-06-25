---
subtitle: "Reposted: originally published on my Pafnuty blog (2008–2014)"
title: "Andrew's Curves now free with python pandas (Reading log)"
date: 2013-10-30
author: "Aman Ahuja"
series:
  - pafnuty-blog
tags:
  - data
  - reading log
categories:
  - reading-log
layout: single
draft: false
---

*Originally published on my old blog, [Pafnuty blog](https://pafnuty.wordpress.com/2013/10/30/andrews-curves-now-free-with-python-pandas-reading-log/). Reposted here as an effort to [consolidate writing](/posts/consolidating-my-writing/) into one place. The original publication date was: October 30, 2013.*

---

[A blog post by Vytautas Jančauskas](http://pandasplotting.blogspot.com/2012/05/andrews-curves.html) talks about the implementation of [Andrew's Curves](http://en.wikipedia.org/wiki/Andrews_plot) in Python [Pandas](http://pandas.pydata.org/). These curves, introduced in David Andrew's paper in 1972, allow one to visualize high dimensional data through transformation.

It is now trivial to generate such a plot from your pandas dataframe:

`import pandas as pd
df = pd.Dataframe(some_data, columns = ['y', 'x1', 'x2', 'x3', 'x4', 'x5'])
pd.tools.plotting.andrews_curves(df, class_column='y')`

I think this is a powerful and exciting tool that could be very insightful for exploratory data analysis.

{{< figure src="so_andrewscurves_03.png" alt="SO_andrewscurves_03" caption="Example: Andrews Plot of randomly generated data" >}}

I noticed a bug in the pandas implementation, which resulted in a [Stack Overflow question](http://stackoverflow.com/questions/19667209/colors-in-andrews-curves) and a [pull request](https://github.com/pydata/pandas/pull/5378) to pandas. The bug was corrected with impressive speed.

I read this paper that expounds upon some of Andrew's ideas:
**César García-Osorio, Colin Fyfe, "Visualization of High-Dimensional Data via Orthogonal Curves" (2005).**

After playing around and reading a bit, I came up with some ideas for future work on this new feature:

## Labels and ticks


In the above example plot, which I generated, the xticks are at multiples of π -- which is sensible because what we are looking at is the projection of data onto the vector of Fourier series on the range (−π < t < π) . But the current pandas implementation has xticks at integer multiples. It also doesn't provide axis labels. I should create a PR for this.

## Column order


The shape of Andrew's curves are highly influenced by the order of variables in the transformation. So in the pandas implementation, the order of the columns is significant.

Here are two plots of the [air quality data set](http://stat.ethz.ch/R-manual/R-devel/library/datasets/html/airquality.html) -- the only difference is column order:
[Added the code I used to generate these plot at the bottom of this section.]

{{< figure src="so_andrewscurves_04_column_order.png" alt="SO_andrewscurves_04_column_order" caption="Andrew's Curves on the same dataset (airquality), but with changed column order." >}}

One might argue this difference does not matter... that if all you are doing is checking for structure in a dataset, then the shape of that structure is not important (compare the airquality Andrew's Plot to the one with random data above). But in fact shapes can be very important when you are using visual data to develop an intuition about numbers. Also, Andrew's Curves can be very informative beyond a binary "yes there is" / "no there isn't" decision with respect to structure, and in that case the column order here could become analogous to bin widths in a histogram.

Here is the same "column-order experiment" as above, this time for the [mtcars dataset](http://stat.ethz.ch/R-manual/R-devel/library/datasets/html/mtcars.html):

{{< figure src="so_andrewscurves_06_column_order.png" alt="SO_andrewscurves_06_column_order" caption="Andrew's Curves on the same dataset (mtcars), but with changed column order." >}}

Surprised? Me too. For the sake of reproducibility, here are the column orders for the three mtcars plots:

`['qsec', 'vs', 'am', 'gear', 'carb', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt']
['wt', 'qsec', 'vs', 'am', 'gear', 'carb', 'mpg', 'cyl', 'disp', 'hp', 'drat']
['drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb', 'mpg', 'cyl', 'disp', 'hp']`

This is an inherent weakness with Andrew's Curves, and no fault of pandas. The people that provide powerful tools cannot be responsible for mistakes that users might make. However, going along with analogy made earlier, anybody creating a tool to generate histograms will provide the capability to adjust bin sizes. In the same way, this vulnerability might need to be acknowledged in some way: by, for example, allowing the user to specify a column order when creating an Andrews Plot, or by allowing the user to generate several plots each with a random column order.

## Other Plots


Andrew's Curves also have other weaknesses, such as biasing some frequencies over others. Variations exist to address these weaknesses, and there are other visualizations built on the principle of transforming high-dimensional data. These might be worth exploring in more detail, but I'm out of time for now. See the paper by García-Osorio for more details.

The code used to generate some of the plots in this post:
https://gist.github.com/amanahuja/7241914

---

/cc @orbitfold @tacaswell @jtratner

---

**Update (2013 Oct 30):**In the above column order test, I was simply cycling the column order, not shuffling them. In the plot below, I'm rearranging the columns completely using random.shuffle(). Also included as a bonus is a side-by-side comparison with a Parallel Coordinates Plot (PCP).

{{< figure src="andrewscurves_ss01_vspcp_shuffle_columns.png" alt="AndrewsCurves_ss01_vsPCP_shuffle_columns" caption="On the left are Andrew's Curves, and the right column of figures are Parallel Coordinate Plots. Each row has a different column order. [Used the mtcars dataset with 'gear' as the class column. ]" >}}
