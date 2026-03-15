# ChoreStory Working Session — Homepage & Game Brainstorm

**Source:** kih-wwbo-ets-2026-03-13 19_53 GMT-6.mp4
**Duration:** 42 minutes 36 seconds
**Speakers:** 2 (Speaker A — Aug, Speaker B — Rocky)
**Confidence:** 88.2%
**Language:** English (US)

## Transcript

**[00:06] Speaker A:** What do I can't record?

**[00:11] Speaker B:** FaceTime, obviously. Can you see my screen? Yeah, cool. So I'm using the create issue skill to create the epic of creating the home page and moving all the routes around. So chorestory.com right now just goes straight to the app, so it's going to move to app.chorestory.com. The home page will take over the root, and then headless.shortstory.com will stay the same. And that's just, uh, I don't know if you've checked it out, but there's a place where the family admin can go and create a token and go into headless mode so that you can put it on, uh, like a shared family iPad, or like I have a touchscreen hanging on my wall that I got a Raspberry Pi hooked up to. It's supposed to be showing me options. I don't see— see.

**[01:37] Speaker A:** Oh, so what happened? We ordered food, the driver got the food, and then drove towards Coquitlam. Not Burnaby.

**[01:47] Speaker B:** Oh yeah, oh yeah.

**[01:48] Speaker A:** And then I'm like, hey, what's going on? I paid express and whatever, and then DoorDash canceled my order, and I was like, okay, that was weird.

**[01:58] Speaker B:** We're a bunch of dickheads.

**[02:00] Speaker A:** Yeah, so I had to order it again.

**[02:09] Speaker B:** Well, now you'll go hungry for a bit.

**[02:13] Speaker A:** Fine. It's just weird, weird shit.

**[02:20] Speaker B:** So it's going to take care of everything on the homepage, the SEO setup, um, uh, like all the marketing hooks, Google Analytics, all that crap. So it'll build out all of the issues to work through. And then I'll use Implement Issue plugin to work them all. Uh, it says join the beta, but what actually happens when someone clicks it? Uh, yeah, let's get them to sign up. Um, B to A max, uh, Mom, I can set either in the database right away or in the platform admin panel as it gets built. He's part of what? And from— what is this? Oh, that's the Epic 220 as part of 220. So how was your day, Aug?

**[04:37] Speaker A:** It was interesting. Started off with, uh, hey, a pipeline did not work in the morning.

**[04:45] Speaker B:** Wake up to— and they fucking run overnight too. Like, why can't they run at noon and then you can be like, okay, I just finished my lunch, I'm ready to fix this shit? No, you got to fix it at 7 AM when you just open your damn eyes.

**[04:58] Speaker A:** Exactly. And it was something so stupid. Um, I don't know what the fuck— sorry, what's wrong with, uh, Fabric, but like sometimes when you try to install like a PyPI, uh, package or something.

**[05:13] Speaker B:** Yeah.

**[05:14] Speaker A:** It doesn't even start a cluster, so it just stays there.

**[05:19] Speaker B:** Okay, so I went from having an issue almost every day on Fabric to I don't even know when my last incident was on Snowflake.

**[05:28] Speaker A:** Yeah.

**[05:30] Speaker B:** Fabric is hot garbage.

**[05:32] Speaker A:** Yeah, but people purchase it.

**[05:36] Speaker B:** People will pay anything to go with Microsoft.

**[05:39] Speaker A:** Yeah, I don't know, man.

**[05:41] Speaker B:** Have you worked with Astro?

**[05:43] Speaker A:** With what?

**[05:43] Speaker B:** Astro.

**[05:45] Speaker A:** Astro?

**[05:46] Speaker B:** Yeah.

**[05:47] Speaker A:** No. What is it?

**[05:49] Speaker B:** Dynamic, dynamic page loading that works really well with SEO. And this is what it recommended to go with for the homepage. Astro marketing site and the React app have completely different Build pipelines, deploy targets, and release cadences. Yeah, that makes sense. The, uh, I got the admin site in there. Did you reach out to Amanda today?

**[06:40] Speaker A:** No, not yet. Um, I'll probably send her a message on Saturday. She usually, um, we usually talk Saturday mornings when you're watching cartoons. Yeah, usually when I have time to like do shit like this. Astro, what is it?

**[07:04] Speaker B:** Astro and Node.js.

**[07:09] Speaker A:** Oh, I see.

