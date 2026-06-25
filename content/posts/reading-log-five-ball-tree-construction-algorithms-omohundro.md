---
subtitle: "Reposted: originally published on my Pafnuty blog (2008–2014)"
title: "Reading Log: \"Five Ball-Tree Construction Algorithms\", Omohundro"
date: 2013-06-19
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

*Originally published on my old blog, [Pafnuty blog](https://pafnuty.wordpress.com/2013/06/19/reading-log-five-ball-tree-construction-algorithms-omohundro/). Reposted here as an effort to [consolidate writing](/posts/consolidating-my-writing/) into one place. The original publication date was: June 19, 2013.*

---

"Five Balltree Construction Algorithms." (1989).
Stephen M. Omohundro

I browsed this paper after reading several blog posts and articles about [balltree](http://en.wikipedia.org/wiki/Ball_tree "Wikipedia: Ball Tree")-related algorithms, including:


1. "Damn Cool Algorithms, Part 1: BK-Trees." Nick Johnson. <http://blog.notdot.net/2007/4/Damn-Cool-Algorithms-Part-1-BK-Trees>

2. "VP trees: A data structure for finding stuff fast." Stephen Hanov. <http://stevehanov.ca/blog/index.php?id=130>



These and Omohundro's paper are worthwhile reading. Even if one is not directly able to apply these data structures, they still have benefit in the read. When I was reading them, I was reminded that:


- A concept that is intuitively straightforward can often be impractical or impossible to implement for a particular application.

- [Data structures](http://en.wikipedia.org/wiki/Data_structure "Data structure") can be designed and built specifically to optimize an operation (that is required by your algorithm)

- That [curse of dimensionality](http://en.wikipedia.org/wiki/Curse_of_dimensionality "Curse of dimensionality"), god damnit.

- There are many really cool and clever algorithms that you'll never be able to apply in your domain.



Balltree and related structures are hierarchical, tree-like representation. They place data points in the tree and provide instructions for traversal of the tree in such a way as to optimize some expected future operation. The clearest application is [nearest neighbor search](http://en.wikipedia.org/wiki/Nearest_neighbor_search "Nearest neighbor search"). They also give you an excuse to sensibly use terms like "hyper-spheres" and "leaf balls".

Construction times for these structures don't tend to scale well. Think O (N^3). A lot of effort is put into improving and optimizing construction, but direct application of these structures to large data sets is not tractable.

Relatedly: kd balls, Burkhard-Keller (BK) trees, and VP-trees. And others.
