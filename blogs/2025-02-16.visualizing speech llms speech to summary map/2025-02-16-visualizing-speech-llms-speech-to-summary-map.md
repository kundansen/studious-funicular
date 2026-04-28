# Visualizing Speech: How Well Do Different LLMs Stand Up to Converting Speech to a Summary Map?

*February 16, 2025*

Today's read is a fun one - with a double objective.

If creating diagrams is a part of your day job, then you are likely familiar with the PlantUML syntax of writing markup code to create a diagram using GraphViz. Nothing new here.

What's new is, of course, GenerativeAI - and what it can do with it.

In the rest of this article, we will explore:

a) How to convert a large chunk of text, using a publicly available transcript of a famous dialog, into a summary one-page diagram, and

b) How a handful of LLMs I tried this out on behave when given the same task and the same set of prompts.

So - as every article written with GenAI shortcuts loves to say, let's dive in! (I'm beginning to cringe at the sound of that phrase, even though it was one of my personal favorite things to say).

### What is a Mind Map?

Pre-requisite check - do you know what is a mind map? Here's a 30-second refresher.

Mind maps are a visual form of Cliff's Notes. They are usually represented in a tree structure, starting from a root note, then a bunch of first-level "parent nodes", each having one or more child nodes, and so on. There are usually no loops and no joins, sticking to a typical tree structure and not becoming a complex graph.

