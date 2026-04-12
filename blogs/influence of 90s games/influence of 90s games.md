# Spawn Points: What 90s Games Left Behind in Modern Tech

This week I had a few completely unrelated conversations that all happened to reference artifacts from the video gaming world of the 1990s. Someone mentioned "nerfing" a feature. Someone else talked about a service that kept "respawning." A third conversation touched on why certain AI benchmarks still run on decades-old game engines.

The 1990s is when I started playing games, so these references land differently for me. But it made me wonder how many of these cultural influences from the early days of gaming are still out there, if I stumbled across three examples in a random week.

There's no better time than now to research any random topic. Half a day of deep research, and this blog was the result.

The vocabulary of modern tech still carries fingerprints from 90s multiplayer games. We talk about nerfing features and buffing metrics. We watch containers respawn. These are compressed protocols that millions of strangers developed to coordinate under pressure, and they work just as well in corporate Teams.

The influence runs deeper than slang. The games of the 1990s stress-tested distribution models, extensibility patterns, and latency-handling techniques that later became standard practice in software. They also created environments that researchers still use to train artificial intelligence (AI) agents today.

I am arguing that 90s games popularized a set of ideas by distributing them at massive scale, then stress-testing them in public until the patterns were production-ready. The inheritance shows up in three layers: the words we still use, the systems we still copy, and the AI research we're still running on 30-year-old game engines.

## Language

### "GG" as compressed sportsmanship (StarCraft, 1998; Quake, 1996)

Two letters are enough to concede a match, acknowledge your opponent's skill, and close out a game with dignity. "GG," short for "good game," became the handshake of online competition in the late 1990s, when typing was the only communication available and every keystroke cost time.

The term existed in earlier competitive communities, but South Korean StarCraft leagues are often credited with formalizing it as the proper way to resign. Typing "GG" before leaving a match signaled that you knew you had lost, that you respected the other player, and that you weren't going to waste everyone's time fighting an unwinnable battle. The absence of a GG became its own statement: a refusal to acknowledge defeat.

Today, GG shows up in incident channels, code reviews, and post-mortems. When a long debugging session finally ends, someone types "GG" and everyone understands that it was hard, it is over, and we made it through.

### "Noob" as onboarding vocabulary (EverQuest, 1999; Doom, 1993)

Early multiplayer games faced a problem: how do experienced players communicate about skill levels when they can't see each other? The answer was a gradient of terms, with "newbie" at the sympathetic end and "noob" at the contemptuous one.

A newbie is simply new. They haven't learned the mechanics yet, but they're trying. A noob, on the other hand, has been around long enough to know better but still makes rookie mistakes - or worse, refuses to learn. The distinction matters. Games like EverQuest had designated "newbie zones" where beginners could learn without getting destroyed, but calling someone a noob was a different message entirely.

This vocabulary persists in tech culture. We don't say "junior developer" with the same connotations, but the underlying gradient exists. There's a difference between someone who's new and learning versus someone who keeps making the same avoidable mistakes. The games gave us words for that spectrum.

### "Nerf" and "Buff" as product vocabulary (Ultima Online, 1997; EverQuest, 1999)

When the developers of Ultima Online weakened an overpowered sword in a patch, players said they had "nerfed" it - made it soft and harmless, like a Nerf toy. The opposite happened too: when a weak skill got strengthened, it was "buffed up." These terms spread through every online game community within a few years.

What makes nerf and buff interesting is that they describe the same thing companies do today when they adjust their products. When a feature flag gets rolled back because it's causing problems, that's a nerf. When a metric gets boosted through optimization, that's a buff. When an application programming interface (API) capability gets deprecated, someone made a nerfing decision.

Online games made iteration visible and culturally normal to millions of players. You release something, see how players exploit it, and adjust. Nerf the overpowered, buff the underpowered, repeat forever. Patch notes were a public, weekly lesson that releasing is not the end of a decision.

### "Respawn" as service recovery (Doom, 1993)

When you die in Doom, you respawn. You pop back into existence at a spawn point, ready to try again. When enemies are killed in certain modes, they respawn too - an endless cycle of death and regeneration that keeps the game going.

Today, "respawn" is operational vocabulary. "The pod respawned at 3:47 am" makes perfect sense to anyone who manages infrastructure. The concept is identical: something died, something brought it back, the system continues. Development and operations teams inherited this word so completely that most practitioners don't realize they're speaking gamer.

