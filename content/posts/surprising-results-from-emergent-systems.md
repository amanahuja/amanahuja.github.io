---
title: "Surprising Results from Emergent Systems"
date: 2008-12-15
author: "Aman Ahuja"
series:
  - pafnuty-blog
tags:
  - emergence
  - evolution
  - fgpa
  - genetic algorithm
categories:
  - observations
layout: single
draft: false
---

*Originally published on my old blog, [Pafnuty blog](https://pafnuty.wordpress.com/2008/12/15/surprising-results-from-emergent-systems/). Reposted here as an effort to [consolidate writing](/posts/consolidating-my-writing/) into one place. The original publication date was: December 15, 2008.*

---

One of my favorite examples of a surprising result from an emergent system is an experiment that utilized a genetic algorithm to solve a sorting problem on a FPGA chip. The hope was to arrive at the best (minimal) solution to the sorting problem faster and with more confidence than a human could. The actual result was that the genetic algorithm found a solution that was better than what theory said was even possible!

How did that happen? It turned out that the models humans used and programmed into computer simulations were not in fact complete. They are based in theoretical simplifications that do not fully describe the physical world, in which nature is not limited to the '1's and '0's of electrical theory, in which nature could take advantage of the minute electromagnetic coupling of electrical components packed tightly into a silicon ship, in which higher order effects not considered by models could be utilized to solve the problem.

By physically wiring an infinitely reprogrammable Xilinx XC6216 FPGA chip to allow the genetic algorithm to use a physical board -- instead of a computer simulation of the board -- the algorithm arrived at a solution that used fewer steps and fewer gates than the best solution previously offered by theory.
> "What is downright scary is this: the FPGA only used 32 of its 100 available logic gates to achieve its task, and when scientists attempted to back-engineer the algorithm of the circuit, they found that some of the working gates were not even connected to the rest through normal wiring. Yet these gates were still crucial to the functionality of the circuit. This means, according to Thompson, that either electromagnetic coupling or the radio waves between components made them affect each other in ways which the scientists could not discern ([Taubes 1997](http://www.sciencemag.org/cgi/content/summary/277/5334/1931?ck=nck "Reference"))."


The structure of the genetic solution discarded the need for models or theory and was allowed to experiment with actual physical properties.  All that was needed were rules that allowed better solutions to survive in each generation until the optimal result was achieved.

Read more: [http://www.cs.bgu.ac.il/~jasminme/ECAL071/Exe3/koza\_evolving.pdf [PDF]](http://www.cs.bgu.ac.il/~jasminme/ECAL071/Exe3/koza_evolving.pdf)

Not all problems are suitable for such an evolutionary approach; it is often impractical even when it does work. But what appeals to me is the idea that we can  do what nature does. We can use simple rules to find an amazingly efficient solutions to a problem, without understanding how that solution really works. Not far in the future, the world might be full of algorithmic solutions as diverse and amazing to a computer scientist as the animals of the world are to a zoologist.
