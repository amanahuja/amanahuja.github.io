---
title: "Reading Log: \"Overlapping Experiment Infrastructure at Google\", D. Tang"
date: 2013-06-11
author: "Aman Ahuja"
series:
  - pafnuty-blog
tags:
  - ab testing
  - data
  - google
  - lean analytics
  - multi-arm bandit
  - reading log
  - testing
  - testing infrastructure
categories:
  - CHANGETHISCATEGORY
layout: single
draft: false
---

*Originally published on my old blog, [Pafnuty blog](https://pafnuty.wordpress.com/2013/06/11/reading-log-overlapping-experiment-infrastructure-at-google-d-tang/). Reposted here as an effort to [consolidate writing](/posts/consolidating-my-writing/) into one place. The original publication date was: June 11, 2013.*

---

"Overlapping Experiment Infrastructure at Google" D. Tang
Published KDD Proceedings 2010
<http://dl.acm.org/citation.cfm?id=1835810>

This paper describes the thought process and concepts behind the extensive testing philosophy and infrastructure at Google.

Reading log: This is a very useful paper I read a while ago and dug up again for a client in June. The concepts I learned here seem to emerge intermittently when meeting with clients.

I think this should be required reading for anyone getting started with overlapping testing infrastructures (those that manage multiple tests at the same time). Lean Analytics!

Key take-aways include:


- the concept of domains, subsets and layers to partition parameters and design infrastructure

- binary push vs data push; separating testing parameters from program code.

- Canary experiments and defining expected range of monitored metrics



My concerns (i.e. interests or applications in mind) with re-reading this paper for my client were:


- Applying overlapping infrastructure to A/B testing vs. Multi-Arm Bandit testing,

- The particulars of having a shared control group

- Using such an infrastructure to test and select machine learning algorithm hyperparameters