### "Smurfing" as identity concealment (Warcraft II, 1996)

In 1996, two highly skilled Warcraft II players named Shlonglor and Warp! had a problem: they were so good that other players on Battle.net refused to play against them. They created alternate accounts with the names "PapaSmurf" and "Smurfette" and started beating unsuspecting opponents who thought they were just playing some random new players.

The practice spread, and so did the name. "Smurfing" became the term for any skilled player hiding behind a fake identity to play against weaker opponents. The term jumped to other contexts: creating alt accounts for anonymous testing, sock puppet accounts in forums, any situation where someone conceals their real identity to gain an advantage. Shlonglor later confirmed he was the originator of the term - a rare case where we know exactly who coined a piece of internet slang.

Games didn't invent slang. Military jargon, sports terminology, and hacker culture all contributed vocabulary to tech. But games provided something those sources couldn't: a mass rehearsal space. Millions of strangers, coordinating under time pressure and anonymity, refined these terms through daily use. The words that survived were compressed, unambiguous, and fast to type. That selection pressure shaped a vocabulary now embedded in how tech teams communicate. The terms also carried a double edge, efficient for coordination but sometimes wielded for gatekeeping. "Noob" can orient a newcomer or push them out, depending on tone.

One reason this slang survived is that it works. Under pressure, teams reach for short, unambiguous signals that close the loop fast, whether that is "GG" after a match or a quick ritual after an incident.

Slang is the surface layer, and it points to something more consequential underneath. Games forced engineers to release networked software to millions of people, then survive the consequences.

## Systems

### Shareware as the freemium ancestor (Doom, 1993)

Before app stores and free trials, there was shareware. The model worked like this: you got the first chunk of the game at no cost, copied it onto floppy disks, gave it to friends, uploaded it to bulletin board systems. If you wanted the rest, you mailed a check to the developer.

id Software perfected this with Doom in 1993. Episode 1, "Knee-Deep in the Dead," was free to copy and distribute. The full registered version (all three episodes) cost around $40 by mail order. The strategy was deliberate: get the game onto as many computers as possible, let it sell itself, then convert a fraction of players into paying customers. Millions played the shareware version. A much smaller number paid for the full game, but that was still enough to make id Software wildly profitable.

This is a direct ancestor of modern free-to-try funnels. Shareware and freemium differ in mechanics, but they share the same insight: make distribution frictionless, then convert a minority of users. The free tier gave you a taste, built word-of-mouth, and created a funnel to the paid version. Modern software-as-a-service (SaaS) companies, mobile games, and open-source projects all use variations of what Doom demonstrated in 1993.

### WAD files as plugin architecture (Doom, 1993)

John Carmack made a decision that shaped decades of software design: he separated the Doom engine from the game content. The engine was the code that made things run. The content (levels, textures, sounds, sprites) was stored in files with a .WAD extension (sometimes jokingly said to stand for "Where's All the Data").

On the same day Doom was released, Carmack published the WAD file format specification. Anyone could make new levels, new enemies, new weapons. The engine would play whatever content you fed it. Within months, players were creating and sharing their own Doom levels. Some turned into professional game designers. Others built total conversions - entirely new games using the Doom engine.

This pattern - shipping a core system and letting users extend it with content, documenting formats so others can build on your work, treating user-generated content as a feature rather than a threat - predates Doom. But Doom demonstrated it at unprecedented scale, to an audience of millions who would later build software themselves. The modding scene became a proving ground for ideas that now seem obvious.

### WASD as input standardization (Quake, 1996)

Before 1996, there was no standard way to control a first-person shooter with a keyboard. Most players used the arrow keys for movement. Then a player named Dennis Fong, known as "Thresh," changed everything.

Thresh was one of the first professional gamers. He realized that using WASD for movement freed his right hand to control the mouse more precisely, giving him faster aiming than arrow-key players. He dominated Quake tournaments with this setup, most famously winning John Carmack's Ferrari at the Red Annihilation tournament in 1997.

Carmack noticed. When Quake II released, Thresh's control scheme was programmed in as a default option. Other games followed. Within a few years, WASD became the universal standard for PC gaming, so deeply ingrained that most players don't know it was ever different. One player's optimization, recognized by one developer, became a permanent feature of how humans interface with computers.

