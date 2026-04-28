# The Rewrite Temptation - When to Modernize, When to Migrate, When to Leave It Alone

*July 27, 2025*

## Executive Summary

Big rewrites seduce smart teams. Clean slate, better architecture, no more hacks. But history is blunt: the "big bang" often overruns, under-delivers, and lands you with **two** broken systems instead of one. This article offers a practical decision playbook for enterprise technologists: when to **modernize in place**, when to **migrate** (rehost/replatform/repurchase/refactor), and when to **leave it alone** (stabilize, ring-fence, and plan the exit). You'll get a scoreboard of signals, a risk budget you can explain to risk partners, and tactics to create momentum **without** betting the bank.

---

## The Pull of a Clean Slate

There's a particular thrill to a rewrite. You can correct yesterday's compromises, sweep away tech debt, and design the system you would have built if you knew everything you know today. The danger is equally familiar: the world doesn't pause while you rebuild. Feature requests keep coming. Regulations shift. Incident queues still need clearing. You end up maintaining the old code **and** building the new—double the burn, double the coordination, and a moving goalpost.

Joel Spolsky's old warning—"never rewrite from scratch"—isn't an absolute law, but it's an important **bias correction**: rewrites fail for organizational reasons more than technical ones. The antidote is not dogma; it's a **disciplined triage** of options and a cadence that keeps value shipping while risk is retired.

---

## Three Doors, Not One: Modernize, Migrate, or Pause

Think in **portfolios**, not absolutes. For any given system, you usually choose among three doors:

### Door A - Modernize in place

Refactor hotspots, carve out seams, add tests, introduce APIs, improve observability, and gradually replace components. Use the **Strangler Fig** pattern to grow new capabilities around the old trunk until it's safe to cut over. This minimizes blast radius and lets you prove value in slices.

**Best when:** the system is stable enough to extend; business rules are poorly documented but encoded in the running system; you need continuous value delivery and cannot afford prolonged dual-run; or the core is written in a legacy language (COBOL, PL/I, Natural/Adabas, RPG, PowerBuilder, classic Perl) where *behavioral fidelity* matters more than cosmetic modernization.

### Door B - Migrate

Move the workload to a new platform or product with as-is functionality. Pick from the well-worn **R-strategies** (rehost, relocate, replatform, refactor/re-architect, repurchase, retire, retain). The point is **operational uplift first**, functional change later. This is often fastest to risk reduction when infrastructure or vendor end-of-life is forcing the issue.

**Best when:** the platform or vendor is the problem (capacity, supportability, cost), not the app's core behavior; you have clear cut-over windows and rollback plans; you can validate parity; or you face **skills scarcity** in legacy stacks and want to land on supported, talent-available platforms (managed cloud databases, container platforms, modern message buses) before refactoring.

### Door C - Leave it alone (for now)

Stabilize, instrument, and ring-fence. Restrict change; document the minimum; create a **decommission path** and contingency plan. Sometimes the bravest decision is to **not** touch a brittle, business-critical system while you lower surrounding complexity and build a safer bridge.

**Best when:** touching it is riskier than carrying it; usage is declining; a commercial or upstream replacement is imminent; imminent EOL timelines give you a bounded runway to plan; or the runtime is a legacy platform with **extinct skills** where any change increases operational risk—so you isolate, insure, and plan replacement externally.

---

## Legacy Languages, Vendor Traps, and the Translation Problem

Many enterprises run critical revenue paths on languages and platforms today's workforce barely knows. Think **COBOL/PL-I/Natural-Adabas/RPG**, fourth-gen tools, or ETL suites whose **business logic is trapped in visual graphs** (Informatica, Ab Initio, SSIS) and scheduler spaghetti. The challenge isn't only technical; it's *epistemic*: how to preserve decades of tacit rules while moving to modern runtimes.

### The real problem: behavioral fidelity

Rewrites stumble when teams chase "equivalent code" rather than **equivalent outcomes**. For legacy stacks, require a **semantic test harness**:

