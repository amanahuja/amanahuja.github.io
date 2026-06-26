---
subtitle: "Reposted: originally published on my Pafnuty blog (2008–2014)"
title: "Aggregates, Crystals and a simple algorithm to explore."
date: 2009-02-18
author: "Aman Ahuja"
series:
  - pafnuty-blog
tags:
  - aggregation
  - chaos
  - crystals
  - diffusion
  - dla
  - emergence
  - nature
  - simple
categories:
  - experiments
layout: single
draft: false
---

*Originally published on my old blog, [Pafnuty blog](/posts/aggregates-and-crystals/). Reposted here as an effort to [consolidate writing](/posts/consolidating-my-writing/) into one place. The original publication date was: February 18, 2009.*

---

A particle randomly floats through space eventually encountering a stationary 'seed'. The two stick together and form a cluster that grows and grows as more randomly floating particles encounter it and attach themselves.  This is a simple algorithm, and it is actually quite provocative.

{{< figure src="dla21.png" alt="Simple Fractal created using the described method." caption="Simple Fractal created using the described method." >}}

Known as diffusion limited aggregation (DLA), the process produces clusters like the ones in the above images. The clusters are called Brownian Trees and are fractal with a dimensionality of about 1.7.  They were the inspiration for all sorts of computer art in and since the 90s (see [Paul Bourke's work and images](http://local.wasp.uwa.edu.au/~pbourke/fractals/dla3d/ "Paul Bourke") -- if you try his software, let me know what you think of it).

{{< figure src="coral.png" alt="Coral Growth Pattern" caption="Coral Growth Pattern" >}}

DLA simulates several types of natural processes. Paul Bourke notes that zinc particles in an electrolytic solution wander around aimlessly before attaching themselves to electrodes. More familiar might be the path taken by electricity in a lightning bolt (using a plane instead of a point as the attractor) or in those plasma globes you can find at stores like Spencer's Gifts (using a spherical attractor).

Aggregation of the soot produced in the combustion of motor fuels reduces the performance of the engine, and the network structures they produce are DLA-based. ...and so on -- the world is full of DLA.

A seed is often carefully chosen to reduce randomness in the controlled growth of crystals, but a seed is also that piece of dirt on your window on a cold cold day that serves as an attractor for the frost that begins to form. And this frost can be so very beautiful.
> When I came down to breakfast, two of the windows were almost opaque and the others were etched with graceful, fernlike sprays of ice which looked rather like the impressions left in rocks by some of the antediluvian plants, and they were almost as beautiful as anything which the living can achieve. Nothing else which has never lived looks so much as though it were actually informed with life.
> -- Joseph Wood Krutch, "The Colloid and the Crystal."


Diffusion Limited Aggregation is a very simple algorithm to describe and to visualize.  As a simulation for countless natural phenomenon, it has applications in science and in engineering. It is beautiful to look at, and with small variations yields even more interesting results. It is algorithms like these that inspire us to explore of the world of algorithms.