**[07:11] Speaker B:** Astro Tailwind from scratch. Yeah. Astro Template Accelerator. Sassifier Astros. It is faster to MVP, but the Claymorphism— yeah, okay, we're gonna go with approach one. It's actually almost done asking questions, and then it's gonna go and build requirements. And then turn them into a GitHub epic with child issues. Well, here it is. Does this issue breakdown look right? Okay, subdomain, yep. Scaffold Astro homepage MVP. Hero Social, beta user cap configurable, and then SEO foundation meta tags. Yeah, this looks pretty good. Phase 2, Phase 3. Oh yeah, so I'm going to— I want to do a developer blog on it. So once we get into the swing of things, Can you run that since you know how to do that?

**[08:48] Speaker A:** Would be fun.

**[08:49] Speaker B:** Yeah. Oh yeah, especially as we get it like hot and heavy into the game development. Oh, that's gonna be so fun. And we could do like a, a vlog too, like a bi-weekly vlog, and put it on there. All right, architecture review. Pay attention, Aug. Yeah, I mean, for a guy who doesn't understand how Astro is supposed to be set up, this looks right. I said that's like the great thing about this point in my career. I don't need to know the technology to know if it's right or not.

**[09:42] Speaker A:** I don't know about that, dude.

**[09:48] Speaker B:** Uh, no, I mean right from a how systems are supposed to work together perspective, right? Like from a systems perspective, this layout looks, looks right. Yeah, corporate.

**[10:04] Speaker A:** Now, yeah, kind of like what I posted about that dude.

**[10:17] Speaker B:** Oh yeah, yeah, yeah. Uh, it's missing one. It's missing headless stuff.

**[10:25] Speaker A:** What's Bob Ross?

**[10:27] Speaker B:** That's the dev server.

**[10:35] Speaker A:** This is nice. It's kind of cool. I was reading the Astro, uh, documentation.

**[10:39] Speaker B:** Yeah, I gave it a quick glance before, before I called you too. It looks like you can do some really neat, like, the, like, animated, like, as you scroll type of stuff. I mean, you can do that with HTML too, but all of these integrations and you could do templating and all that's super easy too. Yeah, cool.

**[11:07] Speaker A:** Okay, I'll stop poking at it. Um, once, once food gets here, I'm gonna have to—

**[11:14] Speaker B:** yeah, that's fine.

**[11:18] Speaker A:** Um, I wanted to kind of show you what I started. I did a BMAD project, and I'm gonna go and start like brainstorming ideas for the game. Um, one of the cool things about this brainstorming thing is it comes up with more ideas while you're kind of brainstorming.

**[11:37] Speaker B:** What is it called?

**[11:38] Speaker A:** BMAD.

**[11:39] Speaker B:** BMAD. Yeah, okay.

**[11:41] Speaker A:** I thought you used it.

**[11:46] Speaker B:** Yeah, um, you sent it to me last week, right? Yeah, but it's— yeah, I looked into it and it's more of a, like, it's an application unto itself kind of thing. Like, but I was looking at it from the context of, like, is this something I would use over Rawgentik? Not, is this something I would use in addition to Rawgentik for different purposes? And I think the answer to the second question is yes, it would be quite helpful. Okay, decisions. Why does it need ng-inx when we have Traefik?

**[12:35] Speaker A:** There's an E between the A and the S. Traefik or something. There you go. Um, I'm gonna like do the, the thing here with BMAD, just like go through the brainstorming.

**[12:53] Speaker B:** Yeah.

**[12:54] Speaker A:** And then I'll share the MD file with you so you could like check it out.

**[13:02] Speaker B:** Uh, yeah, okay, that sounds great. Old shortstory.com URLs. APIs, blah, blah, blah. Get 301 redirects to app. I don't know. I think they should be rebuilt. Be rebuilt with— this is Claude being lazy. Claude is notoriously lazy. I have to yell at it every day for being fucking lazy. It's like, well, the easier way would be to do it this way, because if you do it, if you do it the proper way, it's going to take you 6 weeks. I'm like, no, it would take me 6 weeks. It's going to take you 45 minutes. I think they should be filled with proper passing, uh, but being lazy. Dev mirror Bob Ross source.com equals dev homepage. Yes, yes, okay. I mean, it's not blowing my hair back in the kinds of designs that it's showing me in this, in the site, in the brainstorming, but it's enough to wrap your head around, around what it's trying to do. I wish they were a little more polished, but I guess without doing the assets, that's kind of hard. You know, one of the favorite things that it generated for me, that NotebookLM generated for me, is, is this. I want to find a way to use it.

