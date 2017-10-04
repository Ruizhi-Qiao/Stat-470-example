class scene1():
	def opening():
		print("LV1.1")
		print("""You have waked up in an empty room,
there is only 1 table with some food on it and a wardrobe.
It seems that you have been sleeping for days,
and you are quite hungry.
When you are about to eat the food, there is a
note with both side writing.""")
		print("""
FrontPage:
Welcome, you are 6th person came here.
As the Master, I have provide you some food.
You must be hungry, take them. You cannot go home with en empty stomach.
Oh yeah, and remember. DO NOT GET OUT, there are terrible things out there.
Rescue will come soon for you. 
--Master""")
		print("""
BackPage:
FrontPage is Bullshit. Don't trust it!
Run, there is a way out in the wardrobe.
The food is poisonous, you would die once u eat it!
And don't stay at home, zombie is coming.
--Anonymous""")
		survive = choice(["eat","skip"],2,["food has killed you"])
		if survive:
			scene1.LV2()

	def LV2():
		print("\nLV1.2")
		print("You have open the wardrobe, there is a secret way out")
		print("You walked carefully into there, with the fear of darkness")
		print("There are three doors there")
		print("Left door is locked, there is a smell of flower coming from")
		print("Middle door is opened, there is a window in the room with sunlight into it")
		print("Right door seemed to be opened half way, the secret way behind it is scaring")

		survive = choice(["Left", "Middle", "Right"],3,
			["door cannot be opened, while you were trying, a giant zombie ate you",
			"You chosed the Middle door, but there is a zombie behind it",
			""])
		if survive:
			scene1.LV3()

	def LV3():
		print("\nLV1.3")
		print("""You chose right door. It is a dark, scaring way with little light.
You are walking in the dark, step by step.
Suddenly you were stumbled by the stage, you fall down painfully.
You found a another note when you were trying to stand up.
You can barely saw the note, there are two arrows.
One to the Left and One to the right.
You were confused, so you looked around. 
Your left side has some light, but leads to nowhere you can know.
Your right side is unlimited darkness. Some zombie might be waiting for having an wonderful meal.
But you saw there is a door at the end of it, you might get up.
You were struggling because right side seems to be too risky.""")
		survive = choice(["Left", "Grab a light from left then go Right"],2,
			["You are always afraid of darkness. And now there is a bright way out\n\
so you run like mad, but at the time you were trying to escape.\n\
LIGHT OUT!. Something fast, strong has grabbed you. You lost your breadth",
			""])
		if survive:
			scene1.LV4()

	def LV4():
		print("\nLV1.4")
		print("""Light has empowered you to the end of right side.
It seemed like you have no choice but enter the door, because the back has been blocked by another door.
You walked into the door carefully and thought you have escaped.
Meanwhile, there were two person came in.
One is a girl as young as you are, one is a nurse. They are both beautiful.

Nurse came to you and said: 
"It is nice you did eat the poisonous food. or i wont see you. Come with me, I will lead you escape."
"The girl over there is mad, you cannot trust her. She will kill you"

Once Nurse finished, the girl came to whisper you:
"Don't trust that nurse, many people have been ate by zombie because they don't trust me.
"The nurse is the master here, she will send zombie to kill you."
"You have to come with me, or you will die. Don't trust here!"
""")
		print("You were struggling, but it is time for you to choose")
		survive = choice(["Nurse", "Girl"],2,
			["You chose the Nurse, she send you to the zombie base. You..."])
		if survive:
			scene1.LV5()

	def LV5():
		print("\nLV1.5")
		print("""You chose girl with doubt, but you know the master will not let you go so easily, though she left.
Girl warned you to be be careful, but you still have triggered the trap.
Zombie rushed into the room, you and girl are forced into a small corner.
You Left Side is a window. You can jump out of it, but you don't whether you will die because it is too high.
You right side is a door, but you are afraid there are more zombies in it.
Time is running out, you have to make a choice!.""")
		survive = choice(["Jump out of window", "Take the door"],1,
			["", "Congratulation, zombie ate you!"])
		if survive:
			scene1.closing()

	def closing():
		print("\n End Scene in Scene 1")
		print("You jumped out of the window, fell into the water.")
		print("You came into an island with a wood")
		print("The girl left you to go back and save others.")
		print("---------Congratulation you have passed Stage 1---------")


def choice(choice, live, deathsentence):
	print("Your choice?:")
	order = ["1:", "2:", "3:"]
	i = 0;
	for sentence in choice:
		print(order[i] + sentence)
		i += 1

	while True:
		n = input("Please Enter the number of you choice:")
		try:
			n = int(n)
		except:
			continue

		if n in range(1,len(choice) + 1):
			if n == live:
				return True
			else:
				game_over(deathsentence[n-1])
		

def game_over(message):
	print(message)
	print("GAME OVER")
	n = input("Press any button to exit:")
	exit("GAME OVER")



def main():
	scene1.opening()


if __name__ == "__main__":
	main()
