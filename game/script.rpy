
init python:
    def beepy_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("dialogueBlip.mp3")
        elif event == "slow_done":
            renpy.sound.stop()

    def drag_placed(drags, drop):
        if not drop:
            return

        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name

        return True

    def click_counter():
        global click_times
        global start_timer

        if click_times == 0:
            start_timer = True

        click_times += 1

    def reset_click_counter():
        global click_times
        global start_timer
        global countdown_time
        global count_clicks

        click_times = 0
        start_timer = False
        count_clicks = True
        countdown_time = 5

default badpoints= 0
default caff = 0
default kaff = 0
default faff = 0

default click_times = 0
default count_clicks = False
default start_timer = False
default countdown_time = 5

define c = Character("Candy", color="#1d7e42", callback=beepy_voice)
define m = Character("Me", color="#B20100", callback=beepy_voice)
define f = Character("Fish", color="#2b3b7f", callback=beepy_voice)
define t = Character("???", color="#105c53", callback=beepy_voice)

image candy = "defcan.png"
image candy surprised = "supcan.png"
image candy smirk = "smirkcan.png"
image candy look = "lookcan.png"
image fish = "deffish.png"
image fish eek = "eekfish.png"
image fish daring = "lookfish.png"
image fish serious = "srsfish.png"

image net = "netplace.png"
image castnet = "castnet.png"
image dynamite = "dynamite.png"
image fishie = "fishtopher.png"

image bg townent = "townEntrance.png"
image bg mnhouse = "mnhouseplacehold.png"
image bg mhouse = "mhouseplacehold.png"
image bg market = "market.png"
image bg cboat = "cboat.png"
image bg fboat = "fboat.png"
image bg mini1 = "mini1.png"