**[14:54] Speaker A:** Thank you.

**[14:54] Speaker B:** Is it this one? Yeah, this, this graphic.

**[15:01] Speaker A:** Yeah, yeah, I thought it was cool too. Like the one on the right is— it gave me like a bit of a wow, right? Type of—

**[15:09] Speaker B:** yeah, yeah. There's a— there's another one too that I think I actually like. Yeah, I like this one too. Yeah, so then, so now while I'm brainstorming this, it was like, oh, this is the first time hearing about your game. Do you have any information about your game? And I'm like, actually, use the NotebookLM plugin to go in to go to this project and here's all my business research. And it just went and Pulled it all in. Okay. Uh, Chainlink is a root node of files. Oh. Backends but can't serve static files itself. Oh, we need— okay. So what is serving? What is serving my React app then?

**[16:04] Speaker A:** Nginx.

**[16:07] Speaker B:** No.

**[16:08] Speaker A:** Why not?

**[16:12] Speaker B:** Use the corrected architecture deployment changes homepage busy box. Okay, yeah, no, and, uh, terrific handles SSL compression security headers. Yeah, that's what I was getting at, because the way I had my site set up before when I had it on one, like on my old server— did I tell you about my new server? It's crazy. Anyways, on my old server, it was just one, like, one Linux installation, right? So I had dev and prod on the same, on the same instance. And I had to do all sorts of separating. So I used Nginx on that. When I switched over so that dev and prod are on their own VMs, I switched over to— so I have a a routing VM, and that's all it does. It has Traefik on it, and it just routes everything, and it simplified the shit out of everything as far as like what ports go where. And so anyways, it's pretty cool. So yeah, this new server I got, it's a dual Xeon with 128 gigs of RAM, and I got, uh, and, uh, 12 hot swap disk bays. It's an old Intel McAfee server that I picked up, and I got on last Friday, I ordered a Tesla P40 for it, so I can run most of the models that you see on Ollama.

**[17:52] Speaker A:** Nice. Oh, what now?

**[17:55] Speaker B:** A what?

**[17:57] Speaker A:** Uh, we bought a what now?

**[17:58] Speaker B:** Oh, it's Tesla P40. It's an Nvidia AI card. It's got 24 gigs of RAM, 3840 CUDA cores.

**[18:21] Speaker A:** I've never heard of this one.

**[18:27] Speaker B:** Oh, I'll watch. Lucy's trying to drink all my rum.

**[18:32] Speaker A:** Uh-huh, that's good.

**[18:41] Speaker B:** She's a bit of a liquor pig. Okay, there we go, corrected routing. True story. That's how it came off. Yep. So we are going to put this in a new repo. Make sure the homepage issues are created in that repo and app issues to adjust routing and whatnot. Routing, routing, footer, and whatnot are in the repo. Create the assets for homepage in—

**[20:02] Speaker A:** What did you just say? Tour story.

**[20:20] Speaker B:** To who? Cool.

**[20:20] Speaker A:** Very cool.

**[20:20] Speaker B:** Oh, it's the full page flow. It must have heard me trash talking its capabilities. It's going to show me the—

**[20:26] Speaker A:** Now you want to see lazy? I'll show you lazy.

**[20:31] Speaker B:** Like, you want me to burn through all your credits? I'll burn through all your credits. Doing next week, um, we're doing a half-day AI workshop for all of IT next week, and then the day after we're doing a whole day hackathon, taking like bite-sized pieces that would What the fuck is with the color scheme? That looks stupid. I mean, it looks pretty good. I don't— I just don't like the yellows up here. Uh, think of the content flow. Okay. Special. This is the— yeah, this is one of the most powerful imagery images out of the slide, right? Like the whole, how do you get kids to do something they are notoriously resistant to doing? Well, you make it so that they earn something they care about. Oh yeah, here we go. Pre-turn beta. Um, if you are just showing me the Oh, it looks good. Not a fan of the whole burning and desert. There we go. So, so Oh, see how it works as a smooth scroll to Section 3. Sweet. Writing the specs. Yeah, hurry up. Oh, and did you see that you can— that, uh, Opus is now, a million, a million token context.

**[23:09] Speaker A:** And you don't— yeah, I saw that.

**[23:12] Speaker B:** They've had it for a few weeks where you could, like, it would burn double the tokens to switch to a million context, but now it doesn't. So that's pretty cool. It actually hasn't compacted this entire time.