### Client-side prediction as optimistic UI (QuakeWorld, 1996)

Quake had a problem: it was designed for local area networks, where latency was measured in single-digit milliseconds. When players tried to connect over dial-up modems with 300+ millisecond latency, the game became unplayable. You'd press a key, wait a third of a second, then see your character move.

John Carmack rewrote the entire network code for a free update called QuakeWorld, released in December 1996. The key innovation was client-side prediction: your computer would immediately show the results of your actions, then quietly correct any discrepancies when the server's authoritative response arrived. You pressed forward, your character moved forward instantly, and if the server disagreed about exactly where you ended up, the game smoothly adjusted.

Modern web applications call a similar pattern "optimistic UI" - showing results immediately, then reconciling with the server. When you post a comment and it appears instantly, or send a message that shows before the server confirms, you're seeing a descendant of this idea. The guarantees differ (games need frame-perfect correction, while web apps tolerate more drift), but the core insight is the same: don't make humans wait for the network. Carmack wasn't the first to implement this - Duke Nukem 3D had a version earlier in 1996 - but QuakeWorld made it famous.

### ELO ranking as competitive matchmaking (StarCraft Battle.net, 1998)

The Elo rating system was invented in 1960 to rank chess players. The math is elegant. Beat a higher-rated player and you gain more points than if you beat someone lower. Over time, ratings converge on true skill levels, and you can match players who should have competitive games.

Competitive video games adopted this wholesale. StarCraft's Battle.net service used Elo-style ratings to create ranked ladders. Counter-Strike ranks work similarly. The system proved so robust that it spread far beyond games. Tinder uses Elo-style ratings to match users. The Large Language Model Systems (LMSYS) benchmark ranks AI models using the same math. FIFA's world rankings are based on it.

What games contributed was scale testing. Chess tournaments happen a few times a year, but StarCraft matches happened thousands of times per day. The games proved that Elo worked for high-volume, rapid-turnaround competitive systems, which made it safe to adopt everywhere else.

### Demo files as observability (Doom, 1993; StarCraft, 1998)

Doom could record your gameplay session to a .LMP file. Quake used .DEM files. StarCraft used .REP replays. These weren't video recordings - they were logs of every input and game event, which the engine could replay to reconstruct exactly what happened.

The implications were profound. Replays let players analyze their own performance. They let tournaments verify that matches were legitimate. They let communities share and study exceptional gameplay. In StarCraft's case, the replay files eventually became training data for AI research - first thousands of Brood War replays for early bots, then millions of StarCraft II games for systems like DeepMind's AlphaStar.

Replay files are closer to structured event logs and session replay than to full observability (which also includes metrics, alerting, and service-level objectives). But the shared idea is reconstructability: the ability to debug what happened after the fact. Session replay tools like FullStory record user interactions and play them back. Audit logs capture every state change. Distributed tracing reconstructs request flows. All of these share something with Doom's .LMP files: turning ephemeral events into durable, analyzable records.

### Digicel animation as asset pipeline (Aladdin, 1993)

Disney's Aladdin for the Sega Genesis was one of the best-looking games of 1993, and it almost didn't happen. The development team at Virgin Games partnered with Disney animators to create something unprecedented: hand-drawn animation digitized for a 16-bit console.

Disney animators produced 1,400 individual frames for the game, far more than any comparable title. The frames then went through a "Digicel" process to work within the Genesis's constraints: limiting colors, optimizing palettes, using techniques like holds (freezing on a frame), loops (repeating sequences), and X-flipping (mirroring sprites to save memory). The budget hit $1-1.5 million, roughly four times the average game development cost at the time.

The result proved that with proper tooling, high-quality creative assets could flow into constrained technical systems. Modern asset pipelines do the same thing at greater scale: taking raw creative output - video, audio, 3D models, images - and optimizing it for delivery to devices with limited bandwidth and storage. The Aladdin team solved version 1.0 of this problem with hand tools. We've automated it, but the challenge is the same.

None of these patterns were invented by games. Shareware existed before Doom. Modular architecture predates WAD files by decades. Elo came from chess. Distributed systems research was solving latency problems in parallel. What games contributed was a massive proving ground. The patterns had to work under real-time constraints, with paying customers, at scale. Techniques that might have stayed academic got stress-tested by millions of teenagers on dial-up connections, and the ones that worked spread.