- A **golden corpus** of transactions, edge cases, and statements that must produce identical results.
- **Back-to-back testing**: old vs. new system run on the same inputs; compare outputs, side-effects, latency, and audit logs.
- **Metamorphic tests** for data transforms: invariants that must hold even when inputs are perturbed.

### Choosing a path

- **Modernize in place** when rules are opaque and encoded in running code or ETL graphs. Add **observers** (probes, logs, lineage) and carve seams; translate capability by capability.
- **Migrate-then-modernize** when the runtime or hardware is the burning platform. Land on supported managed services (e.g., mainframe offload/emulation, managed DBs, event streams) with behavior preserved; only then refactor for domain clarity.
- **Repurchase** when an industry platform now covers the capability with strong fit, compliance, and exit terms. Plan data migration and contract guardrails.

### Human-in-the-loop translation

Automated translators and GenAI **accelerate** but do not replace judgment. Set policy: **machine translates, humans own**. Require code reviews by bilingual SMEs, parity tests, and telemetry proving the new path is safer or faster before decommissioning.

### Data lineage and reconciliation

For data-heavy estates, build **end-to-end lineage** as you move—sources → transforms → sinks—plus **reconciliation jobs** that compare aggregates and critical fields (amounts, balances, statuses). Treat any unexplained delta as a release blocker.

### Talent strategy

Pair senior SMEs nearing retirement with modern engineers in **two-pizza squads**. Capture knowledge via executable specifications, example-based documentation, and recorded walkthroughs tied to the golden corpus. This creates continuity and audit-ready evidence.

---

## The Decision Scoreboard

Use a **scoreboard** rather than gut feel. Rank each criterion 1–5 (low→high). Doors with the strongest combined score win. Tie-break with risk and time.

*[image: The Decision Scoreboard]*

> **How to use it.** Calibrate the weights once with architecture, product, and risk partners. Keep the table in every steering pack; update quarterly. The visibility reduces "rewrite religion" and keeps decisions repeatable.

---

## Risk Budgeting That You Can Explain to Risk Partners

Large changes fail as **socio-technical** projects, not purely technical ones. Half of major change programs underperform or fail, and only about a third land as clear successes. Treat risk as a budget, not a binary. Allocate risk spend across five buckets and reduce each with concrete controls:

1. **Operational risk** - outages, degraded service, data loss. *Controls:* dark launches, parallel run, automated rollback, synthetic monitoring, chaos days.
2. **Information security & privacy** - new attack surface, configuration drift. *Controls:* NIST RMF-aligned control mapping, least-privilege defaults, threat modeling on every major epic.
3. **Regulatory & audit** - traceability, model risk for AI components, vendor due diligence. *Controls:* change records tied to DORA metrics, evidence packs, third-party attestations.
4. **Delivery risk** - schedule overrun, scope creep, people churn. *Controls:* thin slivers, walking skeletons, bound WIP, explicit exit criteria per milestone.
5. **Reputational risk** - customer impact, media attention. *Controls:* comms playbooks, customer credits policy, hypercare staffing.

Make the budget explicit: "We're buying down **operational** and **regulatory** risk first with a migrate-then-modernize path; functional refactors come after parity SLOs hold for 90 days."

---

## Evidence That Should Change Your Mind

A few facts are decision-shifting:

- **End-of-Support is a calendar, not an opinion.** Windows 10 reaches end of support on **October 14, 2025** (with ESU options extending security updates, and Microsoft 365 security updates continuing on Windows 10 through **October 10, 2028**). If you're sitting on large Windows 10 fleets or VDI images, that's a hard boundary for migration planning.
- **Big-bang migrations can be existential.** TSB's 2018 core platform migration outage triggered months of disruption and a **£48.65m** penalty from UK regulators; the CEO stepped down.
- **Tech debt is not a rounding error.** CIOs estimate tech debt equals **20–40%** of the value of the technology estate, and more than **20%** of new-build budgets can be siphoned to service it.
- **Delivery performance is measurable.** The **DORA** metrics (deployment frequency, lead time, change failure rate, mean time to restore) correlate with organizational performance. Use them to prove that modernization is paying off—or that a rewrite is quietly stalling delivery.
- **Software ages by interacting with its environment.** Lehman's Laws explain why evolving systems grow in complexity unless active work controls it. If the surrounding ecosystem is shifting fast, "leave it alone" is rarely stable for long.

