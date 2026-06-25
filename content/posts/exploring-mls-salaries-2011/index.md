---
title: "Exploring MLS Salaries 2011"
date: 2012-04-20
author: "Aman Ahuja"
series:
  - pafnuty-blog
tags:
  - data
  - david beckham
  - football
  - mls
  - salaries
  - soccer
  - sport salaries
  - thierry henry
categories:
  - observations
layout: single
draft: false
---

*Originally published on my old blog, [Pafnuty blog](https://pafnuty.wordpress.com/2012/04/20/exploring-mls-salaries-2011/). Reposted here as an effort to [consolidate writing](/posts/consolidating-my-writing/) into one place. The original publication date was: April 20, 2012.*

---

**[I wrote this in April 2012, but never cleaned it up and posted it. Here it is, finally, back-posted.]**

My friend Arian and I were conversing over Google Talk about footballer (read: soccer player) salaries, and found a source for the 2011 salaries and positions of each player in the US soccer league, MLS. I loaded this data into Pandas, and as we chatted, we poked around and had some fun with the data.

Some of this might be interesting to others as well, so I cleaned it all up a little to post here on my blog. Some of the highlights are directly pasted below, and I've also included the PDF and other files below, in case anyone is interested in poking around some more.

Technical setup:


- We were using my [iPython notebook server](http://ipython.org/ipython-doc/dev/interactive/htmlnotebook.html "iPy Notebook Server") to share and discuss "live".

- Analysis / visualization with Python: [matplotlib](http://matplotlib.sourceforge.net/ "Matplotlib") and [pandas](http://pandas.sourceforge.net/ "Pandas").




### A quick look at salaries of soccer player in the US Major League Soccer 2011.


{{< figure src="playercountandsalarybyposition.png" alt="MLSPlayerCountandSalaryByPosition" caption="Bar graph of MLS Player count and average salary, by position." >}}

Our source data consisted of 525 MLS players. The above plot shows the distribution of these players across field positions. Also plotted there is the average salary for each field position. Forward / attacking players apparently earn the most money, however that observation may be skewed by a small number of high-profile forwards that earn huge amounts of money.

|
 Club |
 Last Name |
 First Name |
 Position |
 Base Salary |
 Compensation |




|
 LA |
 Beckham |
 David |
 M |
 $5,500,000 |
 $6,500,000 |


|
 NY |
 Henry |
 Thierry |
 F |
 $5,000,000 |
 $5,600,000 |


|
 NY |
 Marquez |
 Rafael |
 D |
 $4,600,000 |
 $4,600,000 |


|
 LA |
 Keane |
 Robbie |
 F |
 $2,917,241 |
 $3,417,243 |


|
 LA |
 Donovan |
 Landon |
 F |
 $2,300,000 |
 $2,300,000 |


This table shows the top 5 paid players in MLS 2011. They are not all forwards. Out of the top 20 compensated players, there are 9 forwards, 9 mid-fielders, 1 defender and 1 keeper.

These players clearly earn huge compensation, but this is not typical of MLS players. Half of the players earn a salary less than $80,000 (and the [mode](http://en.wikipedia.org/wiki/Mode_(statistics) "Definition of Mode") of the distribution is $42k). The *log-scale* boxplot below helps us visualize this distribution of wealth.

{{< figure src="salarybyposition_boxplot.png" alt="SalaryByPosition_boxplot" caption="Log-scale boxplot of MLS player salary by position" >}}

With Occupy Wall Street in full swing at the time of our conversation, it was natural to draw a connection between the distribution of wealth in MLS and "the 99%". We determined that the top-earning MLS player makes as much money ($6,500,000) as the bottom-earning 166 players combined!

After a few iterations of Arian and I asking: "How many bottom-earning players does it take to earn *as much as*N top-earning players?", we created this plot of "as much as":

{{< figure src="mlssalaryasmuchas.png" alt="MLSSalaryAsMuchAs" caption="Graph answering the question: &quot;Y bottom-earning MLS players make as much money as X top-earning MLS players&quot;" >}}

(Also interesting: the top 0.09% of players make 50% of the total MLS Compensation, $42,539,737.)

Not all clubs pay the same to their players. The following a plot of Average Salary, by MLS Club team. LA Galaxy and the NY Red Bulls pay the highest average salaries, with Toronto's football club as a distant third.

{{< figure src="salarybyclub_barchart.png" alt="SalaryByClub_barchart" caption="Bar plot of average salary, by MLS Club team" >}}

### Other ideas

There's more to explore with the existing data set, but I would be interested in comparing MLS salaries with other soccer leagues, such as the English Premier League. The change in footballers' salaries over time would be great to see, too, especially if one could see how this change over time compares to other sport's salaries. Are MLS players making any progress at all towards catching up to NBA or NFL salaries?  If anyone knows where to get more useful data along these lines, or if this analysis already exists, please do let me know.

### Downloads:

- [MLS\_Salaries [PDF]](http://pafnuty.wordpress.com/2012/04/20/exploring-mls-salaries-2011/mls_salaries_ipy03/)
- [MLS\_Salaries [ZIP with PDF, IPYNB, and data in CSV]](https://dl.dropbox.com/u/30953532/MLS-Salaries.zip)
- Data source: <http://www.mlsplayers.org/salary_info.html>
