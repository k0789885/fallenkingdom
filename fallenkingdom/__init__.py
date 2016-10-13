from random import randrange
#x = randrange(y,z)
from sys import exit
#exit(X)
choice = []

class Male:
    def __init__(self):
        self.pronoun = " M'Lord"
        self.address = " Sir"
        self.highaddress = " King"
        self.refer = " he"
        self.refer2 = " him"

class Female:
    def __init__(self):
        self.pronoun = " M'Lady"
        self.address = " Mam"
        self.highaddress = " Queen"
        self.refer = " she"
        self.refer2 = " her"

class GenderNeutral:
    def __init__(self):
        self.pronoun = " Young heir"
        self.address = ""
        self.highaddress = " Ruler"
        self.refer = " they"
        self.refer2 = " them"

class equipment:
    def __init__(self, equipped):
        self.equipped = equipped
        
class Variables:
    def __init__(self, boolean):
        self.boolean = boolean
        opt = boolean
        
class NPC:
    def __init__(self, care):
        self.care = care
        char = care
        
#Range for "care".
#100 Best Friend
#80 Good Friend
#60 Friends
#40 Null
#20 Enemies
#0 Worst Enemies
        
maul = NPC(60)
father = NPC(80)
mother = NPC(95)
roth = NPC(80)
civ = NPC(35)
saber = NPC(60)
shale = NPC(40)
bidden = NPC(30)

weapon = equipment(0)
outfit = equipment(0)
rock = equipment(0)

easedropmeet = Variables(0)
shalecarevar1 = Variables(0) #def Ch1
bidcarevar1 = Variables(0) #def Ch1
sabercarevar1 = Variables(0) #def Ch1
siscarevar1 = Variables(0) #def Ch1
  
class Menu(object):

   def __init__(self):
       self.choices = []
       self.texts = []
       self.selected_value = None
       self.invalid_text = "That's not one of the choices, please use one of the numbers displayed."

   def add_choice(self, display_text, value):
       self.choices.append(value)
       self.texts.append(display_text)

   def prompt(self, text):

        while self.selected_value is None:
            print text
            num = 1
            for display_text in self.texts:
               print "%d. %s" % (num, display_text)
               num = num + 1

            user_choice = (raw_input("> "))
            
            try:
                user_choice = int(user_choice)
            except:
                print ""
                print self.invalid_text
                print ""
                continue

            if user_choice < 1 or user_choice > len(self.texts):
                print self.invalid_text
                print choice
            else:
                self.selected_value = self.choices[user_choice - 1]
                choice.append(user_choice)
        
