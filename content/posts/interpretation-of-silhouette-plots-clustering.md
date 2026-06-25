---
title: "Interpretation of Silhouette Plots (Clustering)"
date: 2013-02-04
author: "Aman Ahuja"
series:
  - pafnuty-blog
tags:
  - algorithm
  - cluster analysis
  - clustering
  - cross validated
  - data
  - data analysis
  - data mining
  - exploratory data analysis
  - k-means
  - silhouette coefficient
  - silhouette plot
  - stack overflow
  - visualization
categories:
  - experiments
layout: single
draft: false
---

*Originally published on my old blog, [Pafnuty blog](https://pafnuty.wordpress.com/2013/02/04/interpretation-of-silhouette-plots-clustering/). Reposted here as an effort to [consolidate writing](/posts/consolidating-my-writing/) into one place. The original publication date was: February 4, 2013.*

---

I am cross-posting here one of my answers on [Stack Exchange - Cross Validation](http://stats.stackexchange.com/ "Cross Validated (Stack Exchange Network)") (that's like Stack Overflow for statistics). The question had already been answered and accepted when I posted my answer several months later, but I chose to spend some time putting in my thoughts anyway.

I'm particularly interested in the interpretation of simple plots in the context of [exploratory data analysis](http://en.wikipedia.org/wiki/Exploratory_data_analysis "Exploratory data analysis"), and am planning to compile resources for data explorers on this subject. My plan is to do this via a wiki -- which I have [already installed](http://eda.amanahuja.me/ "EDA wiki") but not yet populated with much information. So busy these days!

**[Q: How to interpret the meaning of a Silhouette plot?](http://stats.stackexchange.com/questions/10540/how-to-interpret-mean-of-silhouette-plot/44653 "Cross Validated")**

How does one determine the number of clusters through interpretation of a Silhouette plot?

[I have paraphrased the OP's question. -AA]

## **My answer**


(Click through to [my answer on Cross Validated](http://stats.stackexchange.com/questions/10540/how-to-interpret-mean-of-silhouette-plot/44653#44653) for the most recent version of the answer, which may have changed.)

Sergey's answer contains the critical point, which is that the silhouette coefficient quantifies the quality of clustering achieved -- so you should select the number of clusters that maximizes the silhouette coefficient.

---

The long answer is that the best way to evaluate the results of your clustering efforts is to start by actually examining -- human inspection -- the clusters formed and making a determination based on an understanding of what the data represents, what a cluster represents, and what the clustering is intended to achieve.

There are numerous quantitative methods of evaluating clustering results which should be used as tools, with full understanding of the limitations. They tend to be fairly intuitive in nature, and thus have a natural appeal (like clustering problems in general).

Examples: cluster mass / radius / density, cohesion or separation between clusters, etc. These concepts are often combined, for example, the ratio of separation to cohesion should be large if clustering was successful.

The way clustering is measured is informed by the type of clustering algorithms used. For example, measuring quality of a *complete* [clustering algorithm](http://en.wikipedia.org/wiki/Cluster_analysis "Cluster analysis") (in which all points are put into clusters) can be very different from measuring quality of a threshold-based fuzzy clustering algorithm (in which some point might be left un-clustered as 'noise').

---

The silhouette coefficient is one such measure. It works as follows:

For each point p, first find the average distance between p and all other points in the same cluster (this is a measure of cohesion, call it *A*). Then find the average distance between p and all points in the nearest cluster (this is a measure of separation from the closest other cluster, call it *B*). The silhouette coefficient for p is the difference between *B* and *A* divided by the greater of the two (*max(A,B)*).

We evaluate the cluster coefficient of each point and from this we can obtain the 'overall' average cluster coefficient.

Intuitively, we are trying to measure the space between clusters. If cluster cohesion is good (*A* is small) and cluster separation is good (*B* is large), the numerator will be large, etc.

I've constructed an example here to demonstrate this graphically.

![Clustering coefficient](http://i.stack.imgur.com/iAWnF.png) ![Results of clustering for nclusters = 2:5](http://i.stack.imgur.com/wqQvq.png)

In these plots the same data is plotted five times; the colors indicate the clusters created by [k-means clustering](http://en.wikipedia.org/wiki/K-means_clustering "K-means clustering"), with k = 1,2,3,4,5. That is, I've forced a clustering algorithm to divide the data into 2 clusters, then 3, and so on, and colored the graph accordingly.

The silhouette plot shows the that the silhouette coefficient was highest when k = 3, suggesting that's the optimal number of clusters. In this example we are lucky to be able to visualize the data and we might agree that indeed, three clusters best captures the segmentation of this data set.

If we were unable to visualize the data, perhaps because of higher dimensionality, a silhouette plot would still give us a suggestion. However, I hope my somewhat long-winded answer here also makes the point that this "suggestion" could be very insufficient or just plain wrong in certain scenarios.
