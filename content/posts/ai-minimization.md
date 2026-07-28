---
title: "AI Minimization"
subtitle: "Use no more AI than necessary." 
date: 2026-07-07
author: "Aman Ahuja"
categories:
- observations
tags:
- llm
- compute
- minimization
- ai
layout: single
draft: false
---

Like many people, I've found LLM technologies to be useful in many surprising
ways, and in addition to my professional work as an AI/LLM consultant and 
advisor, I have been using LLMs to make my own workflows and tasks easier.
When doing so, though, I've been working hard to minimize rather than
maximize the way I invoke LLMs. 

{{< pullquote >}}                                                                                                                                                                
AI minimization is a principle that you should use only the minimal
amount of AI necessary to accomplish a legitimate purpose. 
{{< /pullquote >}}      

Depending on where you sit on the AI adoption and hype spectrum, you may
find this obvious, surprising, or insufficient. I get that. If you believe
that no one should use these technologies at all, I understand and
respect your perspective. Just because I use these technologies doesn't
mean I don't hate them, too.

Until recently, most who work actively with LLM technologies would advocate
against the "premature optimizations" of LLM systems, in favor of letting
models think longer, running many agents in parallel, and using compute
resources to replace engineering time and effort. There are still many who
are focused on finding ways to give greater access to LLM agents, and have
them work harder and longer on increasingly complex tasks. 

At the same time, there's an increased interest in getting benefit from
these technologies while also using fewer tokens and smaller models. Partly
this is coming out of concerns about prices. Tokens cost money, and there
is good reason to believe that AI providers will be changing their
pricing models soon in order to help recover their investments. 

That's great, in my opinion. It's good for the environment and the world at
large if the price of tokens rises to meet the actual cost of tokens. 

My interest in minimizing is also value-driven.

Using fewer resources is, first of all, always better. (I sometimes make
slightly absurd choices pertaining to reusing food takeout containers,
avoiding car trips, or traveling light.)

In the case of LLM technologies, there are many specific reasons that I
care about using fewer resources.

There are security and privacy reasons that affect my choices. Using local
models, or avoiding unnecessary utilization of the frontier models from Big
AI, goes hand-in-hand with protecting my data and caring about my privacy.
I don't trust many of these companies to follow their own stated policies,
or to not to quietly change them later. 

I also care about switching costs, as I always have with any of my tech
choices. This points me towards open models, which in turn points me
towards doing my work with smaller models and smaller contexts. 

The combination of these concerns has led me to a principle of AI
Minimization, analagous to the principle of data minimization. Applying
this principle means having some opinions and practices about models,
context, tokens, and more.  

{{< preformat >}}
An aside on language about "AI".

I don't like the term "AI", as it is misleading and inaccurate. "LLM", or
"Large Language Model" is imprecise as we are going to be talking about
small language models, too, and "language models" would be too inclusive 
a term. 

I suppose I'm referring to specific transformer architectures, especially
the decoder-only transformer systems which have driven this current cycle
of artificial neural networks, but it is hard to know what architectures
are actually being used, and how they evolve, and certainly by now most
providers use a combination of architectures anyway.

So I guess I will use "AI" in this post for simplicity, but, just so you
know, it's under protest. 
{{< /preformat >}}

## Optimization vs. Minimization

Why Minimization and not "AI Optimization"?  

Optimization is about finding the best tradeoff. It focuses equally on the
acceptability of the outcome and on the resources needed to get there.
Minimization takes a different stance: start with less and add only what is
necessary.

The principle of data minimization, which motivated me, suggests collecting
only the smallest amount of data truly needed for a given purpose. 

> Data minimization is the principle that you should collect, use, retain,
> and share only the minimum amount of data necessary to accomplish a
> legitimate purpose.

We do not strive to "optimize" the data we are collecting. That would be an
aspiration with no teeth. We strive to _minimize_ it. 

A similar principle applies for AI systems. 

## Model, Context, Tokens, Compute

When asking "What is the least amount of AI necessary?" I'm not just
interested in keeping the number of tokens low. I try to look at the
tokens, the model, the compute, and the data. 

## <u>Minimizing the Model</u>

It's obvious that not every task requires the most capable model available.
There is much already written about "modelmaxxing", but here are a few
of my thoughts: 

**1) I prefer open models to closed models**, even if I'm not fine-tuning or
otherwise messing with the weights and layers. This feels analogous to my
overall preference for FOSS. 

