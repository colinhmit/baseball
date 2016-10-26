import random

class BaseballGame:

	def __init__(self, team_a, team_b, sim):
		#set up the baseball game's attr
		self.home_score = 0
		self.away_score = 0
		self.home_name = team_a
		self.away_name = team_b
		self.inning = 0
		self.sim = True

		if sim == 'y':
			self.sim = False
			print('(Hit enter when it says "Batter up!")')

	#play the game
	def play_game(self):
		print('Play ball!')
		batting_team = 'away'
		inning = 0 

		while inning < 10:
			if batting_team == 'away':
				print('/////////////////////////////')
				print('Starting the top of the ' + str(inning))
				print('/////////////////////////////')
			else:
				print('/////////////////////////////')
				print('Starting the bottom of the ' + str(inning))
				print('/////////////////////////////')

			self.play_inning(batting_team)

			if batting_team == 'away':
				batting_team = 'home'
			else:
				inning += 1
				batting_team = 'away'

		self.print_score()

	#play an inning
	def play_inning(self,team):
		outs = 0
		self.bases = [0,0,0]
		while outs < 3:
			self.print_game_state(team,outs)
			if not self.sim:
				raw_input("Batter up!")
			ab = self.at_bat()
			self.print_hit(ab)
			if ab == 0:
				outs += 1
			else:
				self.advance_runners(ab, team)

	#advance runners using force moves.
		#psuedocode helper
		# start [0 1 1]
		# hit ab=2, new=[0 1 0], i in [0;1]
		# 	i=0, i=1 -> bin=[0 0 2 0]

		# i=2
		# 	new=[0 1 1], bin=[0 0 2 1]
		# i=3
		# 	score 1

		# start [0 1 1]
		# hit ab=3, new=[0 0 1], i in [0;2]
		# i=0, i=1 -> bin=[0 0 2 0], i=2 -> bin=[0 0 0 2]

		# i = 3
		# 	score 2
	def advance_runners(self, ab, team):
		if ab == 4: 
			if team == 'home':
				print('Home team scores!')
				self.home_score += sum(self.bases) + 1
				self.print_score()
			else:
				print('Away team scores!')
				self.away_score += sum(self.bases) + 1
				self.print_score()
			self.bases = [0,0,0]

		else:
			bin_basestate = list(self.bases)
			bin_basestate.append(0)

			new_basestate = list(self.bases)
			for i in range(0,ab):
				if bin_basestate[i] > 0:
						bin_basestate[i+1] += bin_basestate[i]
						bin_basestate[i] = 0
						new_basestate[i] = 0
			new_basestate[ab-1] = 1

			i = ab
			while bin_basestate[i] > 0:
				if i == 3:
					if team == 'home':
						print('Home team scores!')
						self.home_score += bin_basestate[i]
						self.print_score()
					else:
						print('Away team scores!')
						self.away_score += bin_basestate[i]
						self.print_score()
					break
				else:
					new_basestate[i] = 1
					bin_basestate[i+1] += (bin_basestate[i]-1)
				i+=1

			self.bases = list(new_basestate)

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


	def print_hit(self,ab):
		print('----------------------')
		if ab == 0:
			print('Out!')
		elif ab == 1:
			print('Hit a single!')
		elif ab == 2:
			print('Hit a double!')
		elif ab == 3:
			print('Hit a triple!')
		elif ab == 4:
			print('Home Run!!!')

	def print_game_state(self,team,outs):
		print('----------------------')
		print('                      ')
		print('           ('+str(self.bases[1])+')        ')
		print('          /    \      ')
		print('       ('+str(self.bases[2])+')      ('+str(self.bases[0])+')   ')
		print('          \    /      ')
		print('           ( )        ')
		if team == 'home':
			print(self.home_name + ' at the plate.')
		else:
			print(self.away_name + ' at the plate.')
		print(str(outs) + ' outs.')

	def print_score(self):
		print('///////////////')
		print('Scoreboard:')
		print(self.home_name + ' = ' + str(self.home_score))
		print(self.away_name + ' = ' + str(self.away_score))
		print('///////////////')

if __name__ == '__main__':
	print('Lets play baseball!')
	team_a = raw_input("Enter the home team's name:")
	team_b = raw_input("Enter the away team's name:")
	sim = raw_input("Do you want to play manually (y/n)?")
	game = BaseballGame(team_a, team_b, sim)
	game.play_game()
