#import SPGL
import spgl
import turtle
import math
import random
import time

#Initial game setup / Title
game = spgl.Game(1000, 800, "black", "Hangman", 7)

#Words List 
words = ["sacred", "adult", "bob", "madeline", "because", "whatever", "hangman", "chairs", "backpack", "bodywash", "clothing",
"computer", "python", "program", "glasses","sweatpant", "mattress", "friends", "clocks", "biology","algebra", "suitcase", "knives",
"ninjas", "shampoo", "madeline", "okay", "because", "whatever"]

#Create classes

class Hangman(object):
	def __init__(self):
		self.correct_answer = random.choice(words)
		self.player_guess = "_______________________________________"
		self.score = 0 
		self.chances = 5
				
	def check_guess(self, player_letter):
			
		temp = ""
		for index in range(len(self.correct_answer)):
			print(self.correct_answer, self.player_guess)
			if self.correct_answer[index] == player_letter:
				temp += player_letter
			elif self.player_guess[index] != "_":
				temp += self.player_guess[index]
			else:
				temp += "_"
				

		self.player_guess = temp	
		
		output = ""
		for player_guess in temp:
			output += player_guess + " "
		print(output)		
		dash_label.update(output)
		
		# Update letters from white to blue
		if player_letter == "a":
			keyboard_A.set_image("keyboard_change_A.gif", 20, 20)
		
		elif player_letter == "b":
			keyboard_B.set_image("keyboard_change_B.gif", 20, 20)
			
		elif player_letter == "c":
			keyboard_C.set_image("keyboard_change_C.gif", 20, 20)
			
		elif player_letter == "d":
			keyboard_D.set_image("keyboard_change_D.gif", 20, 20)
			
		elif player_letter == "e":
			keyboard_E.set_image("keyboard_change_E.gif", 20, 20)
		
		elif player_letter == "f":
			keyboard_F.set_image("keyboard_change_F.gif", 20, 20)
			
		elif player_letter == "g":
			keyboard_G.set_image("keyboard_change_G.gif", 20, 20)
			
		elif player_letter == "h":
			keyboard_H.set_image("keyboard_change_H.gif", 20, 20)
			
		elif player_letter == "i":
			keyboard_I.set_image("keyboard_change_I.gif", 20, 20)
			
		elif player_letter == "j":
			keyboard_J.set_image("keyboard_change_J.gif", 20, 20)
			
		elif player_letter == "k":
			keyboard_K.set_image("keyboard_change_K.gif", 20, 20)
			
		elif player_letter == "l":
			keyboard_L.set_image("keyboard_change_L.gif", 20, 20)
			
		elif player_letter == "m":
			keyboard_M.set_image("keyboard_change_M.gif", 20, 20)
			
		elif player_letter == "n":
			keyboard_N.set_image("keyboard_change_N.gif", 20, 20)
			
		elif player_letter == "o":
			keyboard_O.set_image("keyboard_change_O.gif", 20, 20)
			
		elif player_letter == "p":
			keyboard_P.set_image("keyboard_change_P.gif", 20, 20)
			
		elif player_letter == "q":
			keyboard_Q.set_image("keyboard_change_Q.gif", 20, 20)
			
		elif player_letter == "r":
			keyboard_R.set_image("keyboard_change_R.gif", 20, 20)
			
		elif player_letter == "s":
			keyboard_S.set_image("keyboard_change_S.gif", 20, 20)
			
		elif player_letter == "t":
			keyboard_T.set_image("keyboard_change_T.gif", 20, 20)
			
		elif player_letter == "u":
			keyboard_U.set_image("keyboard_change_U.gif", 20, 20)
			
		elif player_letter == "v":
			keyboard_V.set_image("keyboard_change_V.gif", 20, 20)
			
		elif player_letter == "w":
			keyboard_W.set_image("keyboard_change_W.gif", 20, 20)
			
		elif player_letter == "x":
			keyboard_X.set_image("keyboard_change_X.gif", 20, 20)
			
		elif player_letter == "y":
			keyboard_Y.set_image("keyboard_change_Y.gif", 20, 20)
			
		elif player_letter == "z":
			keyboard_Z.set_image("keyboard_change_Z.gif", 20, 20)
			
		if player_letter in "abcdefghijklmnopqrstuvwxyz":
			game.play_sound("alphabet_clicked.wav") 


		if "_" not in hangman.player_guess:
			hangman.score += 10
			game.play_sound("correct_answer_sound.wav -v 0.1")
			score_label.update("SCORE: {}".format(hangman.score))
			you_win.showturtle()
			game.tick()
			time.sleep(5)
			self.correct_answer = random.choice(words)
			self.player_guess = "_______________________________________"
			self.chances = 5
			hangman_face.hideturtle()
			hangman_body.hideturtle()
			hangman_hands.hideturtle()
			hangman_legs.hideturtle()
			you_win.hideturtle()
			hangman.check_guess(" ")
			keyboard_A.set_image("keyboard_A.gif", 20, 20)
			keyboard_B.set_image("keyboard_B.gif", 20, 20)		
			keyboard_C.set_image("keyboard_C.gif", 20, 20)
			keyboard_D.set_image("keyboard_D.gif", 20, 20)
			keyboard_E.set_image("keyboard_E.gif", 20, 20)
			keyboard_F.set_image("keyboard_F.gif", 20, 20)
			keyboard_G.set_image("keyboard_G.gif", 20, 20)
			keyboard_H.set_image("keyboard_H.gif", 20, 20)
			keyboard_I.set_image("keyboard_I.gif", 20, 20)
			keyboard_J.set_image("keyboard_J.gif", 20, 20)
			keyboard_K.set_image("keyboard_K.gif", 20, 20)
			keyboard_L.set_image("keyboard_L.gif", 20, 20)
			keyboard_M.set_image("keyboard_M.gif", 20, 20)
			keyboard_N.set_image("keyboard_N.gif", 20, 20)
			keyboard_O.set_image("keyboard_O.gif", 20, 20)
			keyboard_P.set_image("keyboard_P.gif", 20, 20)
			keyboard_Q.set_image("keyboard_Q.gif", 20, 20)
			keyboard_R.set_image("keyboard_R.gif", 20, 20)
			keyboard_S.set_image("keyboard_S.gif", 20, 20)
			keyboard_T.set_image("keyboard_T.gif", 20, 20)
			keyboard_U.set_image("keyboard_U.gif", 20, 20)
			keyboard_V.set_image("keyboard_V.gif", 20, 20)
			keyboard_W.set_image("keyboard_W.gif", 20, 20)
			keyboard_X.set_image("keyboard_X.gif", 20, 20)
			keyboard_Y.set_image("keyboard_Y.gif", 20, 20)
			keyboard_Z.set_image("keyboard_Z.gif", 20, 20)
			
			
	
		if player_letter not in hangman.correct_answer and player_letter != " ":
			hangman.chances -= 1
			chances_label.update("CHANCES: {}".format(hangman.chances))
			
					
		self.display_hangman()
		
	def display_hangman(self):
		if self.chances == 4:
			hangman_face.showturtle()
		elif self.chances == 3:
			hangman_body.showturtle()
		elif self.chances == 2:
			hangman_hands.showturtle()
		elif self.chances == 1:
			hangman_legs.showturtle()
		elif self.chances == 0:
			you_lose.showturtle()
			correct_word_label.update("CORRECT WORD: {}".format(self.correct_answer))
			game.play_sound("fail_answer_sound.wav -v 0.1") 