def meeting():
  print ""
  print "Father: Alright men, I apologize for the delay in this meeting but I thought my child should be here to start getting into the position."
  print "Father: Now that were all fond of eachother we can start."
  print "Father: Lord Shale, if I understand correctly this meeting was made because a militia of yours was confronted along a trade route and attacked by the assumed kingdom of Silverwood?"
  print ""
  print "Lord Shale: That's correct, your friend here attacked and stole some valuable wares from me."
  print ""
  print "Father: And Lord Bidden, you are here because you said that Rock Dawns militia had attacked and slaughtered your men?"
  print ""
  print "Lord Bidden: Indeed."
  print ""
  print "Father: Welp lets hear both sides then. Tell me the full storys both of you, Bidden you first."
  print ""
  print "Lord Bidden: I had accepted a request from the three towns under our protection, the farthest one had asked that I send some skilled soldiers to help with local wolf being a nuisance."
  print "Lord Bidden: I had simply sent the men in consideration of them providing me with lumber."
  print "Lord Bidden: I saw nothing wrong with such a minor trade so I sent my knights of a division and along the way they encountered his men, his men on a so called 'trade route' attacked and attempted to slaughter my men."
  print "Lord Bidden: One survived and returned to my throne room covered in blood. No wagon was seen or reported, fully armored soldiers, even in rock hide."
  print "Lord Bidden: Now we are here."
  print ""
  print "(After a moment father speaks)"
  print ""
  print "Father: Lord Shale, let's hear your side."
  print ""
  print "Lord Shale: Well M'lord as much as I'd like to say my men attacked him right now, they didn't."
  print "Lord Shale: I was working on a trade agreement with one of the same towns this boy was talking about and they asked for some Rockhide in exchange for a hefty supply of iron."
  print "Lord Shale: I told them alright I'd see what I can do, so I sent those men four pounds worth of Rockhide. Rockhide is a very precious thing to my kingdom so I sent fully armored men in case they came across any complications."
  print "Lord Shale: A few weeks went by and I had received a message from the town that they were coming through to ask about the shipment and found my men's dead bodies."
  print "Lord Shale: I told them to return my men to me and they could have the armor. When I received there corpses I thought how on all did they die so rapidly. Then I saw the weapons being use by the other men. Silverwood."
  print "Lord Shale: Now I'm here."
  print ""
  print "Father: Well, I see that most of this was quite a misunderstanding however one of your men are still at fault."
  print "Father: Compensation is do for one party though from what it seems and I really don't know."
  print "Father: On behalf of both parties I will not judge this event, I will let my child. I obviously have a bias along Bidden and my heir does not. So%s will make the decision."
  print ""
  print "Lord Bidden: M'Lord do you think this is such a--"
  print ""
  print "Father: No arguements, I asked for%s to be here for a reason."
  print ""
  
  meeting = Menu()
  meeting.add_choice('Lord Shale is at fault.',1)
  meeting.add_choice('Lord Bidden is at fault.',2)
  meeting.add_choice("Both men are at fault.",3)
  
  meeting.prompt("What do you think %s who is at fault here? % ChaName")


  if meeting.selected_value == 1:
    shale.care -= 5
    print "Lord Shale:%s one of his men got to go home. I have to inform four families of a death. Please understand I had no intentions of--"
    print "Father: Silence, my child has spoken and that will be your answer. We'll work on some sort of fee for what happened. Possibly ore of sorts, I promise to not let your pride enter the table."
    print "Thank you your highness, I promise to never let an incident like this happen again."
  elif meeting.selected_value == 2:
    bidden.care -= 8
    print "Lord Shale:%s one of his men got to go home. I have to inform four families of a death. Please understand I had no intentions of--"
    print "Father: Silence, my child has spoken and that will be your answer. We'll work on some sort of fee for what happened. Possibly ore of sorts, I promise to not let your pride enter the table."
    print "Thank you your highness, I promise to never let an incident like this happen again."
  elif meeting.selected_value == 3:
    shale.care -= 2
    bidden.care -= 4
           
           
            