The systems layer has a pattern: design for extension, design for latency, and treat recovery as a feature. Games taught those lessons in public, at scale, long before most of us had dashboards.

Systems are the middle layer, covering how software gets distributed, extended, and made responsive. The deepest layer is where games became laboratories for decision-making under uncertainty.

## AI

### Fog of war as partial observability (StarCraft, 1998; Age of Empires II, 1999)

In real-time strategy games, you can only see parts of the map where you have units. The rest is hidden under "fog of war" - you might have explored it before, but you can't see what's happening there now. Enemy movements are concealed. You have to make decisions with incomplete information, inferring what your opponent might be doing from limited observations.

AI researchers have a formal name for this: Partially Observable Markov Decision Process, or POMDP. Fog of war maps cleanly onto that mathematical structure, describing any situation where an agent must act without seeing the full state of the world.

In 2020, researchers at Samsung published DefogGAN, a system that uses Generative Adversarial Networks (GANs) to predict where hidden enemy units might be based on observable information. The StarCraft fog of war, designed to keep players guessing in 1998, became a benchmark for machine learning techniques 22 years later.

### ViZDoom as visual reinforcement learning benchmark (Doom, 1993 -> 2016)

For years, reinforcement learning (RL) researchers used Atari 2600 games as benchmarks. But Atari games are flat: 2D sprites on simple backgrounds. In 2016, researchers at Poznan University published ViZDoom, a platform that exposes the Doom engine as an RL environment.

