from flask import Flask, render_template, request
from character  import Character
import requests

app = Flask(__name__)
#homepage. Currently sits on character creation page
#values passed in this form are send through to /newcharacter
@app.route('/')
def home():
	return render_template('new.html')
#values obtained from new.html passed through character.py and printed out via newcharacter.html
@app.route('/newcharacter', methods=['GET', 'POST'])
def new():
	if request.method =='POST':
		username = request.form['name']
		race = request.form['race']
		job = request.form['job']
		strength = request.form['strength']
		dexterity = request.form['dexterity']
		constitution = request.form['constitution']
		intelligence = request.form['intelligence']
		wisdom = request.form['wisdom']
		charisma = request.form['charisma']
		new_character = Character(username, race, job, int(strength), int(dexterity), int(constitution), int(intelligence), int(wisdom), int(charisma))

	return render_template('newcharacter.html', newchar=new_character)




if __name__ == '__main__':
	app.run(debug=True)