def Ch1():
    meetkings = Menu()
    meetkings.add_choice('Talk to Lord Shale',1)
    meetkings.add_choice('Talk to Lord Bidden',2)
    meetkings.add_choice('Talk to Sir Saber',3)
    meetkings.add_choice('Talk to Father',4)
    
    meetkings.prompt("(What do you want to do?)")
    
    if meetkings.selected_value == 1:
        print "Lord Shade: Ahh, greetings. You must be the young %s. Pleasure to meet you."
        print "Sir Saber: %s %s this is Lord Shale, he rules over the Rockdawn kingdom. Their well known for their 'Rock Hide' armor."
        print "Lord Shade: Damned right, our metal is the best you'd ever see. The only thing that can beat it is the gods themselves."
        i = 0
    
        while i != 1:
            shalequest = Menu()
            shalequest.add_choice('How are you?',1)
            shalequest.add_choice('What is Rock Hide?',2)
            shalequest.add_choice('Where is Rockdawn?',3)
            shalequest.add_choice('Back',4)
            
            if outfit.equipped == 2 and shalecarevar1.boolean == 0:
                shale.care += 2
                shalecarevar1.boolean = 1
            else:
                pass
            
            shalequest.prompt("Ask:")
            print shale.care
            
            if shalequest.selected_value == 1:
                print "Lord Shale: Me? I'm fine, enjoying the sights of this pleasant kingdom you have here and trying not to step anear that rubbish Bidden."
                print "(Lord Shale and Bidden Exchange a few dirty stares)"
                print "Lord Shale: Don't worry about him, he's got his head to far up his arse."
            elif shalequest.selected_value == 2:
                print "Lord Shale: Don't know about it yourself? Rock Hide is one of the best damned metals you'll ever see. It makes that fancy paladin armor of your look like a wet leaf." 
                print "Lord Shale: We mine it from our caves and then we have special smith's craft it into armor. The damned armor resist almost any attack and is light and mobile."
                print "(Lord Shale pulls a flat piece of rock out of his pocket and places it on the table)"
                if weapon.equipped == 4:
                    print "Lord Shale: I'll tell ya now that mace you got there would probably bust it if you tried hard enough. No point in wasting it. Here you have it, a little gift from Rockdawn to you."
                    shale.care += 2
                    rock.equipped == 1
                    print "(Rock Hide piece added to inventory)"
                else:
                    print "Lord Shale: Go on, try it."
                    hitrock = Menu()
                    hitrock.add_choice('Yes',1)
                    hitrock.add_choice('No',2)
                    
                    hitrock.prompt("Hit it?")
                    
                    if hitrock.selected_value == 1:
                        if weapon.equipped == 1:
                            print "(You swing your sword at the rock and it bounce of on collision)"
                            print "Lord Shale: Many have tried, many have failed, and many will continue to fail just like that."
                        elif weapon.equipped == 2:
                            print "(Your shield collides with the rock... It doesn't do anything)"
                            print "Lord Shale: I'm not sure if you're trying to hit the metal or add it to your shield. Either way I don't think it worked."
                        elif weapon.equipped == 3:
                            print "(Your lance strike at the rock and slides off)"
                            print "Lord Shale: A direct strike like that to it would never pierce it."
                    else:
                        print "Lord Shale: Ha, don't worry. Such an item is quite intimidating."
                        
                        
            elif shalequest.selected_value == 3:
                print "Lord Shale: Rockdawn is a kingdom to the northeast near the mountains range, that's where all of our mines and mead are. (Lord Shale begins laughing)"
                print "Lord Shale: Legend has it that all the ore we mine up is really old dragon bones that have just gotten covered with time."
            elif shalequest.selected_value == 4:
                Ch1()
    elif meetkings.selected_value == 2:
        print "Lord Bidden: Hello, I am Lord Bidden, your father and I have had an alliance for years now. You must be his heir, pleasure."
        print "Sir Saber: Lord Bidden has been in alliance with your family for almost seventeen years. Almost as long as you've been alive."
        print "Sir Saber: His family obtained the throne for their efficient use of Silverwood. Silverwood is a mysterious item molded by a specific tree and some ore mixing, that in turn created a new metal we know as Silverwood."
        i = 0
    
        while i != 1:
            bidquest = Menu()
            bidquest.add_choice('How are you?',1)
            bidquest.add_choice('What is Silverwood?',2)
            bidquest.add_choice('Where is the kingdom of Silverwood?',3)
            bidquest.add_choice('Back',4)
            
            if weapon.equipped == 1 and shalecarevar1.boolean == 0:
                bidden.care += 2
                bidcarevar1.boolean = 1
            else:
                pass
            
            bidquest.prompt("Ask:")
            print bidden.care
            
            if bidquest.selected_value == 1:
                print "Lord Bidden: I've been here for three hours and your father persist on sharing an alliance with those brutes. It's been a long day your highness."
            elif bidquest.selected_value == 2:
                print "Lord Bidden: Your servent explained already." 
                bidden.care -= 1
            elif bidquest.selected_value == 3:
                print "Lord Bidden: Look on the map, it's the kingdom to the west of yours."
            elif bidquest.selected_value == 4:
                Ch1()
    elif meetkings.selected_value == 3:


#Come back and fix!!!!!!!!!!!!!!!!!!!!!!!!!!




        i = 0
    
        while i != 1:
        
          sabletalk = Menu()
          sabletalk.add_choice('Yes.',1)
          sabletalk.add_choice('No, I just wanted to talk.',2)
        
          sabletalk.prompt("Sir Saber: Hello%s, can I get you something?")
          
          if sabletalk.selected_value == 1:
            
            saberget = Menu()
            saberget.add_choice('Get me food.',1)
            saberget.add_choice('Bring me my other outfit',2)
            saberget.add_choice('Return this weapon to the sparing room',3)
            saberget.add_choice('(Back)',4)
            
            saberget.prompt("What can I get you%s?")
            
            if saberget.selected_value == 1:
                print "(Sir Saber brings a tray af assorted fruits)"
                print "Gage: No, I'm not programming in an option for the fruit tray, you just eat the damn fruits."
            elif saberget.selected_value == 2:
                print "Sir Saber: Right away%s."
                if outfit.equipped == 1:
                    outfit.equipped = 2
                    print "(You excuse yourself and put on your Royal Apparel)"
                elif outfit.equipped == 2:
                    outfit.equipped = 1
                    print "(You excuse yourself and put on your Sparing Uniform)"
            elif saberget.selected_value == 3:
                print "Sir Saber: Right away%s."
                weapon.equipped = 0
            elif saberget.selected_value == 4:
                Ch1()
            
          elif sabletalk.selected_value == 2:
            
            saberquest = Menu()
            saberquest.add_choice('How are you?',1)
            saberquest.add_choice('What do you think of Lord Shale?',2)
            saberquest.add_choice('What do you think of Lord Bidden?',2)
            saberquest.add_choice('(Back)',4)
            
            saberquest.prompt("What would yoy like to know%s?")
             
            if saberquest.selected_value == 1:
                print "Sir Saber: I'm quite well, thank you for asking%s."
                
                saber.care += 5
                
                if sabercarevar1.boolean == 0:
                  saber.care += 5
                  sabercarevar1.boolean = 1
                else:
                  pass
                
            elif saberquest.selected_value == 2:
                print "Sir Saber: Lord Shale is quite hardy fellow, he enjoys being a child from what I hear but don't let that fool you. He can be quite the ruler if need be."
                print "Sir Saber: He and your father are quite a new alliance but have made much progress to prevent another unnecessary war."
            elif saberquest.selected_value == 3:
                print "Sir Saber: Lord Bidden is very quiet, he is strategic and often know the next step. Much more a scholar then even I know myself."
                print "Sir Saber: As I said before he and your father are very familiar with each other, they've been an alliance for about seventeen years now but friends for almost two centuries. I do believe Lord Bidden was her for your birth."
            elif saberquest.selected_value == 4:
                Ch1()
    elif meetkings.selected_value == 4:
        meeting()

