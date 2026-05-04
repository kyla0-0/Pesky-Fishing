
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

default badChoice = False
default caff = 0
default faff = 0

default click_times = 0
default count_clicks = False
default start_timer = False
default countdown_time = 5

define c = Character("Candy", color="#1d7e42", callback=beepy_voice)
define m = Character("Me", color="#B20100", callback=beepy_voice)
define f = Character("Fish", color="#2b3b7f", callback=beepy_voice)
define t = Character("???", color="#ae7906e0", callback=beepy_voice)

image candy = "defcan.png"
image candy lt = "defcanLate.png"
image candy surprised = "supcan.png"
image candy surprised lt = "supcanLate.png"
image candy smirk = "smirkcan.png"
image candy smirk lt = "smirkcanLate.png"
image candy look = "lookcan.png"
image candy look lt = "lookcanLate.png"
image fish = "deffish.png"
image fish lt = "deffishLate.png"
image fish eek = "eekfish.png"
image fish eek lt = "eekfishLate.png"
image fish daring = "lookfish.png"
image fish daring lt = "lookfishLate.png"
image fish serious = "srsfish.png"
image fish serious lt = "srsfishLate.png"

image lednet = "lednetLate.png"
image castnet = "castnet.png"
image trawlNetSide = "trawlNetSide.png"
image dynamite = "dynamite.png"
image litDynamite = "litDynamite.png"
image fishie = "fishtopher.png"
image fishSilhouettes = "fishSilhouettes.png"
image seaPlants = "seaPlants.png"

image bg townent = "townEntrance.png"
image bg mhouse = "mhouse.png"
image bg market = "market.png"
image bg cboat = "cboat.png"
image bg cboatlt = "cboatLate.png"
image bg fboat = "fboat.png"
image bg flash = "flash.png"
image bg purple = "purple.png"
image bg mini1 = "mini1.png"
image bg seaFloor = "seaFloor.png"

