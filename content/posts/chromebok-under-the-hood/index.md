---
title: "Chromebook: Under the Hood"
date: 2011-05-26
author: "Aman Ahuja"
series:
  - pafnuty-blog
tags:
  - chipset
  - chrome os
  - chromebook
  - cr-48
  - disassembled
  - intel nm10
  - under-the-hood
categories:
  - CHANGETHISCATEGORY
layout: single
draft: false
---

*Originally published on [pafnuty.wordpress.com](https://pafnuty.wordpress.com/2011/05/26/chromebok-under-the-hood/) in May 2011. Reposted here as part of pulling old writing into one place.*

---

[(A second post about my chromebook).](http://pafnuty.wordpress.com/2011/05/23/nothing-but-the-web/ "Nothing but the web?")
Chromebooks are known to come in [two different hardware configurations](http://www.winmatrix.com/forums/index.php?/topic/31598-google-chromebooks-hardware-specifications/ "Chromebook hardware configurations"), one by Acer and the other by Samsung. Based on display size (I have a 12.1" screen) and built-in 3G modem, my unlabeled device seemed at first to be the Samsung type. But not quite: I have standard VGA, not mini-VGA like the Samsung Chromebook. And I have only one USB port.
So if this Chromebook is not Acer and not-quite-Samsung, what is it?
Peeling back the gift wrapping:
[![Chromebook Disassembled](img_1617.jpg?w=1024 "IMG_1617")](img_1617.jpg)
So, what can we spot here? I googled the part numbers:
[caption id="attachment\_531" align="aligncenter" width="225" caption="3G Modem: Novatel wireless PC card modem with Qualcomm (Gobi2000, based on Google search)"][![3G Modem: Novatel wireless PC card modem with Qualcomm](img_1622.jpg?w=225 "3G Modem: Novatel wireless PC card modem with Qualcomm")](img_1622.jpg)[/caption]
[caption id="attachment\_532" align="aligncenter" width="300" caption="16GB Sandisk SATA solid state drive SDSA4DH-016G"][![SDSA4DH-016G](img_1624.jpg?w=300 "16GB Sandisk solid state drive")](img_1624.jpg)[/caption]
[caption id="attachment\_533" align="aligncenter" width="300" caption="Atheros BlueTooth Modem AR5BBU12"][![AR5BBU12](img_1625.jpg?w=300 "Atheros BlueTooth Modem")](img_1625.jpg)[/caption]
[caption id="attachment\_536" align="aligncenter" width="300" caption="Hynix 2Gbit DDR3 SDRAM H5TQ2G83BFR-H9C"][![H5TQ2G83BFR-H9C](img_1636.jpg?w=300 "Hynix 2Gbit DDR3 SDRAM H5TQ2G83BFR-H9C")](img_1636.jpg)[/caption]
I saved the best for last. Meet the brains:
[caption id="attachment\_538" align="aligncenter" width="300" caption="Intel NM10 Express Chipset - CG82NM10 SLGXX"][![Intel NM10 Express Chipset - CG82NM10 SLGXX](img_16381.jpg?w=300 "Intel NM10 Express Chipset - CG82NM10 SLGXX")](img_16381.jpg)[/caption]
To totally geek out here, we can look at the Intel NM10 chipset architecture:
[caption id="attachment\_540" align="aligncenter" width="300" caption="IntelNM10 chipset block architecture diagram"][![Intel NM10 architecture](intelnm10-architecture1.png?w=300 "Intel NM10 architecture")](intelnm10-architecture1.png)[/caption]
So that's what we actually have under the hood. This device has been called the CR-48, or, if you prefer, the "Limited Edition Google Chrome Cr-48 Notebook". There's a few resources that have been setup for talking about the device (including a Google Site called "[CR-48ite](https://sites.google.com/site/cr48ite/)"), but I've been bothered by how information across these resources doesn't seem very consistent.
