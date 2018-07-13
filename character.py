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
		self.racemod()
		self.jobmod()
		#self.getChar()

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
	racedict ={
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
	jobdict ={
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
	#alters skill attributes based on chrRace, by calling the appropriate function using racedict
	def racemod(self):
		self.racedict[self.chrRace](self)
	#Alters hit die which influences hit points. Should eventually determine available spells
	def jobmod(self):
		self.jobdict[self.chrJob](self)