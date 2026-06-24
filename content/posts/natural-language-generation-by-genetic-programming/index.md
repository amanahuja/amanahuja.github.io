---
title: "Reading Log: Natural Language Generation by Genetic Programming"
date: 2010-11-12
author: "Aman Ahuja"
series:
  - pafnuty-blog
tags:
  - algorithm
  - evolution
  - evolutionary algorithm
  - genetic algorithm
  - grammar
  - linguistics
  - pablo
  - publication
  - reading log
categories:
  - CHANGETHISCATEGORY
layout: single
draft: false
---

*Originally published on [pafnuty.wordpress.com](https://pafnuty.wordpress.com/2010/11/12/natural-language-generation-by-genetic-programming/) in November 2010. Reposted here as part of pulling old writing into one place.*

---

Part of the "[Today I read](http://pafnuty.wordpress.com/category/today-i-read/)" series.
**Today I read** this paper:
"Language Generation for Conversational Agent by Evolution of Plan Trees with Genetic Programming" by Sungsoo Lim and Sung-Bae Cho. [Link.](http://www.springerlink.com/content/6pub0gk67v0frt1u/)
Anya was able to get this paper for me from NYU resources. It was a quick read. I had hoped for something that could apply to the Pablo project, but that was not to be.
The paper uses a population of (initially simple) sentences and joining operators to form new (initially more complex) sentences. They generated 20 sentences (*population size*), humans rated each on their quality (*fitness score*), and then used the fittest of these sentences to contribute to the next generation. 90 generations later, they ended up with sentences approximately 60% more fit than the first generation.
Ten human subjects were used to rate sentences (at least 10,800 of them) and I'm curious about the inevitable problems with that. For example, the authors mention that there was a statistically visible bias in ratings which wasn't compensated for.
Since Pablo is web-based and public, it would be easy to implement a rating system for this kind of algorithm. However, there are a lot of associated problems that suggest this would be a difficult idea, with questionable results.
Two more comments. The researchers wrote the joining operators and performed the work in the Korean language, which made some of the details of their work less interesting for me to read. Also, Pablo attempts to generate sentences from words, not sentences from sentences.
