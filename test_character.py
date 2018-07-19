import pytest
from character import Character, Spells, get_Spells


# test format for character.py

# creates character Per and ensures starting value logic works as intended
def test_default_bard():
	Per = Character('Per', 'Dragonborn', 'Bard', 12, 12, 12, 12, 12, 12)
	assert Per.chrName == 'Per'
	assert Per.chrRace == 'Dragonborn'
	assert Per.chrJob == 'Bard'
	assert Per.chrStr == 14
	assert Per.chrDex == 12
	assert Per.chrCon == 12
	assert Per.chrInt == 12
	assert Per.chrWis == 12
	assert Per.chrCha == 13

# following code tests that the amount of spells available for each class is working as intended, up to date with current spell directory
def test_barbarian_spells():
	barb_spells = get_Spells('Barbarian', 10)
	assert len(barb_spells) == 0

def test_bard_spells():
	bard_spells = get_Spells('Bard', 10)
	assert len(bard_spells) == 6

def test_cleric_spells():
	cleric_spells = get_Spells('Cleric', 10)
	assert len(cleric_spells) == 10

def test_druid_spells():
	druid_spells = get_Spells('Druid', 10)
	assert len(druid_spells) == 10

def test_fighter_spells():
	fighter_spells = get_Spells('Fighter', 10)
	assert len(fighter_spells) == 0

def test_monk_spells():
	monk_spells = get_Spells('Monk', 10)
	assert len(monk_spells) == 0

def test_paladin_spells():
	paladin_spells = get_Spells('Paladin', 10)
	assert len(paladin_spells) == 6

def test_ranger_spells():
	ranger_spells = get_Spells('Ranger', 10)
	assert len(ranger_spells) == 7

def test_rogue_spells():
	rogue_spells = get_Spells('Rogue', 10)
	assert len(rogue_spells) == 0

def test_sorcerer_spells():
	sorcerer_spells = get_Spells('Sorcerer', 10)
	assert len(sorcerer_spells) == 7

def test_warlock_spells():
	warlock_spells = get_Spells('Warlock', 10)
	assert len(warlock_spells) == 3

def test_wizard_spells():
	wizard_spells = get_Spells('Wizard', 10)
	assert len(wizard_spells) == 21