label start:

    scene bg townent with fade

    play music "MatenLasBallenas.mp3" volume 0.5

    m "I've finally arrived..."

    m "To the town named Salmontin."

    m "Smells like salmon. Not like too much like tin, though."

    m "The only thing reminiscent of tin here is me."

    m "Yep. Me. Tin is my name!"

    m "When I meet up with Candy, this town will have Tin and Candy...Tin Can!"

    m "I haven't talked to her in a good while, so I'm glad we're still good friends. Yay!"

    m "I bet she's really happy I'm moving into Salmontin."
    
    m "Salmontin? I wonder if anyone here is called \"Salmon.\" Or \"Fish.\""

    show candy with zoomin

    c "...Tin? Hey hey hey, Tin! You're here pretty early."

    m "Haha, yep! I'm kinda surprised too."

    c "Welcome to Salmontin, Tin! Hehe…"

    c "This is a great town, I'm glad you decided to move here!"

    c "And I'm also glad that you decided to become a fisher."

    c "Fishing life… It's something else."

    c "Do you like fish?"

    menu:
        "Yeah":
            "That's nice! Or not, depending on whether you like them dead or alive…"

        "Nope":
            show candy surprised
            c "Like, personally? If so, I have some good news for you…"

    show candy -surprised
        
    c "Y'know, I like fish both as an animal and as a dish. Speaking of fish..."

    c "I know you just got here, but we should fish now before it gets dark. It's best you learn how to fish as soon as possible."

    m "What's with the rush? Can't I get situated first? In my house?"

    c "The movers are still getting things ready. You were supposed to arrive tomorrow morning."

    c "Follow me, I'll carry your bags for you. I have some more supplies for you in my boat."

    scene bg cboat
    show candy at left
    with fade

    c "Welcome aboard matey! My grand green galleon!"

    m "...A galleon?"

    show candy surprised

    c "It's a type of ship...Like the one pirates have..You don't follow pirate lore?"

    m "?"

    show candy smirk
    c "...Moving on. This boat isn't a galleon by the way. And there aren't many pirates around these waters anyway."
    show candy -smirk

    c "And especially not in the spot we're at right now. Nice and uncrowded, good for beginner fishers like yourself."

    show castnet at Position(xpos=640, ypos=500) with easeinbottom
    c "This is a cast net. The the string part is called a handline."

    c "So what you do is hold one end of the handline and then throw the net into the water."

    c "The net has weights around it so it'll sink. Keep at tight grip so you don't drop the net."

    c "How about you try throwing it?"
    
    c "Please try to choose an area with not a lot of fish, though. Fish populations have been scarce recently and they need time to replenish."

    call screen castnet_game with pixellate
    hide castnet

    c "That was good for a beginner! Now we wait."

    c "In the meanwhile, I'll tell ya about responsible fishing practices. There's all types of rules and guidelines you have to follow."

    c "First of all, you should only fish in areas where you're allowed to."
    
    c "There will be areas where there's a sign that says fishing is prohibited. Don't go in those prohibited areas."

    c "They're prohibited for a reason! Fish populations need time to replenish, and there's also endangered species in those areas."

    c "Another rule among fishers! Don't fish more than the daily limit."

    c "Only catch as much fish as you can fit in one boat trip. That way the fish populations stay in check."

    c "And as a fisher, try your best to only catch fish. No sharks, turtles, or any of the like. And don't cause environmental damage."

    c "To do this, you need to use the right fishing methods."
    
    c "Don't use bottom trawls. Bottom trawls are nets dragged across the sea floor. Very destructive!"

    show candy surprised
    c "And don't use dynamite???? That is really illegal. But I've seen it happen, unfortunately."
    show candy smirk
    c "Best to stick with the methods I show you."
    show candy -smirk

    c "Oh, and one last rule. Don't work for big fisheries! You're plenty fine on your own."

    m "What are fisheries?"

    c "They're basically fishing businesses. A lot of 'em just care about profit, and only profit. The quotas are terrible and the work is very physically taxing."

    "(Some time later...)"

    c "Ok, the nets are full. Now pull your net in."

    c "Any questions so far?"

    m "Nope"

    c "Ok, that'll be it for today. Let's fish again tomorrow morning!"

    c "And let's stop by your house to see if it's done."

    scene bg mnhouse
    show candy
    with fade

    c "..Yep, seems good to me!"

    c "Well, see ya later, alligator!"

    m "See ya!"

    hide candy with easeoutright

    m "Home sweet home..."

    m "Looks just like my old home."

    scene bg mhouse with dissolve

    "The next day: Morning"

    m "Yawwwwn"

    m "...Who is that at the door?"

    show fish with fade

    f "Well hello there! Ny name's Fish!"

    show fish eek
    f "Welcome to Salmontin, Tin! (heheheh, tin tin...)"
    show fish -eek

    m "(Is everyone gonna say this?)"

    f "The town is very excited to get to know you. We've heard a bit about you already and you seem great."

    f "I'm offering fishing lessons for free, if you need any. I'd be more than happy to help, I love meeting new people and teaching people new things."

    m "One more fishing buddy couldn't hurt."

    f "You have one already? Who is..."

    show fish serious
    f "Oh."
    show fish daring

    f "Candy, right?"
    show fish -daring
    m "Yep."

    show fish eek
    f "Heh, I know her! She's one of the best fishers in town. Not as good as me though!"
    show fish -eek

    f "Y'know, you might hear some rumors about her, but I wouldn't pay them any mind. A lot of people stretch the truth."

    show fish daring
    f "And before you ask, no I won't tell you what those rumors are."
    show fish -daring

    m "(I was gonna ask...)"

    f "Don't mention it to her either, it makes her very upset."

    f "If it's alright with you, we could go on a little fishing trip today. After you get ready, of course!"

    f "The town is still working on getting you a boat, so in the meantime, you'll have to fish with all of us!"

    m "Let's go in the afternoon. Candy and I made plans to go fishing this morning."

    f "Ok, you can find me at the town market when you're done."

    scene cboat
    show candy at left
    with fade

    "Later..."

    c "It's nice to see you again, Tin."
    
    c "Since we caught quite a bit of fish yesterday, let's do some casual fishing next."
    
    c "It's important not to overfish! We'll catch fish one at a time with fishing rods."

    c "They're not very efficient for commercial fishing, but you still need to know how to use them efficiently. We use them for town fishing competitions!"

    c "First, we attach the bait to the hook. Then we cast the rod into the water and wait."

    c "When you feel a tug, reel it in!"

    c "Any questions in the meantime?"
    
    default canq1 = set()
    default knorumor = False
    $ cdone = False

    while not cdone:
        menu:
            set canq1
            "Good fishing methods?":
                $ knorumor = True
                show candy
                c "Hook-and-line fishing is good. They're basically lines with with hooks attached. There's many types of hook-and-line-fishing."
                
                c "Longlines, like the name implies, are long lines with a bunch of baited hooks attached. There's buoys keeping the line afloat."

                c "Another good fishing method is harpooning. You just aim and throw. It's very fun!"

                c "Any other questions?"

            "What does overfishing do?":
                $ knorumor = True
                show candy
                c "It depletes the population of marine species faster than they can reproduce. Messes up the whole ecosystem."

                c "Makes fishing harder for everyone. People can't get the fish they want and fishers struggle more and more to fish enough fish."

                c "They need to fish to make a living, but they're limited on what they can fish, so prices for fish have gone way up."

                c "Fishers aren't the only ones who rely on fish, people eat fish!! Most of our restaurants serve seafood, so they have to raise their prices as well."

                c "And those fishing subsidies sure don't help either!"

                c "Fishing subsidies are monetary grants given by the government to help fisheries. You'd think they help, but they don't!"

                c "All it does is encourage fisheries to overfish to make more money. Bad for everyone else, and for themselves too, but they can only think in the present moment, apparently."

                show candy surprised
                c "Even the fish were tired of it! They whispered to me..."
                show candy -surprised

                c "Oh! By the way, fishery means fishing industry, at least in general. Did I mention that already?"

                c "Any other questions?"

            "The rumors about you?" if knorumor == False:
                $ caff -= 1
                c "..."

                show candy look
                c "Who told you about that?"

                m "Fish told me. He wasn't specific though."

                show candy surprised
                c "He's one to talk! Rumor has it that he's the town's worst fisher!"
                show candy -surprised

                show candy look
                c "Not in terms of skill, but in terms of damage. He is demolishing the fish populations!"

                c "And sorry, I don't want to talk too much about my rumors. Just know that people have been slandering me."

            "No questions":
                show candy
                c "That's alright."

                c "Oh! I almost forgot. I need to tell you about this amazing new fishing technology, LED nets."

                c "They're nets with LED lighting that are great for targeting specific species since different LED colors attract different species."

                c "Different species have different responses to the different lights. Pretty cool!"

                c "They're also great at reducing bycatch! Bycatch is the unintentional capture of non-target species when trying to catch other species. It's against this town's rules to have too much bycatch."

                c "I've been introducing these nets to all the fishers in town. Since then, a lot less turtles have been caught in nets. Turtles are my favorite animal."

                $ cdone = True
                jump fishingRod