label start:
    scene bg townent with pixellate
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
    c "Y'know, I like fish as an animal but not as a dish. I don't like the taste of seafood in general."
    
    c "Speaking of seafood and fish..."

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

    scene bg mhouse
    show candy
    with fade

    c "..Yep, seems good to me!"

    c "Well, see ya later, alligator!"

    m "See ya!"
    hide candy with easeoutright
    m "Home sweet home..."

    m "Looks just like my old home."

    m "It even has the spider web in the corner!"

    scene bg mhouse with fade

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

            "The rumors about you?":
                if knorumor == False:
                    $ caff -= 1

                c "..."

                show candy look
                c "Who told you about that?"

                m "Fish told me. He wasn't specific though."

                show candy surprised
                c "He's one to talk! Rumor has it that he's the town's worst fisher! According to me at least."
                show candy -surprised

                show candy look
                c "Not in terms of skill, but in terms of damage. He is demolishing the fish populations!"

                c "And sorry, I don't want to talk too much about my rumors. Just know that people have been slandering me."

            "No questions":
                show candy
                c "That's alright."

                c "Oh! I almost forgot. I need to tell you about this amazing new fishing technology, LED nets."

                c "They're nets with LED lights attached to the perimeter. They're great for targeting specific species since different LED colors deter different species."

                c "Green lights deter sea turtles, and blue lights deter small cetaceans, which are whales, dolphins, and porpoises."

                c "This is great for reducing bycatch! Bycatch is the unintentional capture of non-target species when trying to catch other species. We only want to catch fish, not creatures like turtles."

                c "I've been introducing these nets to all the fishers in town. Since then, a lot less turtles have been caught in nets. Turtles are my favorite animal."

                c "I don't have one right now, but I'll get some more soon."

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

    c "I'm gonna sail us back to the dock. Don't talk to me for a while, ok?"

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

    c "You can keep the money."

    m "Thanks, Candy!"

    c "No problem, Tin."

    c "Y'know, just about everyone in this town is very welcoming and friendly."

    c "If anyone needs help, people will help. That's what I love about this town. We all look out for each other."
    show candy look
    c "Well, for the most part."

    c "Some people...really don't care about this town. Or about the world, it seems like."

    c "Just be wary of people's actions. Some people are very friendly, but very selfish too."

    if knorumor == False:
        c "..I know I said I wouldn't talk about this, but it's best you hear the real story from me."
    else:
        c "I don't know if you heard, but there are some rumors about me. It's best you hear the real story from me."

    c "A couple months ago, there was an incident. There used to be a fisher in this town, a horrible fisher who used horrible fishing methods."

    c "One day, I caught this fisher using dynamite to fish. I reported them and they were sent to serve 5 years in prison."

    c "The problem was that this fisher was someone with a good reputation. They donated a lot of money to the town."

    c "This person was very rich, so they were planning on getting out on bail, but I convinced the judge that what they did was too severe to allow for bail. Y'know, small town things."

    c "The culprit had to wait in jail for a long time because their trial kept getting delayed."

    c "A lot of people think the punishment was too severe. This fisher was quite young and had a bright future."

    c "It kind of makes me feel guilty."

    c "I was holding off on telling you about this incident because I worried it would affect how you view me."
    show candy -look
    c "If you're still cool with me, we could fishing tomorrow. I could teach you sustainable fishing methods."

    m "Sure."

    t "Hey Candy!!! You suck!! How can you live with yourself?!"

    c "Hold on one second, Tin. I'll be right back, I need to go kick someone real quick."
    hide candy with easeoutleft
    m "What"
    show fish daring at right with easeinright
    f "Hello again…"
    show fish -daring at center with ease
    f "Are you ready to go fishing with me yet?"

    m "I'm waiting for Candy."

    f "Oh, that's fine. I'll wait for her too."

    t "YOWCH!"
    show candy smirk at left with easeinleft
    c "Hey, Fish."
    
    f "Hey, Candy."
    show candy -smirk
    f "I'm planning on taking Tin to go fishing now."
    show candy surprised
    c "Oh, really? I'll come with you two, then! That'd be fun, right?"
    show candy -surprised
    c "Sure. Let's take my boat."

    f "Actually, can we go to the pub first, though? It'd be fun!"

    m "Burger?"

    f "Lots of them!"

    m "I'm in."

    c "I'm in too."

    scene bg cboatlt
    show candy lt at left
    show fish lt at center
    with Fade(0.5, 0.5, 0.5)

    c "That was a great several hours spent."

    f "I didn't know y'all were so fun to be around!"

    c "You're really fun to be around too, Fish."
    show fish lt eek
    f "Aw shucks!"
    show fish lt -eek
    f "Now what are we gonna do on this fishing trip? I could teach you some new stuff, Tin. What have you taught Tin already, Candy?"

    c "I've taught Tin about the town's fishing rules and some good fishing methods."

    f "Ok, have you taught Tin about bottom trawling yet?"

    c "Yes, I've taught that it's bad!"
    show fish lt serious
    f "Don't hate on one my favorite fishing methods..."
    show candy lt smirk
    c "Don't you know it's really harmful for the ecosystem? It has an insane amount of bycatch."

    c "Everything gets caught in the trawl nets...Plants, animals...How can the ecosystem recover from the loss of so much stuff?"
    show candy lt -smirk
    show fish lt -serious
    f "..I never thought of it that way."

    f "Then what do you suggest we use instead?"

    c "Oh! Do you still have those LED nets I gave you?"

    f "I'll have to check."
    hide fish lt with easeoutbottom
    f "Hmm.. Yep..."

    f "Ooh, the lights are green!"
    show fish lt
    show lednet at Position(xpos=640, ypos=500)
    with easeinbottom
    f "Here it is!"

    m "What do the lights do again?"

    c "Green lights deter sea turtles, and blue lights deter small cetaceans, which are whales, dolphins, and porpoises."

    f "There are usually lots of turtles during this hour. Let's stick with green lights."
    hide lednet with easeoutright
    c "While we wait, let's catch up. How have y'all been?"

    menu:
        "Good":
            c "That's good to hear!"

        "Bad":
            f "Why? Did something happen?"

            m "I'd rather not talk about it."

            f "Ok."

        "I don't know":
            c "That's ok, I know life has been stressful for you lately."

    f "I've been doing fine."

    c "That's good."

    m "How have you been, Candy?"

    c "Good. I've been having lots of fun fishing with you."
    show fish lt daring
    f "Heh! I don't know if Tin has been having fun with you, though. The way you fish is so boring."
    show fish lt -daring
    show candy smirk lt with hpunch
    c "Well at least I don't leave carnage everywhere I fish, Fish!"
    show fish lt daring
    f "Oh? Since when have you ever seen me fish?"

    c "I don't have to see you fish to know that you've fished. I can tell by how much damage you leave behind!"

    f "Why are you blaming me for all of the so called \"damage\" around here?! It's not just me."
   
    c "What do you mean \"so called\"?? Don't you notice the lack of fish and other stuff in the sea??"

    f "Yeah, but not as much with the way I fish, I don't. If you're lacking fish, then don't blame me, blame yourself for not fishing better."

    c "Sure sure, keep it up. Soon even your fishing methods won't work when there's literally no fish."

    c "You're literally selFISH. By fishing basically all of what's left of our ecosystem, you're making it harder for anyone else to catch fish."

    f "You're being dramatic. There are still plenty of fish. And what does it matter to me? I can always move and other people can too."

    c "Are you serious? No, not everyone can afford to move, and part of it is because you make it so hard to catch enough fish to make a living."

    f "There are plenty of other jobs in Salmontin."

    c "Are you really saying other people should find different jobs when the reason they have to is because of you?"

    f "Listen here Candy, if you want to save the ecosystem or whatever so badly, then you should stop fishing. And stop forcing other people to fish."

    c "I need the money from fishing, I have responsibilities. You wouldn't get it. Tin does too, that's why I'm teaching Tin how to fish SUSTAINABLY. I'm not gonna stop because of you."

    f "Hey Tin, do you even like fishing?"

    menu:
        "Yeah":
            show fish lt serious
            c "See? Why do you want us to be miserable? Fishing is awesome."

            f "Yeah yeah whatever."
            show candy lt -smirk
            c "And besides, how are we gonna promote sustainable fishing if we're not fishers ourselves? We need to be reputable and respected fishers."

            f "I get your point. But why are you trying so hard to protect the environment? There are plenty of them around, I don't see what's special about this one."

            c "This town relies on the fishing industry. Half the places here serve seafood and a good chunk of our money comes from exporting fish."

            c "If the source of our profit is destroyed, then our town basically is too."
            show fish lt daring
            f "Hm. I might understand now."
            show fish lt -daring
            f "This town is basically fish city. I mean, it's called Salmontin. If there were no fish, it'd just be called Tin!"

            f "Not that being called Tin is a bad thing, heh."

            f "I guess I can't let Salmontin become Nothingtin. I'd hate to see the pub get shut down, they have good fish fillets. I'll start being careful with my fishing."

            m "Yay!"

            c "I'm glad. There's no Salmontin without you, Fish!"
            show candy lt surprised
            c "Get it? Ha, because your name is Fish and there's a lot of fishes in Salmontin?"
            show candy lt -surprised
            m "I get it!"

            f "Good pun, kid."

            c "(Yes! Pun successful!)"

            scene bg townent with Dissolve(1.5)

            m "This was the day that changed my life."

            m "Candy, Fish, and I became besties."

            m "I was worried I wouldn't fit in at Salmontin, but I was wrong. I found people I could be myself with."

            m "We started going on fishing trips together often."

            m "Salmontin relies on a strong marine ecosystem for food and money, so we only fish as much as we need to. We've set an example for the whole town."

            m "We use nets with LED lighting when fishing so that nothing other than our target species gets caught. This helps keep our ecosystem stable."

            m "We make sure each of us has sustainable fishing habits because every action of ours builds up."
            
            m "Us and the rest of the fishing community keep watch and confront people fishing unsustainably."

            m "Candy's reputation has improved now that people realize how much overfishing affects Salmontin. She has made a lot of new friends."

            m "And Fish is really good at catching bad fishers, he always knows where to find them. We've persuaded tons of bad fishers to change their ways."

            m "Over time, we've noticed a decrease in overfishing and an increase in fish populations."

            m "I love Salmontin. I found a community that I'm accepted in."

            m "The End (Community Ending)"

            return


        "No":
            show candy lt look
            show fish lt -daring
            f "See? Tin doesn't like to fish, so you should stop forcing Tin to fish. One less environmental impact."

            c "I had no idea..."

            c "I'm sorry Tin, I guess I never asked you if you really wanted to fish."
            show candy lt -look
            c "What would you like to do instead? I'm not on good terms with many people but I'll try to get you a job."

            menu:
                "Bartender":
                    c "I know a club that could use one. No problem!"

                    m "Let's head there after this fishing trip. We can hang out there."

                    f "I'm coming along."

                    c "Sure. But only if you follow my advice on fishing sustainably."

                    f "Deal. You'll have to teach me how, though."

                    c "I will, and don't forget, I will know if you break your end of the deal."

                    f "Alrighty then."

                    scene bg townent with Dissolve(1.5)

                    m "This was the fishing trip that changed my life."

                    m "We had a blast at the bar. Candy and Fish worked out their differences and became good friends."

                    m "He said he enjoyed our company and that we made this town worth staying in. We all became besties for life!"
                    
                    m "He wanted to make sure Salmontin stays lively, so he stopped using harmful fishing practices and fishing in prohibited areas."

                    m "I'm really happy here. We all go on a lot of fun adventures around town and at the club where I work."

                    m "As a bartender, I chat with lots of people. I've been able to convince people to stop judging Candy so harshly, and thus we've made a lot more friends and aquaintances."

                    m "Eventually, Candy started working part time at the club as security. She makes sure no one hurts anybody. She's built up a lot of strength from fishing, so no one messes with her either."

                    m "She's still a fisher though, she just uses her earnings from the club to buy sustainable fishing equipment for everyone."

                    m "Salmontin relies on a strong marine ecosystem for food and money, so we as a town only fish as much as we need to."

                    m "Even though I don't like fishing myself, I still support my fisher friends with things related to it."

                    m "We use LED nets when fishing so that nothing other than our target species gets caught. This helps keep our ecosystem stable."

                    m "We make sure each of us has sustainable fishing habits because every action of ours builds up. The fishing community and I keep watch and confront people fishing unsustainably."

                    m "Fish is really good at catching bad fishers, he always knows where to find them. We've persuaded tons of bad fishers to change their ways."

                    m "Over time, we've noticed a decrease in overfishing and an increase in fish populations."

                    m "I love Salmontin. You're accepted whether you like fishing or not."

                    "The End (Tender Ending)"

                    return

                "Detective":
                    c "That's cool! Salmontin could use someone who can figure out who keeps overfishing."
                    show fish lt daring
                    f "Let's hope you're not too good, heheh."
                    show fish lt -daring
                    c "Got any ideas?"

                    m "We could put GPS tracking technology on boats that tell us their location. We could monitor them to make sure they're not fishing in prohibited areas."

                    m "We could also use the info to figure out who could be overfishing and investigate them."

                    m "Could we work out something with the mayor to implement this?"

                    c "I'm sure we could. Great idea, Tin!"

                    f "You're smarter than you look, kid."

                    m "Thanks guys!"

                    scene bg townent with Dissolve(1.5)

                    m "And so, I started an investigative team that focused on Salmontin's fishing industry."

                    m "Candy and Fish were on my team. Fish was reluctant at first, but he became cooperative when I convinced him it'd be like Sherlock. I barely know anything about Sherlock."

                    m "With the help of my friends and the mayor, all of Salmontin's fishing vessels were equipped with tracking technology."

                    m "I recruited more people to my team so we could analyze vessel data, note patterns, and investigate suspicious activity."

                    m "We got real-time alerts every time a vessel was in a prohibited area, allowing us to take swift action."

                    m "We could use our data to set appropriate regulations."

                    m "Due to my team's efforts, populations of fish and other sea creatures started to increase."

                    m "We've noticed a decrease in overfishing and people using harmful fishing methods."

                    m "It's really fun to investigate stuff with my besties, Candy and Fish. We go on undercover operations all the time."

                    m "I love Salmontin."

                    "The End (Detective Ending)"

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
        "How do I know you're a good fisher?":
            f "There's only one way to find out. If you've gotta see to believe, then so be it."

            menu:
                "..Ok":
                    jump fishTrip

        "Sure!":
            jump fishTrip

