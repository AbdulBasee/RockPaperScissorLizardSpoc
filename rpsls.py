



import tkinter as tk
from PIL import ImageTk, Image
import random
import pygame
pygame.init()


lis = {"Rock": 0, "Spock": 1, "Paper": 2, "lizard": 3, "Scissor": 4}                # the dictionary of different options to choose from
window = tk.Tk()
user_score = 0              # user score set to zero before the game starts
comp_score = 0             # comp score set to zero before the game starts

def user_choose(user):
    """

    :param user: this parameter takes strings of 'rock, paper,scissor, lizard, or spock as parameter'
    :return: it returns the digits starting 0 to 5
    """

    for i, j in lis.items():          # i refers to the key of above dictiionary.
                                         # j refers to the value of above dictioanry
        if user == i:
            return j

def computer(random_selc):
    """

    :param random_selc: This takes in numbers 0 to 5 as input
    :return: it returns the strings of rock, paper,scissor, lizard, or spock
    """


    for m, n in lis.items():               # i refers to the key of above dictiionary.
                                         # j refers to the value of above dictioanry
        if random_selc == n:
            return m

def rock(roc):
    """

    :param roc: it takes in "rock' as parameter in the rock button
    :return: returns None
    """
    global user_score
    global comp_score

    pygame.mixer.music.load("rock.mp3")  # Loading File Into Mixer
    pygame.mixer.music.play()


    result = user_choose(roc)


    comp = random.randint(0,4)
    comp_result = computer(comp)

    modulus = (result - comp) % 5
    if modulus == 1 or modulus == 2:

        user_score += 10


    elif modulus == 3 or modulus == 4:

        comp_score += 10

    else:
        result = 'it is a tie'

    text_area = tk.Text(master=window, height=12, width=30, bg="#FFF0F5")
    text_area.place(x = 400, y = 50)
    answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} \n result: {res} ".format(
        uc=roc, cc=comp_result, u=user_score, c=comp_score, res = result)
    text_area.insert(tk.END, answer)




def spock(spoc):
    """

    :param spoc: it takes in spock as parameter in the spock button
    :return: None
    """
    global user_score
    global comp_score

    pygame.mixer.music.load("spock01.mp3")  # Loading File Into Mixer
    pygame.mixer.music.play()

    result = user_choose(spoc)

    comp = random.randint(0, 4)
    comp_result = computer(comp)

    modulus = (result - comp) % 5
    if modulus == 1 or modulus == 2:

        user_score += 10


    elif modulus == 3 or modulus == 4:

        comp_score += 10

    else:
        result = 'it is a tie'

    text_area = tk.Text(master=window, height=12, width=30, bg="#FFF0F5")
    text_area.place(x=400, y=50)
    answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} \n result: {res} ".format(
        uc=spoc, cc=comp_result, u=user_score, c=comp_score, res= result)
    text_area.insert(tk.END, answer)



def paper(pape):
    """

    :param pape: it takes in paper as parameter in the spock button
    :return: None
    """
    global user_score
    global comp_score

    pygame.mixer.music.load("paper2.mp3")  # Loading File Into Mixer
    pygame.mixer.music.play()


    result = user_choose(pape)

    comp = random.randint(0, 4)
    comp_result = computer(comp)

    modulus = (result - comp) % 5
    if modulus == 1 or modulus == 2:

        user_score += 10


    elif modulus == 3 or modulus == 4:

        comp_score += 10

    else:
        result = 'it is a tie'


    text_area = tk.Text(master=window, height=12, width=30, bg="#FFF0F5")
    text_area.place(x=400, y=50)
    answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} \n result: {res} ".format(
            uc=pape, cc=comp_result, u=user_score, c=comp_score, res=result)
    text_area.insert(tk.END, answer)


def lizzard(lizz):
    """

    :param lizz: it takes in lizard as parameter in the spock button
    :return: None
    """
    global user_score
    global comp_score


    pygame.mixer.music.load("lizard.mp3")  # Loading File Into Mixer
    pygame.mixer.music.play()


    result = user_choose(lizz)

    comp = random.randint(0, 4)
    comp_result = computer(comp)

    modulus = (result - comp) % 5
    if modulus == 1 or modulus == 2:

        user_score += 10

    elif modulus == 3 or modulus == 4:

        comp_score += 10


    else:
        result = 'it is a tie'

    text_area = tk.Text(master=window, height=12, width=30, bg= "#FFF0F5")
    text_area.place(x=400, y=50)
    answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} \n result: {res} ".format(
        uc=lizz, cc=comp_result, u=user_score, c=comp_score, res= result)
    text_area.insert(tk.END, answer)




def scissor(sciss):
    """

    :param sciss: it takes in scissor as parameter in the spock button
    :return: None
    """
    global user_score
    global comp_score


    pygame.mixer.music.load("scissorsound.mp3")  # Loading File Into Mixer
    pygame.mixer.music.play()



    result = user_choose(sciss)

    comp = random.randint(0, 4)
    comp_result = computer(comp)

    modulus = (result - comp) % 5
    if modulus == 1 or modulus == 2:

        user_score += 10

    elif modulus == 3 or modulus == 4:

        comp_score += 10


    else:
        result = 'it is a tie'

    text_area = tk.Text(master=window, height=12, width=30, bg="#FFF0F5")
    text_area.place(x=400, y=400)
    answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} \n result: {res} ".format(
        uc=sciss, cc=comp_result, u=user_score, c=comp_score, res= result)
    text_area.insert(tk.END, answer)





def main():

    roc = tk.PhotoImage(file="rocks.gif")
    button1 = tk.Button(window, image = roc, text = "Rock", command = lambda: rock("Rock")).place(x = 900, y = 0)


    spoc = tk.PhotoImage(file = "spockss.gif")
    button2 = tk.Button(window, image = spoc, text = "spock", command =lambda: spock("Spock")).place(x = 900, y = 400)


    pap = tk.PhotoImage(file = "papers.gif")
    button3 = tk.Button(window, image = pap, text = "Paper", command =lambda: paper("Paper")).place(x = 100, y = 500)


    liz = tk.PhotoImage(file = "lizardsss.gif")
    button4 = tk.Button(window, image = liz, text = "lizard", command =lambda: lizzard("lizard")).place(x = 500, y = 300)


    scis = tk.PhotoImage(file="scissorss.gif")
    button5 = tk.Button(window,image = scis,  text = "scissor", command =lambda: scissor("Scissor")).place(x = 50, y = 10)



    window.mainloop()           # creates a mainloop window of tkinter

main()
