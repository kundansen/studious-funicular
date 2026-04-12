# Blog Outline

## Status: COMPLETE

---

## TITLE

**Final:** Spawn Points

---

## INTRO (180-250 words)

**Opening Scene:** 2am incident channel. Production is down. After 47 minutes of debugging, someone finds the issue - a misconfigured cache that kept respawning zombie connections. The fix goes out. The site recovers. In Slack, someone types two letters: "GG."

**Bridge:** Nobody explains what GG means. Nobody needs to. But pause on it: that phrase traveled from South Korean StarCraft tournaments in the late 1990s to a San Francisco incident channel in 2026. It's not alone.

**Preview:** Gaming vocabulary saturates modern tech culture, but the influence runs deeper than slang. The games of the 1990s pioneered distribution models we now call freemium, introduced extensibility patterns that became plugin architectures, and created environments that researchers still use to train AI agents today.

**Arc statement:** This is about three layers: the language we inherited, the systems we copied, and the AI research we're still running on 30-year-old game engines.

---

## SECTION 1: LANGUAGE

### 1.1 "GG" as compressed sportsmanship (StarCraft, 1998; Quake, 1996)
- Two letters encoding concession, respect, and closure
- South Korean pro scene formalized it
- Now: Slack sign-offs, post-mortems, acknowledging a lost argument
- ~150 words

### 1.2 "Noob" as onboarding vocabulary (EverQuest, 1999; Doom, 1993)
- Distinction between "newbie" (neutral) and "noob" (pejorative)
- Created a gradient for skill assessment among strangers
- Now: "Junior dev," onboarding friction, expertise signaling
- ~120 words

### 1.3 "Nerf" and "Buff" as product vocabulary (Ultima Online, 1997; EverQuest, 1999)
- Origin: Nerf toys (soft, harmless) - weapon felt like a Nerf gun after patch
- Balance patches as early A/B testing
- Now: feature flags, capability changes, API deprecation language
- ~150 words

### 1.4 "Frag" as task elimination (Doom, 1993; Quake, 1996)
- Military origin (fragmentation grenade) adopted by FPS community
- Kill counts as primitive metrics
- Now: ticket resolution, task completion language
- ~100 words

### 1.5 "Respawn" as service recovery (Doom, 1993)
- Enemies reappearing, players regenerating
- Now: container restarts, service recovery, "the pod respawned"
- Ubiquitous in DevOps vocabulary
- ~100 words

### 1.6 "Camping" as strategic patience (Counter-Strike, 2000; Quake, 1996)
- Controversial tactic: waiting in one spot for prey
- Created vocabulary for passive-aggressive coordination
- Now: lurking in Slack, watching a thread, passive monitoring
- ~120 words

### 1.7 "Smurfing" as identity concealment (Warcraft II, 1996)
- Origin story: Shlonglor and Warp! created PapaSmurf/Smurfette accounts
- Good players hiding from those who avoided them
- Now: alt accounts, anonymous testing, sock puppets
- ~130 words

**Section word count target:** ~870 words

---

## SECTION 2: SYSTEMS

### 2.1 Shareware as the freemium ancestor (Doom, 1993)
- Episode 1 free, Episodes 2-3 paid ($9 + $9)
- 2-3 million shareware copies distributed
- BBS distribution, disk copying encouraged
- Now: free tiers, open core, trial versions
- ~180 words

### 2.2 WAD files as plugin architecture (Doom, 1993)
- "Where's All the Data" - engine/content separation
- Carmack released WAD format docs same day as game
- Led to level editors, total conversions, professional careers
- Now: modular architecture, user-generated content, extension markets
- ~180 words

### 2.3 WASD as input standardization (Quake, 1996)
- Dennis "Thresh" Fong's setup: WASD + mouse aim
- Won Ferrari at Red Annihilation 1997
- Carmack coded Thresh's config into Quake 2 as default
- Now: de facto standard, keyboard shortcuts, muscle memory
- ~150 words

### 2.4 Client-side prediction as optimistic UI (QuakeWorld, 1996)
- Modem latency problem: 300+ ms made Quake unplayable
- Carmack's solution: client guesses results, server corrects later
- Duke Nukem 3D actually had it first (Jan 1996)
- Now: optimistic updates, eventually consistent systems
- ~180 words

### 2.5 ELO ranking as competitive matchmaking (StarCraft Battle.net, 1998)
- Chess ELO system (1960) adapted for games
- Leagues and ladders as product features
- Now: Tinder matchmaking, LLM benchmarks (LMSYS), FIFA rankings
- ~150 words