**2) I prefer local models to hosted models.** Many limitations apply: 
my GPUs and VRAM are often insufficient for all but the simplest tasks, 
but many tasks I want done are in fact pretty simple. 

**3) I prefer smaller models to larger models.** I'll often try to do a task
with a smaller model, and escalate only if it doesn't perform
satisfactorily. For one-off tasks and ad-hoc work this can backfire, as
it is inefficient to have to attempt a task multiple times in progressively
bigger models. 

Having said that, even for one-off tasks, there is a benefit in that my
intuitions are getting better. I learn what models are capable of and what
they will struggle with, and what techniques might help me select the
right model. 

**4) I prefer cheaper models.** This is related but separate from the
above, particularly when pricing does not always match or even correlate
with true costs. 

**5) I prefer tools that allow model switching**.  Codex or Claude Code, for
example, are blatant attempts to get users hooked on a tool that
confines them to only the LLM provider's models. Opencode
(https://opencode.ai/) is a great alternative to these. It provides
comparable features while allowing users to pick whatever model and LLM
provider they want to use, including free, open source, and local models. 

## <u>Minimizing Context</u>

"Context" is all the data that is sent to the LLM in a query, such as
whatever you put in the chat, and files that you attach. It may also
include a system prompt and the conversation's history. Depending on
what tool you are using, there may be other things injected into the context
that you may not pay as much attention to: like "custom instructions" or
"memories", and the instructions in a coding agent or harness. 

Controlling and understanding LLM context windows is a whole world unto
itself, and often requires careful tool and customization and plug-in
selection. As of July 2026 this is all unnecessarily complex, as a simple
result of incentives -- the more tokens you use, the more an LLM provider
can charge you, and the better claims it can make to its funders, etc.  As
"tokenmaxxing" fully jumps the shark, better and easier-to-use tools will
surely become commonplace. 

**6) I prefer tools that provide transparency and control over the
context**. In many mainstream tools context windows are intentionally
obfuscated, and far from optimizing context, such tools often encourage
workflows and user behavior that produces very large contexts. I like the
pi coding agent (https://pi.dev/). 

**7) I try to use only the context necessary for the task.** This means I
take the time to think about what I'm asking and what information is
required for the LLM to provide a quality response. 

**8) I prefer short LLM interactions over long-running agents, and small
tasks to large tasks.** Long "conversations" (another unfortunate misnomer)
lead to overloaded context windows that contain far more information than
is actually needed. Note that long-running tasks and scheduled tasks are
still possible with short LLM interactions. 

**9) I prefer small-sized skills**. I use or build small _skills_, and I
don't give an agent free reign to go fill up its context window with web
fetches. I manually trigger almost all skills that I use, rather than
agent-triggered skills. The latter requires consuming part of the LLM
context window with descriptions of available skills, and when triggered
incorrectly leads to wasted tokens and bad steering. 

These efforts to minimize my context are awkward and clunky. I often have
to start new conversations, switch between conversations, or use multiple
running instances of a tool. These are temporary hacks that already have
emerging tooled solutions which are getting better every time I look. 

{{< pullquote >}}
Maintaining context control today is difficult. Many smart teams are
working on this problem, and it will smooth many rough edges when,
inevitably, this becomes very easy for everyone. 
{{< /pullquote >}}

Context rot is about more than just _long_ contexts. Just as a human might
be "primed" by information to produce a biased response, LLMs produce
different results that are influenced by irrelevant information --
including, for example, skill descriptions. Thus all these minimizations
have the added benefit of reducing the likelihood of undesired model
behavior.

## <u>Minimizing Tokens</u>

Minimizing context often also minimizes input tokens, but we have to think
about output tokens slightly differently. 

Output tokens cost more than input tokens. When I want an LLM to give me a
straightforward answer and it paraphrases what I asked and provides
extraneous information, and options for what I might want to do next, 
that's annoying, but also generating extra output tokens. Sometimes
it can be quite difficult to constrain the output of the model. This
is double frustrating because the provider is billing me for this 
output micro-slop. 

In an LLM conversation, every previous message stays in the context window.
Each exchange ("turn") is accumulating tokens. Those unnecessarily
long-winded answers from the LLM are polluting the rest of the
conversation. 

**10) I provide explicit instructions to shorten LLM responses** as appropriate
for the task or skill. Brevity. Structured outputs. Avoiding repetition. 