label fishTrip:
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

    m "( Hmm..Didn't Candy say that those were bad for the environment?)"

    menu:
        "Sounds good!":
            f "That's the spirit!"
            $ badChoice = True
            jump bottomtrawl

        "Can we use something else?":
            m "Bottom trawling is really bad for the environment and the ecosystem, so I don't want to do that."

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
                                $ faff -= 1
                                f "Oh! What??"
                                show fish daring
                                f "Sorry, but that sounds really stupid."
                                show fish -daring
                                f "Let's just use regular ol' cast nets."
                                jump castnet
                            
                            "The lights can target specific species":
                                f "Oh! That's very useful."

                                f "Now that I think about it, I remember Candy telling me something about that."

                                f "She might've given me some of those things."

                                m "What's your opinion on Candy?"

                                f "Candy's a preachy nature activist."

                                f "Half of what she says feels like virtue signalling."

                                f "\"Oh look at me! I care about the environment and global warming and the animals!\""
                                show fish serious
                                f "Makes me want to pour kerosene everywhere."
                                show fish -serious
                                f "Though, she is kind to me, even though we don't see eye to eye on a lot of things. She's a good person."
                                show fish daring
                                f "Too bad I'm not! I'm so wicked."
                                show fish -daring
                                f "This is getting off-task. Lets cast the nets first, then talk. I'm gonna try to find the LED nets."
                                jump lednet