label fishingRod:
    
    "*Glub glub bubble bubble*"

    c "Oh?? A fishie? Reel it in!"

    call screen rod_game with pixellate

label contin1:
    c "Nice! That's a very good fish."

    c "That would sell for like, a decent amount of money."

    c "Oop! I've caught a fish too."

    c "Yay, it's pretty good as well!"

    c "This was a nice little fishing trip."

    menu:
        "You make it enjoyable":
            $ caff += 1
            show candy surprised
            c "Whaa-?"
    
            c "gashgfajdksgfjgfjhahaaAAAAA"
            show candy -surprised

            c "I enjoy your company too."

            c "You are a nice person, Tin."

            jump canRoute

        "It was so boring":
            show candy smirk
            c "..Oh..."

            c "..What did you find boring about it?"

            menu:
                "You":
                    $ caff -= 2
                    jump canless

                "No, it's just that I feel tired":
                    show candy

                    c "Ohhhhh. That makes sense, you just got here after all. And my condolences for what happened to your old house!"

                    jump canRoute

label canless:
    c "..."

    show candy look with hpunch

    c "Wow."

    c "I'm going to sail us back to the dock. Don't talk to me for a while, ok?"

    jump fishRoute

label canRoute:
    c "Let's head back to the dock, I'll show you where to sell your fish at."

    scene bg market
    show candy
    with fade

    c "This is the market!! We sell fish here."

    c "All you have to do is stand around and wait for someone to offer for your fish."

    t "Hey, I'll buy those fish from y'all for $20!"

    c "(Go for it!)"

    m "Sold!"

    t "Pleasure doing business with ya."

    c "See? Nice and easy. The townspeople here are reasonable, so you can usually agree to the first price offered."

    c "Keep the money, I insist."

    m "Thanks, Candy!"

    c "No problem, Tin."

    c "Y'know, just about everyone in this town is very welcoming and friendly."

    c "If anyone needs help, people will help. That's what I love about this town. We all look out for each other."

    c "Well, for the most part."

    c "Some people...really don't care about this town. Or about the world, it seems like."

    c "Just be wary of people's actions. Some people are very friendly, but very selfish too."

    c "..I know I said I wouldn't talk about this, but it's best you hear it from me."

    c "A couple months ago, there was an incident. There used to be a fisher in this town, a horrible fisher who used horrible fishing methods."

    c "One day, I caught this fisher using dynamite to fish. I reported them and they were sent to serve 15 years in prison."

    c "The problem was that this fisher was someone who donated a lot of money to the town."

    c "This person was very rich, so they were planning on getting out on bail, but I convinced the judges that what they did was too severe to allow for bail."

    c "A lot of people think the punishment was too severe. The fisher was quite young and had a bright future."

    c "It kind of makes me feel guilty."

    c "I was holding off on telling you about this incident because I worried it would affect how you view me."

    c "If you're still cool with me, we could fishing tomorrow. I'm could teach you sustainable fishing methods."

    m "Sure."

    c "Ok, that's nice."
    return