**[23:26] Speaker A:** I usually take care of seeing the percentage, um, like once it gets to 60 I ask it to save with BMAD, and then I just open a new context window and just picks up where it left off. That's what BMAD does for me.

**[23:41] Speaker B:** I, uh, yeah, I got that. I got that mostly built into, um, Rogentik.

**[23:48] Speaker A:** You need to check out BMAD, man.

**[23:50] Speaker B:** Yeah, I'm going to.

**[23:52] Speaker A:** Cheese and rice. Does this sound correct? It gamifies doing chores so that children earn something they care about. Parents can provide incentives in the form of currency for their favorite video games or for our own video game. Our video game is a massive multiplayer online world with quests where you can level your equipment with MK currency, which is, uh, generated By real world tours. Now let me grab all of that and ask my buddies.

**[24:30] Speaker B:** That looks pretty right. Yeah, that sounds pretty right. Yeah. The other thing I would love to get in the game is like— and this is something that I'm surprised hasn't been done very well at all yet— but like AI, like actual AI characters in the game. That you can interact with in a non-scripted manner. I have no idea why that's not built yet. Probably because every game releasing today was started 3 years ago. Yeah, we're gonna build a full MMO with 2 dudes in a, uh, box of root beer in 6 months.

**[25:13] Speaker A:** Dude, it would be awesome if we actually did the AI thing, like interactions. That would be pretty cool. Help me with my homework.

**[25:23] Speaker B:** Actually, that would be pretty sick. Oh my God, add that, add that. Like, that is actually a great idea. Let's explore that. Well, because I'm trying to turn this into— like, so many people think kids on video games is a bad thing, and a lot of the times it is right? But the whole educational aspect and financial literacy aspect and learning aspect, there's huge power in video games for kids if you can keep them engaged and present them something that they're actually learning with and wanting to come back to. This is the boring part. Where it does all its gesundes.

**[26:43] Speaker A:** So that's a very good question. So this thing has like a game, um, studio, uh, type of deal where you could like— the agents are different types of people that work at a game studio. And it says here, questions to consider: What feeling do you want players to have when they put down the controller?

**[27:11] Speaker B:** Yeah, that is a good question for a game. And I can see how it would be very different for very different types of games. Like, right, because anxious.

**[27:26] Speaker A:** Well, like what I was thinking of when, when you were explaining this, it would be pretty cool. Something like the Minecraft, the Sons of the Forest, or Valheim, any of those like survival resource kind of deals where you could go and create your own base and stuff like that. It would be pretty cool that you could give a family a little bit of a server to play kind of together and build like a virtual space together.

**[27:55] Speaker B:** That's what's rattling in my head is essentially like you get your virtual space and then when your friends join, You can connect them, connect your virtual spaces together to build, start building a town. And then your chores turn into like, um, stuff for the town, stuff for the town, stuff to enhance your armor. Like do a load of laundry and get 100 magic fibers that give, um, your wall a, a buff for a month or whatever. Stuff like that.

**[28:28] Speaker A:** Did you ever play Ultima online?

**[28:31] Speaker B:** Oh my God, a million years ago for like a day maybe.

**[28:36] Speaker A:** Okay, because I remember I used to play it a lot and it was web-based, it wasn't an actual like 3D type of deal, and it was kind of like that. You would get together with different people that had the, the game, like you would make a guild and then you would get together in the map and kind of like build this is like town and whatever. But I don't think kids that are small, like between like, I don't know, 8 years old, 10 years old, that is going to be very boring. So we need to kind of figure out something fun, or we create a Roblox, um, server or Roblox deal and you get, you know, play games there because I know people that do that. Type of deal where you could— it's, it's Ruby or something like that.

**[29:26] Speaker B:** I think, I think Roblox is on Ruby. Yeah. Um, yeah, I mean, that's an ideal, an idea, but that kind of partnership, that's where Roblox takes a cut, right? I want to be taking the cut from Roblox. Um, but I mean, it is an option. I'm not, I'm not At this ideation phase, I'm not kicking any— anything out of bed for crackers.

**[29:53] Speaker A:** Um, let me— I'll think a little bit more about this because like it has 4 questions. Let me just, um, I could share my screen too, right? At the same time we did that last time.

**[30:05] Speaker B:** Yeah, well, I think you can just share your screen. My screen is doing boring stuff.

**[30:11] Speaker A:** Well, mine's boring too.

**[30:13] Speaker B:** Mine's, mine's writing specs. Oh, it wants me to review them.