label bottomtrawl:
    f "I bottom trawl all the time, so I've got it half set up already. I've got one end attached to the back of my boat."
    hide fish with easeoutbottom
    f "I just need to throw the rest of the net into the water."
    show fish at left with easeinbottom
    f "Done. Now we sail the boat forward."

    scene bg seaFloor
    show seaPlants
    show fishSilhouettes
    with pixellate
    show trawlNetSide with easeintop
    show trawlNetSide with Dissolve(0.2)
    hide seaPlants
    hide fishSilhouettes
    hide trawlNetSide
    with easeoutright

    scene bg fboat
    show fish at left
    with fade

    f "Nice haul! It's got a bit of debris in there, but no harm no done!"

    m "I agree with and fully endorse whatever that statement was."

    f "We're on a roll! Let's use some dynamite to really show these fish who's boss!"

    menu:
                "I've always wanted to do this":
                    f "Heh! Your dream is just about to come true."

                    jump dynamiteEnd
                    
                "What? No!":
                    show fish daring
                    f "What? Never had fun before? Had too much fun already? Come on!"

                    menu:
                        "That would get us in trouble":
                            show fish -daring
                            f "I guess it would get us in big trouble. You're right, it's better not to risk it."

                        "You have the brain of a plankton":
                            f "Sheldon J. Plankton! Not everyone can comprehend my genius."
                            $ faff -= 2

                    f "Let's head back to the market."

                    jump steadyEnd