You can read a lot about mind maps at [https://www.mindmapping.com/](https://www.mindmapping.com/).

If you have used Freeform for visual doodles on your iOS device - you have used mind-mapping concepts.

### What is a Dialog Map?

Take it one step further. A dialog map is a concept introduced in the paper [https://cognexus.org/dmforwp2.pdf](https://cognexus.org/dmforwp2.pdf) - "Dialog Mapping: An Approach for Wicked Problems", by Jeff Conklin.

Explained briefly - a dialog map is a mind map summary created from a text transcript of a human dialog. It can be any dialog - a one-on-one conversation, a webinar, a training course, a panel discussion, or a famous speech.

Explained even simpler - it's the ultimate Cliff's Notes version of a large chunk of text, a one-pager diagram representing the text.

Copying the summary from Jeff's paper: "*Dialog Mappers allow the intelligence and learning of the group to emerge organically. Instead of agendas and control, the group's energy is reflected and channeled in a self-correcting way by each person's ability to see, in the structure of the Dialogue Map, how their own comments contribute to the coherence and order of the group's thinking. Dialog Mapping is a new paradigm of facilitation and meeting process.*"

### Why the Excitement, Why Now?

Naturally, it's GenAI and LLMs. Large Language Models are fantastic with - drumroll - language. Dialog mapping from unstructured text is very much a language domain problem. A mind map is very close to the associative structure of a knowledge graph. Summarizing blobs of text into a short phrase, and then linking the phrases into a navigable tree structure, appears to fit right into the core working model of LLMs.

What we need to do is a set of a few basic prompts to guide the LLM on what we want, and to teach it the basics of Jeff's paper without having to parse PDFs and whatnot. Since we want to produce an image representation as the final output, a secondary set of instructions will prompt the LLM on the basics of PlantUML markup - how to separate the ideas, questions, notes, pros, cons, and decisions into a color-coded map format.

## Today's Experiment

Today's experiment will involve a prompt with 3 key features:

1. Instructions on how to summarize a large chunk of text into a dialog map (from Jeff's paper)
2. Instructions on how to represent a map in PlantUML format
3. A text transcript of your choosing.

I went for ['Why did I say 'yes' to speak here?' by Malcolm Gladwell](https://www.neil.blog/full-speech-transcript/why-did-i-say-yes-to-speak-here-by-malcolm-gladwell) as the standard text across a handful of LLMs. Once the PlantUML output was produced I used Visual Studio Code with a PlantUML preview plugin to convert it into an image, as we are horrible as humans in reading image-as-code.

### Candidate 1: OpenAI's GPT 4o

*[image: GPT 4o's PlantUML dialog map summary of Malcolm Gladwell's 'Why did I say 'yes' to speak here?']*

### Candidate 2: Anthropic's Claude 3.5 Sonnet

*[image: Claude 3.5 Sonnet's PlantUML dialog map summary of Malcolm Gladwell's 'Why did I say 'yes' to speak here?']*

### Candidate 3: Google Gemini 2.0 Flash

*[image: Gemini 2.0 Flash's PlantUML dialog map summary of Malcolm Gladwell's 'Why did I say 'yes' to speak here?']*

### Candidate 4: GPT o1

*[image: GPT o1's PlantUML dialog map summary of Malcolm Gladwell's 'Why did I say 'yes' to speak here?']*

## Verdict?

First of all - dialog maps are great when used as a medium to recollect the key points from something you have read or watched in detail, such as a talk in this case, and also books, movies, and discussions. If you have not spent the time experiencing the original medium of the content you will likely not trigger the associations in your own brain from the compressed format of a dialog map.

Now - what any of the maps above did, was reduce the time from a 19-minute video, or about a 12-minute read of the text, to what should take under 2 minutes to scan and recollect. A compression ratio of approximately 1:10, and the advantage of having the entire summary laid out in a single page - which means if you are looking specifically for one chain of thought it's almost an O(1) recall from the map.

How did the LLMs compete against humans? I am not an expert in creating mind maps, and it takes me roughly 4x the time of the original content to effectively create a map out of it - as it involves consuming the content and revisiting parts, then mapping chains of thought that were covered in separate sections of the content into one area, then cleaning it up. Having an LLM do the map for me was a tremendous speed-up.

How did the LLMs fare against each other? There's no Abstract Syntax Tree notation for a speech, and turning text into a map is highly subjective. This makes the creation of a dialog map a lot more of an art and a little bit of science. Art is subjective - so I will refrain from saying one art form is better than another. However, there are some differences, so let's take a quick look through them:

1. All 4 LLMs above latched on to the key phrase in Malcolm's talk, about EICD - Elite Institution Cognitive Disorder. Note that if you watched the video instead of reading then you had an advantage of taking in cues from Malcolm's pauses - the LLMs did not have this advantage. It's reassuring that when used at scale, there's some confidence from this small experiment that the key messages will get captured.
2. Another example - all of them picked up on Malcolm's "Relative Deprivation Theory" as the root cause for the drop in STEM enrollment.
3. GPT 4o produced what I would call the most detailed map. Note that the most detail does not mean the highest signal-to-noise ratio - just the most elaborate map.
4. Gemini seems to be tuned for the Google keyword, making it the top node of the map. Others also picked up on the location but went for a less prominent placement.
5. Claude is more focused on numbers and metrics. Makes sense, as it's generally considered better at coding and technical skills. If I were to choose one of these models for a data analysis project, I would likely go for Claude.
6. Claude is the only one who picked up on the Happy Countries theory - that our self-assessments are relative to our immediate circle. Given the level of detail and consistency across all of the models, I would call this as hitting a sensitive keyword on the other models. I'll avoid the keyword myself as I don't know how LinkedIn treats its mention.
7. Claude also came up with what I found as the most logical format - clearly picking up the tone of the speech to separate out the definition of the problem, the symptoms, and then a list of measures we can take to address it. Note that the prompt used across all of these LLMs was exactly the same. This hints at a more mathematical, technical approach by Claude towards what was a language problem.

## What Next?

I'll leave you with 2 quick takeaways.

First, if you have not watched Malcolm's talk and you were speed-reading this - please go back and watch the video. The video has the advantage of leveraging Malcolm's excellent presentation skills. It's a superb talk on a very interesting topic - and if you are a hiring manager for any role, something for you to consider incorporating.

Second, LLMs are the Swiss Army knives of pretty much anything in writing - speech, code, data. Play around with any and all ideas you have. You never know what will click. Every little aha moment will make new gears spin in your head - and there will be dozens of aha moments if you keep at it.