---

## Patterns That De-Risk the Journey

### The Strangler Fig

Wrap the legacy core with a façade or API gateway. Route new traffic to new services, gradually replacing internals. Keep **seams**—places you can cut—visible. Plan for dual-write/dual-read periods with reconciliation tooling. Close the loop with parity tests.

### Compatibility shells and adapters

Create thin adapters that let old interfaces talk to new services (and vice versa). This buys you time to replace edge systems without touching the core immediately.

### Migrate-then-modernize

When infrastructure EOL or cost is the driver, keep functionality constant. **Rehost or replatform**, get SLOs green, then modernize in place with feature flags. This avoids coupling functional change to platform risk.

### Canary and shadow traffic

Ship small. Send a slice of real production traffic to the new path while the old handles the load. Compare results, error shapes, and latency distributions before full cutover.

### Walking skeletons and narrative demos

Stand up the end-to-end path early—thin and ugly is fine. Demo with a story: a real user, a real scenario, real telemetry. Momentum beats perfection.

### Back-to-back semantic test harness

Run legacy and target systems in parallel on curated corpora. Automate diffing of outputs, timings, and side-effects. Gate cutovers on **zero material variance** within declared tolerances and on sustained SLO health.

### Automated translation with human-in-the-loop

Use rule-based or GenAI translators to draft target-language code and mapping docs. Require SME sign-off, property-based tests, and observability hooks before promotion. Treat every translator as **untrusted** until proven with data.

### Data lineage & reconciliation jobs

Promote every major transform with reconciled totals and exception buckets. Track unresolved mismatches as first-class defects; do not hide them in ops queues.

---

## Case Notes (What We Learn from the Field)

### A costly lesson: big-bang core migration

A retail bank planned a weekend cutover to a new core. Customers woke up locked out of accounts; call centers melted; the incident spanned weeks. Regulators later fined the bank **£48.65m** for operational resilience failings. The post-mortem points to insufficient testing, poor governance, and optimism bias. **Lesson:** if a system is mission-critical and customer-facing, assume unknowns. Favor parallel run, staged cohort cutovers, and long canaries.

### Quiet wins: strangling a mainframe

An insurance carrier exposed policy and claims functions through a modern API layer, then replaced low-risk read paths first. Write paths followed with dual-write reconciliation and audit-friendly evidence. Customer portals improved without ever announcing "a rewrite." **Lesson:** your users care about outcomes. Replace nouns (capabilities), not adjectives (technologies).

### Migrate, then modernize

A payments processor faced database EOL and on-prem capacity limits. They replatformed to managed cloud services with **no** functional change, established SLOs, then started carving domains into event-driven services. Deployment frequency rose, change failure rate fell, and the modernization pace became a function of evidence—not aspiration. **Lesson:** treat platform risk as a separate backlog from functional ambition.

---

## A Playbook You Can Run Next Week

1. **Map the estate and the dates.** Inventory systems, dependencies, data flows, user cohorts—and the **hard dates** (EOL, contract, regulatory milestones). Put dates on a single wall chart.
2. **Harvest the rulebook and a golden corpus.** Capture representative inputs/outputs, edge cases, and financial totals. Record SME walkthroughs that explain *why* results look the way they do. This corpus becomes the truth set for back-to-back testing.
3. **Score each system.** Use the scoreboard table. Socialize it with product, risk, and operations. Decide the door—**A: modernize**, **B: migrate**, or **C: leave**—for each.
4. **Define the first shippable slice.** For Door A, pick a capability to strangle in 4–8 weeks. For Door B, define a smallest cohort to migrate with full rollback. For Door C, set guardrails, monitoring, and a decommission trigger.
5. **Stand up the semantic test harness.** Automate back-to-back runs, diffs, tolerances, and reports that auditors can consume.
6. **Instrument with DORA.** Baseline today. Commit to publish trendlines in every steering deck. Celebrate movement, not promises.
7. **Pre-commit to cut criteria.** If error budgets blow or schedule slips beyond X weeks without value, pause and reassess. Courage is a control.
8. **Narrate the journey.** Hold monthly narrative demos for stakeholders: story, metrics, surprises, next slice. Good narratives defuse rewrite fever—and build trust.

