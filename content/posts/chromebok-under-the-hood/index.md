---
subtitle: "Reposted: originally published on my Pafnuty blog (2008–2014)"
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
  - experiments
layout: single
draft: false
---

*Originally published on my old blog, [Pafnuty blog](https://pafnuty.wordpress.com/2011/05/26/chromebok-under-the-hood/). Reposted here as an effort to [consolidate writing](/posts/consolidating-my-writing/) into one place. The original publication date was: May 26, 2011.*

---

[(A second post about my chromebook).](http://pafnuty.wordpress.com/2011/05/23/nothing-but-the-web/ "Nothing but the web?")

Chromebooks are known to come in [two different hardware configurations](http://www.winmatrix.com/forums/index.php?/topic/31598-google-chromebooks-hardware-specifications/ "Chromebook hardware configurations"), one by Acer and the other by Samsung. Based on display size (I have a 12.1" screen) and built-in 3G modem, my unlabeled device seemed at first to be the Samsung type. But not quite: I have standard VGA, not mini-VGA like the Samsung Chromebook. And I have only one USB port.

So if this Chromebook is not Acer and not-quite-Samsung, what is it?

Peeling back the gift wrapping:

[![Chromebook Disassembled](img_1617.jpg?w=1024 "IMG_1617")](img_1617.jpg)

So, what can we spot here? I googled the part numbers:

{{< figure src="img_1622.jpg" alt="3G Modem: Novatel wireless PC card modem with Qualcomm" caption="3G Modem: Novatel wireless PC card modem with Qualcomm (Gobi2000, based on Google search)" link="img_1622.jpg" >}}
{{< figure src="img_1624.jpg" alt="SDSA4DH-016G" caption="16GB Sandisk SATA solid state drive SDSA4DH-016G" link="img_1624.jpg" >}}
{{< figure src="img_1625.jpg" alt="AR5BBU12" caption="Atheros BlueTooth Modem AR5BBU12" link="img_1625.jpg" >}}
{{< figure src="img_1636.jpg" alt="H5TQ2G83BFR-H9C" caption="Hynix 2Gbit DDR3 SDRAM H5TQ2G83BFR-H9C" link="img_1636.jpg" >}}

I saved the best for last. Meet the brains:

{{< figure src="img_16381.jpg" alt="Intel NM10 Express Chipset - CG82NM10 SLGXX" caption="Intel NM10 Express Chipset - CG82NM10 SLGXX" link="img_16381.jpg" >}}

To totally geek out here, we can look at the Intel NM10 chipset architecture:

{{< figure src="intelnm10-architecture1.png" alt="Intel NM10 architecture" caption="IntelNM10 chipset block architecture diagram" link="intelnm10-architecture1.png" >}}

So that's what we actually have under the hood. This device has been called the CR-48, or, if you prefer, the "Limited Edition Google Chrome Cr-48 Notebook". There's a few resources that have been setup for talking about the device (including a Google Site called "[CR-48ite](https://sites.google.com/site/cr48ite/)"), but I've been bothered by how information across these resources doesn't seem very consistent.