label fishRoute:
    scene bg market with fade

    m "..Candy really just disappeared."

    m "And I'm just here with a fish in hand."

    show fish with easeinbottom

    f "Hello there.."

    m "Hello"

    f "It's me, Fish."

    f "It's nice to meet you again."

    m "Thanks, it's nice to meet you again too."

    f "You've got a fish in your hands. Nice!"

    f "This place you're in right now is the market. You can just stand here and someone will buy fish from you."

    t "Hey, I'll buy that fish for $10!"

    f "That's a good price."

    m "Sold!"

    t "Pleasure doing business with ya."

    f "That was quick."

    f "..So, what do you think? About fishing with me?"

    menu:
        "I heard you're a bad fisher":
            jump ft1

        "Sure!":
            jump ft2

label ft1:
    
    show fish daring
    f "Oh really?"
    show fish -daring

    f "You shouldn't believe everything you hear, you know."

    f "That fact? It may be true, it may not be."

    f "Want to find out?"

    menu:
        "..Ok":
            jump ft2

label ft2:
    f "Great! Then we'll fish right now! I've got food on my boat if you're hungry."

    scene bg fboat
    show fish at left
    with fade

    f "Welcome to my humble boat. I'm what you call a classic fisherman. Boat made of wood, heart made of fish."

    m "What.."

    f "My name is Fish"

    m "I know"

    f "I eat fish too. I'm a cannibal."

    menu:
        "That's fine with me":
            f "Hehe, glad you're open-minded!"
            $ faff += 1

        "Weird....":
            $ faff -= 1
            show fish daring
            f "Well, it's not like I'm a human cannibal!"
            
            show fish eek
            f "Humans are too precious for that. I don't support the human meat industry!"

    show fish
    f "Anyway, let's get fishing. I got some bottom trawls we can use."

    menu:
        "Sounds good!":
            f "That's the spirit!"
            $badpoints += 1

        "Can we use something else?":
            m "Bottom trawling is really bad for the environment and the fishies, so I don't want to do that."

            show fish serious
            f "Says who? I've been bottom trawling for 20 years and there are still fish in the ocean!"

            m "Candy said so."
            
            f "Really?"

            show fish -serious
            f "..Now that I think about it, I move towns whenever fish get scarce..."

            f "And I've moved like 21 times.."

            m "No one ever told you this before?"

            f "Well, I mainly fish at night when no one's around. And when people approach I slip away quick."

            f "I don't like when people accuse me of doing bad stuff! I'm just fishing..."

            f "So what do you suggest we use? I've got a bunch of fishing equipment."
            
            default fishq1 = set()
            $ fdone = False

            while not fdone:
                menu:
                    set fishq1
                    "Fishing rods?":
                        f "Too little fish. I'm trying to teach you how to make a living, we need something more effective."

                    "Cast nets?":
                        $ fdone = True
                        f "I have some of those."
                        jump castnet

                    "LED nets?":
                        $ fdone = True
                        f "What are those?"
                        
                        menu:
                            "It's so you don't need a flashlight":
                                $ faff -+ 1
                                f "Oh! What??"

                                show fish daring
                                f "Sorry, but that sounds really stupid."
                                show fish -daring

                                f "Let's just use regular ol' cast nets."
                                jump castnet
                            
                            "The lights can target different species":
                                f "Oh! That's very useful."

                                f "Now that I think about it, I remember Candy telling me something about that."

                                f "She might've given me some of those things."

                                m "What's your opinion on Candy?"

                                f "Candy's a preachy nature activist."

                                f "Half of what she says feels like virtue signaling."

                                f "\"Oh look at me! I care about the environment and global warming and the animals!\""

                                show fish serious
                                f "Makes me want to pour kerosene everywhere."
                                show fish -serious

                                f "Though, she is kind to me, even though we don't see eye to eye on a lot of things. She's a good person."

                                show fish daring
                                f "Too bad I'm not! There's gotta be some bad in this world too. Makes you appreciate the good."
                                show fish -daring

                                f "This is getting off-task. Lets cast the nets first, then talk. I'm going to try to find the LED nets."
                                jump lednet

