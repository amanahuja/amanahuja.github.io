---
title: "Nginx - based stack"
date: 2011-06-14
author: "Aman Ahuja"
series:
  - pafnuty-blog
tags:
  - centos
  - code
  - coding
  - natural language
  - nginx
  - nltk
  - pablo
  - thesexycow
  - ubuntu
  - wordpress
categories:
  - CHANGETHISCATEGORY
layout: single
draft: false
---

*Originally published on [pafnuty.wordpress.com](https://pafnuty.wordpress.com/2011/06/14/nginx-based-stack/) in June 2011. Reposted here as part of pulling old writing into one place.*

---

I've been working on moving this blog to a different server, and simultaneously performing a migration operation on some other sites I spend time on.
In an attempt to do something new and to create an environment that provides some much needed flexibility, I'm putting some extra time and energy into selecting a server and technology stack. Here are the highlights:

- *[nginx](http://nginx.org/) instead of Apache.* Nothing against Apache, honestly; LAMP-ish stacks have been my M.O. for a long while. Nginx will, however, provide many benefits: first, exploring a completely new web server will improve my understanding of how web servers work; second, I suspect using Nginx with uWSGI will make it easier to deploy my increasing number of Python + virtualenv + (some framework) projects; third, I run several low-traffic domains on the same box, and Apache has really been struggling with that.
- *Transfer my blog [out of WP.com](http://en.support.wordpress.com/com-vs-org/ "ORG vs. COM").* I find myself wanting to do more and more with my Wordpress blog that just isn't possible with wordpress.com hosting. Having built several WP themes now, I feel nimble enough to put a custom theme together quickly. The ability to install certain currently inaccessible plugins will be very satisfying and I want to play around with writing some of my own plugins as well.
- Use the [Natural Language Toolkit](www.nltk.org) (nltk) to made Pablo more fun at [thesexycow.com](http://thesexycow.com "Pablo at The Sexy Cow") and to do some for-fun natural language analysis on my blog content.
- I will [stick with Linode](http://www.linode.com/?r=3583ef2ac6abe7c3e68604e4edc0cef2bc998cda); I've been happy with them in servers past. I'll be using Ubuntu 11.04 Natty Narwhal, which has Python 2.7.1 and other impressive version numbers that Cent-#&$@#$-OS will probably get around to implementing no sooner than 2020.

So far, I have setup the server and Nginx with FastCGI, and started working on configuring wordpress and the first iteration of this blog's theme.