def premeeting(): 
    print "Mother: Good morning you too."
    print "Lord Maul: Morning M'Lady, what brings you to the sparing room?"
    print "Mother: I actually was wondering if%s'd attend a meeting with me. I want%s to learn a bit more about the other kingdoms." % (player.refer, player.refer2)
    print "Lord Maul: Well, we have been going at it for a while now. I suppose you can barrow%s%s for now." % (player.pronoun, ChaName)
    print "(A few moments late)"
    if outfit.equipped == 1:
        print "At Least you dressed for such a meeting."
    else:
        print "I wish we had time to change your outfit, that filthy uniform won't exactly do anything in this meeting."
    
    premeeting = Menu()
    premeeting.add_choice('I like them both.',1)
    premeeting.add_choice('I despise them both.',2)
    premeeting.add_choice('I do not know.',3)
    premeeting.add_choice('(No reply)',4)
    if easedropmeet.boolean == 1:
        premeeting.add_choice('Rockdawn is at fault for the massacre.',5)
        premeeting.add_choice('Silverwood is at fault for the attack.',6)
    else:
        pass
    
    premeeting.prompt("So%s what do you think of the Kingdom of Rockdawn and Silverwood?" % ChaName)
     
    if premeeting.selected_value == 1:
        print "Mother: Hmm... trusting those we don't really know hmm?"
    elif premeeting.selected_value == 2:
        print "Mother: Mind your manors around them both then."
    elif premeeting.selected_value == 3:
        print "Mother: Then this meeting should be very enlightening for you and I both."
    elif premeeting.selected_value == 4:
        print "Mother: Don't worry dear, I don't know much myself."
    elif premeeting.selected_value == 5:
        print "Mother: Know some things you're not supposed to yet? Well in anycase Rockdawn and Silverwood got into a big mess. I don't think either are at fault"
    elif premeeting.selected_value == 6:
        print "Mother: So you already know then? Well from what I've heard it's just a big mess that keeps spreading. Hopefully we can settle this with both them."
    
    print "Mother: This meeting is about our standing with Rockdawn, you should know we have an alliance with Silverwood already and that they both loth each other."
    if easedropmeet.boolean == 1:
        print "Mother: And it doesn't matter who did it, we must strive for peace"
    
    print "(You and the queen enter a large room with a map in the middle)"
    print "(There are two unknown men and your father arguing, Sir Saber is standing by the door when you enter)"
    print "Sir Saber: Good morning your highness and%s. They have already started the meeting and Lady Roth is in the dining hall." % player.pronoun
    print "Mother: Now listen, I want you to introduce yourself to both the men while I speak to your father. Once you're done come speak to me and your father."    
    Ch1()
    
def swordfight():
    r = randrange(0,2)
     
    if r == 0:
        print "(You swing your sword with great might at Lord Maul)"
        print "(He blocks a strike with his wrist guard and takes the sword by its blade from your hands)"
        print "Lord Maul: Seems you need to work on the force behind such a powerful blade."
        print "Lord Maul: Don't worry, I'm sure one day you'll get me."
        print "Just stick to that silver tongue of yours for now, it'll do more power then this rusty blade anyday."
    elif r == 1:
        print "(You jab your sword in between lord malls armor)"
        print "(One jab pierces his chainmail, Lord Maul starts bleeding)"
        print "Lord Maul: Ahhhh! I understand you want to win but don't forget I'm not really trying to kill ya."
        print "Lord Maul: Oh, don't worry. Your father nearly took of my head his first match."
        print "Lord Maul: Just remember, there always room for diplomacy in a battle."
        
    premeeting()
        
def shieldfight():
    print "(You block a series of attacks from Lord Maul)"
    print "(Eventually his attacks slow and he's out of breath.)"
    print "Lord Maul: Damn crown, you got some good defense there%s." % player.pronoun
    print "Lord Maul: You know, if you'd actually hit back sometime you would actually win right?"
    print "Lord Maul: Your ability to not fight is astonishing, keep up that defence and talk to your opponent and you may actually be a great%s" % player.highaddress
    maul.care += 5
    
    premeeting()
        
def lancefight():
    r = randrange(0,2)
     
    if r == 0:
        print "(You jab your lance with great might at Lord Maul)"
        print "(He pushes the lance out of the way and presses his sword against your shoulder)"
        print "Lord Maul: Footwork needs more practice."
        print "Lord Maul: Don't worry, practice will eventually pay off."
        print "Lord Maul: Your father wasn't that good with a lance either."
    elif r == 1:
        print "(You jab your sword in between lord malls armor)"
        print "(One jab pierces his chainmail, Lord Maul starts bleeding)"
        print "Lord Maul: Ahhhh! I understand you want to win but don't forget I'm not really trying to kill ya."
        print "Lord Maul: Oh, don't worry. Your father nearly took of my head his first match."
        print "Lord Maul: Just remember, there always room for diplomacy in a battle."
        
    premeeting()
        
def macefight():
    print "(You swing your mace at Lord Maul)"
    print "(It penetrates his armor immediately and knocks him down)"
    print "Lord Maul: Ahhhh! Damn crown, don't need to prove anything to anyone do you?"
    maul.care -= 5
    print "Lord Maul: Now I got to go to the blacksmith and have him remove this damned thing from my chest plate."
    print "Lord Maul: Bah, don't worry. Your father nearly took of my head his first match."
    print "Lord Maul: Just remember, there always room for diplomacy in a battle Don't need to kill to win always."
    
    premeeting()
               