label castnet:
    hide fish with easeoutbottom
    f "Hmm.. yep."

    show fish at left
    show castnet at Position(xpos=640, ypos=500)
    with easeinbottom
    f "Here it is!"

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
                    f "Ok, let's head back to the market when the net's full. You've got your whole life to learn, no need to rush."

                "I said no you old fool":
                    $ faff -= 2
                    show fish daring with hpunch
                    f "Whoa there!"

                    f "Listen here kid, I'm not that old! I'm only 55."

                    f "Alrighty then, we'll head back to the market when the net's full.."
                    show fish serious
                    f "Kids these days..."

            jump steadyEnd

        "Yeah!":
            f "What an eager soul!"

            f "Let's use dynamite. Don't worry about blowing up, I'm an expert."

            menu:
                "What? No!":
                    show fish daring
                    f "What? Never had fun before? Had too much fun already? Come on!"

                    "..."
                    show fish -daring
                    f "If you insist, then let's go back to the market when we're done."
                    
                    jump steadyEnd

                "I've always wanted to do this":
                    f "Heh! Your dream is just about to come true."

                    jump dynamiteEnd

label lednet:
    hide fish with easeoutbottom
    f "Hmm.. yep..."
    show fish at left
    show castnet at Position(xpos=640, ypos=500)
    with easeinbottom
    f "..Here it is!"

    f "Can you turn the lights on?"

    m "Yessir!"

    f "Here you go."
    hide castnet with easeoutbottom
    f "How do the lights work if it's daytime? Isn't the sunlight too strong near the surface?"

    m "Oh."

    f "That's alright. Let's use this net anyway."

    f "Let's chat a bit. Is this your first time living in a coastal town?"

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
            f "Probably! She got a guy sentenced to 5 years in prison for dynamite fishing."
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
                    $ faff -= 2
                    m "It obviously affects the entire ecosystem. Dynamite explodes stuff, you know?"
                    show fish serious
                    f "You're so pretentious. Petulant fool."
                    f "I'd throw you overboard so you could be one with the ecosystem, but unfortunately that would count as attempted murder."
                    show fish daring
                    f "Heh! You are truly a friend of Candy. As soon as we reach the dock, you better be off my boat before I even blink."
                    
                    jump stubbornEnd
                    
        "That's rich coming from you":
            $ faff -= 1
            f "Heh!"

            f "I know what I'm viewed as and I simply don't care."

    f "Looks like the net has caught enough fish now. Let's return to the market."

    jump steadyEnd