label bottomtrawl:
    hide fish with easeoutbottom
    f "Hmm.. yep."

    show fish at left with easeinbottom
    f "Here they are!"

    f "I use these nets all the time! Do you know how to use them?"

    m "Nope"

    f "Then I'll show you."

    "PLACEHOLDER TEXT - TIMESKIP :3"

    f "Nice haul! It's got a bit of debris in there, but no harm no done!"

    m "I agree with and fully endorse whatever that statement was."

    f "We're on a roll! Let's use some dynamite to really show these fish who's boss!"

    menu:
                "I've always wanted to do this":
                    f "Heh! Your dream is just about to come true."

                    jump dynamiteRoute
                    
                "What? No!":
                    show fish daring
                    f "What? Never had fun before? Had too much fun already? Come on!"

                    "..."

                    show fish -daring
                    f "If you insist, then let's head back to the market."

label castnet:
    hide fish with easeoutbottom
    f "Hmm.. yep."

    show fish at left
    show castnet at Position(xpos=640, ypos=500)
    with easeinbottom
    f "Here they are!"

    f "Do you know how to use cast nets?"

    m "Yep!"

    f "Ok then, let's get fishing."

    call screen castnet_game with pixellate
    hide castnet

    f "Hm. Good technique."

    f "Considering you are already familiar with cast nets, would you be up to using another fishing method? Y'know, trying something new?"

    menu:
        "We've fished plenty":
            f "Come on..You need to learn fishing sooner or later."

            menu:
                "No thanks":
                    f "Ok, let's head back to the market. You've got your whole life to learn, no need to rush."

                "I said no you old fool":
                    $ faff -= 2
                    show fish daring with hpunch
                    f "Whoa there!"

                    f "I'm not that old! I'm only 55."

                    f "Alrighty then, let's head back to the market."

                    show fish serious
                    f "Kids these days..."

            scene bg market
            show fish
            with fade

            f "We've got a decent amount of fish to sell."

        "Yeah!":
            f "What an eager soul!"

            f "Let's use dynamite. Don't worry about blowing up, I'm an expert."

            menu:
                "What? No!":
                    show fish daring
                    f "What? Never had fun before? Had too much fun already? Come on!"

                    "..."

                    show fish -daring
                    f "If you insist, then let's go back to the market..."

                "I've always wanted to do this":
                    f "Heh! Your dream is just about to come true."

                    jump dynamiteRoute