#((((Sparing Pit 1 / Weapon Select))))

def weapon_sel():
    weapon_sel = Menu()
    weapon_sel.add_choice('Sword',1)
    weapon_sel.add_choice('Shield',2)
    weapon_sel.add_choice('Lance',3)
    weapon_sel.add_choice('Mace',4)
    
    if startgame.selected_value == 1:
        print "Lord Maul: Good morning%s, glad you got here early. Maybe I'll go easy on you during training today." % player.pronoun
    else:
        print "Lord Maul: Sleep in early today again? You know the King never slept in during his sparring days. He alway wanted to try and put me in my place before he filled himself with mead."
        maul.care -= 1
    print ""
    print "Alright, let's get to it."
    print ""
    
    weapon_sel.prompt("What do you want to work on today?")
    
    if weapon_sel.selected_value == 1:
        weapon.equipped = 1 #Sword
        print "(A few hours late)"
        swordfight()
    elif weapon_sel.selected_value == 2:
        weapon.equipped = 2 #Shield
        print "(A few hours late)"
        shieldfight()
    elif weapon_sel.selected_value == 3:
        weapon.equipped = 3 #Lance
        print "(A few hours late)"
        lancefight()
    elif weapon_sel.selected_value == 4:
        weapon.equipped = 4 #Mace
        print "(A few hours late)"
        macefight()
        
def Throneroom_1():
    thr1 = Menu()
    thr1.add_choice('Persuade to enter the room',1)
    thr1.add_choice('Go to Sparing Room',2)
    thr1.add_choice('Dining Hall',3)
    thr1.add_choice('Sisters Room',4)
    
    print "You walk down the hall to the throne room but are stopped by two guards at the doors."
    print "Guard: Sorry%s, the Queen is in a negotiation right now with the Rockdawn Kingdom." % player.pronoun
    
    thr1.prompt("What do you say?")
    
    if thr1.selected_value == 1:
        thr2 = Menu()
        thr2.add_choice('(Threaten)',1)
        thr2.add_choice('(Politely ask)',2)
        thr2.add_choice('(Lie)',3)
        thr2.add_choice('Nevermind.',4)
        
        
        if thr2.selected_value == 1:
          print "Fine, your highness just go in and don't make a nuecence of yourself."
        elif thr2.selected_value == 2:
          print "Alright,%s just please do be quiet, don't want to get in trouble."
        elif thr2.selected_value == 3:
          print "My pardens%s, I hadn't known."
        elif thr2.selected_value == 4:
          Throneroom_1()
        
    elif thr1.selected_value == 2:
        weapon_sel()
    elif thr1.selected_value == 3:
        Dinehall_1()
    elif thr1.selected_value == 4:
        sisroom_1()
        
def sisroom_1():
    sis_1 = Menu()
    sis_1.add_choice('Try to open door',1)
    sis_1.add_choice('Go to Sparing Room',2)
    sis_1.add_choice('Go to Dining Hall',3)
    sis_1.add_choice('Go to Throne room',4)
    
    
    
    sis_1.prompt("What do you do?")
    
    if sis_1.selected_value == 1:
        print "(The door is too strong, if you had a mace maybe you could break the door)"
    elif sis_1.selected_value == 2:
        weapon_sel()
    elif sis_1.selected_value == 3:
        Dinehall_1()
    elif sis_1.selected_value == 4:
        Throneroom_1()
      