label dynamiteEnd:
    hide fish with easeoutbottom
    f "Let me see where I put them..."
    show fish at left
    show dynamite at Position(xpos=640, ypos=400)
    with easeinbottom
    f "Aha! Haven't used these in a long time. It's been a few months. I had to flee the last town I used it at."
    hide dynamite
    play sound "tssss.mp3"
    show litDynamite at Position(xpos=640, ypos=400)
    with Dissolve(2.0)
    f "It's lit! You got a good throwing arm?"

    m "They call me the pitcher."
    hide litDynamite with easeoutright
    f "Nice throw! Now we wait for the dynamite to sink..."
    play sound "explosion.mp3"
    scene bg flash with vpunch
    scene bg fboat
    show fish at left
    with dissolve
    f "Let's sail over there now and collect the fish."

    f "..Wait."
    show fish serious
    f "Oh shoot."

    t "Hey!! No dynamite allowed!!"
    show fish -serious
    f "Welp. This is why I fish at night. See ya in jail."

    scene bg purple with fade
    stop music fadeout 5.0
    m "Come on, pick up..."

    "(...)"

    m "Hey Candy, it's Tin. I'm calling from prison."

    c "..Hey."

    c "You ok?"

    m "Not really."

    c "Well um, I have some good news for you. Seems like you'll get a lesser sentence than Fish."

    c "Yeah, we've been collecting evidence and we have a strong case against him."

    c "I just can't believe you would use dynamite. Fish coerced you into it, right?"

    menu:
        "Yes (lie)":
            m "I was scared."

            c "..I see."

        "No (truth)":
            m "I wanted to blow things up."

            c "..You know prisons record and monitor calls, right?"

    c "Thanks for calling, but I have to go now, Tin. Bye."

    m "Bye."

    c "..Wait."

    c "Before I hang up, I have to tell you."

    m "What?"

    c "You're an idiot."

    c "You decide to use dynamite? After I told you not to? Come on.."

    c "The blast damaged too much. There's barely anything in the ocean now. Our income, our food sources, all gone!"

    c "It pushed our marine ecosystem over the edge and now there's nothing left."

    c "But hey! Don't worry, you'll spend a few less years in jail than Fish."

    c "Though considering the damage done, those extra years won't matter."

    c "Have a good one, Tin."

    menu:
        "You too":
            m "You-"

        "You're so annoying":
            m "You-"

    "(...)"

    m "She hung up."

    "The End (Dynamite Ending)"
    return

label steadyEnd:
    scene bg market
    show fish
    with fade
    f "We've got a decent amount of fish to sell."

    if faff < -2:
        f "I have some business to attend to, so I'll have to leave you here. Farewell, good luck with the fish!"

        m "Bye bye!"
        hide fish with easeoutright

        jump candyMeet

    f "That guy over there looks like they could use some fish. One second."
    hide fish with easeoutright
    f "..Fish needed?"

    t "Fish needed affirmative."

    if badChoice == True:
        f "200 dollars. Take it or leave it."

        t "What?! But there's a bunch of debris in these!"

        f "Take it. Or leave it."
    else:
        f "100 dollars. Take it or leave it."

    t "It seems like what you have is not worth what I'm paying."

    f "..."
    
    t "No no, I'll accept!"
    show fish daring with easeinright
    f "That is how experts do it."
    show fish -daring
    f "And you can keep the money, kid."

    m "Thanks, Fish!"

    f "You should go and explore the town now and get some stuff. There's a lot of fun places."

    m "Aren't you gonna come with me?"
    show fish daring
    f "No can do, I have to lay low for a while. I drank a lot of whiskey last week and caused a ruckus."
    show fish -daring
    f "I've got a long day ahead of me, so I'll see you off now. Toodles!"

    m "Byeeee!"
    hide fish with easeoutright

    jump candyMeet

