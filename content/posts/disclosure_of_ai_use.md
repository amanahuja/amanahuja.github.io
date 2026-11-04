---
title: "Disclosures of AI use"
subtitle: "A discussion of a few AI disclosure frameworks"
description: "A discussion of a few AI disclosure frameworks"
date: 2026-10-09
author: "Aman Ahuja"
categories:
  - observations
  - reading-log
tags:
  - LLM
  - AI
  - artificial-intelligence
  - responsible-ai
layout: single
---


I love that more and more people are thinking about how to disclose how
they are using AI, and how much. They want to be transparent about it. 
This push towards transparency is coming from authors, from platforms,
and from institutions. 

> How much of this post was written by me, versus written by an AI model? 

I noticed that a colleague, Beau Cronin was using a system he created for
himself ([beaucronin.com/tail](/https://beaucronin.com/tail/)). Soon I 
was noticing them in more places. I was particularly interested in 
journalists and writers: many publishers are devising their own approach
for disclosure. Searching, I found several attempts to standardize,
such as Disclose AI Usage ([DAIU](https://daiu.org) ). 

My first thought was that I should pick one of these approaches and
start using it myself. In reviewing a few of the ones I had encountered, 
I found
* They often use scales that aren't aligned with my interests
* Adding complexity makes it more accurate, but with a price. 
* This will get more confusing as AI gets better at writing
* Adding such a disclosure might backfire

So where does that leave me? 

### 1. A scale from little to much

Disclosure methods often introduce a scale from "little AI use"
to "lots of AI use". That seems intuitive, but it requires a hierarchy
of AI use. 

Consider an example (`EXAMPLE A`): An author asks an AI to pick a topic for
a blog post that will attempt to get the most views, to research the
subject, and write an outline of an article with three thought provoking
arguments. The author then usese this outline to write the final copy
_themselves_. They pen every word -- in their own style and words, with
spelling and grammar mistakes.  

This feels like a pretty significant use of AI to me. My interpretation is
that AI took the lead in informing the topic, the substantive content, and
the structure of the argument and/or narrative. Therefore a scale or ranked
system should place this example pretty "high". 

This is how this example might show up in TAIL, REAL, and DAIU. 

**TAIL.** Example A would be **TAIL 1**, which suggests minimal use of AI
instead of significant use. 

**REAL.** The REAL framework (https://arxiv.org/html/2610.04021v1)
recognizes that "ideas" are a form of contribution. Example A would land in
**Level 2 ("Brainstorming")**. If the author deemed the AI to be a co-author, it
would be Level 4. If I was the author, I might consider those contributions
substantial, but the guidance isn't precise about this. 

**DAIU.** The DAIU standard differentiates "Content Origin" such that
my Example A would be categorized as a "AG" / "AI Collaborator", if we
agree that drafting the outline qualifies as a draft. I think it does.
The AI contributions seem to land on category "Major" (which is
numerically 3 in a scale from 0-4). so the ranking would be **AG-Major/3**.
(Notably, ChatGPT selected AG-Remix/2, but I disagree). 

What if we reverse this fabricated example, such that the AI contributes
only the copy? The human comes up with the topic, spends an amount of time
on desk research appropriate to the topic, comes up with a narrative
structure and the key arguments. Then the author hands a "spec" to an AI
agent. The AI agent writes every word of the blog post, which the human
then reads and approves, for the sake of argument no revision are required.
Let's call this `Example Z`.

I asked an AI to consider these examples, and it provided this commentary:

{{< preformat >}}
In Example A, the author could produce a beautifully idiosyncratic piece
of writing, rich in personal voice, without contributing a single original
idea.
In Example Z, the author might produce a generic, unmistakably
AI-sounding article despite having done all the intellectually demanding work. 
...
Example A could look human while thinking like AI. Example Z could look
like AI while thinking like a human.
{{< /preformat >}}                                                                                                                                                                

Haha, okay, okay. 

This is how Example Z would rank in those systems: 
* **TAIL**: TAIL 4 or TAIL 5. Probably 4, because the author could confidently
  "stand by" the specific output. 
* **REAL**: Level 5. AI contributions to prose seems to tip the scales, leading
  perhaps to a "Level 3", even if the ideas were the authors. 
* **DAIU**: "HM-Major". Again, this depends on what the framework considers to be
  the first draft. Is the spec or outline a draft? This could be AG-Major
  or HM-Major, depending. 

I find this to be a little troubling about these ranking systems. `Example
Z` seems to be a more significant use of AI than `Example A` in these three
systems, at least for what I had in mind: writing an article, a whitepaper,
or a blog post. 

However, what if instead we consider a poem or a play? In that case a
thorough outline (or "specification") contains _merely_ plot and structure,
but the importance of the final prose cannot be understated. The style and
choice of work become much more important to the whole. Likewise if we
consider a drawing, a musical composition, or an animation. 

Code, poem, research paper, a math proof. The significance of AI
contribution depends on the context. 

### Multidimensional and narrative disclosure 

The DAIU approach of indicating both level and origin is interesting. 
One could imagine adding more dimensions. 

"How much did AI contribute to ..." 
* ... editorial: selection of topic and audience strategy
* ... intellectual : origin of arguments and structure
* ... expression: language, diction, prose
* ... research: fact checking, citations, verification

This starts to get complex really quickly. Simplicity seems more
important than precision, when providing a disclosure to a casual reader
who isn't immersed in these topics. 

Maybe a scale isn't necessary at all. The team at
[Intertidal](https://www.intertidalagency.org/) shared a different
approach, from Elsevier. The system that Elsevier uses doesn't a
numeric score at all. 
They provide editorial guidelines on acceptable
use of AI, and disclosure requirements. Authors following Elsevier's policy 
are asked to describe how they used AI. 

Elsevier policy might not allow Example A at all, as it raises a
authorship-integrity concern. Example Z under this policy might say
something like: 
> During the preparation of this manuscript, the author used Anthropic
> Opus-5 to generate the article's text from a detailed author-developed
> specification. The author independently conducted the research and
> developed the article's analysis, structure, arguments, and conclusions.
> The AI-generated manuscript was reviewed and approved by the author, who
> takes full responsibility for its content.

I don't claim to be an expert on these policies, but it is significant that
Elsevier's policy might not allow Example A at all -- a scenario which in
other disclosure systems was ranked low. 

## The "AI Smell" is a-changing. 

Automated AI detectors are fighting an arms race in trying to detect when 
content is generated by AI. I don't know how they work, but they seem 
to be looking for tells -- for statistical patterns in the style and the
writing. These might include for diction, style, even sentence structures
or paragraph structures. I'm sure it gets more complex than that, and at
some point it's AIs detecting AIs (or, AIs providing statistical estimates
of whether some writing is similar to that produced by AI.)

Substack is trying out an automated [feature that flags
AI-generated
writing](https://support.substack.com/hc/en-us/articles/50891130623508-How-can-I-detect-AI-on-Substack)
using
[Pangram](https://pangram.substack.com/p/how-does-pangram-work) (which,
BTW, sparked some
[backlash from authors](https://www.404media.co/substackers-say-new-ai-detection-tool-is-a-witch-hunt/) on the platform). 

These products must have their hands full keeping up-to-date with model
releases, and with an ever-increasing variety of models. 

{{< preformat >}}
Aside: Evidence is mixed about how AI Disclosure policies might affect
readers. Research by trustingnews suggests that people want disclosures
from newsrooms in general, but mistrust a specific article if it has an
AI-use disclosure. 
{{< /preformat >}}

The most frustrating AI contribution today isn't the proverbial em-dash.
Not anymore. It's the type of writing that sounds poignant but is lacking
in substance. That's a lot harder to detect than some of the "tells"
listed in [Wikipedia: "Signs of AI
writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).

Possibely soon in the future, both of these will be gone: the AI "smell",
the current superficial kind and the next deeper one, will not show up 
in these models output. 

Then we have to ask the question, why do we care if it's AI or human? We 
will still care, but we'll need to think carefully about why. Recent
discussions about AI math proofs had split opinions -- some mathematicians
said that if the proof is sound, authorship doesn't matter. 

I will still want to know when a colleague sends me a message that an AI
wrote for them, or when an essay by an admired writer contains astute
observations that aren't their own. A poem written by a human will always
be imporant, even if someone like me can no longer spot the AI in a
double-blind poetry reading. 


## So what should Aman do?  

I'll disclosure THIS post using ALL the systems. 

* TAIL: **TAIL 2** 
* REAL: AI Influence **Level 2** "Brainstorming".  
* AI Flags: **B - AI Assisted**. 
* DAIU: **HM-REMIX/2**.

I am giving weight to the fact that I used AI to help "rank" or evaluate
fabricated examples. I reviewed the two A/Z examples I ended up including,
but didn't independently review all the fabricated examples. 

I include AI-generated text directly in a pullquote, clearly attributed. I
consider that to be like other quotations, and not direct authorship of
this blog's text. 

(By the way, I had previously neglected to directly review just one of the
frameworks. I went back and reviewed it specifically to keep this post's
disclosure ranking lower. Maybe I wouldn't have done that otherwise. Thus
including an AI disclosure forced me to be more thorough.)

Let me attempt the Elsevier disclosure as well: 

{{< preformat >}}
**AI use disclosure (Elsevier-style)**
This article was written with assistance from ChatGPT. I developed the
central thesis, examples, narrative structure, arguments, and conclusions,
and wrote the prose.

I used ChatGPT to research AI disclosure frameworks, explore their
implications, test hypothetical scenarios, and suggest interpretations and
classifications. I evaluated these suggestions, sometimes disagreed with
them, and retained my own judgments. The article contains an explicitly
attributed quotation from ChatGPT.

I reviewed the AI-generated contributions and take responsibility for the
article's content.
{{< /preformat >}}

I find the narrative disclosure to be the most helpful and most attractive.
I can see myself using something like that for longer posts, and maybe a
different simpler one for short posts. 

If you know of a disclosure system you like better than the ones I've
mentioned, I'd love to hear about it. 

--- 

Links to the frameworks mentioned: 
* Beau Cronin. “Transparent AI Labeling (TAIL).” https://beaucronin.com/tail/
* Goumiri, Cortez-Rodriguez, et al. (2026). “The Reported Engagement with AI Level (REAL) Rating: A Framework for Disclosing Human-AI Collaboration.” https://arxiv.org/abs/2610.04021
* Responsible AI Usage Foundation. (2025) “Disclose AI Usage (DAIU): AI Usage Disclosure Framework.” https://daiu.org/framework/
* Elsevier Publishing Ethics and Policies (2026). “Generative AI Policies for Journals.” . https://www.elsevier.com/en-gb/about/policies-and-standards/generative-ai-policies-for-journals
* AI Flags. “AI Flags: AI Authorship Classification Framework.” https://www.aiflags.eu/

Interesting reads: 
* Trusting News. (2026). “Building Trust with AI: AI Trust Kit.” https://trustingnews.org/trustkits/ai/
* Trusting news has many more examples of AI Policies, Disclosures and explainers: https://trustingnews.org/examples/ai-journalism-examples/

Newsroom examples:
* The Guardian. https://www.theguardian.com/help/insideguardian/2023/jun/16/the-guardians-approach-to-generative-ai
* Associated Press. https://www.ap.org/the-definitive-source/announcements/ap-updates-newsroom-standards-for-artificial-intelligence/
* WIRED. https://www.wired.com/about/generative-ai-policy/
