#!/usr/bin/python3
#Random laser and feelings character generator
#Laser and Feelings is copyright John Harper (http://onesevendesign.com/) and is licensed under a CC BY-NCSA 3.0 license
#Program is Copyright Jeff Demers under the MIT License

#PACKAGES
import random
import string
import sys
from locale import Locale

class Logic:
    #METHODS
    @staticmethod
    def OpeningSpiel():
        return Locale.text()["openingSpiel"]
    
    @staticmethod
    def NumberOfHeroesText():
        return Locale.text()["numberOfHeroes"]
    
    @staticmethod
    def GetHeroes(numHeroes):
        styles = Locale.text()["hero"]["styles"]
        roles =  Locale.text()["hero"]["roles"]
        numbers = [2,3,4,5]
        goals =  Locale.text()["hero"]["goals"]
        arHeroes = []
        for x in range(numHeroes):
            #only allows this role once
            role = random.choice(roles)
            roles.remove(role)
            name = Logic.GetName()
            style = random.choice(styles)
            number = random.choice(numbers)
            lof =  Locale.text()[("lasers" if number > 3 else "feelings")]
            lofRating = f'{Locale.text()["high"]} ' if number == 2 or number == 5 else ""
            goal = random.choice(goals)
            arHeroes.append(f'{name} ({number}, {lofRating}{lof}) {style} {role}, {Locale.text()["goal"]}: {goal}')
        return arHeroes
    
    @staticmethod
    def GetShip():
        strengths = Locale.text()["ship"]["strengths"]
        weaknesses = Locale.text()["ship"]["weaknesses"]
        ar = []
        i = 0
        while i < 2:
            choice = random.choice(strengths)
            strengths.remove(choice)
            ar.append(choice)
            i+=1
        ar.append(random.choice(weaknesses))
        return ar
    
    @staticmethod
    def GetThreat():
        adversary = random.choice(Locale.text()["threat"]["adversary"])
        wantsTo = random.choice(Locale.text()["threat"]["wantsTo"])
        the = random.choice(Locale.text()["threat"]["the"])
        whichWill = random.choice(Locale.text()["threat"]["whichWill"])
        return f'{adversary} wants to {wantsTo} the {the} which will {whichWill}'
    
    @staticmethod
    def GetNamePart(length):
        VOWELS = "aeiou"
        CONSONANTS = "".join(set(string.ascii_lowercase) - set(VOWELS))
        word = ""
        for i in range(length):
            if i % 2 == 0:
                word += random.choice(CONSONANTS)
            else:
                word += random.choice(VOWELS)
        return word.capitalize()
    
    @staticmethod
    def GetName():
        return Logic.GetNamePart(random.randint(3,6)) + ' ' + Logic.GetNamePart(random.randint(4,10))
