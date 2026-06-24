---
title: "R2D3 and other letters and numbers"
date: 2012-12-08
author: "Aman Ahuja"
series:
  - pafnuty-blog
tags:
  - coding
  - d3
  - data
  - document object model
  - ggplot
  - ggplot2
  - hadley wickham
  - mike hemesath
  - open source
  - open source software
  - python
  - r
  - r2d3
  - raphael
  - rstats
categories:
  - CHANGETHISCATEGORY
layout: single
draft: false
---

*Originally published on [pafnuty.wordpress.com](https://pafnuty.wordpress.com/2012/12/08/r2d3-and-other-letters-and-numbers/) in December 2012. Reposted here as part of pulling old writing into one place.*

---

Check out the alphabet soup of data web visualizations I am swimming in today.

- [R](http://www.r-project.org) is statistical and computational software.
- [d3.js](http://d3js.org/) is a JavaScript library for building beautiful visualizations on the web. It uses scalable vector graphics (SVGs) directly from data through the [document object model (DOM)](http://en.wikipedia.org/wiki/Document_Object_Model "Document Object Model").
- [ggplot2](http://ggplot2.org/) is a graphing library for R, developed by [Hadley Wickham](http://had.co.nz/ "Hadley Wickham").

- [Raphaël.js](http://raphaeljs.com/) -- This is a JavaScript library for working with vector graphics. (It's different: Raphaël.js creates and manipulates vector graphical objects that are also DOM objects. D3.js is primarily designed to tie data directly to DOM objects.  There is some overlap, but they're different.)

The first three are pretty powerful and, if they are not already, are fast becoming critical parts of the data toolkit. The last is a promising newcomer, worth keeping an eye on.
So far so good. If you're a data nerd, you probably already know all this. Stick with me.
It turns out that all these libraries, doing slightly different but related things, and doing them well, would work very well together. They're not tightly integrated (yet) but there are several efforts to make it so.
Hadley Wickam, creator of the R package ggplot2, is a fan of d3.js and [has suggested](http://www.youtube.com/watch?v=hsFMcen0okI) that the next version of ggplot2 will probably be redone on the web, likely using d3. He's also working on [a new R library](https://github.com/hadley/r2d3) that more immediately allows them to work well together. This is  great news.
He's calling it **R2D3** (-- named, supposedly, more at the insistence of friends that are [Star Wars](http://www.netflix.com/Movie/Star-Wars-Episode-IV-A-New-Hope/60010932 "Star Wars") geeks than due to his own fandom).

![r2d3](r2d3.jpg)

(Confusingly, there were some unfounded rumors that Hadley's next version of ggplot would be called **R2D3.**)
There are also a few projects to get Raphaël.js to work well with d3.js. One of them is called '[d34raphael](http://webmonarch.github.com/d34raphael/)'. Another, a bit more ambitious, is [a custom build of d3 powered by Raphael](https://github.com/mhemesath/r2d3/). Awesome! Guess what it's called? **R2D3.**
It's not that uncommon for two open source libraries to have the same name, but these libraries both address the needs of a pretty niche audience. They both work with d3.js, but one extends "upstream" towards the data and the other extends "downstream" toward the graphics. It's more than conceivable for someone to want to use all them at the same time: R, R2D3, D3, R2D3, and Raphael.
Apparently the the two authors, Mike Hemesath and Hadley Wickham didn't know about each other's projects when they named their own. If both projects are adopted widely, it will be interesting to see if either of them eventually decides to change names.