---

## Choose Boring Wins

Rewrites make for heroic stories. Enterprises are better served by **boring wins**: smaller surface area, faster feedback, measurable progress. Treat modernization as an operating habit, not a one-time event. Most importantly, insist on evidence. If the data says the new path isn't yet safer or faster, keep strangling, keep migrating in slices, or keep the guardrails tight and wait. The point isn't to rewrite—it's to reduce risk and increase flow.

---

### References & Further Reading

1. Spolsky, J. *Things You Should Never Do, Part I* (2000). A classic caution against full rewrites; useful as a bias-check, not dogma. [Things You Should Never Do, Part I – Joel on Software](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/)
2. Fowler, M. *Strangler Fig Application* (updated 2024). Canonical pattern for incremental legacy displacement; includes links to mainframe seam techniques. [Strangler Fig](https://martinfowler.com/bliki/StranglerFigApplication.html)
3. Lehman, M. M.; Belady, L. A. *Laws of Software Evolution* (1974 onward); and *On the Evolution of Lehman's Laws* (2013). Explains why systems accrue complexity and require active control. [plg.uwaterloo.ca/~migod/papers/2013/lehmanPaper.pdf](http://plg.uwaterloo.ca/~migod/papers/2013/lehmanPaper.pdf)
4. DORA. *The Four Keys Metrics.* Empirical link between delivery performance and outcomes. [DORA's software delivery metrics: the four keys](https://dora.dev/guides/dora-metrics-four-keys/)
5. McKinsey Digital. *Demystifying digital dark matter* (2022) and *Breaking technical debt's vicious cycle* (2023). Quantifies tech-debt drag (20–40% of estate value) and budget diversion (>20%). [A new standard to measure and tame technical debt | McKinsey](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/demystifying-digital-dark-matter-a-new-standard-to-tame-technical-debt) — [Tame tech debt to modernize your business | McKinsey](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/breaking-technical-debts-vicious-cycle-to-modernize-your-business)
6. AWS Prescriptive Guidance. *Migration strategies (the 7 Rs)* and *Design principles - Migration Lens*. Pragmatic guidance to choose R-types per workload. [Design principles - Migration Lens](https://docs.aws.amazon.com/wellarchitected/latest/migration-lens/well-architected-migration-design-principles.html)
7. Microsoft. *Windows 10 support ends on October 14, 2025*; *Lifecycle for Windows 10 22H2*; and Microsoft 365 support dates (security updates to Oct 10, 2028). Concrete EOL anchors for planning. [Windows 10 end of support and Microsoft 365 Apps | Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365-apps/end-of-support/windows-10-support)
8. FCA & PRA. *TSB fined £48.65m for operational resilience failings* (2022). A regulatory case study on migration risk. [TSB fined £48.65m for operational resilience failings | FCA](https://www.fca.org.uk/news/press-releases/tsb-fined-48m-operational-resilience-failings)
9. Gartner (via Organizational Change Management insights). Only **34%** of major changes are clear successes; half fail—important backdrop for big-bang caution. [Organizational Change Management | Gartner](https://www.gartner.com/en/human-resources/insights/organizational-change-management)
10. Thoughtworks. *Embracing the Strangler Fig pattern for legacy modernization*. Practical benefits and pitfalls in real programs. [Embracing the Strangler Fig pattern for legacy modernization | Thoughtworks](https://www.thoughtworks.com/en-us/insights/articles/embracing-strangler-fig-pattern-legacy-modernization-part-one)
