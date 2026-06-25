---
subtitle: "Reposted: originally published on my Pafnuty blog (2008–2014)"
title: "Link: 'Hello World' genetic algorithm"
date: 2009-08-13
author: "Aman Ahuja"
series:
  - pafnuty-blog
tags:
  - emergence
  - fitness function
  - genetic algorithm
  - hello world
categories:
  - experiments
layout: single
draft: false
---

*Originally published on my old blog, [Pafnuty blog](https://pafnuty.wordpress.com/2009/08/13/hello-world-genetic-algorithm/). Reposted here as an effort to [consolidate writing](/posts/consolidating-my-writing/) into one place. The original publication date was: August 13, 2009.*

---

I enjoyed a post today at [Hidden Clause](http://cvalcarcel.wordpress.com/# "Hidden Clause blog") talking about an attempt to generate the string 'hello, world!' using a genetic algorithm.
> In the first chapter of the documentation for the Watchmaker Framework Daniel W. Dyer presents [an interesting genetic algorithm example: what if we wanted to evolve the string “HELLO WORLD”?](http://cvalcarcel.wordpress.com/2009/08/11/jgap-a-second-example-and-observations/trackback/) ... My first thought: implementing this in JGAP shouldn’t be that hard.


The setup reminds me of the game 'Mastermind' -- we're dealing with a fixed-length string and scoring based on how many of the correct characters occur in the string and if they are in the right position. You combine some better strings and sometimes mutate them to generate new strings, and repeat that process until, hopefully, you arrive at the target string, 'hello, world!'.

Did it work? Well, almost. The first result, "'!ello, or!d!",  was reached after 1 million iterations on a population size of a thousand -- and, it used a limited alphabet containing only the letters and punctuation in the target string (and not, for example, 'z').

The reason the solution was not reached, the post's author notes, is that the algorithm doesn't have the breadth or the convergent ability to match the statistical odds involved. Recalling the old problem of monkeys on typewriters producing Shakespeare , the author notes how unlikely it is to produce the desired result.

Of course, we're not simply monkeying at typewriters. We're making random changes and mutations, but we're intelligently selecting the parents. Apparently, the method first tried wasn't intelligent enough to arrive at the desired solution within that number of iterations, and increasing iterations or population size, apparently, isn't going to be practical.  So we need to use a better way of selecting the parents.

We could improve the fitness function. Let's say we take the whole alphabet and the punctuation and number them (for instance: A=1... Z=26 and space and comma and exclamation could be 27, 28, and 29, respectively). Now, assign fitness based on the difference between actual and target values of each character. Is this cheating? Well, no. Our new fitness function requires no a priori knowledge of the solution and will work equally well for a different target string. This is providing our GA with a lot more information per epoch, and therefore we should see a much faster convergence.

(Aside: there are much better way of numbering the letters and punctuation to encourage faster convergence, based on the frequency the characters are used in the English language. In fact, one could develop a system that took advantage of commonly grouped letters like 'th' and 'ing', and if dealing with sentences, commonly grouped words...  Is *that* cheating? Well, we must remember that the more such information we encode, the more pre-disposed or biased our output will be. Also, the point of a using a genetic algorithm is to substitute computation time for programming complexity. In a contrived problem, it's up to us where that line lies. )

There are a number of other ways to improve the fitness function, but my instinct is that this suggestion or a similar modification would be sufficient. I hope the Hidden Clause crew reports the result of another attempt.
