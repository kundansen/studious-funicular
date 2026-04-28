# Lights, Camera, Action - Content Creation for the Camera-Shy

*January 5, 2025*

---

If you are in the crowd with us who do not have a radio voice, are somewhat of an introvert when it comes to creating video content, yet are interested in our own way to create content to express what we would love to let the world know - here's a quick article on the joys of the tools already available to us.

Take a quick look at the short video above, **Majungasaurus Crenatissimus (at) Stony Brook, NY**. At the onset - there's nothing remarkable about this movie, it's like any of the tens of thousands of similar educational movies available everywhere.

What made it interesting for me was how I could create it - almost effortlessly, using a combination of tools commonly available to most of us. Here's a quick summary:

- Shot on an iPhone using the Cinematic mode
- The content came from a photo of an explanatory poster
- Azure AI did the voice-over
- iMovie puts the video and audio tracks together

Intrigued? Let's get down to the details for each of these steps.

---

### Step 1: Create the script

I started with the script, as that made it easier to figure out how long to capture the video. Creating informative, interesting, and perfectly crafted voice-over text takes time. I took the easy way out. Next to this dinosaur skeleton, there was a poster explaining the details. I took a photo of the poster and then used the built-in text copy from images feature on phones to extract the text. Simple markdown formatting in VSCode gave it a structure through basic formatting.

### Step 2: Convert the script into voice

Here's where my love for everything AI comes in. Truthfully - all of this was an experiment to figure out Azure's SSML (Speech Synthesis Markup Language) and the relatively new inflections based on styles and roles.

Start your reading journey from [Microsoft's documentation on SSML](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup). Navigate through the documents to read through the steps to spin up a speech service on your Azure portal account. Also, read up on [voice styles and roles](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts#voice-styles-and-roles) to see which combination of parameters best matches what you are after.

A few voices that I liked:

- **en-US-JennyMultilingualNeural**: Neutral, crisp voice that can handle multiple languages
- **en-US-SaraNeural, style = cheerful, styledegree = 2**: This is what you hear in the video. This was the best given my context.
- **en-US-SaraNeural, style = depressed, styledegree = 2**: Audibly different from the cheerful Sara. Perhaps for a darker movie someday.
- **en-US-SaraNeural, style = shouting, styledegree = 2**: This expressed anger better than the angry style. While very different from the depressed Sara and the cheerful Sara, I would not want to hear the shouting Sara for too long. Good to keep as backup for when you want to create a video to annoy everyone around.

After you spin up your Azure voice service, it's fairly simple to set up the basic API call. I used Python - the [quickstart guide](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-text-to-speech?tabs=windows%2Cterminal&pivots=programming-language-python) was enough for this exercise.

Once the basic setup was working, I replaced the sample text with what I had from Step 1 above and tweaked the voice name, style, and styledegree in the config settings.

I recorded the resulting audio via Audacity. I'm sure there are easier ways to save the recording from the API call.

### Step 3: Record your video

Working backward (audio first) is fantastic for creating educational content like this one. It's so much easier to figure out how to move around my subject, the dinosaur, given the entire script in the audio form.

I'm showing my age here, our mobile devices have evolved into rather powerful content-creation devices. I say this while flinching a little - I love my mirrorless full-frame and also keep my Sony consumer-grade handycam in working order. That said - neither was available when I wanted to play around and as the saying goes, the best camera is the one that you have on yourself when you want to capture.

On the other hand - the cinematic mode on iPhones has evolved beautifully, as have the sensors and the in-device stabilization. For a decently lit daytime scene as my subject, I doubt using a full-frame mirrorless or a dedicated UHD camcorder would have added any benefit to the quality of the video.

### Step 4: iMovie to put it all together

This is a simple step. I used iMovie on my phone which I had on myself. As I understand the mobile version of iMovie does not have image stabilization - this is the only feature I wished I had access to, since I was walking around the scene while capturing the video. Except for the lack of stabilization, the interface of iMovie is super simple to allow removal of the audio track from the original recording and adding in the voice-over track that was produced in Step 2 from Azure Text-to-Voice.

### And that's a wrap!

I'm sure you can feel my excitement with all this tech and AI that is available to us readily, abundantly, and inexpensively. The future is here and it's beautiful. I am in the camp of people who hate how they sound when they hear their own voice in recordings, and this pipeline of tech described above avoided the need entirely for me to use my voice. Also, it prevented me from becoming conscious of my accent - another insecurity that I carry around with me.

What do you think? Does this help you get started with your next fun content-creation exercise? If you tried out the voices, styles, and roles - which ones did you find interesting? Drop me a note in the comment so I can try them out!

Happy content creation!