ViZDoom lets AI agents navigate 3D corridors, shoot enemies, pick up items, and complete objectives, all from first-person visual input. The step up from Atari was significant. Agents now had to process 3D spatial reasoning, handle partial observability (you can't see behind you), and deal with much more complex visual scenes.

The platform has accumulated hundreds of academic citations. The Farama Foundation now maintains it alongside other RL benchmarks. A game designed to feel claustrophobic in 1993 became a testbed for teaching machines to see and act in three-dimensional space.

### Pathfinding as autonomous navigation (Quake III Arena, 1999)

Quake III Arena came with sophisticated AI bots, computer-controlled opponents that could navigate the 3D levels, pick up weapons, hunt players, and compete effectively. The bots used techniques like A* pathfinding to find routes through complex environments, avoiding obstacles and tracking targets.

The id Tech 3 engine became a platform for academic research beyond entertainment. Researchers used it to study navigation algorithms, test virtual reality interfaces, and train agents in simulated environments. The engine's bot architecture provided a starting point for understanding how artificial agents could move through physical space.

This work fed into modern autonomous systems. Robot navigation, drone pathfinding, and game AI all draw on techniques refined in the Quake III era. The games were simulators before simulation was a buzzword.

### Wait-and-watch as observation action (Half-Life, 1998)

Half-Life's enemy soldiers were smarter than anything players had seen before. They used cover, threw grenades to flush you out, and communicated with squad members. But perhaps their most interesting behavior emerged from a design decision about faction fighting: soldiers would fight alien creatures if they encountered them.

Players quickly discovered a tactic. You would step into a doorway just long enough to wake the room up - marines barking, aliens screeching, grenades starting to arc - then backpedal into the hall. Sometimes you would leave the area entirely and listen from around the corner while the two factions erased each other. Only then would you go back in and clean up the survivor, usually low on health and ammo.

The game's AI used condition bits and schedules to determine behavior. Soldiers had conditions like "SEE_HATE" that triggered combat with aliens. The wait-and-watch tactic was not explicitly programmed. It emerged from the AI rules interacting with player strategy.

This matters for modern AI because it demonstrates something counterintuitive: sometimes the optimal action is no action. Observing and waiting can be a legitimate strategy. When we build AI agents today, we have to account for the possibility that the best move is to gather more information before acting. Half-Life players figured this out by accident in 1998. AI researchers formalized it as part of optimal policy design.

### Scripted vs learned behavior (Half-Life, 1998; F.E.A.R., 2005)

Half-Life's soldiers weren't learning anything. Their impressive behavior came from carefully designed rules: if condition X, do action Y. The schedule and task system gave them flexibility, but every behavior was authored by a human.

Seven years later, F.E.A.R. introduced Goal-Oriented Action Planning (GOAP). Enemies had goals ("kill the player") and available actions ("throw grenade," "take cover," "flank"). The AI planned sequences of actions to achieve goals, adapting to circumstances rather than following fixed scripts.

That trade-off - scripted behavior versus systems that figure out what to do - persists in AI today. Rule-based systems are predictable and explainable but brittle. Learned systems can adapt but may behave unexpectedly. Modern approaches often combine both, using rules for constraints and learning for optimization. The games were working through this decades before "AI safety" became a research area.

### StarCraft as strategic AI benchmark (StarCraft, 1998; StarCraft II, 2010)

StarCraft became the chess of AI research for real-time strategy. The game offers everything difficult: imperfect information (fog of war), long-horizon planning (matches last 10-30 minutes), real-time decisions (no time to compute optimal moves), and strategic diversity (three asymmetric factions with different units and abilities).

The original StarCraft: Brood War attracted an early research community, with thousands of professional replay files providing training data. But the landmark breakthrough came with the sequel. DeepMind's AlphaStar, released in 2019, trained on StarCraft II using millions of games - both human replays and self-play - and eventually defeated top professional players.

More recently, researchers have connected large language models (LLMs) to StarCraft II through interfaces like TextStarCraft II, letting these models issue strategic commands and testing whether they can reason about complex, adversarial, real-time domains. A franchise that began in 1998 remains a frontier for AI research.

### Text adventures as reasoning benchmarks (Zork, 1980; Hitchhiker's Guide, 1984)

Before 3D graphics, there were text adventures, and they started with a sentence instead of a cutscene. Zork opens with one of the most quoted lines in the genre: "You are standing in an open field west of a white house, with a boarded front door." From there you typed commands - "open mailbox," "take lantern," "go north" - and the game answered in prose, tracking the world entirely in text. Infocom's parser could understand surprisingly complex English sentences, which is part of why these games still matter.

These games have found new life as AI benchmarks. In 2024, researchers released TextQuests, a suite of 25 classic Infocom games set up for LLM evaluation. The challenge is unique. Unlike video games with a few hundred possible actions per frame, text adventures accept any English sentence. The space of possible inputs is effectively infinite.

This tests reasoning rather than pattern recognition. An AI that can solve Zork must understand language, maintain state over long sequences, and develop strategies without any visual input. The games that entertained players in the 1980s now probe the limits of language model intelligence.

Games make good benchmarks, but they have limits. They're controllable, reproducible, and cheap to run, unlike robots in the physical world. But they're also artificial. An agent that masters StarCraft may not transfer that skill to supply chain logistics. The simulation-to-real gap is real. Learning in a game environment doesn't automatically translate to learning in the messy physical world. Researchers use games not because they're perfect proxies for reality, but because they're tractable. They let you iterate fast, fail cheap, and isolate specific capabilities. The 90s games endure as benchmarks because they hit a sweet spot, complex enough to be hard, constrained enough to be solvable, and documented enough to be reproducible.

If you want to test decision-making under uncertainty, you need an environment that is hard, repeatable, and cheap to run. That is why games keep showing up in machine learning research, even when the real world is the end goal.

## Conclusion

The colleague who mentioned "nerfing" a feature probably doesn't think about where that word came from. The site reliability engineer (SRE) watching containers respawn probably hasn't thought about Doom in years. The machine learning researcher running experiments on ViZDoom might never have played the 1993 original.

Either way, the inheritance is there, whether anyone notices it or not.

The three layers of this legacy build on each other. First came language, because millions of strangers needed shorthand to coordinate in real-time combat, so they compressed social signals into keystrokes. GG, noob, nerf, buff, respawn - each term solved a communication problem under severe constraints. Second came systems, because developers needed distribution models and extensibility patterns, so they stress-tested shareware, WAD files, and client-side prediction at massive scale. Third came AI, because researchers needed environments to train agents, and the games were already there - complex, adversarial, partially observable worlds where machines could learn from experience.

Games forced ordinary people to live inside distributed systems problems, dealing with latency, partial failure, and coordination under imperfect information. They stress-tested patterns that later became standard practice in software. And they created benchmarks that researchers still use to push the boundaries of what machines can learn.

Half a day of research turned three random conversations into this exploration. The next time you hear someone mention nerfing a feature, or watch a container respawn, or see a reinforcement learning benchmark running on a 30-year-old game engine, you're seeing one of the streams that fed modern tech. Those streams are still running, and we still build on them.