label lednet:
    hide fish with easeoutbottom
    f "Hmm.. yep..."

    show fish at left
    show net
    with easeinbottom
    f "..Here they are!"

    f "Can you configure them?"
    hide net with zoomout
    f "Now we wait."

    f "Is this your first time living in a coastal town?"

    m "Yeah."

    f "Salmontin is a good first impression, yeah? That's due to our townsfolk. Everyone works together to make this town the way it is."

    f "The townsfolk here are so friendly with the plants and animals that I almost can't fathom it. Disgusting."

    menu:
        "How so?":
            $ faff += 1
            f "..Hm."

            show fish serious
            f "It's so peaceful it's boring."

            f "I can't do anything in this town without getting in trouble."

            f "Candy would get me a life sentence in jail."

            m "Really?"
            show fish -serious
            f "Probably! She got a guy sentenced to 15 years in prison for dynamite fishing."

            show fish serious
            f "How absurd! They're just fish! I don't see what the big deal is."
            show fish -serious

            menu:
                "It affects the whole ecosystem":
                    m "The dynamite blows up the plants and everything else too!"

                    m "Without those plants and other marine species, other species can't get enough nutrients need to survive."

                    m "So then those species start dying too and even more species are affected. It creates a chain reaction."

                    m "Doesn't this town rely on seafood?"

                    f "I guess it does. I see your point."

                "You are stupid":
                    m "It obviously affects the entire ecosystem. Dynamite explodes stuff, you know?"

                    show fish serious
                    f "You're so pretentious. Petulant fool."

                    f "I'd throw you overboard so you could be one with the ecosystem, but unfortunately that would count as attempted murder."
                    show fish daring
                    f "Heh! You are truly a friend of Candy. As soon as we reach the dock, you better be off my boat before I even blink."
                    
                    jump candyRoute
                    
        "That's rich coming from you":
            $ faff -= 1
            f "Heh!"

            f "I know what I'm viewed as and I simply don't care."

    return

label dynamiteRoute:
    hide fish with easeoutbottom
    f "Let me see where I put them..."

    show fish at left
    show dynamite at Position(xpos=640, ypos=400)
    with easeinbottom
    
    f "Aha! Haven't used these in a long time. It's been a few months."

    "placeholder timeskip o_o"
    hide dynamite with zoomout

    f "Oh shoot."

    t "Hey!! No dynamite allowed!!"

    f "Welp. This is why I fish at night. See ya in jail."

    scene bg void with fade

    "(Ring ring)"

    ".."

    c "..Hey Tin. How's it going?"

    c "Um, I have some good news for you. You'll get a lesser sentence than Fish."

    c "Yeah, we've been collecting evidence and we have a strong case against him."

    c "I just can't believe you would use dynamite. Fish coerced you into it, right?"

    menu:
        "Yes (lie)":
            m "I was scared."

        "No (truth)":
            m "I wanted to blow things up."

    c "..I see."

    c "Thanks for the information. I have to go now, Tin. Bye."

    m "Bye."

    c "..Wait."

    c "Before I hang up, I have to tell you."

    m "What?"

    c "You're an idiot."

    c "You decide to use dynamite? After I told you not to? Please, Tin..."

    c "There's barely anything in the ocean now. Our income, our food sources, all gone."

    c "Your little stunt pushed our ecosystem off the edge and now there's nothing left."

    c "But hey! Don't worry, you'll spend a few less years in jail than Fish."

    c "Though considering the damage done, those extra years won't matter."

    c "Have a good one, Tin."

    menu:
        "You too":
            m "You-"

        "You're so annoying":
            m "You-"

    "(Click)"

    "The End"

    return

