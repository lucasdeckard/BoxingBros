import pygame
import button
import math

pygame.init()

#create game window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

clock = pygame.time.Clock()
fps = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

display_surface = pygame.display.set_mode((1280, 720))

font = pygame.font.Font('BoxingBros/assets/fortnite.ttf', 100, bold=True)
text = font.render('Boxing Bros', True, (252,252,252))
textRect = text.get_rect()
textRect.center = (350, 150)
#game variables
game_paused = False
menu_state = "main"

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)

#load button images
resume_img = pygame.image.load("boxingbros/assets/button_resume.png").convert_alpha()
options_img = pygame.image.load("boxingbros/assets/button_options.png").convert_alpha()
quit_img = pygame.image.load("boxingbros/assets/button_quit.png").convert_alpha()
video_img = pygame.image.load('boxingbros/assets/button_video.png').convert_alpha()
audio_img = pygame.image.load('boxingbros/assets/button_audio.png').convert_alpha()
keys_img = pygame.image.load('boxingbros/assets/button_keys.png').convert_alpha()
back_img = pygame.image.load('boxingbros/assets/button_back.png').convert_alpha()
play_img = pygame.image.load('boxingbros/assets/button_play.png').convert_alpha()
#create button instances
resume_button = button.Button(304, 125, resume_img, 1)
options_button = button.Button(297, 250, options_img, 1)
quit_button = button.Button(336, 375, quit_img, 1)
video_button = button.Button(226, 75, video_img, 1)
audio_button = button.Button(225, 200, audio_img, 1)
keys_button = button.Button(246, 325, keys_img, 1)
back_button = button.Button(332, 450, back_img, 1)
play_button = button.Button(300, 275, play_img, 1)
options_button2 = button.Button(260, 375, options_img, 1)
quit_button2 = button.Button(300, 475, quit_img, 1)

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
        #adding all the images to sprite array
        self.images = []
        self.images.append(pygame.image.load('BoxingBros/assets/GaryMenu1.png'))
        self.images.append(pygame.image.load('BoxingBros/assets/GaryMenu2.png'))
        self.images.append(pygame.image.load('BoxingBros/assets/GaryMenu3.png'))
 
        #index value to get the image from the array
        #initially it is 0 
        self.index = 0
 
        #now the image that we will display will be the index from the image array 
        
 
        #creating a rect at position x,y (5,5) of size (150,198) which is the size of sprite 
        self.rect = pygame.Rect(700, 75, 150, 198)
 
    def update(self):
        #when the update method is called, we will increment the index
        self.index += 0.08
 
        #if the index is larger than the total images
        if self.index >= len(self.images):
            #we will make the index to 0 again
            self.index = 0
        
        #finally we will update the image that will be displayed
        self.image = self.images[math.floor(self.index)]


#game loop
run = True
my_sprite = MySprite()
my_group = pygame.sprite.Group(my_sprite)
menu_state = "menu"
while run:
  clock.tick(60)
  screen.fill((52, 78, 91))
  display_surface.blit(text, textRect)
  #check if game is paused
  if game_paused == True:
    #check menu state
    if menu_state == "main":
      #draw pause screen buttons
      if resume_button.draw(screen):
        game_paused = False
      if options_button.draw(screen):
        menu_state = "options"
      if quit_button.draw(screen):
        run = False
    #check if the options menu is open
    if menu_state == "options":
      #draw the different options buttons
      if video_button.draw(screen):
        print("Video Settings")
      if audio_button.draw(screen):
        print("Audio Settings")
      if keys_button.draw(screen):
        print("Change Key Bindings")
      if back_button.draw(screen):
        menu_state = "main"
  else:
    if menu_state == "menu":
      if play_button.draw(screen):
          print("Press to Play")
      if options_button2.draw(screen):
          menu_state = "options"
      if quit_button2.draw(screen):
          run = False
    if menu_state == "options":
      #draw the different options buttons
      if video_button.draw(screen):
        print("Video Settings")
      if audio_button.draw(screen):
        print("Audio Settings")
      if keys_button.draw(screen):
        print("Change Key Bindings")
      if back_button.draw(screen):
        menu_state = "menu"
    
    

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False
  
  my_group.update()
  my_group.draw(screen)
  pygame.display.update()

pygame.quit()
