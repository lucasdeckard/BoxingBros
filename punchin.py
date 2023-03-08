import pygame
import random

pygame.init()

# set up the screen
screen_width = 834
screen_height = 581
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Punch Out Game - MOO ICT")

# set up the fonts
font = pygame.font.SysFont(None, 30)

# load the images
background = pygame.image.load('BoxingBros/assets/background.jpg')
player_image = pygame.image.load("BoxingBros/assets/boxer-stand.png")
player_left_punch_image = pygame.image.load("BoxingBros/assets/boxer-left-punch.png")
player_right_punch_image = pygame.image.load("BoxingBros/assets/boxer-right-punch.png")
player_block_image = pygame.image.load("BoxingBros/assets/boxer-block.png")
enemy_image = pygame.image.load('BoxingBros/assets/enemy-stand.png')
enemy_punch1_image = pygame.image.load("BoxingBros/assets/enemy-punch1.png")
enemy_punch2_image = pygame.image.load("BoxingBros/assets/enemy-punch2.png")
enemy_block_image = pygame.image.load("BoxingBros/assets/enemy-block.png")

# set up the variables
fps = 60
player_block = False
enemy_block = False
enemy_speed = 5
index = 0
player_health = 100
enemy_health = 100
enemy_attacks = ["left", "right", "block", "stand"]
clock = pygame.time.Clock()
player_x = 370
player_y = 350
enemy_x = 350 
enemy_y = 150
last_attack_time = pygame.time.get_ticks()
player_original_y = player_y
enemy_original_y = enemy_y
playerat = False
enemyat = False



# set up the functions
def reset_game():
    global player_health, enemy_health, enemy_speed
    player_health = 100
    enemy_health = 100
    enemy_speed = 5
    enemy_rect.centerx = 400


def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def check_collision():
    global player_health, enemy_health
    if enemyat == True and not player_block:
        player_health -= 10
    if playerat == True and not enemy_block:
        enemy_health -= 10

def losescreen():
    global running
    screen.fill('black')
    draw_text("You LOSE, Click SPACE to Play Again or ESCAPE to Return to the Menu", (255, 255, 255), screen_width // 2, screen_height // 2)

def winscreen():
    global running
    screen.fill('black')
    draw_text("You WIN, Click SPACE to Play Again or ESCAPE to Return to the Menu", (255, 255, 255), screen_width // 2, screen_height // 2)
        
        
# load the music and play it
#pygame.mixer.music.load("punchout.wav")
#pygame.mixer.music.play(-1)

player_rect = player_image.get_rect()
player_rect.centerx = player_x
player_rect.centery = player_y

enemy_rect = enemy_image.get_rect()
enemy_rect.centerx = enemy_x
enemy_rect.centery = enemy_y

# set up the game loop
running = True
while running:
    clock.tick(30)
    screen.blit(background, (0,0))
    screen.blit(enemy_image, (enemy_x, enemy_y))
    screen.blit(player_image, (player_x, player_y))
    
    

    draw_text("{}".format(enemy_health), (255, 255, 255), 175, 50)
    draw_text("{}".format(player_health), (255, 255, 255), 625, 50)



    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_image = player_left_punch_image
                player_block = False
                playerat = True
                player_y = 250
                check_collision()
            if event.key == pygame.K_RIGHT:
                player_image = player_right_punch_image
                player_block = False
                playerat = True
                player_y = 250
                check_collision()
            if event.key == pygame.K_DOWN:
                player_image = player_block_image
                player_block = True
                playerat = False
                player_y = player_original_y
            if event.key == pygame.K_SPACE:
                reset_game()
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.KEYUP:
            player_image = pygame.image.load("BoxingBros/assets/boxer-stand.png")
            player_block = False
            playerat = False
            player_y = player_original_y




    
    # check if it's time for the enemy to attack
    time_since_last_attack = pygame.time.get_ticks() - last_attack_time
    if time_since_last_attack >= 500:
        # select the enemy attack
        index = random.randint(0, len(enemy_attacks) - 1)
        if enemy_attacks[index] == "left":
            enemy_image = enemy_punch1_image
            enemy_block = False
            enemyat = True
            enemy_y = 180
            check_collision()
        elif enemy_attacks[index] == "right":
            enemy_image = enemy_punch2_image
            enemy_block = False
            enemyat = True
            enemy_y = 180
            check_collision()
        elif enemy_attacks[index] == "block":
            enemy_image = enemy_block_image
            enemy_block = True
            enemyat = False
            enemy_y = enemy_original_y
        else:
            enemy_image = pygame.image.load('BoxingBros/assets/enemy-stand.png')
            enemy_block = False
            enemyat = False
            enemy_y= enemy_original_y
    

        # reset the timer
        last_attack_time = pygame.time.get_ticks()

    # check for the end of game scenario
    if enemy_health < 1:
        winscreen()
    elif player_health < 1:
        losescreen()
    pygame.display.update()
pygame.quit()