### 2.6 Demo files as observability (Doom, 1993; StarCraft, 1998)
- .lmp, .dem, .rep files captured entire sessions
- Enabled replay analysis, proof of skill, training data
- Now: session replay (FullStory), audit logs, observability pipelines
- ~140 words

### 2.7 Digicel animation as asset pipeline (Aladdin, 1993)
- Disney animators produced 1,400 hand-drawn frames
- Digitized for Sega Genesis with holds, loops, palette cycling
- $1-1.5 million budget (4x average) for unprecedented fidelity
- Now: digital asset pipelines, content delivery optimization
- ~150 words

**Section word count target:** ~1,130 words

---

## SECTION 3: AI

### 3.1 Fog of war as partial observability (StarCraft, 1998; Age of Empires II, 1999)
- Map hidden until explored, enemy movements concealed
- Formal equivalent: Partially Observable Markov Decision Process (POMDP)
- DefogGAN (2020): GANs predicting hidden enemy positions
- ~170 words

### 3.2 ViZDoom as visual reinforcement learning benchmark (Doom, 1993 -> 2016)
- 2016: Researchers built ViZDoom for 3D visual RL
- First-person environments vs 2D Atari benchmarks
- 666+ academic citations, Farama Foundation maintenance
- ~150 words

### 3.3 Pathfinding as autonomous navigation (Quake III Arena, 1999)
- A* algorithm, bot navigation, collision avoidance
- id Tech 3 engine used for VR/simulation research
- Now: robot navigation, autonomous systems
- ~130 words

### 3.4 Wait-and-watch as observation action (Half-Life, 1998)
- Emergent tactic: trigger aliens vs marines, hide, let them fight, clean up survivors
- AI used condition bits, schedules, faction awareness
- Profound insight: doing nothing is sometimes the optimal action
- Connect to modern agents: observation as strategic action
- ~200 words

### 3.5 Scripted vs learned behavior (Half-Life, 1998; F.E.A.R., 2005)
- Half-Life: schedules and tasks (rule-based)
- F.E.A.R.: Goal-Oriented Action Planning (GOAP)
- Modern debate: rule-based vs ML agents, hybrid approaches
- ~150 words

### 3.6 StarCraft as strategic AI benchmark (StarCraft: Brood War, 1998)
- 30,000+ professional replays available
- AlphaStar (2019) defeated top human players
- Challenges: partial observability, long-horizon planning, real-time decisions
- TextStarCraft II: LLM agents in RTS environments
- ~180 words

### 3.7 Text adventures as reasoning benchmarks (Zork, 1980; Hitchhiker's Guide, 1984)
- Not technically 90s, but foundational
- TextQuests (2024): 25 Infocom games as LLM benchmark
- Quadrillions of text inputs vs hundreds of video game actions
- Tests reasoning without visual processing
- ~130 words

**Section word count target:** ~1,110 words

---

## CONCLUSION (200-300 words)

**Callback:** Return to the 2am incident channel. The engineer who typed "GG" probably doesn't know they're quoting South Korean esports. The SRE watching containers respawn probably hasn't thought about Doom. The ML researcher running experiments on ViZDoom might not have played the 1993 original.

**Arc synthesis:** These three layers - language, systems, AI - tell a single story. First, millions of strangers needed shorthand to coordinate in real-time combat, so they compressed social signals into keystrokes. Then developers needed distribution models and extensibility patterns, so they invented shareware and WAD files. Finally, researchers needed environments to train agents, and the games were already there - complex, adversarial, partially observable worlds where machines could learn.

**Observation:** Games were testbeds before we knew we needed testbeds. They were distributed systems before we had the vocabulary for distributed systems. They taught humans to coordinate across networks, then taught software to be modular and responsive, and finally taught machines to navigate uncertainty.

**Closing thought:** The next time someone types "GG" in your incident channel, or you watch a container respawn, or you see an RL benchmark running on a 30-year-old game engine - you're not seeing nostalgia. You're seeing the infrastructure that made modern tech possible, still running, still teaching.

**Target:** ~280 words

---

## TOTAL WORD COUNT TARGETS

- Intro: ~220 words
- Language: ~870 words
- Systems: ~1,130 words
- AI: ~1,110 words
- Conclusion: ~280 words
- **Total: ~3,610 words** (within 3,000-4,500 target)

---

## CHECKLIST BEFORE WRITING

- [x] Aladdin 1993 included (Section 2.7)
- [x] Half-Life wait-and-watch included (Section 3.4)
- [x] Academic sources available for each section
- [x] Acronyms will be expanded (WASD, ELO, POMDP, GAN, RL, etc.)
- [x] No em dashes, semicolons, or horizontal dividers planned
- [x] Varied H3 openings planned