def Dinehall_1():
    i = 0
    dine_1 = Menu()
    dine_1.add_choice('Sit with Sister',1)
    dine_1.add_choice('Go to Sparing Room',2)
    dine_1.add_choice('Sisters Room',3)
    dine_1.add_choice('Go to throne room',4)
    
    dine_1.prompt("What do you do?")
    
    if dine_1.selected_value == 1:
        
        if siscarevar1.boolean == 0:
            roth.care += 3
            siscarevar1.boolean = 1
        else:
            pass
        
        while i != 1:
            sisquest = Menu()
            sisquest.add_choice('How are you?',1)
            sisquest.add_choice('Heard any news?',2)
            sisquest.add_choice('(Go somewhere else)',3)
            
            
            sisquest.prompt("Ask:")
            print bidden.care
            
            if sisquest.selected_value == 1:
                print "Roth: It's been a slow day, Sir Saber woke me up and had me go to classes. I wish he'd understand how boring he is at teaching alchemy sometimes."
            elif sisquest.selected_value == 2:
                print "Roth: Actually, I did hear that Lords Shale and Bidden are here for a meeting, and I hear that you'll be involved. Don't burn down the castle okay?" 
            elif sisquest.selected_value == 3:
                Dinehall_1()
                
    elif dine_1.selected_value == 2:
        weapon_sel()
    elif dine_1.selected_value == 3:
        sisroom_1()
    elif dine_1.selected_value == 4:
        Throneroom_1()
        
#((((Start of Game))))

gender = Menu()
gender.add_choice('Male',Male)
gender.add_choice('Female',Female)
gender.add_choice('No preference',GenderNeutral)

print "What's your name?" 
ChaName = raw_input("> ")

gender.prompt("Gender?")

player = gender.selected_value()
print "---------------------------------------------------------------------------------------------------"
print "---------------------------------------------------------------------------------------------------"
print "---------------------------------------------------------------------------------------------------"
print "Welcome %s, you are a child of the royal family. Next in line for the throne and become the next%s." % (ChaName, player.highaddress)
print "Right now your kingdom is in a mess and everyone is watching a war brew between Rockdawn, Silverwood, and your kingdom."
print "Your younger sister, Roth, is worried you may be in danger and could be on an assassins list along with the rest of your family."
print "You will have to make choices that influence your kingdom and watch your own neck for it may become a lot lighter if you don't."
print "Keep your eyes peeled, watch out for danger and rule your kingdom how you want."
print "Do all that and you shall make a fine%s." % player.highaddress
print "---------------------------------------------------------------------------------------------------"
print "---------------------------------------------------------------------------------------------------"
print "---------------------------------------------------------------------------------------------------"
print " "

print "It's early in the day and the sun has just rose through the curtains."
print "Sir Saber(Your Butler): You know the sun only goes up once a day, might wanna see it before it's gone%s. Whenever you do decide to leave your bed don't forget that you have training today with Lord Maul. So please do get some breakfast and be on your way." % player.pronoun
print " "
print "(You shuffle out of bed and Sir Saber leaves the room)"
print " "

startgame = Menu()
startgame.add_choice('Sparing Pit',1)
startgame.add_choice('Sisters Room',2)
startgame.add_choice('Throne Room',3)
startgame.add_choice('Dining Hall',4)


armor = Menu()
armor.add_choice('Royal Apparel',1)
armor.add_choice('Sparing Uniform',2)

armor.prompt("Which outfit will you wear?")

if armor.selected_value == 1:
    print "Your royal clothing, fashioned silk with various jewelry ready to astonish anyone."
    outfit.equipped = 1 #Royal
elif armor.selected_value == 2:
    print "Your Sparing Uniform, a clean yet durable piece of armor fashioned for light attacks and minor blows."
    outfit.equipped = 2 #Spar

startgame.prompt("You get dressed and look out the window, where would you like to go?")

if startgame.selected_value == 1:
    weapon_sel()
elif startgame.selected_value == 2:
    sisroom_1()
elif startgame.selected_value == 3:
    Throneroom_1()
elif startgame.selected_value == 4:
    print "(You walk into the dining hall and see a variety of servents working to make lunch for your family)"
    print "(On the far table you see your sister Roth waving to you)"
    print "Roth: Good morning %s, come in for a snack as well? Well come sit down for a moment won't you?"
    Dinehall_1()



