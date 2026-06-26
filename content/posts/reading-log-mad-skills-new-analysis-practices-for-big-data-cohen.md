---
subtitle: "Reposted: originally published on my Pafnuty blog (2008–2014)"
title: "Reading Log: \"MAD Skills: New Analysis Practices for Big Data\", Cohen"
date: 2013-03-15
author: "Aman Ahuja"
series:
  - pafnuty-blog
tags:
  - algorithm
  - data
  - reading log
categories:
  - reading-log
layout: single
draft: false
---

*Originally published on my old blog, [Pafnuty blog](/posts/reading-log-mad-skills-new-analysis-practices-for-big-data-cohen/). Reposted here as an effort to [consolidate writing](/posts/consolidating-my-writing/) into one place. The original publication date was: March 15, 2013.*

---

"MAD Skills: New Analysis Practices for Big Data"
Cohen, et al.
Proceedings of the VLDB Endowment, Volume 2 Issue 2, August 2009

Reading log: I'm not sure when I read this paper, so the back-dating is pretty much arbitrary.

Abstract from the paper:
> As massive data acquisition and storage becomes increasingly affordable, a wide variety of enterprises are employing statisticians to engage in sophisticated data analysis. In this paper we highlight the emerging practice of Magnetic, Agile, Deep (MAD) data analysis as a radical departure from traditional Enterprise Data Warehouses and [Business Intelligence](http://en.wikipedia.org/wiki/Business_intelligence "Business intelligence"). We present our design philosophy, techniques and experience providing MAD analytics for one of the world's largest advertising networks at Fox Audience Network, using the [Greenplum](http://www.greenplum.com "Greenplum Database") parallel database system. We describe database design methodologies that support the agile working style of analysts in these settings. We present dataparallel algorithms for sophisticated statistical techniques, with a focus on*density* methods. Finally, we reflect on database system features that enable agile design and flexible algorithm development using both SQL and [MapReduce](http://en.wikipedia.org/wiki/MapReduce "MapReduce") interfaces over a variety of storage mechanisms.


Notes:

I was concerned that this paper would turn into a white-paper or technical sales piece on joint hardware-software product offerings by Greenplum. Presents a Greenplum case study: Greenplum database for their client Fox Networks.


- MAD is Magnetic, Agile, Deep data analysis

- The authors define the MAD acronym as a re-imagination of the data warehouse concept such that:

  - Magnetic: encourages (attracts) new data sources, has reduced sensitivity to cleanliness of data sources

  - Agile: logical and physical contents of the database can evolve and adapt rapidly

  - Deep: Avoid BI rollups and sampling to serve more demanding statistical analyses.

- Presented as an alternative to "traditional Enterprise Data Warehouses and Business Intelligence."

- Emphasis is on moving data to a data warehouse rapidly, and using a staged approach to clean and integrate the new data.



Provides background / definitions: [OLAP](http://en.wikipedia.org/wiki/Online_analytical_processing "Online analytical processing"), data cubes, common statistical systems, parallel processing paradigms, some statistical concepts, tf-idf analysis, Ordinary least squares curve fitting, etc.  Then basically just states that all this possible in a fast, dynamic, fashion using Greenplum technology.

I skimmed rather than read this paper. It felt like it was at least a review of some important concepts, but actually I'm not sure I actually got anything out of this read.
