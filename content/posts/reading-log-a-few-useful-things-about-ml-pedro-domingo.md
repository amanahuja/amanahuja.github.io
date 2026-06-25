---
title: "Reading log: \"A few useful things about ML\", Pedro Domingo"
date: 2012-11-23
author: "Aman Ahuja"
series:
  - pafnuty-blog
tags:
  - algorithm
  - computer science
  - cross-validation (statistics)
  - data
  - kaggle
  - machine learning
  - overfitting
  - reading log
  - training set
categories:
  - reading-log
layout: single
draft: false
---

*Originally published on my old blog, [Pafnuty blog](https://pafnuty.wordpress.com/2012/11/23/reading-log-a-few-useful-things-about-ml-pedro-domingo/). Reposted here as an effort to [consolidate writing](/posts/consolidating-my-writing/) into one place. The original publication date was: November 23, 2012.*

---

"A few useful things to know about machine learning." CACM, 55(10) 2012
Pedro Domingo, Department of [Computer Science and Engineering](http://en.wikipedia.org/wiki/Computer_science "Computer science"), [University of Washington](http://www.washington.edu/ "University of Washington")
Published October 2012.

Read this paper in November 2012 (backdated post).
Compare this paper to many similar ones with general advice or observations on [Machine Learning](http://en.wikipedia.org/wiki/Machine_learning "Machine learning"), such as the one by Andrew Ng.
These are the useful things Pedro chooses to highlight in this paper.


- Selection of an ML algorithm is simpler if you understand the three components: representation, evaluation (scoring function), optimization.

- Generalization is the goal. Use [cross validation](http://en.wikipedia.org/wiki/Cross-validation_%28statistics%29 "Cross-validation (statistics)"), optimize for the test set, not training data.

- Data and algorithms must be combined with domain knowledge and experience for good results. This is a good thing. Anti-[Kaggle](http://www.kaggle.com/ "Kaggle").

- Understand bias vs. variance in [overfitting](http://en.wikipedia.org/wiki/Overfitting "Overfitting"). Use techniques like regularization to combat them.

- Curse of dimensionality

- Theoretical guarantees in ML algorithms are not a criterion for practical decisions.

- Feature engineering is the most important contributor to success/failure of ML.

- More data > algorithmic sophistication, but adds scalability issues. Try the simplest learners first.

- Use ensemble methods. More models are better.

- "... Simpler hypotheses should be preferred because simplicity is a virtue in its own right, not because of a hypothetical connection with accuracy. This is probably what Occam meant in the first place."

- Just because something has a representation doesn't mean it can be learned.

- [Correlation is not Causation](http://en.wikipedia.org/wiki/Correlation_does_not_imply_causation "Correlation does not imply causation").



**Links:**
<http://www.cs.washington.edu/homes/pedrod/class>
<http://www.videolectures.net>