label candyMeet:
    m "These past two days have been crazy. First I move into town and then I find out crazy stuff."

    m "Now that I have time to reminisce, I'm recalling what I said to Candy on our last fishing trip."

    if badChoice == True:
        m "I don't regret it. She was making me fish without even asking me first, it's only natural I get annoyed."    
    if badChoice == False:
        m "Maybe I should apologize. I'm trying to make friends in this town, not lose them."

    show candy with moveinleft
    c "Hey, Tin."

    c "I've been looking for you. What are you doing here?"

    m "I went fishing with Fish."
    show candy surprised
    c "FISH?!?!?!?!"

    c "He didn't make you use dynamite, did he?"
    
    m "Nope."
    show candy smirk
    c "That's a relief."
    show candy -smirk
    c "That would be bad."

    if badChoice == True:
        jump unfrenCan

    m "..About our last fishing trip, I'm sorry for what I said to you, it wasn't personal. Fishing talk just bores me."

    m "I wasn't too happy being a fisher back then, but things have changed now."

    c "I appreciate the apology, Tin."

    c "I guess I have been a bit pushy with all the fishing stuff."

    c "Say, if you want, I could introduce you to some of my buddies and we could get ice cream together."

    m "That sounds great."

    m "And can we invite Fish one day? It'd be nice if we befriended each other."
    show candy smirk
    c "Don't you think he's too much of a bad influence?"
    show candy -smirk
    m "We can be good influences for him."

    c "..I'll think about it."

    scene bg townent with Dissolve(1.5)
    if faff < -2:
        jump cycleEnd

    m "It took some time but, I ended up becoming good friends with a lot of people: Candy, her friends, and Fish."

    m "Fish mostly hung out with me and wasn't too friendly with Candy and the others at first, but soon he started getting used to them."

    m "Fish learned to respect Candy and now he follows her fishing advice. He stopped using harmful fishing practices such as bottom trawling."

    m "He found a town he wants to stay in, and now he's trying not to destroy it so that Salmontin stays lively."

    m "Salmontin relies on a strong marine ecosystem for food and money, so we only fish as much as we need to. When demand is low, we use fishing rods."

    m "We also use LED nets when fishing so that nothing other than our target species gets caught. This helps keep our ecosystem stable."

    m "We make sure each of us has sustainable fishing habits because every action of ours builds up. We also keep watch and confront people fishing unsustainably."

    m "I'm really happy here. Candy takes me on a lot of fun adventures around town. We rarely go fishing together, though. I usually fish by myself or with my other friends."

    "The End (Steady Ending)"
    return

label unfrenCan:
    show candy look
    c "Anyways...About our last fishing trip.."

    c "..."

    c "Did you really mean that?"

    m "You made me fish without even asking me if I wanted to. Why wouldn't I be bored listening to someone talk about something I don't want to do?"

    c "I'll admit I was a bit pushy about fishing, but I was just excited to show you my favorite activity. I didn't mean to make you upset."

    c "I wanted to share my joy with you. You didn't have to be so rude about it."

    m "I didn't have to, but I wanted to. I do what I want."

    c "I don't think we can be friends anymore."

    m "That's one thing we can agree on."
    hide candy with easeoutleft

    scene bg townent with Dissolve(1.5)
    m "After I ended my friendship with Candy, I ended up becoming a lone fisher. Other fishers heard how rude I was and started avoiding me."

    m "I didn't mind. Fishing by myself meant I could fish however I wanted. No one could tell me what to do or what not to do."

    if faff < -2:
        m "I could go bottom trawling as much as I wanted to."

        m "But gradually, less and less sea creatures appeared in the water."

        m "In response, the town placed restrictions on how much you could fish and where you could fish, but I ignored them."

        m "One day, I was bottom trawling when I got caught."

        m "I had to go to court and they were trying to hold me responsible for all of the environmental damage around town."

        m "I didn't realize they had a lot of evidence of my wrongdoing. I didn't cover up my tracks well."

        m "I got a long sentence. So many years."
        
        if caff < -2:
            m "No possibility of parole. Will I ever see the light of day again?"
        else:
            m "There's still a possibility of parole, though. Maybe I can turn my life around."

        "The End (Lone Ending)"
        return

    m "However, there was one person who didn't avoid me: Fish. We went fishing sometimes and it was so much fun."

    m "We talked about how pretentious this town was and how particular they were about their fishing methods."

    m "We could go bottom trawling as much as we wanted to. He offered me lots of tips on how not to get caught."

    m "But gradually, less and less sea creatures appeared in the water."

    m "In response, the town placed restrictions on how much you could fish and where you could wish, but I ignored them."

    m "One day, I was bottom trawling by myself when I got caught."

    m "I had to go to court and they were trying to hold me responsible for all of the environmental damage around town."

    m "I was offered a lighter sentence if I could provide testimony against Fish. I accepted."

    m "I've burned all my bridges in Salmontin."

    "The End (Betrayal Ending)"
    return

