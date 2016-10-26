import random



class BaseballGame:

	def __init__(self):
		#set up the baseball game's attr
		self.bases = {'first':0,'second':0,'third':0}
		self.home_score = 0
		self.away_score = 0
		self.inning = 0

	#play the game
	def play_game(self):
		team = 'away'
		inning = 0 

		while inning < 10:
			self.play_inning(team)

			if team == 'away':
				team = 'home'
			else:
				inning += 1

	#play an inning
	def play_inning(self,team):
		outs = 0
		self.bases = {'first':0,'second':0,'third':0}

	  	while outs < 3:
	  		ab = self.at_bat()
	  		if ab == 0:
	  			outs += 1
	  		else:
	  			self.advance_runners(ab, team)

	#advance runners using force moves.
	#ugly if statement.
	def advance_runners(self, ab, team):

		base_state = 'Undefined'

		if self.bases['first'] == 1:
			if self.bases['second'] == 1:
				if self.bases['third'] == 1:
					base_state = '111'
				else:
					base_state = '110'
			else:
				if self.bases['third'] == 1:
					base_state = '101'
				else:
					base_state = '100'
		else:
			if self.bases['second'] == 1:
				if self.bases['third'] == 1:
					base_state = '011'
				else:
					base_state = '010'
			else:
				if self.bases['third'] == 1:
					base_state = '001'
				else:
					base_state = '000'

		if ab == 0:
			pass

		elif ab == 1:
			if (base_state == '000') or (base_state == '011') or (base_state == '001') or (base_state == '010'):
				self.bases['first'] = 1
			elif base_state == '111':
				if team == 'home':
					self.home_score += 1
				else:
					self.away_score += 1
			elif base_state == '110':
				self.bases['third'] = 1 
			elif base_state == '100':
				self.bases['second'] = 1
			elif base_state == '101':
				self.bases['second'] = 1
			else:
				pass

		elif ab == 2:
			if (base_state == '000') or (base_state == '001'):
				self.bases['second'] = 1
			elif base_state == '010':
				self.bases['third'] = 1
			elif base_state == '011':
				if team == 'home':
					self.home_score += 1
				else:
					self.away_score += 1
			elif base_state == '111':
				self.bases['first'] = 0
				if team == 'home':
					self.home_score += 2
				else:
					self.away_score += 2
			elif base_state == '110':
				self.bases['first'] = 0
				self.bases['third'] = 1 
				if team == 'home':
					self.home_score += 1
				else:
					self.away_score += 1
			elif base_state == '100':
				self.bases['first'] = 0
				self.bases['second'] = 0
				self.bases['third'] = 1
			elif base_state == '101':
				self.bases['first'] = 0
				self.bases['second'] = 1 
				if team == 'home':
					self.home_score += 1
				else:
					self.away_score += 1
			else:
				pass

		elif ab == 3:
			if (base_state == '100') or (base_state == '010') or (base_state == '001'):
				self.bases['first'] = 0
				self.bases['second'] = 0
				self.bases['third'] = 1
				if team == 'home':
					self.home_score += 1
				else:
					self.away_score += 1
			elif (base_state == '110') or (base_state == '011') or (base_state == '101'):
				self.bases['first'] = 0
				self.bases['second'] = 0
				self.bases['third'] = 1
				if team == 'home':
					self.home_score += 2
				else:
					self.away_score += 2
			elif base_state == '000':
				self.bases['third'] = 1
			elif base_state == '111':
				self.bases['first'] = 0
				self.bases['second'] = 0
				self.bases['third'] = 1
				if team == 'home':
					self.home_score += 3
				else:
					self.away_score += 3
			else:
				pass

		elif ab == 4:
			if (base_state == '100') or (base_state == '010') or (base_state == '001'):
				self.bases['first'] = 0
				self.bases['second'] = 0
				self.bases['third'] = 0
				if team == 'home':
					self.home_score += 2
				else:
					self.away_score += 2
			elif (base_state == '110') or (base_state == '011') or (base_state == '101'):
				self.bases['first'] = 0
				self.bases['second'] = 0
				self.bases['third'] = 0
				if team == 'home':
					self.home_score += 3
				else:
					self.away_score += 3
			elif base_state == '000':
				if team == 'home':
					self.home_score += 1
				else:
					self.away_score += 1
			elif base_state == '111':
				self.bases['first'] = 0
				self.bases['second'] = 0
				self.bases['third'] = 0
				if team == 'home':
					self.home_score += 4
				else:
					self.away_score += 4
			else:
				pass

		else:
			pass

	#sim an at bat
	def at_bat(self):
		outcome = random.randint(0,100)

		ab = -1

		if outcome < 50:
			ab = 0
		elif outcome < 80:
			ab = 1
		elif outcome < 90:
			ab = 2
		elif outcome < 96:
			ab = 3
		else:
			ab = 4

		return ab

if __name__ == '__main__':
    game = BaseballGame()
    game.play_game()
