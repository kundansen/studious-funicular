# Research Notes

## Status: COMPLETE
All major research gathered. Ready for Concept Ledger construction.

---

## LANGUAGE LAYER RESEARCH

### GG (Good Game)
- Wikipedia Glossary: "Abbreviation meaning 'good game'. Typically exchanged as parting words at the end of a competitive game or match as a gesture of good sportsmanship."
- Variations: GGWP (good game, well played), GGEZ (taunting)
- Used to denote inevitable victory situations
- Source: https://en.wikipedia.org/wiki/Glossary_of_video_game_terms

### Noob/Newbie
- Someone new to the game, generally used as pejorative (light-hearted)
- Distinguished from "noob" which is more pejorative
- Source: Wikipedia Glossary

### Frag
- "To kill or achieve a kill in a game against a player or non-player opponent"
- Military origin (fragmentation grenade), adopted by Doom community
- Source: Wikipedia Glossary

### Nerf/Buff
- Nerf: "A change intended to weaken a particular item, tactic, ability, or character"
- Buff: Opposite of nerf, strengthening
- Origin: Nerf toys (soft, harmless) - comparing weapons to Nerf guns
- Popularized in MMOs like Ultima Online, EverQuest
- Source: Wikipedia, Reddit r/gaming

### Camping
- Hiding in a location to ambush opponents
- Tactical patience strategy
- Used in Call of Duty, Counter-Strike, etc.
- Source: GeniusCrate Blog

### Smurfing
- Origin: Warcraft II (1996) players Shlonglor and Warp! created accounts "PapaSmurf" and "Smurfette" to hide from players who avoided them
- Definition: Good/famous players using fake names to beat unsuspecting players
- From StackExchange with extensive Usenet archaeology:
  - First documented use: alt.games.warcraft August 1996
  - Battle.net Warcraft II Glossary confirms origin
- Quote from Shlonglor (2003): "I was the originator of the term 'Smurf' or 'Smurfing'"
- Source: https://english.stackexchange.com/questions/17209/where-does-the-term-smurfing-come-from

### Respawn
- Entity reappearing after death
- Now used for service restarts, container recovery
- Source: Wikipedia Glossary

### Grinding
- Repetitive actions to earn experience points
- Source: Bemowski 2017 academic paper

---

## SYSTEMS LAYER RESEARCH

### Shareware Distribution
- Doom (1993) pioneered modern shareware: Episode 1 free, Episodes 2-3 paid
- id Software released WAD format docs same day as game
- John Carmack: Separated level data from game engine intentionally
- Doom sold 2-3 million shareware copies
- Modern equivalent: Freemium, open core, free trials
- Source: Digital Antiquarian "The Shareware Scene, Part 5: Narratives of DOOM"
- Source: Wikipedia id Software

### WAD Files and Modding
- WAD = "Where's All the Data" (trivia name from NVIDIA article)
- Engine/content separation enabled legal mod distribution
- Carmack "released documentation of the WAD format on the same day id released the game itself"
- Led to level editors, total conversions, professional careers (Tim Willits)
- Source: NVIDIA History of PC Game Mods
- Source: ACM C&T 2019 "Malleable Games" literature review

### WASD Control Scheme
- Dennis "Thresh" Fong popularized WASD + mouse aim in Quake tournaments
- Won Ferrari in Red Annihilation 1997 tournament using this setup
- John Carmack programmed Thresh's configuration into Quake 2
- Before: Arrow keys were standard
- Source: Wikipedia Dennis Fong
- Source: PC Gamer "How WASD became the standard PC control scheme"

### Client-Side Prediction / QuakeWorld
- Quake (1996) had poor netcode for modem users (300+ ms latency)
- Carmack rewrote entire netcode for QuakeWorld (Dec 1996)
- "I am now allowing the client to guess at the results of the users movement until the authoritative response from the server comes through"
- Enabled rocket jumping over network
- Duke Nukem 3D actually had client-side prediction first (Jan 1996)
- Modern equivalent: Optimistic UI, eventually consistent systems
- Source: Wikipedia Client-side prediction
- Source: Fabien Sanglard Quake Source Analysis
- Source: QuakeWorld Wiki history

### ELO-Style Ranking
- Chess ELO system (1960) adopted by games
- StarCraft Battle.net leagues, Counter-Strike ranks
- Now used in: Tinder matchmaking, LLM benchmarks (LMSYS), FIFA rankings
- Source: Wikipedia Elo Rating System
- Source: Liquipedia StarCraft Battle.net Leagues

