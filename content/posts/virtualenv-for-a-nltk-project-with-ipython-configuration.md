---
subtitle: "Reposted: originally published on my Pafnuty blog (2008–2014)"
title: "virtualenv for a nltk project with ipython configuration"
date: 2012-02-13
author: "Aman Ahuja"
series:
  - pafnuty-blog
tags:
  - code
  - coding
  - configuration
  - ipython
  - nltk
  - python
  - pyyaml
  - sys.path
categories:
  - experiments
layout: single
draft: false
---

*Originally published on my old blog, [Pafnuty blog](/posts/virtualenv-for-a-nltk-project-with-ipython-configuration/). Reposted here as an effort to [consolidate writing](/posts/consolidating-my-writing/) into one place. The original publication date was: February 13, 2012.*

---

On a new Ubuntu machine, I needed to use NLTK. This serves as a quick reference for myself, and maybe you'll find it useful as well.

`> mkdir bananaproject
> cd bananaproject
> virtualenv ENV
> source ENV/bin/activate`

I created a new folder for my project, and a new [virtualenv](http://pypi.python.org/pypi/virtualenv "virtualenv") for it. Virtualenv comes in  damn handy for managing portability and dependencies on multiple python projects. The last command activated the virtual environment, so subsequent commands are now taking place within it.

`> pip install yolk
> yolk -l`

I installed yolk, which then tells me what I have installed and ready to use in my virtualenv. I use this to check dependencies before I can install NLTK.

`> sudo apt-get install python-numpy
> pip install pyyaml`

Numpy is a package I'm okay with having installed system-wide, not just in this virtualenv. Pyyaml on the other hand I installed just for this project.

`> mkdir ENV/src
> cd ENV/src
> wget http://nltk.googlecode.com/files/nltk-2.0.1rc1.zip
> unzip nltk-2.0.1rc1.zip
> cd nltk-2.0.1rc1
> python setup.py install`

Self-explanatory. Of course, the link to NLTK will soon be outdated; the latest can be found at <http://www.nltk.org/download>. The virtualenv was activated while I ran the install.

At this point I thought I was done, but when I started ipython and tried to `import nltk`, I got an import error. I need to tell ipython about the python executable I'm using and the changes to sys.path.

*This is only necessary because of the way I set up my virtualenv and the order in which I have installed things. A simple alternate is to to use a virtualenv with the `--no-site-packages` option, and then install ipython afresh for that project.*

This post came in handy: [http://blog.ufsoft.org/2009/1/29/ipython-and-virtualenv](c.InteractiveShellApp.exec_files = []). However, it was written in 2009, and I'm using ipython 0.12. A slight variation is necessary for ipython >= 0.11.

`> vi ~/.ipython/virtualenv.py
[ Use this, or a variation thereof: https://gist.github.com/1176035 ]
> ipython profile create`

The profile create command tells ipython to create default config files, which we can then play with. The command will tell you where the `ipython_config.py` file has been created, and in it we need to find this line:
`c.InteractiveShellApp.exec_files = []`
and change it to:
`c.InteractiveShellApp.exec_files = ['virtualenv.py']`

Now whenever I start ipython, the `virtualenv.py` script will be executed, which will set my sys.path variables the way I need them. I can now happily `import numpy` and `import nltk` in ipython.

`In [1]: import nltk
In [2]: phrase = nltk.word_tokenize("That was easy.")
In [3]: nltk.pos_tag(phrase)
Out[3]: [('That', 'DT'), ('was', 'VBD'), ('easy', 'JJ'), ('.', '.')]`
