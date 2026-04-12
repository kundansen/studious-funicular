# Concept Ledger

## Status: COMPLETE

---

## LEDGER TABLE

| # | Concept Name | Layer | Game(s) | Modern Equivalent | Evidence | Sources | Notes |
|---|---|---|---|---|---|---|---|
| 1 | GG (Good Game) | Language | StarCraft (1998), Quake (1996) | Slack sign-offs, post-mortem closings | cultural + primary | [Wikipedia Glossary](https://en.wikipedia.org/wiki/Glossary_of_video_game_terms) | Variations: GGWP, GGEZ. Now signals "inevitable conclusion" |
| 2 | Noob/Newbie | Language | EverQuest (1999), Quake (1996) | "Junior dev," onboarding language | cultural | [Wikipedia Glossary](https://en.wikipedia.org/wiki/Glossary_of_video_game_terms) | Nuanced: "newbie" neutral, "noob" pejorative |
| 3 | Frag | Language | Doom (1993), Quake (1996) | "Kill count" metrics, eliminating tasks | cultural + primary | [Wikipedia Glossary](https://en.wikipedia.org/wiki/Glossary_of_video_game_terms) | Military origin (fragmentation grenade), adopted by Doom community |
| 4 | Nerf/Buff | Language | Ultima Online (1997), EverQuest (1999) | Feature rollbacks, API deprecation, capability changes | cultural + academic | [Wikipedia](https://en.wikipedia.org/wiki/Glossary_of_video_game_terms), [Bemowski 2017](https://www.researchgate.net/) | From Nerf toys (soft, harmless). Buff is opposite |
| 5 | Camping | Language | Counter-Strike (2000), Quake (1996) | Lurking in Slack, passive monitoring | cultural | [Wikipedia Glossary](https://en.wikipedia.org/wiki/Glossary_of_video_game_terms), [GeniusCrate Blog](https://www.geniuscrate.com) | Tactical patience strategy |
| 6 | Smurfing | Language | Warcraft II (1996) | Alt accounts, anonymous testing | primary + cultural | [StackExchange](https://english.stackexchange.com/questions/17209/where-does-the-term-smurfing-come-from), [Battle.net Glossary](https://battle.net) | Origin: Shlonglor and Warp! created "PapaSmurf"/"Smurfette" accounts (1996) |
| 7 | Respawn | Language | Doom (1993), Quake (1996) | Container restarts, service recovery | common knowledge | [Wikipedia Glossary](https://en.wikipedia.org/wiki/Glossary_of_video_game_terms) | Ubiquitous in DevOps language |
| 8 | Grinding | Language | Diablo II (2000), EverQuest (1999) | Repetitive work, ticket queues | academic + cultural | [Bemowski 2017](https://www.researchgate.net/), [Wikipedia](https://en.wikipedia.org) | Academic linguistics paper documents term |
| 9 | Shareware Distribution | Systems | Doom (1993) | Freemium, open core, free trials | primary + academic | [Digital Antiquarian](https://www.filfre.net/2020/04/narratives-of-doom-part-1/), [Wikipedia id Software](https://en.wikipedia.org/wiki/Id_Software) | Episode 1 free, Episodes 2-3 paid. 2-3M shareware copies sold |
| 10 | WAD/Engine-Content Separation | Systems | Doom (1993) | Plugins, mods, user-generated content | primary + academic | [NVIDIA History of Mods](https://www.nvidia.com/en-us/geforce/), [ACM C&T 2019](https://dl.acm.org/) | WAD = "Where's All the Data". Carmack released format docs same day as game |
| 11 | WASD Control Scheme | Systems | Quake (1996), Quake II (1997) | Universal input standard, keyboard shortcuts | primary + cultural | [Wikipedia Dennis Fong](https://en.wikipedia.org/wiki/Dennis_Fong), [PC Gamer](https://www.pcgamer.com/how-wasd-became-the-standard-pc-control-scheme/) | Thresh won Ferrari at Red Annihilation 1997. Carmack coded config into Quake 2 |
| 12 | Client-Side Prediction | Systems | QuakeWorld (1996), Duke Nukem 3D (1996) | Optimistic UI, eventually consistent systems | primary + academic | [Wikipedia Client-side prediction](https://en.wikipedia.org/wiki/Client-side_prediction), [Fabien Sanglard](https://fabiensanglard.net/) | Duke3D had it first (Jan 1996). QuakeWorld (Dec 1996) made it famous |
| 13 | ELO-Style Ranking | Systems | StarCraft Battle.net (1998) | Tinder matchmaking, LLM benchmarks (LMSYS), FIFA rankings | academic | [Wikipedia Elo](https://en.wikipedia.org/wiki/Elo_rating_system), [Liquipedia](https://liquipedia.net/starcraft/) | Chess ELO (1960) adapted for competitive gaming |
| 14 | Demo/Replay Files | Systems | Doom (1993), StarCraft (1998) | Session replay (FullStory), audit logs, observability | primary + academic | [ViZDoom paper](https://arxiv.org/abs/1605.02097), Game histories | .lmp (Doom), .dem (Quake), .rep (StarCraft) |
| 15 | Digicel Animation Pipeline | Systems | Aladdin (1993, Sega Genesis) | Digital asset pipelines, content delivery optimization | primary | [Sega-16](https://www.sega-16.com/2006/05/behind-the-design-disneys-aladdin/), [Wikipedia Aladdin](https://en.wikipedia.org/wiki/Disney%27s_Aladdin_(video_game)) | 1,400 hand-drawn frames digitized. $1-1.5M budget (4x average). Holds, loops, X-flipping, palette cycling |
| 16 | Fog of War | AI | StarCraft (1998), Age of Empires II (1999) | Partial Observable MDP (POMDP), hidden state estimation | academic | [DefogGAN AAAI 2020](https://ojs.aaai.org/), [Machinations Glossary](https://machinations.io) | Formal AI equivalent. DefogGAN uses GANs to predict hidden positions |
| 17 | ViZDoom Research Platform | AI | Doom (1993) -> ViZDoom (2016) | Visual RL benchmarks, 3D environment testing | academic | [arXiv:1605.02097](https://arxiv.org/abs/1605.02097), [vizdoom.cs.put.edu.pl](http://vizdoom.cs.put.edu.pl/) | 666+ citations. Farama Foundation (2022). First-person 3D visual RL benchmark |
| 18 | Pathfinding / Navigation | AI | Quake III Arena (1999), StarCraft (1998) | A* routing, robot navigation, game AI | academic + primary | [Trenholme & Smith 2008](https://www.researchgate.net/), [id Tech 3](https://en.wikipedia.org/wiki/Id_Tech_3) | Quake III bots used in VR/simulation research |
| 19 | Wait-and-Watch Tactic | AI | Half-Life (1998) | Observation as action, agent strategic patience | primary + academic | [TWHL Wiki](https://twhl.info/wiki/page/Monsters_Programming_-_The_Concepts_of_Half-Life%27s_AI), Reddit r/HalfLife | Trigger room, hide, let factions fight, clean up. Emergent behavior from AI system |
| 20 | Scripted vs Learned Behavior | AI | Half-Life (1998), F.E.A.R. (2005) | Rule-based vs ML agents, hybrid AI | academic + primary | [TWHL AI docs](https://twhl.info/), [Arcen Games](https://www.arcengames.com/) | Half-Life: schedules/tasks. F.E.A.R.: GOAP. Modern: hybrid approaches |
| 21 | StarCraft as AI Benchmark | AI | StarCraft: Brood War (1998) | RL testbeds, LLM agent evaluation | academic | [arXiv:2312.11865](https://arxiv.org/abs/2312.11865), [DeepMind AlphaStar](https://deepmind.com/blog/article/alphastar-mastering-real-time-strategy-game-starcraft-ii) | 30,000+ pro replays. AlphaStar (2019). PySC2, TextStarCraft II |

---

## Narrative Arc Summary

The legacy of 1990s games unfolds in three layers that build on each other. First, **language**: millions of strangers needed shorthand to coordinate in real-time combat, so they invented terms like "GG," "frag," and "nerf" that compressed complex social signals into keystrokes - vocabulary that now echoes through Slack channels and incident retros. Second, **systems**: game developers pioneered distribution models (shareware), extensibility patterns (WAD files), input standards (WASD), and responsiveness tricks (client-side prediction) that became blueprints for modern software architecture, from freemium SaaS to optimistic UI updates. Third, **AI**: game environments became the proving grounds for machine learning, with fog of war formalizing partial observability, StarCraft replays training agents, Doom becoming ViZDoom, and Half-Life's emergent "wait-and-watch" tactic prefiguring the idea that observation itself is an action. The arc is this: games first taught humans how to coordinate at scale, then taught software how to be extensible and responsive, and finally taught machines how to learn from worlds that don't reveal everything at once.

---

## Next Step
Proceed to STEP 3 - Review 04_CITATIONS_PACK.md, then STEP 4 - Build 05_BLOG_OUTLINE.md
