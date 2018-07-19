import json

#define the character class 
class Character():

	def __init__(self, name, race, job, rollStr, rollDex, rollCon, rollInt, rollWis, rollCha):
		#base stats, will be modified by race and job choices
		self.chrName=name		
		self.chrStr=rollStr
		self.chrDex=rollDex
		self.chrCon=rollCon
		self.chrInt=rollInt
		self.chrWis=rollWis
		self.chrCha=rollCha
		self.chrHitDie=0
		self.chrLvl=1
		self.chrSpeed=0
		self.chrRace=race
		#job instead of class for syntax reasons
		self.chrJob=job
		self.chrSpells=[]
		self.race_mod()
		self.job_mod()
		#self.getChar()

	#Adds a Spell object to list of spells held by Character instance
	def add_spell(self, spell_name):
		self.chrSpells.append(spell_name)

	#race alters base stats
	def dwarf(self):
		self.chrCon+=2
		self.chrSpeed=25

	def elf(self):
		self.chrDex +=2
		self.chrSpeed=30

	def half(self):
		self.chrDex+=2
		self.chrSpeed=25

	def human(self):
		self.chrStr+=1
		self.chrDex+=1
		self.chrCon+=1
		self.chrInt+=1
		self.chrWis+=1
		self.chrCha+=1
		self.chrSpeed=30

	def dragon(self):
		self.chrStr+=2
		self.chrCha+=1
		self.chrSpeed=30

	def gnome(self):
		self.chrInt+=2
		self.chrSpeed=25

	def halfelf(self):
		self.chrCha+=2
		#note +=1 here will be user choice
		self.chrStr+=1
		self.chrCon+=1
		self.chrSpeed=30

	def halforc(self):
		self.chrStr+=2
		self.chrCon+=1
		self.chrSpeed=30

	def tiefling(self):
		self.chrInt+=1
		self.chrCha+=2
		self.chrSpeed=30
	#9 different races to choose from
	race_dict ={
		"Dwarf": dwarf,
		"Elf": elf,
		"Halfling": half,
		"Human": human,
		"Dragonborn": dragon,
		"Gnome":gnome,
		"Half-Elf": halfelf,
		"Half-Orc": halforc,
		"Tiefling": tiefling
	}
	#jobs offer differing criteria including hit die and spells (spells implemented later)
	def barbarian(self):
		self.chrHitDie=12
	def bard(self):
		self.chrHitDie=8
	def cleric(self):
		self.chrHitDie=8
	def druid(self):
		self.chrHitDie=8
	def fighter(self):
		self.chrHitDie=10
	def monk(self):
		self.chrHitDie=8
	def paladin(self):
		self.chrHitDie=10
	def ranger(self):
		self.chrHitDie=10
	def rogue(self):
		self.chrHitDie=8
	def sorcerer(self):
		self.chrHitDie=6
	def warlock(self):
		self.chrHitDie=8
	def wizard(self):
		self.chrHitDie=6

	#12 different jobs to choose from
	job_dict ={
		"Barbarian" : barbarian,
		"Bard" : bard,
		"Cleric" : cleric,
		"Druid": druid,
		"Fighter" : fighter,
		"Monk" : monk,
		"Paladin" : paladin,
		"Ranger" : ranger,
		"Rogue" : rogue,
		"Sorcerer" : sorcerer,
		"Warlock" : warlock,
		"Wizard" : wizard
	}
	# Alters skill attributes based on chrRace, by calling the appropriate function using racedict
	def race_mod(self):
		self.race_dict[self.chrRace](self)
	# Alters hit die which influences hit points. Should eventually determine available spells
	def job_mod(self):
		self.job_dict[self.chrJob](self)
	# Stat mod shows added bonus for each individual stat. Rounds down, so -11
	def stat_mod(self, stat):
		if stat % 2 == 0:
			return (stat-10) / 2
		return (stat-11) / 2 

class Spells():

	#Spell class holds all spell information
	def __init__(self, spell_name, description, spell_range, spell_level, attack_save, cast_time, duration):
		self.spell_name = spell_name
		self.description = description
		self.spell_range = spell_range
		self.spell_level = spell_level
		self.attack_save = attack_save
		self.cast_time = cast_time
		self.duration = duration

def get_Spells(char_job, char_level):
	available_spells =[]
	data = json.loads(open('spells.json').read())
	for x in range(0, len(data)):
		if char_job in data[x]['class'] and (char_level >= int(data[x]['level'])):
			available_spells.append((Spells(data[x]['name'], data[x]['description'], data[x]['range'], data[x]['level'], data[x]['attack_save'], data[x]['casting_time'], data[x]['duration'] )))
	return available_spells



#print Per.__dict__
#print Per.stat_mod(Per.chrStr)


