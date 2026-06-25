---
title: "Patent on Music Genome Project"
date: 2012-03-16
author: "Aman Ahuja"
series:
  - pafnuty-blog
tags:
  - algorithm
  - data
  - music genome project
  - pandora radio
  - reading log
  - stanford
  - tim westergren
categories:
  - reading-log
layout: single
draft: false
---

*Originally published on my old blog, [Pafnuty blog](https://pafnuty.wordpress.com/2012/03/16/patent-on-music-genome-project/). Reposted here as an effort to [consolidate writing](/posts/consolidating-my-writing/) into one place. The original publication date was: March 16, 2012.*

---

Reading log: Patent on [Music Genome Project](http://en.wikipedia.org/wiki/Music_Genome_Project "Music Genome Project")

Patent 7,003,515 B1, February 2006.  [Tim Westergren](http://en.wikipedia.org/wiki/Tim_Westergren "Tim Westergren"), Will Glaser, Stanford.

Also: Wikipedia and various articles

I was originally interested in the techniques used by this project after a discussion and project proposal in 2008. I read the patent then and these ideas have reared their head on several occasions since then, most recently for a client in March 2012, so I'll back-date this post to around then.

This is a well written Patent and has several interesting and applicable ideas. Worth a read.

The Music Genome project attributes various qualities to each song in the database. This allows for quantitative comparisons between songs, [Pandora](http://Pandora.com "Pandora"), etc.  Each song in the music db has 400+ musical characteristics entered manually.



Representation of a song's gene:



- Each gene is a number b/w 1-5 (half integer values allowed)

- There are n ~ 150 genes

- This is represented by a n-dimensional vector



Since entries are made by humans (albeit professionals with training) this is a non-linear scale, and must be compensated with a scaling function.




Distance between each song and each of the database song vector is calculated using distance squared metric. SBT song match method. Uses the "Focus Traits" triggering rule.




Thanks to the visibility and success of the music genome project and Pandora, this patent and related paper have probably been pretty influential.