## <u>Minimizing Compute</u>

There is no longer a simple relationship where the amount of compute used
is merely a function of the size of the model and the amount of
input / output tokens, as many tools often make multiple calls to a
provider or model, and many providers aren't simply taking one feed-forward
pass through a single language model. 

For example, there is another type of token, sometimes called "thinking
tokens". These are tokens used to internally process a task before
providing a final response. Sometimes this process is called "reasoning".
Both these terms are misleading. 

{{< preformat >}}
Needless to say, an LLM cannot think. This is still an LLM just probabilistically predicting "the next token". Internally, it has a set of instructions to generate and use these tokens as a type of "memory" beyond its internal activations; it's still a transformer going through decoding steps. 
{{< /preformat >}}

Reasoning tokens are usually priced as output tokens. Depending on the
provider, a user might not be able to see the reasoning at all, or see
only a summarized version. Sometimes the use of these extra tokens can have
esoteric triggers ("think carefully", "be thorough") rather than explicit
settings, which obfuscates user control. Furthermore, providers do not
share architectural details so it's hard to know what's actually 
happening behind the scenes. 

It's clear that reasoning improves results on certain types of tasks. It is 
valuable for longer and more complex tasks where the user is
not concerned about control or inspecting the details. 

**11) I don't use reasoning and deep thinking features** because this 
tradeoff does not meet my needs. 

If I do want to take on a really complex task with LLMs, I prefer
to treat the task as a project, and break it down into smaller steps such
that I can stay fully engaged, follow along, ask questions, and opt to
intervene.  

Agentic workflows and subagents provide one way to tackle complex tasks
without some of those negative trade-offs. 

"Subagents" refer to tool-using workflows initiated by a main agent -- "go
do this task", says the agent, "and then come back and tell me what you
learned." Subagent processes also expend tokens, of course, in order to
run, and then they produce summaries that are added to the context
window of the spawning agent. 

This pattern is very useful as it can be leveraged to keep context windows
small. Furthermore, in harnesses like Opencode, one can specify
permissions, available tools, and even LLM model separately and
specifically for each subagent. 

**12) I use subagents to create isolated contexts** for common tasks.**
This can be a powerful technique but requires some practice to get
right. 

There are some gotchas. Subagent invocation and the associated token use
isn't always clear to the user. Often agent harnesses do not correctly or
clearly display this information. So using such subagents can have
unexpected token compute and token consumption. 

Agents are often justifiably maligned, and the term itself is not clear.
Many writers have described "agents" as efforts to give LLMs access to live
data and real-world actions, and have warned us about what could go wrong.
That is not what we are doing here. There are risks, yes, but these are
called "agent harnesses" because they put reigns on the models, not unleash
them. 

---

## Concluding Thoughts

{{< pullquote >}}                                                                                                                                                                
When asking "What is the least amount of AI necessary?" I'm not just
interested in keeping the number of tokens low. I try to look at the
tokens, the model, the compute, and the data. 
{{< /pullquote >}}                                                                                                                                                                
I follow these minimization ideas for my own purposes. In the near future I
think we will see tools and best practices emerging for minimizing, or at
least optimizing, the use of LLMs. 

Emerging best practices might look something like this: 
* Start new conversations when changing tasks.
* Periodically summarize and reset long-running chats.
* Avoid carrying unnecessary context forward.
* Use the smallest instruction set that achieves the objective.
* Retrieve specific information instead of loading entire documents.
* Start with smaller models and escalate only when necessary.
* Convert repeatable workflows into code, templates, or automations.
* Treat context as a scarce resource, not a free resource.
... and so on. 

An "Awesome AI Minimization" resource list might be helpful; I didn't see
one when searching recently. I could see tools, agents, skills, context
management techniques, small-model workflows all being useful categories.
I'd love to see more transparency about token usage in tools, and agent
harness plugins that display costs and environmental impacts. 

AI Minimization might be a step too far for some: engineering time is more
expensive than inference, after all, and premature optimization is an old
trap. 

Nevertheless, it's a principle with a worthy provocation. As data
minimization improves more than merely privacy, AI minimization improves
more than efficiency. In a moment when we offload too much to these models,
we could use a push in the opposite direction, from de-skilling to critical
thinking, from abdication to co-creation. I hope this idea encourages some
to think differently about how they're using LLMs, and perhaps ask if
that task that they're working on needs an AI at all. 