label cycleEnd:
    m "It took some time but, I ended up becoming good friends with a lot of people: Candy and her friends, some of whom are also fishers."

    m "I didn't end up becoming friends with Fish. It seems he doesn't like me that much."

    m "Salmontin relies on a strong marine ecosystem for food and money, so my friends and I only fish as much as we need to. When demand is low, we use fishing rods."

    m "We also use LED nets when fishing so that nothing other than our target species gets caught. This helps keep our ecosystem stable."

    m "We make sure each of us is has sustainable fishing habits because every action of ours builds up. We also keep watch and confront people fishing unsustainably."

    m "However, there's a few people who fish at night that we've never been able to catch. They overfish and uses unsustainable fishing methods, but they always escape when we try to catch them."

    m "Local fishers have been reporting a decrease in fish in the sea. It's getting harder to fish, and in turn, it's getting harder for fishers to makes money, driving up marine prices for locals."
    
    m "Limits have gotten stricter for where and how much you can fish."

    m "Fishers annoyed by these limits have decided to break the rules and fish illegally wherever and whenever there's no one around."

    m "Fish decrease, so restrictions get placed, but some people ignore those restrictions, so fish decrease. Thus, more restrictions get placed, incentivizing even more people to fish illegally."

    m "The End (Cycle Ending)"
    return

label stubbornEnd:
    scene bg market with fade
    m "His stare is so scary.."
    show candy with moveinleft
    c "Hey, Tin."

    c "I've been looking for you. What are you doing here?"

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

    m "You sentenced someone to 5 years in jail because of it?"
    show candy smirk
    c "Oh, he told you about that? Just so you know, that's not entirely accurate."
    show candy -smirk
    c "I'm not judge, jury, or executioner, I'm just a caring citizen."

    c "All I did was ensure that they could not get out on bail."

    c "They still have parole and I had nothing to do with the length of the sentence."
    show candy look
    c "Anyways...About our last fishing trip.."

    m "Sorry about that, what I said wasn't personal. Fishing talk just bores me."

    m "I wasn't too happy being a fisher back then, but I've changed a lot since then."
    show candy -look
    c "I appreciate the apology."

    c "I guess I have been a bit pushy with all the fishing stuff."

    c "Say, if you want, I could introduce you to some of my buddies and we could get ice cream together."

    m "That sounds great."

    scene bg townent with Dissolve(1.5)
    m "It took some time but, I ended up becoming good friends with a lot of people: Candy and her friends, some of whom are also fishers."

    m "Salmontin relies on a strong marine ecosystem for food and money, so we only fish as much as we need to. When demand is low, we use fishing rods."

    m "We also use LED nets when fishing so that nothing other than our target species gets caught. This helps keep our ecosystem stable."

    m "We make sure each of us is has sustainable fishing habits because every action of ours builds up. We also keep watch and confront people fishing unsustainably."

    m "..But I wish we kept watch a little better."

    m "One day, someone spread a bunch of dynamite across the sea and ignited it. We had a good idea of who it was. The suspect seemed to have skipped town."

    m "Piles and piles of marine carcasses and debris floated to the top of the water."

    m "Salmontin's ecosystem never fully recovered from this. Too much of the environment was destroyed."

    m "It got harder and harder to fish. A good chunk of people had to move or switch professions because the marine industry was no longer profitable enough."

    m "Seafood became more expensive, which made less people eat at local seafood restaurants."

    m "Candy and I have been working hard to promote sustainable fishing and consumption habits to everyone. The whole town is shaken by what happened."

    m "Some areas are off limits to fish in now so that fish have time to repopulate. We keep close watch to make sure no one fishes there."

    m "Some people blame me for what happened. They say the culprit blew everything up as an act of spite toward me."

    "The End (Stubborn Ending)"
    return


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