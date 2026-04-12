**Why We Celebrate Fire-fighters but Ignore Fire-proofers**

*The alert blares at 2 : 03 a.m. An engineer—half-awake, wholly adrenalised—grabs the phone. “Regulatory report SEV-1 failed SLA, please address immediately.” Within minutes a virtual war-room fills: directors on video, graphs bleeding crimson, ‘all-hands’ pings lighting up Slack or Teams. Three frantic hours later the report revives. Emoji applause cascades, and the on-call hero’s legend grows another notch.*

A corridor away, a quieter crew has been rewriting deploy scripts, chaos-testing edge cases, and tightening feature-flag rollouts. Their reward? Silence. Nothing caught fire, so nothing was noticed.

Why do we laud the midnight saviour yet starve the guardians of quiet? Daniel Kahneman and Amos Tversky predicted the bias half a century ago—and our tech cultures still dance to its tune.


### 90-Second Primer: Thinking Fast, Thinking Slow

Long before “AI bias” entered our vocabulary, psychologist Daniel Kahneman and his collaborator Amos Tversky were mapping the shortcuts every human brain takes. They argued that our minds run on **two intertwined engines**:

* **System 1** – lightning-fast, automatic, and emotional. It’s the snap-judge that makes you hit the brakes when brake lights flare, or reach for coffee without thinking.
* **System 2** – methodical, logical, and effortful. It’s the part that double-checks a spreadsheet or proofs a regex—brilliant, yet easily fatigued.

Because System 1 does most day-to-day driving, it leans on *heuristics*—mental rules of thumb. In their 1973 landmark paper on the **availability heuristic**, Kahneman and Tversky showed we instinctively judge probability by how *vividly* and *quickly* an example springs to mind. Sharks feel deadlier than falling coconuts, plane crashes loom larger than bathtub slips—despite statistics that say otherwise.

This insight underpins the entire book *Thinking, Fast and Slow* (and won Kahneman a Nobel Prize in economics). It explains why managers remember last quarter’s 3 a.m. outage but struggle to recall three uneventful months of perfect uptime. **System 1 stores drama; System 2 stores data—when it’s awake.**

Keep that tug-of-war handy as we turn to pagers, budgets, and engineering culture. In every section that follows, we’ll watch System 1 crown heroes in the glow of a burning dashboard while System 2 whispers, “Prevent the fire in the first place.”


### 1. Sirens, Spotlights and the Original Hero Engineer

*Grimy cobblestones, a crackling blaze, brass helmets flashing under gas lamps.* In the 1840s New York volunteers raced hose carts through Broadway while brass bands blared. Newspapers retold the exploits, and theatre crowds lionised “Mose the Fireboy,” modelled on real firefighter Mose Humphrey ([en.wikipedia.org][2]). Fighting flames was public spectacle; enforcing chimney sweeps or installing fire-proof walls was dull bureaucracy.

Digital outages reprise that nineteenth-century pageant. Tweets of blood-red dashboards spread faster than the fix. Drama is memorable, prevention invisible, so memory crowns the loudest story.


### 2. Memory’s Trick: We Trust What We Remember

Ask an engineering VP how often production “really explodes.” Their recollection leans on System 1 snapshots: that Friday-night API meltdown, last quarter’s Kubernetes loop. Quiet weeks blur. Kahneman’s availability heuristic shows why—we gauge likelihood by ease of recall. The more cinematic the incident, the larger it looms, even when raw metrics say otherwise.

Companies thus measure mean-time-to-recovery down to seconds yet treat “weeks without a page” as trivia. Over time the bias ossifies: budgets swell around incident response; prevention becomes nice-to-have.


### 3. Dollars and Drama: Why Budgets Chase Spectacle

Finance adores counts and columns. An on-call rota is easy math: people × hours × premium rate. Preventative work is subtler—its success is announced by nothing happening.

But the economics are brutal. In ITIC’s 2024 global survey, **41 % of large enterprises said a single hour of downtime now costs \$1 million–\$5 million** ([itic-corp.com][3], [itic-corp.com][4]). Those figures dwarf the overtime that fuels hero stories.

Yet spectacle rules spending. After the CrowdStrike update crash of July 2024—a flaw that paralysed banks, airlines and hospitals—LinkedIn feeds brimmed with war-stories and post-mortems ([linkedin.com][5]). Vendors doubled advertising on “rapid response” tooling, while investments in rigorous release gates barely budged. Drama, not probability, wrote the cheque.


### 4. The ROI of Silence: Money You Never Notice

Picture a dashboard that stays green for ninety straight days. Inspiring? Perhaps. Exciting? Hardly. Still, those placid pixels save fortunes. Amazon once calculated that every extra 100 ms of latency trims 1 % from revenue; an internal memo credited a single feature-flag framework with averting dozens of brownouts.

Google’s SRE handbook embeds this arithmetic in policy: burn your error-budget and feature launches freeze until reliability recovers ([sre.google][6]). Forrester’s 2024 *Total Economic Impact* series shows seven-figure returns from modest reliability projects—returns that flow precisely because no crisis captured headlines ([tei.forrester.com][7]).

