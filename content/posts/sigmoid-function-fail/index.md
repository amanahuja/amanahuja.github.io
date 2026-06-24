---
title: "sigmoid function fail"
date: 2011-04-01
author: "Aman Ahuja"
series:
  - pafnuty-blog
tags:
  - backpropagation
  - coding
  - fail
  - matplotlib
  - neural network
  - neural networks
  - python
  - sigmoid
categories:
  - CHANGETHISCATEGORY
layout: single
draft: false
---

*Originally published on my old blog, [Pafnuty blog](https://pafnuty.wordpress.com/2011/04/01/sigmoid-function-fail/). Reposted here as an effort to [consolidate writing](/posts/consolidating-my-writing/) into one place. The original publication date was: April 1, 2011.*

---

Plot the sigmoid function.

$latex sig(u)=\frac{1}{1+e^{-u}}$

{{< figure src="sigmoid_fail.png" alt="sigmoid_fail" caption="Does this look sigmoidal to you?" link="sigmoid_fail.png" >}}
A result that confused me until [Thanks, Sasha] I noticed the tick values on my x-axis, which matplotlib selected unintelligently.  If we simply correct the plot domain.
`xs = [0.01*x for x in range(-1000,1000)]`
[![](win-sigmoid.png?w=300 "win-sigmoid")](win-sigmoid.png)

I would like to know more about how different plotting packages, such as matplotlib and ggplot2 in R, select default values for xrange and yrange.