class Title(spgl.Sprite):
	def __init__ (self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.shape("title.gif")
		
class Hangman_Images(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)

class Keyboard_Image(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		
class You_Lose(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
				
class You_Win(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		


#Create Functions

def keypress(event):
	key = event.char
	hangman.check_guess(key)

root = spgl.turtle.getcanvas()
root.bind("<Key>", keypress)
#Create instances		
title = Title("title.gif", "black", 190.0,348.0) 

hangman_stand = Hangman_Images("hangman_stand.gif","white", -325.0, 100.0)
hangman_face = Hangman_Images("hangman_face.gif","white", -248.0, 228.0)
hangman_body = Hangman_Images("hangman_body.gif","white", -235.0, 158.0)
hangman_hands = Hangman_Images("hangman_hands.gif","white", -245.0, 158.0)
hangman_legs = Hangman_Images("hangman_legs.gif","white", -235.0, 92.0)
you_lose = You_Lose("you_lose.gif","white", 0, 0)
you_win = You_Win("you_win.gif","white", 0, 0)
hangman_face.hideturtle()
hangman_body.hideturtle()
hangman_hands.hideturtle()
hangman_legs.hideturtle()
you_lose.hideturtle()	
you_win.hideturtle()	
keyboard_A = Keyboard_Image("keyboard_A.gif","white", -335.0,-207.0)
keyboard_B = Keyboard_Image("keyboard_B.gif","white", 25.0,-280.0)
keyboard_C = Keyboard_Image("keyboard_C.gif","white", -135, -280.0)
keyboard_D = Keyboard_Image("keyboard_D.gif","white", -175.0, -207.0)
keyboard_E = Keyboard_Image("keyboard_E.gif","white", -215.0, -147.0)
keyboard_F = Keyboard_Image("keyboard_F.gif","white", -95.0, -207.0)
keyboard_G = Keyboard_Image("keyboard_G.gif","white", -15.0,-207.0)
keyboard_H = Keyboard_Image("keyboard_H.gif","white", 65.0,-207.0)
keyboard_I = Keyboard_Image("keyboard_I.gif","white", 185.0, -147.0)
keyboard_J = Keyboard_Image("keyboard_J.gif","white", 145.0, -207.0)
keyboard_K = Keyboard_Image("keyboard_K.gif","white", 225.0, -207.0)
keyboard_L = Keyboard_Image("keyboard_L.gif","white", 305.0, -207.0)
keyboard_N = Keyboard_Image("keyboard_N.gif","white", 105.0, -280.0)
keyboard_M = Keyboard_Image("keyboard_M.gif","white", 185.0, -280.0)
keyboard_O = Keyboard_Image("keyboard_O.gif","white", 265.0, -147.0)
keyboard_P = Keyboard_Image("keyboard_P.gif","white", 345.0, -147.0)
keyboard_Q = Keyboard_Image("keyboard_Q.gif","white", -375.0, -147.0)
keyboard_R = Keyboard_Image("keyboard_R.gif","white", -135.0, -147.0)
keyboard_S = Keyboard_Image("keyboard_S.gif","white", -255.0,-207.0)
keyboard_T = Keyboard_Image("keyboard_T.gif","white", -55.0, -147.0)
keyboard_U = Keyboard_Image("keyboard_U.gif","white", 105.0, -147.0)
keyboard_V = Keyboard_Image("keyboard_V.gif","white", -55.0, -280.0)
keyboard_W = Keyboard_Image("keyboard_W.gif","white", -295.0, -147.0)
keyboard_X = Keyboard_Image("keyboard_X.gif","white", -215.0, -280.0)
keyboard_Y = Keyboard_Image("keyboard_Y.gif","white", 25.0, -147.0)
keyboard_Z = Keyboard_Image("keyboard_Z.gif","white", -295, -280.0)

hangman = Hangman()

# Create Labels
dash_label = spgl.Label("_", "white", 0,0)

dash_label.set_font_name("Krungthep")
dash_label.set_font_size(100)

dash_label.set_font_name("Krungthep")
dash_label.set_font_type("bold") 
dash_label.set_font_size(60)


score_label = spgl.Label("SCORE: 0", "white", -459.0,-77.0)
score_label.set_font_name("Krungthep")
score_label.set_font_size(20)

chances_label = spgl.Label("CHANCES: 6", "white",-459.0,-100.0)
chances_label.set_font_name("Krungthep")
chances_label.set_font_size(20)


# -444.0,-100.0)

correct_word_label = spgl.Label(" ", "red", 7.0,95.0)
correct_word_label.set_font_name("Krungthep")
correct_word_label.set_font_size(30)




while True:
    # Call the game tick method
	game.tick()


	