---
title: "Predicting Gambling behavior (Reading log)"
date: 2009-07-21
author: "Aman Ahuja"
series:
  - pafnuty-blog
tags:
  - algorithm
  - backpropagation
  - emergence
  - neural network
  - neural networks
  - poker
  - prediction
  - publication
  - reading log
categories:
  - CHANGETHISCATEGORY
layout: single
draft: false
---

*Originally published on [pafnuty.wordpress.com](https://pafnuty.wordpress.com/2009/07/21/predicting-gambling-behavior/) in July 2009. Reposted here as part of pulling old writing into one place.*

---

"Using Neural Networks to Model the Behavior and Decisions of Gamblers, in Particular, Cyber-Gamblers." by Victor K. Y. Chan.
A system is written that utilizes a back-propagation [neural network](http://en.wikipedia.org/wiki/Neural_network) to model [Texas Holdem](http://en.wikipedia.org/wiki/Texas_hold_%27em "Texas hold 'em") gamblers' behavior, based on data collected from a cyber gambling website.
> This article describes the use of neural networks and an empirical data sample of, inter alia, the amounts of bets laid and the winnings/losses made in successive games by a number of cyber-gamblers to longitudinally model gambler's behavior and decisions as to such bet amounts and the temporal trajectory of winnings/losses. The data was collected by videoing Texas Holdem gamblers at a cyber-gambling website.

The full article is [available on Scribd.](http://www.scribd.com/doc/17472377/Using-Neural-Networks-to-Model-the-Behavior-and-Decisions-of-Gamblers-in-Particular-CyberGamblers)
[![Gambler-ANNstructure-M1](gambler-annstructure-m1.jpg?w=300 "Gambler-ANNstructure-M1")](gambler-annstructure-m1.jpg)The above diagrams shows the structure utilized for one of the two neural networks developed for the paper. This one, dubbed "M1", attempts to predict the bet amounts laid by each individual Texas Holdem gambler, based on winnings and losses in immediately preceding games, and the gambler's current account balance.

M1: the model for successive bet amounts, which longitudinally models and thus

predicts the bet amounts in the successive game laid by each individual Texas Holdem

gambler based on his/her winnings/losses in a number of immediately preceding games

and his/her current gambling account balance.

Apparently, the ANN was generally speaking pretty successful, showing a mean magnitude of relative error on the order of 10^(-2). Two things caught my eye: 1) General betting trends were very well represented by the model, but short-lived ("high-frequency", if you will) deviances in behavior were not.  The author notes that the same can be said of financial market models. 2) The same model was developed to predict six different gamblers -- and achieved a high accuracy of prediction. What does this mean?  In the words of the author Victor Chan:
> The influence of a gambler’s skills, strategies, and personality on his/her successive bet amounts is almost totally reflected by the pattern(s) of his/her winnings/losses in the several immediately preceding games and his/her gambling account balance.

Exclamation mark.
Article found on [SciAm](http://scientificamerican.com/ "Scientific American"):  ["Artificial Intelligence Predicts Gambling Behavior"](http://www.scientificamerican.com/podcast/episode.cfm?id=artificial-intelligence-predicts-ga-09-07-21 "Predicting Gambling Behavior") via [Mindhacks](http://www.mindhacks.com/blog/2009/07/ai_predicts_poker_be.html "Mindhacks").