Shopify even gamified the idea: “Reliability Credits” award teams for zero-incident streaks, redeemable for hack-time or conference allowances. The prize? Prestige for making nothing happen.


### 5. The Human Toll: A Night in the Life

Maya’s phone buzzes—Slack or Teams, take your pick. She’s on-call again. Twenty sleepy minutes later her toddler wakes, startled by hallway light. Cortisol spikes, code quality sinks the next day. Catchpoint’s 2025 SRE survey lists burnout—not pay—as the top reason engineers consider quitting ([catchpoint.com][8]).

Hero narratives worsen the load. “Real ownership means you’re always on,” a staff engineer once joked—half joke, half expectation. Meanwhile prevention teams, enjoying saner shifts, struggle for recognition. The bias is more than economic; it shapes who stays in tech and who ghost-quits for calmer pastures.


### 6. Cultures that Pay Prevention First

Quick confession: I used to worship the fire-fight. Pager duty felt like valor, deployment freezes like red tape. Then a three-day incident left half my team sick and the other half sending résumés. We rewrote our rituals. Here’s what worked:

*Surface the invisible.* A weekly “Boring Changelog” email now celebrates silent saves: a chaos-test catch, a rollback script sharpened, a flaky test slain.

*Tie money to silence.* If overtime rewards firefighting, bonus pools should honour quarters without pages.

*Freeze on failure.* Google’s error-budget halt is blunt but fair—ship new features only after reliability debts are repaid.

*Rewrite the story.* Atlassian’s engineering all-hands open with “Silence Slides” listing high-risk services that logged zero pages, spotlighting the engineers behind that quiet.

Narratives sculpt memory; memory sculpts budgets. Teach System 1 to cheer for green dashboards, not just flaming ones.


### 7. Call to Action

1. **Celebrate prevention publicly.** Mention quiet wins at all-hands with the same gusto reserved for Sev-1 takedowns.
2. **Budget by statistics, not stories.** Use outside-view baselines—industry downtime cost, actuarial risk—to fund resilience.
3. **Audit cultural signals.** Swag and promotions should mirror error-budget burn-down, not chat-thread heroics.
4. **Measure burnout honestly.** Pair incident counts with pulse surveys; the stress you *don’t* remember is still real.
5. **Institutionalise boring glory.** Make the absence of catastrophe a named, celebrated metric.

Fire-fighters will always deserve gratitude. But the future worth coding belongs to engineers who make the sirens unnecessary.


### References & Further Reading

1. Tversky, A., & Kahneman, D. (1973). *Availability: A heuristic for judging frequency and probability.* *Cognitive Psychology*, 5, 207-232. ([sciencedirect.com][1])
2. Information Technology Intelligence Consulting. (2024). *Hourly Cost of Downtime Report.* ([itic-corp.com][3], [itic-corp.com][4])
3. Google SRE Workbook. “Error Budget Policy for Service Reliability.” Accessed June 28 2025. ([sre.google][6])
4. Catchpoint. (2025). *Annual SRE Survey – Call for Participants* (blog notes rising burnout concerns). ([catchpoint.com][8])
5. Mose Humphrey. Wikipedia entry. Accessed June 28 2025. ([en.wikipedia.org][2])
6. Forrester Consulting. (2024). *Total Economic Impact™ Study – Device Reliability & Downtime Savings.* ([tei.forrester.com][7])
7. Tripathi, V. (2024). “Case Study: The CrowdStrike Outage.” *LinkedIn*, July 21 2024. ([linkedin.com][5])

[1]: https://www.sciencedirect.com/science/article/pii/0010028573900339?utm_source=chatgpt.com "Availability: A heuristic for judging frequency and probability"
[2]: https://en.wikipedia.org/wiki/Mose_Humphrey?utm_source=chatgpt.com "Mose Humphrey - Wikipedia"
[3]: https://itic-corp.com/itic-2024-hourly-cost-of-downtime-report/?utm_source=chatgpt.com "ITIC 2024 Hourly Cost of Downtime Report Part 1"
[4]: https://itic-corp.com/itic-reports-surveys/?utm_source=chatgpt.com "ITIC Reports & Survey Results"
[5]: https://www.linkedin.com/pulse/case-study-crowdstrike-outage-vishal-tripathi-zdfbc?utm_source=chatgpt.com "Case Study : The CrowdStrike Outage - LinkedIn"
[6]: https://sre.google/workbook/error-budget-policy/?utm_source=chatgpt.com "Error Budget Policy for Service Reliability - Google SRE"
[7]: https://tei.forrester.com/go/dell/device-reliability/?utm_source=chatgpt.com "The Total Economic Impact™ Of Dell Latitude And OptiPlex Devices"
[8]: https://www.catchpoint.com/blog/calling-ops-eng-practitioners-take-our-annual-sre-survey?utm_source=chatgpt.com "Calling ops & eng practitioners: Take our annual SRE Survey"
