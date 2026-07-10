---
title: "Privacy Review Skill"
subtitle: "This shows up in previews (homepage and listing)"
date: 2026-05-01
author: "Aman Ahuja"
categories:
  - experiments 
tags:
  - LLM
  - skills
  - AI
  - privacy
  - terms-of-service
layout: single
---

I published an agent skill that I have found useful: [amanahuja/privacy-skills](https://github.com/amanahuja/privacy-skills)
{{< pullquote >}}
amanahuja/privacy-skills: Review a privacy policy or terms of service
against a structured scorecard. Combines ToS;DR's human-curated ratings
with LLM analysis. <br>
<br>
Use it next time instead of just clicking "Accept"! 
{{< /pullquote >}}

## Skill Design thought process

ToS;DR has an excellent framework and methodology for reviewing privacy
policies, and the community has reviewed many privacy policies by hand,
covering many popular tools and services.  If you haven't heard of ToS;DR,
definitely pay them a visit: https://tosdr.org .

So first I wanted my agent to check if the privacy policy had already been
reviewed, and to use ToS;DR's review when possible. It's by humans, well
considered. They have an API that makes this easy. 

When a human review from them is not available, we can still follow their
framework, categories, and approach, all of which is well documented. 

Privacy policies are updated all the time, so I was very concerned about 
outdated analysis. 

I'm in Wisconsin, USA, but as I started thinking about publishing this as
a public agent skill, I began thinking about jusidiction. If the user is in
the EU and GDPR applies, that should change the analysis. 

I wanted the agent's review to be easy to understand for people who are not
privacy nerds.

The agent's claims should be strongly grounded.  The skill includes
instructions to providie direct quotes from the policy document. This
abandons brevity. While that's fine for me, I was conscious that most users
will want something short, and if they read any details it would only be
for a section that they felt was important. This led to a scorecoard idea
that worked well alongside the existing ToSDR framework. 

Everyone's needs are different, and vary by context or the type of tool
they are evaluating. Such evaluations depend on one's threat model. This is
both a challenge and the real value of having an LLM analysis. I've stared
simple with a methodology that adjusts the review depending on the level of
privacy concern. 

General skill-building best practices should apply. 

## Example : my own website. 

I'll share the agent's analysis when I used this skill to review the privacy
policy on my own website. 

My query: "review this privacy policy: https://amanahuja.me/privacy-policy/"
I was using Sonnet 4.6 in this exchange. 

The agent asks:
> "Which TOSDR result matches the service you wan reviewed?" 

My website has been previously submitted to TOSDR and has a service ticket
at: tosdr.org/en/service/7069 — Rating: N/A (not yet reviewed).  

The agent found this and asked me to confirm if it is a match. I said
"Yes". There's no human review available yet for this ticket, so the agent
was not able to get any information from TOSDR. 

Agent asks: 
> "What level of review do you need?" 

I chose "Standard". 

{{< preformat >}}
What level of review do you need?

1.Standard (Recommended)
Deciding whether to interact with this personal site — covers the most important considerations

2.Enhanced
Deeper analysis of data collected and who sees it

3.High Sensitivity
Full analysis including law enforcement access, sensitive data categories, and consent rights

4.Type your own answer
{{< /preformat >}}


Agent asks: 
> "What jurisdiction should I apply when assessing your privacy rights?" 

I chose "United States" with no specific state. 

{{< preformat >}}
What jurisdiction should I apply when assessing your privacy rights?

1.United States (no specific state)
Default — general US privacy law context

2.California (CCPA/CPRA)
California privacy law applies to you

3.European Union / GDPR
GDPR applies to you

4.Other
Specify your jurisdiction

5.Type your own answer
{{< /preformat >}}


And then, finally, the response. The agent, using the skill, generated this analysis: 

{{< preformat >}}
Confirmed: 0 approved TOSDR points. This will be a full LLM-generated
analysis from the policy text. Here is the review:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SERVICE:         Aman Ahuja (personal website)
POLICY URL:      https://amanahuja.me/privacy-policy/
LAST UPDATED:    Not stated
TOSDR:           Found — Grade N/A, 0 approved points, not comprehensive
TIER:            Standard
JURISDICTION:    United States (no specific state)
ANALYSIS METHOD: LLM-generated only (TOSDR record exists but unreviewed)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

── TOSDR RECORD ──────────────────────────────────
Grade: N/A  |  Points: 0 approved  |  Comprehensive: No
Link: https://tosdr.org/en/service/7069

── SCORECARD ─────────────────────────────────────

1. Cookies & Tracking       ⚙ LLM-generated    [GREEN]
   First-party analytics cookies only; third-party trackers explicitly
   excluded, DNT respected, site functional without cookies.
   "Web analytics and server logs are hosted on our own servers and
   related data are not shared with any third party services."

2. Data Collection          ⚙ LLM-generated    [GREEN]
   Minimal collection: no PII by default; optional contact info on form
   submission; IP partially anonymized (2 bytes masked).
   "When you visit or view amanahuja.me, the site collects no personally
   identifiable information about you."

3. Data Sharing             ⚙ LLM-generated    [GREEN]
   Analytics data explicitly not shared with third parties; no mention of
   any data sale or brokering.
   "Web analytics and server logs are hosted on our own servers and
   related data are not shared with any third party services."

4. Advertising              ⚙ LLM-generated    [GREEN]
   No advertising, no ad networks, no targeted advertising mentioned or
   apparent.
   Not addressed in this policy (no ad operations present).

5. Your Rights              ⚙ LLM-generated    [YELLOW]
   Contact mechanism exists for privacy requests, but no explicit right
   to deletion, access, correction, or data export is stated.
   "Please contact Aman Ahuja with your questions and privacy-related
   requests using the options available on the contact page."

6. Content Ownership        ⚙ LLM-generated    [YELLOW]
   No content license terms stated (site appears read-only/no user-generated
   content). Not a meaningful concern for a personal informational site,
   but the policy is silent on it.
   Not addressed in this policy.

7. Data Retention           ⚙ LLM-generated    [GREEN]
   Logs purged on an approximate quarterly schedule — a specific and
   reasonable commitment for a personal site.
   "Logs are purged periodically, approximately once a quarter."

8. Terms Changes            ⚙ LLM-generated    [RED]
   Changes can be made at any time without notice; no commitment to notify
   visitors of material changes.
   "We may amend this Privacy Policy at our discretion at any time."

9. Account Suspension       ⚙ LLM-generated    [GREEN]
   No user accounts exist on this site; not applicable.
   Not addressed in this policy (no accounts).

10. Arbitration & Disputes  ⚙ LLM-generated    [YELLOW]
    No arbitration clause present — this is positive. However, no dispute
    resolution process is stated at all. Governing law and jurisdiction
    are not specified.
    Not addressed in this policy.

11. Acquisition & Shutdown  ⚙ LLM-generated    [YELLOW]
    No data transfer or acquisition clause. For a personal site with
    minimal data, this is low risk but the policy is silent on what
    happens to any collected data if the site changes hands.
    Not addressed in this policy.

12. Government Requests     ⚙ LLM-generated    [YELLOW]
    Compelled disclosure is acknowledged; the policy commits to
    independently objecting to overbroad requests, which is above
    average for a personal site. No warrant requirement or user
    notification commitment is stated, however.
    "This site may disclose data when required to by law, in response to
    a subpoena, or if served with a search warrant. We will independently
    object to overly broad requests for access to information about users
    of the site."

── NARRATIVE ─────────────────────────────────────
This is an unusually privacy-respecting personal website. The data
minimization posture — no PII by default, first-party-only analytics,
IP anonymization, DNT compliance, cookie-optional design — is materially
better than most personal sites, which typically embed Google Analytics
or social pixels without comment. The policy is templated from credible
sources (Digital Impact Toolkit, ToS;DR) and shows deliberate intent.

The one structural weakness is the terms-change clause: unlimited
discretion to amend without notice is boilerplate, but it is
contradicted in spirit by the otherwise careful policy. Given the
minimal data footprint, the practical risk is low — there is little
data here that could be weaponized by a policy change. The absence of
explicit data subject rights (deletion, access, portability) is a gap,
though the contact page mechanism provides an informal path to exercise
them.

For a US visitor with no specific state privacy law applying, your
rights here are whatever the policy voluntarily offers. The informal
"contact for privacy requests" commitment is the main mechanism. Given
the site's minimal collection, this is adequate in practice but
unenforceable in principle.

── KEY FLAGS ─────────────────────────────────────
⛔ RED items:

  Terms Changes — Policy can be amended at any time without notice or
  consent, removing any expectation of stability.
    "We may amend this Privacy Policy at our discretion at any time."

✓ NOTABLE POSITIVES (genuinely above average for a personal site):
  · IP anonymization (2 bytes masked) — rare commitment for a personal site
  · DNT honored explicitly
  · Site functional without cookies
  · First-party-only analytics, no third-party data sharing
  · Quarterly log purge with approximate timeframe stated
  · Commits to independently objecting to overbroad government requests

── LINKS ─────────────────────────────────────────
TOSDR:              https://tosdr.org/en/service/7069 (registered, unreviewed)
Open Terms Archive: Not tracked
Policy source:      https://amanahuja.me/privacy-policy/
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Bottom line: This is a well-intentioned, minimal personal site policy. The
only genuine flag is the unconstrained terms-change clause, which is
low-risk here given how little data is collected. For a personal
informational site, this policy is well above average.
{{< /preformat >}}


If you're curious what it would do if I selected the "enhanced" option for a very
privacy-conscious review, try it out! I'll put the summary here: 

{{< preformat >}}
Result: 7 Green, 4 Yellow and 1 RED rating, using a very privacy-conscious
review ("Enhanced").

Summary
amanahuja.me is a privacy-respecting personal website. The author has
deliberately chosen privacy-forward practices: self-hosted analytics, no
third-party sharing, IP anonymization, and a quarterly log purge. The
policy is grounded in established frameworks and the author invites
feedback.

The main gap is unilateral amendment rights — the policy can change without
notice. Before submitting contact information, it's worth a quick re-check.
There's also no formal data deletion right, though the contact page
suggests the author will honor removal requests.

For an Enhanced tier (you're considering submitting contact info): This is
a low-risk scenario. Your data won't be sold, shared, or tracked. It will
be retained on the author's own servers and disclosed to government only
under legal process, with the author committing to object to overbroad
requests. The main action item is to revisit the policy before you submit
anything sensitive.
{{< /preformat >}}

I have found this skill to be really useful to review privacy policies for
tools and apps and tech services, for comparing any product that has an
"online" component or requires signup. I also use it sometimes for those
emails that we are all constantly getting: "our privacy policy has
changed". 
