---
title: "Scalable Ad-hoc Analysis of Wireless Telecommunication Transactions"
subtitle: "Building a data infrastructure to unlock insights from rapidly growing transaction volumes"
excerpt: "The Data Guild partnered with BandwidthX to design and implement a scalable analytics platform for exploratory analysis of wireless telecommunication data, providing a foundation for a new business case."
date: 2014-12-31
author: Aman Ahuja
tags:
    - big-data
series:
    - "The Data Guild"
categories: 
    - "Projects"
layout: single-sidebar
draft: false
---

### Overview

The Data Guild partnered with BandwidthX to design and implement a scalable analytics infrastructure for ad-hoc exploratory analysis of wireless telecommunication transaction data. The engagement provided a foundation for both the technical approach and the business case for BandwidthX's network optimization services.

BandwidthX was managing rapidly growing volumes of telecommunication transaction data from pilot programs—reaching over 1 billion records within weeks. Their existing analytics setup (a dedicated workstation running Excel and Tableau against a MySQL database) was hitting performance limits on complex queries and large dataset operations. They needed a way to run exploratory analyses quickly without disrupting production systems, while answering critical business questions about cellular savings and usage patterns.

Over a five-week engagement, The Data Guild built an experimental analytics environment on Rackspace using Hadoop, Spark, and PySpark. This allowed data scientists to perform ad-hoc and interactive analysis on datasets much larger than a single machine could handle. Our team: 

- **Designed the architecture** to be minimally disruptive to existing systems while providing significant analytical capability
- **Set up the Spark cluster** and ETL pipeline to move data from MySQL to HDFS using Apache Sqoop
- **Conducted exploratory analysis** to answer key business questions about usage patterns, savings, and pilot outcomes
- **Identified and resolved data quality issues**, including a methodology for detecting and handling outliers that was generalizable to future analyses

This was a project by The Data Guild, with team members 
- <b>Aman Ahuja</b> - Led analytical work, identifying usage patterns and cost savings in the pilot and developing outlier detection methodology
- <a href="https://www.linkedin.com/in/russelljurney/" target="new">Russell Jurney</a> - Designed and implemented the data infrastructure and provided architecture recommendations
- <a href="https://www.linkedin.com/in/gutelius" target="new">David Gutelius</a> - Business ownership and strategic direction

### About BandwidthX

BandwidthX provides cloud services that optimize mobile data networks by automatically trading unused data capacity between network operators and other actors that lack capacity. The company helps Wi-Fi providers and ISPs monetize unused capacity while helping mobile operators reduce costs.

Note: BandwidthX was acquired in 2023 by Aglocell. 
