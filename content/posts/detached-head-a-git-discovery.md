---
subtitle: "Reposted: originally published on my Pafnuty blog (2008–2014)"
title: "Detached HEAD -- a git discovery"
date: 2013-04-11
author: "Aman Ahuja"
series:
  - pafnuty-blog
tags:
  - branch tracking
  - coding
  - detached head
  - git
  - revision control
  - tools
categories:
  - experiments
layout: single
draft: false
---

*Originally published on my old blog, [Pafnuty blog](https://pafnuty.wordpress.com/2013/04/11/detached-head-a-git-discovery/). Reposted here as an effort to [consolidate writing](/posts/consolidating-my-writing/) into one place. The original publication date was: April 11, 2013.*

---

Recently I found myself with a detached HEAD. In [Git](http://git-scm.com/ "Git (software)").

This was the first time I encountered such a thing. When you are working on, or checkout, commits that are not attached to any branch, you have a detached head situation. Your commits are branchless. There is a pretty easy fix to this, and the solution is pretty easy to find on SO.

Check out SO: [Why did git detach my head?](http://stackoverflow.com/questions/3965676/why-did-git-detach-my-head)

**I retraced my steps to figure out exactly how this happened.**

I created a branch (`git branch newfeature; git checkout newfeature`) and *then* cloned my repository for further work on this branch. This created an ambiguity for git: both the clone and master branch had a branch named `newfeature`. When I pulled my work from master with `git pull` , the commits were not attached to any branch.

**The symptoms**

I didn't recognize this unfamiliar situation. I did notice I couldn't find all those commits.


- They weren't visible with `git log` or `git log newfeature`.

- `git status` with newfeature checked out showed a clean working directory.



With help from [@ddunlop](https://twitter.com/ddunlop), I was finally able to view the commits with `git log <hash>`. I got the commit hash using `git log` in my cloned repo.

**This is how I resolved the problem.**


1. `git checkout <hash>`.  I checked out my most recent commit using its hash. Git informed me that I was now in a 'detached HEAD' state. After that it was easy. I googled the provocative "detached HEAD" message and did some learning.

2. `git checkout newfeature`

3. `git branch newfeature_2 6e51426cdb`

4. `git merge newfeature_2`

5. `git checkout master`

6. `git merge newfeature`



Then I just deleted the extra branches.

In the process, I also learned about "tracking" branches. Check out the useful SO: [Switch branch without detaching head](http://stackoverflow.com/questions/471300/git-switch-branch-without-detaching-head)
