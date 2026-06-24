---
title: "Yann Le Cun"
date: 2009-06-13
author: "Aman Ahuja"
series:
  - pafnuty-blog
tags:
  - at&amp;t bell labs
  - backpropagation
  - genetic algorithm
  - neural network
  - neural networks
  - science and the city
  - tedtalk
  - visual processing
categories:
  - CHANGETHISCATEGORY
layout: single
draft: false
---

*Originally published on [pafnuty.wordpress.com](https://pafnuty.wordpress.com/2009/06/13/yann-lecun/) in June 2009. Reposted here as part of pulling old writing into one place.*

---

Yann Le Cun was recently featured on NYAS's [Science and the City](http://www.nyas.org/snc/podcasts.asp "Science and the City Podcasts") podcast. He spoke about visual processing using Artificial Neural Networks (ANNs) and in particular his work on the system that reads the amounts on your cheques at the ATM.  The host, Alana Range, notes that her ATM has never gotten her cheque amounts wrong. I myself no longer bother to check.
The technology behind the ATMs was developed by Le Cun and others almost 10 years ago, at AT&T Bell Labs [which, tragically, has been closed down]. The algorithm they developed [now] goes under the name LeNet, and is a multi-layer backpropagation Neural network called a Convolution Neural Network.  I will explain this terminology in my next post. [Update: [explanation now posted.](http://pafnuty.wordpress.com/2009/06/13/explanation-of-lenet-jargon/ "Explanation of LeNet jargon")]
In the object recognition demonstration, Yann Le Cun describes four output interpretations in the LeNet algorithm: 1) edges and contours, 2) motifs, 3) categories, and finally 4) objects. By narrowing down options in several steps LeNet can arrive at the final outputn (identifying the object) far more rapidly -- the demonstration on the podcast proceses 4-5 pictures each second, and can recognize five different objects.  There are also [demonstrations online](http://yann.lecun.com/exdb/lenet/index.html "LeNet-5 demonstrations") on Yann Le Cun's website.
I wondered as I listened to this podcast about the comparisons drawn between mammalian visual processing and Le Cun's algorithm. There were some very pronounced differences that suggest that our brains utilize a totally different technique, not simply a more complex version of LeNet, as was implied in the interview. These differences were:

1. LeNet utilizes supervised learning. Our learning is largely unsupervised.
2. We extrapolate, not just interpolate. So while LeNet needs tens of thousands of samples before it starts recognizing an object, babies might see a few toy planes and recognize the one in the sky. In interview, Le Cun notes that his algorithm, when used for letter recognition, needs to be trained with both printed and handwritten samples and is unable to extrapolate from one to the other.

I think there were some other differences that I do not now recall.  I got flashbacks of the TED-talk in which Handspring founder Jeff Hawkins cracked some jokes about the fundamental differences between computer and human visual processing. I'll try to post about that; it was pretty entertaining.
[Update: check out a [Matlab class for CNN implementation](http://www.mathworks.com/matlabcentral/fileexchange/24291 "Matlab class for CNN") on the Matlab file exchange, by Mihail Sirotenko.]
