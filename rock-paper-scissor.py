import pygame
import random
from pygame import mixer

# initialize py_game
pygame.init()

# setup or run the screen
screen = pygame.display.set_mode((600, 600))
running = True

# title and icon
pygame.display.set_caption("Rock Paper Scissors")
icon = pygame.image.load('rockicon.jpg')
pygame.display.set_icon(icon)

# list of values
ele = ['rock', 'paper', 'scissors']

# Rock
rock_img = pygame.image.load('rock.png')

# Paper
paper_img = pygame.image.load('paper.png')

# scissor
scissor_img = pygame.image.load('scissors.png')

# game text
over_font = pygame.font.Font("freesansbold.ttf", 30)


# function of rock
def rock(rock_x, rock_y):
    screen.blit(rock_img, (rock_x, rock_y))


# function of paper
def paper(paper_x, paper_y):
    screen.blit(paper_img, (paper_x, paper_y))


# function of scissor
def scissor(scissor_x, scissor_y):
    screen.blit(scissor_img, (scissor_x, scissor_y))


# Rock button text
def rock_text():
    text = over_font.render("ROCK", True, (0, 0, 128))
    screen.blit(text, (10, 540))


# Rock button text
def paper_text():
    text = over_font.render("PAPER", True, (0, 0, 128))
    screen.blit(text, (110, 540))


# Rock button text
def scissor_text():
    text = over_font.render("SCISSORS", True, (0, 0, 128))
    screen.blit(text, (230, 540))


# player text
def player():
    text = over_font.render("PLAYER", True, (225, 0, 0))
    screen.blit(text, (10, 40))


# computer text
def computer():
    text = over_font.render("COMPUTER", True, (225, 0, 0))
    screen.blit(text, (410, 40))


# computer function
def comp_decider(comp1):
    if comp1 == 'rock':
        rock(380, 100)
    elif comp1 == 'paper':
        paper(380, 100)
    elif comp1 == 'scissors':
        scissor(380, 100)


# function for checking winner
def decider(inp, comp):
    if comp == 'rock' and inp == 'p':
        game_over_text("Player")

    elif comp == 'rock' and inp == 's':
        game_over_text("Computer")

    elif comp == 'paper' and inp == 'r':
        game_over_text("Computer")

    elif comp == 'paper' and inp == 's':
        game_over_text("Player")

    elif comp == 'scissors' and inp == 'r':
        game_over_text("Player")

    elif comp == 'scissors' and inp == 'p':
        game_over_text("Computer")

    elif (comp == 'rock' and inp == 'r') or (comp == 'paper' and inp == 'p') or (comp == 'scissors' and inp == 's'):
        game_over_text1()


# game over function
def game_over_text(win):
    over_text_1 = over_font.render("GAME OVER !!", True, (225, 0, 0))
    over_text_2 = over_font.render(str(win) + " WIN'S", True, (255, 200, 32))
    screen.blit(over_text_1, (200, 250))
    screen.blit(over_text_2, (190, 300))


# game over function 1
def game_over_text1():
    over_text_1 = over_font.render("GAME OVER !!", True, (225, 0, 0))
    over_text_2 = over_font.render("IT'S A DRAW", True, (240, 240, 32))
    screen.blit(over_text_1, (200, 250))
    screen.blit(over_text_2, (210, 300))


inp1 = ''
comp1 = random.choice(ele)

# game loop
while running:

    for event in pygame.event.get():

        # when game is closed
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)
            if 11 <= x <= 95 and 541 <= y <= 565:
                click_sound = mixer.Sound('mouse-click.wav')
                click_sound.play()
                pygame.time.wait(200)
                if inp1 == '':
                    rock(-20, 100)
                    inp1 = 'r'
                    comp_decider(comp1)
                    decider(inp1, comp1)
            if 111 <= x <= 213 and 541 <= y <= 565:
                click_sound = mixer.Sound('mouse-click.wav')
                click_sound.play()
                pygame.time.wait(200)
                if inp1 == '':
                    paper(-20, 100)
                    inp1 = 'p'
                    comp_decider(comp1)
                    decider(inp1, comp1)
            if 231 <= x <= 389 and 541 <= y <= 565:
                click_sound = mixer.Sound('mouse-click.wav')
                click_sound.play()
                pygame.time.wait(200)
                if inp1 == '':
                    scissor(-20, 100)
                    inp1 = 's'
                    comp_decider(comp1)
                    decider(inp1, comp1)

    player()
    computer()
    pygame.draw.rect(screen, (255, 0, 0), (10, 540, 89, 30))
    rock_text()
    pygame.draw.rect(screen, (255, 0, 0), (110, 540, 107, 30))
    paper_text()
    pygame.draw.rect(screen, (255, 0, 0), (230, 540, 162, 30))
    scissor_text()
    pygame.display.update()
