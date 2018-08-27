import json
from cache import Cache
from db import DB

#initial layer for localization and timezones as needed
class Locale:
    fullText = None

    @staticmethod
    def text():
        print("get from cache")
        Locale.fullText = Cache.get("text")
        #if not in cache either, continue
        if  Locale.fullText is None:
            print("db get...")
            Locale.fullText = DB.get("text","all")
            #if not in db either, do initial load
            if  Locale.fullText is None:
                print("db initial load")
                Locale.fullText = Locale.__loadText()
        return Locale.fullText

    @staticmethod
    def __loadText():
        jsonText= {
            'openingSpiel': ['You are the crew of the interstellar scout ship Raptor.','Your mission is to explore uncharted regions of space, deal with aliens both friendly and deadly, and defend the Consortium worlds against space dangers.','Captain Darcy has been overcome by the strange psychic entity known as Something Else, leaving you to fend for yourselves while he recovers in a medical pod.'],
            'numberOfHeroes':"How many heroes would you like to generate (max: 7, one per role):",
            'hero':{
                'styles':["Alien", "Android","Dangerous","Hot-Shot","Intrepid","Savvy","Sexy"],
                'roles':["Doctor","Envoy","Engineer","Explorer","Pilot","Scientist","Soldier"],
                'goals':["Become Captain", "Meet Sexy Aliens", "Shoot Bad Guys", "Find New Worlds", "Solve Weird Space Mysteries", "Prove Yourself", "Keep Being Awesome"]
            },
            'ship':{
                'strengths': ["Fast","Nimble","Well-Armed","Powerful Shields","Superior Senses","Cloaking Device","Fightercraft"],
                'weaknesses': ["Fuel Hog (always needs energy crystals)","Only One Medical Pod (and Captain Darcy is in it)","Horrible Circuit Breakers (in battle, consoles tend to explode on the bridge)","Grim Reputation (Captian Darcy did some bad stuff in the past)"]
            },
            'threat':{
                'adversary': ["Zorgon the Conqueror","The Hive Armada","Rogue Captain","Space Pirates","Cyber Zombies","Alien Brain Worms"],
                'wantsTo': ["destroy/corrupt","steal/capture","bond with","protect/empower","build/synthensize","pacify/occupy"],
                'the': ["space pirate king/queen", "void crystals", "star dreadnought", "quantum tunnel", "ancient space ruin", "alien artifact"],
                'whichWill': ["destroy a solar system", "reverse time", "enslave a planet", "start a war/invasion","rip a hole in reality", "fix everything"]
            },
            'lasers': "lasers",
            'feelings': "feelings",
            'high': "high",
            'goal':"goal"
        }
        print("saving to db")
        DB.set("text","all",jsonText)
        print("save to cache")
        Cache.set("text", jsonText)
        return jsonText