### Demo/Replay Files
- Doom introduced .lmp demo files
- Quake had .dem files
- StarCraft replays critical for esports, AI training
- Modern: Session replay (FullStory), audit logs, observability
- Source: Multiple game histories

### Aladdin (1993) Digicel Pipeline
- Virgin Games + Disney + Sega collaboration
- "Digicel" process: digitizing hand-drawn animation for games
- Disney animators produced 1,400 hand-drawn frames
- Techniques: holds, loops, X-flipping, palette cycling to fit Genesis constraints
- $1-1.5 million development cost (4x average at time)
- Sold 4+ million copies
- Source: Sega-16 "Behind the Design: Disney's Aladdin"
- Source: Wikipedia Aladdin Sega Genesis

---

## AI LAYER RESEARCH

### Fog of War
- RTS game mechanic concealing unexplored areas
- Formal equivalent: Partially Observable Markov Decision Process (POMDP)
- StarCraft fog of war = major AI challenge
- DefogGAN (AAAI 2020): Using GANs to predict hidden enemy positions
- Source: DefogGAN paper (Samsung SDS)
- Source: Machinations Glossary

### ViZDoom Research Platform
- 2016: Doom-based AI research platform for visual RL
- First-person 3D visual RL benchmark (vs 2D Atari)
- 666+ academic citations
- Farama Foundation (2022)
- Tests: navigation, shooting, mazes
- Source: arXiv:1605.02097 (Kempka et al.)
- Source: vizdoom.cs.put.edu.pl

### Pathfinding and Navigation
- A* algorithm used in games like StarCraft, RTS games
- Quake III Arena bots used for AI research
- id Tech 3 engine widely used for VR/simulation research
- Source: Trenholme & Smith 2008 (ResearchGate)
- Source: Lindenwood AI in Games blog

### Half-Life AI and Wait-and-Watch Tactic
- Half-Life (1998) had sophisticated AI: squads, flanking, suppression
- Marines vs aliens faction infighting: "bits_COND_SEE_HATE" conditions
- Emergent tactic: Trigger room, hide, let factions fight, clean up survivors
- AI uses: condition bits, memory bits, schedules, tasks
- Connection to modern agent behavior: Observation as an action
- Source: TWHL Wiki "Monsters Programming - The Concepts of Half-Life's AI"
- Source: Reddit r/HalfLife discussions

### Scripted vs Learned Behavior
- Half-Life marines used "schedule" and "task" system
- F.E.A.R. (2005) used GOAP (Goal-Oriented Action Planning)
- Modern: Rule-based vs ML agents, hybrid approaches
- AI War: Fleet Command used emergent swarm AI
- Source: Arcen Games "Designing Emergent AI" series
- Source: TWHL AI documentation

### StarCraft as AI Benchmark
- StarCraft Brood War: 30,000+ professional replays available
- AlphaStar (DeepMind 2019): Defeated top pros
- PySC2: Python StarCraft II learning environment
- TextStarCraft II: LLM agent interface
- Challenges: partial observability, long-horizon planning, real-time
- Source: arXiv:2312.11865 (LLMs Play StarCraft II)
- Source: DeepMind AlphaStar

### Text Games as AI Benchmarks
- Zork, Colossal Cave Adventure (1970s-80s)
- TextQuests (2024): 25 Infocom games as LLM benchmark
- Tests reasoning without visual processing
- Quadrillions of possible text inputs vs hundreds of video game actions
- Source: IBM Think article on TextQuests

---

## KEY ACADEMIC SOURCES FOUND

1. Kempka et al. (2016) - ViZDoom paper, arXiv:1605.02097
2. Jeong et al. (2020) - DefogGAN, AAAI 2020
3. Thiel & Lyle (2019) - Game modding literature review, ACM C&T
4. Bemowski (2017) - Gaming terminology linguistics
5. Ma et al. (2023) - LLMs Play StarCraft II, arXiv
6. Bernier (2001) - Valve latency compensation (GDC/academic)
7. Gilmour et al. (2021) - Partial observability in games, Naval Research Lab
8. Khan & Aqeel (2025) - ViZDoom RL benchmarking

---

## NEXT STEP
Proceed to 03_CONCEPT_LEDGER.md to build the formal ledger table from this research.
