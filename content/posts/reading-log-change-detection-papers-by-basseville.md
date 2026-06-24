---
title: "Reading log: Change Detection papers by Basseville"
date: 2013-02-05
author: "Aman Ahuja"
series:
  - pafnuty-blog
tags:
  - algorithm
  - basseville
  - change detection
  - cusum
  - data
  - reading log
  - residuals
  - signals analysis
  - stopping rule
  - time series
categories:
  - CHANGETHISCATEGORY
layout: single
draft: false
---

*Originally published on my old blog, [Pafnuty blog](https://pafnuty.wordpress.com/2013/02/05/reading-log-change-detection-papers-by-basseville/). Reposted here as an effort to [consolidate writing](/posts/consolidating-my-writing/) into one place. The original publication date was: February 5, 2013.*

---

I've been increasingly interested in this subject -- given a stream of data, a time-series such as, perhaps, a periodic measurement from a sensor, how do we define and identify anomalous values quickly and efficiently?

[**Update**: Check out this [August 11th post by Ben Lorica](http://practicalquant.blogspot.com/2013/08/anomalies-and-patterns-in-machine-data.html), focusing on IT Ops tools in this space.]

Michèle Basseville has written [several papers](http://scholar.google.com/citations?user=CAMaPqYAAAAJ&hl=en&oi=sra "Google Scholar: Basseville") on the subject which I found very helpful. These two were among the first I read, in February, while researching for a new client.


1. "Statistical methods for change detection." (2002).

2. "Detecting Changes in Signals and Systems: A Survey" Automation, Vol. 2,t, No. 3, pp. 309-326, 1988



His approach involves two major steps. First, from the signal, generate "residuals", which are defined as having three properties: residuals should be close to zero under ambient (normal) conditions, insensitive to noise, and sensitive to fault (anomaly). Second, evaluate the residuals using one or more previously design decision rules (stop conditions).

Bassevile defines multiple criteria for designing detection algorithms, which I found very useful. For each application, different criteria may take priority. They are often opposing or mutually exclusive to implement. An obvious example is balancing false positives and false negatives. Another tradeoff is the mean time between false alarms and the delay in fault detection. He draws the distinction between off-line and on-line change detection, and design differences in algorithms in each case.

Some of the ingredients he uses and discusses include:


- likelihood ratio and cumalative sum tests.

- the Page-Hinkley Stopping Rule

- using local approaches and moving windows to reduce computation costs.

- spectral properties of the incoming signal

- Cumulative Sum Control Chart (CUSUM) by ES Page -- <http://en.wikipedia.org/wiki/Cusum>



If one is interested in this subject, I imagine Basseville is a familiar name already. Following his works and the paper that cite them is a deep dive straight into the subject. I find it all fascinating and hope to get many chances to utilize these techniques in future projects.