**[30:20] Speaker A:** Wait, I can't see yours now.

**[30:22] Speaker B:** Oh, I stopped sharing.

**[30:26] Speaker A:** Oh no, share again.

**[30:30] Speaker B:** I'm on my laptop, so I only have the one screen.

**[30:34] Speaker A:** Oh, never mind. So yeah, um, I just changed it to Toy Story gamifies household chores so children can earn rewards they care about. Parents can offer incentives in the, in the form of currency for their favorite video games or for our own game. Our game is a massive multiplayer online world with quests where players level up their equipment using in-game currency earned by playing real-world chores. Yeah, what, like, how, how can you make it matter to the family and not just the kid?

**[31:11] Speaker B:** Yeah, see, and I struggle with that one. I was thinking about that one. Like, I like playing, I like playing video games with my kids, but I hate helping them with the video games. Yeah, yeah, right. Um, or not hate, but that's not an enjoyable part. The enjoyable part is if it's intuitive enough that the kid can pick it up and I can just play it with them. So for, uh, 8-year-old to play something like this, I think the concepts— you almost need, because you're trying to sprawl that big age group where a lot of development is happening, you need almost different maturity levels of game concepts within one game. Yeah, right. Like 6 to 8, 6 to 10-year-olds are going to enjoy this section of the game. 10 to 14-year-olds are going to enjoy this, but then there's a bunch of stuff wrapped together that they'll all enjoy.

**[32:10] Speaker A:** I had a long time ago an idea. I don't, I don't think you met him. He was in Groundswell.

**[32:19] Speaker B:** Darian. Yeah, I knew Darian.

**[32:22] Speaker A:** Okay, so Darian and I were thinking of creating this like game where it was like 3 different types of games, but it was in a single game and they all affected each other. So imagine it's like a first-person shooter and it's like in the ground, and then you have, uh, a commander that says troops are gonna fall here, here, and here to do like the attack. And then there's like another one where it's resource management and whatever. So like each person who's really good at each one get together and they're like an army going against another army, right? And it was just this idea we had. This sounds kind of like that where you could have like the parents doing, I don't know, maybe not anything, right, but just checking that everything's okay, or they can participate if we want to. Like, I don't know, just—

**[33:10] Speaker B:** I, I think with the parents it has to be really optional. Yeah, because if you make the parents in any way have to log into that video game, you're gonna lose a lot of people.

**[33:23] Speaker A:** Yeah, yeah, yeah. And I think this is something like they just want to like pay for it, do the chores, get the chores done, go and have fun in the video game. Maybe the video game is just the video game and we do like pick, pick and choose, iOS, Google Play, whatever.

**[33:41] Speaker B:** Can we make this a standalone game as well? Do you have to utilize the chore aspect? How could— or to ask the question better, how can we make this game also standalone? Like, it's going to be a free, uh, freemium kind of game. Are there going to be things that are only available through the chore interface? And maybe that's a good thing, like exclusive items that you only get by doing chores, but they're fully cosmetic and there are other ways to get the same functionality. In the game, just do it with different cosmetics, just— I don't know, right? But, or do we just fully accept that these are companion apps and they go together?

**[34:29] Speaker A:** I think it would be cool doing the companion app, um, mostly because that you leave it into the same, like, uh, demography, right? Like, the same type of people are gonna play. It's gonna be families. It has to be safe for families, and the kids have to be like certain like it has to be a very safe and restricted place, right? So I'm going— it has to be like— because if you open it up, you know how it could be, right? Um, where anybody could go and play and then there's interaction. So I'd rather kind of like have it closed.

**[35:07] Speaker B:** I want to— like, I have—

**[35:10] Speaker A:** it doesn't have to be online either, you know what I mean?

**[35:13] Speaker B:** Well, it doesn't have to be, but if you want to play with your friends, it kind of has to be. That is one aspect that I, that I do want in it, right? Like, Clark— Clark's a perfect age for this use case, right? Like, her and her friends play all the same games, recommend games to each other, and— right, Clark? Like, that's a massive, uh, marketing angle. Um, but like, I have a lot of novel ideas on how to architect this thing from an infrastructure perspective, right? Like your whole thing about like families get their own server, like that's what I'm thinking. But not their own server, their own like segregated piece of the world so that if you did open it up, like totally open it up, there has to be some sort of key or something between both of them.

**[35:59] Speaker A:** And yeah, like it has to be another family as well, right?