label candyRoute:
    scene bg market with fade

    m "His stare is so scary.."

    show candy with moveinright

    c "Hey, Tin."

    c "I've been looking for you. Where did you go?"

    m "I went fishing with Fish."
    show candy surprised
    c "FISH?!?!?!?!"

    m "I don't think I'll be fishing with him ever again."
    show candy smirk
    c "That's a relief."
    show candy -smirk
    c "What happened?"

    m "I called him stupid because he didn't get why using dynamite to fish was bad."

    c "That's crazy. How'd that topic even come up? Haha.."

    m "You sentenced someone to 15 years in jail because of it?"
    show candy smirk
    c "Oh, he told you about that? Just so you know, that's not entirely accurate."
    show candy -smirk
    c "I'm not judge, jury, or executioner, I'm just a caring citizen."

    c "All I did was ensure that they could not get out on bail."

    c "They still have parole and I had nothing to do with the length of the sentence."
    show candy look
    c "Anyways...About our last fishing trip.."
    show candy -look
    m "Sorry about that, I was too harsh. Fishing talk just bores me."

    c "With all due respect, why are you a fisher then?"

    m "I never wanted to be a fisher. This is just a fishing town."

    menu:
        "I lowkey don't even like you":
            c "Wow."

            c "????"

        "But I'm adjusting":
            m "I guess I'm a little on edge ever since my house burned down."













screen castnet_game:
    add "mini1.png"

    draggroup:
        drag:
            drag_name "fishschool"
            child "fishieschool.png"
            xpos 0.08
            ypos 0.5
            draggable False
            droppable True
        drag:
            drag_name "fishgroup"
            child "fishiegroup.png"
            xpos 0.75
            ypos 0.5
            draggable False
            droppable True
        drag:
            drag_name "castnet"
            child "castnet.png"
            xpos 0.35
            ypos 0.30
            drag_raise True
            draggable True
            droppable False
            dragged drag_placed

screen rod_game:
    imagebutton idle "cboat.png" sensitive count_clicks action Function(click_counter)
    text "Click mouse or press SPACE as much as you can!" align (0.5, 0.10) size 35
    text "Press button below to start - Get to 30 Power!" align (0.5, 0.20) size 35
    key "K_SPACE" action If(count_clicks, Function(click_counter), NullAction())
    text "Power: [click_times]      Time left: [countdown_time]" align (0.5, 0.65) size 25
    
    if not count_clicks:
        if click_times < 30:
            frame:
                align (0.5, 0.45)
                padding (25, 15)
                textbutton "Start Reeling" action Function(reset_click_counter)
        elif click_times > 50:
            text "Ez!" align (0.5, 0.45) size 30
            frame:
                align (0.5, 0.75)
                padding (25, 15)
                textbutton "Continue" action [Hide("rod_game"), Jump("contin1")]
        else:
            text "Fish caught!" align (0.5, 0.45) size 30
            frame:
                align (0.5, 0.75)
                padding (25, 15)
                textbutton "Continue" action [Hide("rod_game"), Jump("contin1")]

    if start_timer:
        timer 1.0 action If(countdown_time > 0, SetVariable("countdown_time", countdown_time - 1), SetVariable("count_clicks", False)) repeat countdown_time > 0