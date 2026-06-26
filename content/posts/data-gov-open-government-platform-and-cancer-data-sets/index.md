---
subtitle: "Reposted: originally published on my Pafnuty blog (2008–2014)"
title: "Data.gov, Open Government Platform, and Cancer data sets"
date: 2013-09-02
author: "Aman Ahuja"
series:
  - pafnuty-blog
tags:
  - data
  - ghana
  - india
  - open data
  - python
categories:
  - reflections
layout: single
draft: false
---

*Originally published on my old blog, [Pafnuty blog](/posts/data-gov-open-government-platform-and-cancer-data-sets/). Reposted here as an effort to [consolidate writing](/posts/consolidating-my-writing/) into one place. The original publication date was: September 2, 2013.*

---

After attending a lecture at University of San Francisco by Jonathan Reichental (@Reichental) on the use of open data in the US public sector, I started poking around the data sets available at [Data.gov](http://Data.gov).

Data.gov is pretty impressive. The site was established in 2009 by [Vivek Kundra](http://en.wikipedia.org/wiki/Vivek_Kundra "Vivek Kundra"), the first person with the title "Federal CIO" of the United States, appointed by Barack Obama.  It is rapidly adding data sets; sixty-four thousand [data sets have been added](http://www.data.gov/metric/federalagency/dataset-published-per-month) just in the last year.

Interestingly, there is an open-source version of data.gov itself, called the [open government platform](http://www.opengovplatform.org/). It is built on Drupal and available on [github](https://github.com/opengovplatform/). The initiative is spear-headed by the US and the Indian governments, to help promote transparency and citizen engagement by making data widely and easily available. Awesome.

The Indian version is: [data.gov.in](http://data.gov.in/). There is also a [Canadian version](http://data.gc.ca/), a [Ghanaian version](http://data.gov.gh/), and many other countries are following suit.

I started mucking around and produced a plot of the Age-adjusted [Urinary Bladder cancer](http://www.everydayhealth.com/bladder-cancer/bladder-cancer-basics.aspx "Bladder Cancer") occurrence, by state.

![dataGOV_UrinaryBladderCancer_ByState](datagov_urinarybladdercancer_bystate1.png)

Observations:
- The data was easy to find. I downloaded it without declaring who I am or why I'm downloading the data, and I didn't have to wait for any approval.
- The data was well-formatted and trivially easy to digest using python pandas. Ipython notebook and data source available below.
- Data from: [http://wonder.cdc.gov/cancer.html](http://wonder.cdc.gov/cancer.html)

If you're interested in this data, you should also check out <http://statecancerprofiles.cancer.gov/>. I was able to retrieve this interesting map from there:

![statecancerprofiles_Bladder_USmap](statecancerprofiles_bladder_usmap.png)