**[36:03] Speaker B:** That's the, the thing where, yeah, there has to be permission to connect the to connect the world. So if somebody's just playing the game for the sake of playing the game, they can't just interact with these kids. Yeah, um, but I mean, that prevents some of the creeps, but the real creeps would just sign up for the Jor app and fucking get in there anyways.

**[36:24] Speaker A:** So like, that's the part that I want to like really, really, really take care of, right?

**[36:29] Speaker B:** Like those, that, those are the novel concepts I want to explore is how to No family security in a game like this. Yeah, okay, let's, um, let me, let me—

**[36:43] Speaker A:** do you do Notion at all, or do you want, like, do you have a space where we could, like, type out ideas?

**[36:49] Speaker B:** I have, I have Notion, but I wonder if I can share my, uh, NotebookLM.

**[36:55] Speaker A:** I wonder if we can work off that together because I have this and I just did this under my projects. Where are you?

**[37:06] Speaker B:** Ah, where'd you go? Where did you— where did you go? Yeah, I don't know. I tried Notion and I was like, meh. I kind of like— yeah, I'm— I was looking at Obsidian as—

**[37:23] Speaker A:** oh, even better, let's do GitHub and then Not GIF. It's not a— what's it called? Uh, Mass Effect. Let's do— or do you have Premium or Pro for GitHub? Do you want to create a repo and then I like just put a space with docs and then—

**[37:49] Speaker B:** oh, I have a business. I have a business repo already set up.

**[37:53] Speaker A:** Can you add me?

**[37:55] Speaker B:** Yeah, let me find it. Oh, I thought I did. Hold on. Maybe that's just the images. Yeah, no, here it is. How do I add you? Settings. Contributors. See, I think I have to add you to the 3D Stories organization, which is fine anyways. Okay, don't steal my code before I send you an NDA. Uh, I know you won't. I wish we didn't have to like deal with that shit at all.

**[38:41] Speaker A:** Everybody—

**[38:41] Speaker B:** but we have to, we have to. It like it. And we only have to because it actually— it puts us into a sense of like security where we no longer have to even worry about that, right? Like, I don't, I don't want to have any thoughts in my head.

**[39:00] Speaker A:** I don't see it as a bad thing. Yeah, yeah, I just see it as an agreement.

**[39:05] Speaker B:** Okay, member, how do I do that? How do I—

**[39:10] Speaker A:** hold on, I share my screen. Okay, let me go to— I was gonna go to mine, but sure. People, people, invite member.

**[39:29] Speaker B:** Yep, invite member. You obviously see a button.

**[39:35] Speaker A:** You don't. Why? You are the only one who does. We recommend of 2 people. Oh, shit. Let's see.

**[40:03] Speaker B:** Uh, invitations. Is it maybe because I only have 1 seat?

**[40:08] Speaker A:** Probably.

**[40:09] Speaker B:** So I need to increase to 2 seats. Uh, add seats. Oh no, don't add 2 seats, add 1 seat. Oh, now I probably have— okay, hold on, refresh. Oh, now I have 3 seats. I don't want 3 seats.

**[40:34] Speaker A:** Down to 2 seats.

**[40:35] Speaker B:** Remove seats. Is that— no, like this.

**[40:41] Speaker A:** You're moving to 2.

**[40:43] Speaker B:** Yeah. Oh, remove seats. Yeah, there we go. Okay, so, so I have GitHub Pro. Does the organization have it, or Is that—

**[40:58] Speaker A:** no, I think you pay, you pay the org.

**[41:02] Speaker B:** So what's your username?

**[41:04] Speaker A:** J-A-M-I-R-O-S. J-A-M-I-R-O-S.

**[41:11] Speaker B:** I should probably change my I'll make you member until NDA. There, peace of mind. Perfect. Uh, okay, inbox. Now I want to— I want to change my name.

**[41:43] Speaker A:** How come it doesn't show me the org yet? All right, I'll poke around later. I'm gonna go eat because Nora already started eating.

**[42:11] Speaker B:** Okay, sounds good.

**[42:12] Speaker A:** Okay, I'll message you. Is WhatsApp okay just to like dump stuff in there, and then once I get the repo, I'll just put stuff in, in the, uh, on WhatsApp. Yeah, I'll do a little group.

**[42:25] Speaker B:** Yeah, do a little group, and then we can add her once we talk to her.

**[42:29] Speaker A:** Okay, sounds good.

**[42:30] Speaker B:** All right, bye.

**[42:32] Speaker A:** Peace. Bye.
