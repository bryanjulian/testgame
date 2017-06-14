
''' This is Bryan Julian's game. '''

# Import pygame and random libraries
import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (51, 51, 255)

# ---------- All classes ---------
# This is the first enemy on level one, blue squares
class Enemy(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([50, 35])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()
    
# This is the second enemy on level two, green squares
class EnemyTwo(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([30, 20])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()

# The player, a black bow and arrow
class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
 
    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.image.load("player.png")
     
        self.image.set_colorkey(BLACK)
     
        self.rect = self.image.get_rect()   
 
    def update(self):
        """ Update the player's position. """
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
 
        # Set the player x position to the mouse x position
        self.rect.y = pos[1]
        
# This is the moving projectile, a black arrow
class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.image.load("arrows.png")
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the bullet. """
        self.rect.x += 11

# Initiate pygame 
pygame.init()


# ------- Sprite lists ---------
all_sprites_list = pygame.sprite.Group()
all_sprites_list_two = pygame.sprite.Group()
block_list = pygame.sprite.Group()
block_list_two = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
bullet_list_two = pygame.sprite.Group()

# Adds the player sprite to the lists
player = Player()
all_sprites_list.add(player)
all_sprites_list_two.add(player)

# Creates the enemies on the first level
for i in range(25):
    # This represents a block
    block = Enemy(BLUE)
 
    # Set a random location for the block
    block.rect.x = random.randrange(300, 1920)
    block.rect.y = random.randrange(160, 930)
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)

# Creates the enemies for the second level
for i in range(40):
    # This represents the second enemy
    enemytwo = EnemyTwo(GREEN)
    
    # Sets a random location for the blocks
    enemytwo.rect.x = random.randrange(300, 1920)
    enemytwo.rect.y = random.randrange(160, 930)
    
    # Adds to the list of objects
    block_list_two.add(enemytwo)
    all_sprites_list_two.add(enemytwo)


# Set the height and width of the screen
size = [1920, 1080]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Arrow Shooter")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- All of the sounds & images ---------
main_background_image = pygame.image.load("mainbackground.bmp").convert()  
info_background_image = pygame.image.load("instructionsbackground.bmp").convert()
intro_background_image = pygame.image.load("introbackground.bmp").convert()
end_screen_image = pygame.image.load("end_screen.png")
intro_music = pygame.mixer.Sound("bensound-straight.ogg")
hit_sound = pygame.mixer.Sound("successful_hit.ogg")
fire_sound = pygame.mixer.Sound("fire_sound.ogg")
victory_sound = pygame.mixer.Sound("Victory.ogg")

# This is a font we use to draw text on the screen (size 48)
font = pygame.font.Font(None, 48)

display_intro = True
intro = 1

# -------------- Intro Screen --------------
while not done and display_intro:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                done = True        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                instruction_page = 1
                intro = 0
                display_intro = False
                intro_music.stop()
    
    # Sets screen background
    screen.blit(intro_background_image, [0, 0])    
     
    # This will write the text which includes 
    # instructions to advance to the next screen.
    if intro == 1:
        
        # Plays music and sets the volume
        intro_music.set_volume(.07)
        intro_music.play()
        
        # Instructions to advance
        text = font.render("Press SPACE to start", True, WHITE)
        screen.blit(text, [780, 770])
    
        # Title
        text = font.render("~ Arrow Shooter ~", True, WHITE)
        screen.blit(text, [810, 270])
           
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()    
    
    
display_instructions = True
instruction_page = 1
name = ""
# -------- Instruction Page Loop -----------
while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                name += event.unicode
            elif event.key == pygame.K_BACKSPACE:
                name = name[:-1]
            elif event.key == pygame.K_RETURN:
                instruction_page += 1  
                if instruction_page == 3:
                    display_instructions = False                
 
    # Set the screen background
    screen.blit(info_background_image, [0, 0])
 
    if instruction_page == 1:
        # Draw instructions, page 1
        # This could also load an image created in another program.
        # That could be both easier and more flexible.
                
        text = font.render("Instructions", True, WHITE)
        screen.blit(text, [10, 10])
       
        text = font.render("Enter your name: ", True, WHITE)
        screen.blit(text, [10, 45])    
       
        text = font.render(name, True, WHITE)
        screen.blit(text, [290, 45])        
 
        text = font.render("Hit enter to continue", True, WHITE)
        screen.blit(text, [10, 80])
       
        text = font.render("Page 1", True, WHITE)
        screen.blit(text, [10, 120])
 
    if instruction_page == 2:
        # Draw instructions, page 2
        text = font.render("Move your mouse up and down to move your character", True, WHITE)
        screen.blit(text, [10, 10])    
        
        text = font.render("Press left click to fire arrows", True, WHITE)
        screen.blit(text, [10, 45])        
        
        text = font.render("Once you reach 25 points, you will advance to the next level", True, WHITE)
        screen.blit(text, [10, 80])
 
        text = font.render("When you reach 65 points, you win!", True, WHITE)
        screen.blit(text, [10, 120])
        
        text = font.render("Hit enter to continue", True, WHITE)
        screen.blit(text, [10, 160])
 
        text = font.render("Page 2", True, WHITE)
        screen.blit(text, [10, 200])
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
   
# Ensures that the player can only stay at x = 70   
player.rect.x = 70

score = 0
level = 1
level_one = True

# -------- Main Program Loop (LEVEL ONE)-----------
while not done and level_one:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True               
            
            # If the user decides to quit early, get the current score.
            try:
                file = open('highscores.txt', 'r')
                lines = file.readlines()
                prevhighscore = int(lines[0])
                prevname = lines[1]
                file.close()                    
            except IOError:
                file = open('highscores.txt', 'w')
                writescore = str(score) + "\n"
                file.write(writescore)
                writename = name + "\n"
                file.write(writename)
                file.close()

            # If the score is higher than the previous, a new score will be written
            if score > prevhighscore:
                file = open('highscores.txt', 'w')
                writescore = str(score) + "\n"
                file.write(writescore)
                writename = name + "\n"
                file.write(writename)
                file.close()   
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            # Fire a bullet if the user clicks the mouse button
            bullet = Bullet()
            
            # Set the bullet so it is where the player is
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y + 145
            
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)   
            
            # Play shooting sound
            fire_sound.play()
        
        elif score == 25:
            level += 1
            if level == 2:
                level_one = False
            
    # Make the cursor invisible        
    pygame.mouse.set_visible(0)  
    
    
    # Prints the level the player is on
    text = font.render("LEVEL ONE", True, WHITE)
    screen.blit(text, [800, 30])
    
    for bullet in bullet_list:
        # See if it hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
 
        # For each block hit, remove the bullet and add to the score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            
            score += 1
            print(score)
            hit_sound.play()
        
        # Remove the bullet if it flies up off the screen
        if bullet.rect.x > 2000:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet) 
                
    # Set the screen background
    screen.blit(main_background_image, [0, 0]) 
    
    text = font.render("LEVEL ONE", True, WHITE)
    screen.blit(text, [800, 30])
    
    # Update and draw sprites
    all_sprites_list.update()    
    all_sprites_list.draw(screen)
    
    # Score
    scoretext = "Score: " + str(score)
    text = font.render(scoretext, True, WHITE)
    screen.blit(text, [40, 40])
         
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
 
level_two = True
# -------- Main Program Loop (LEVEL TWO)-----------
while not done and level_two:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 
            
            # If the user decides to quit early, get the current score.
            try:
                file = open('highscores.txt', 'r')
                lines = file.readlines()
                prevhighscore = int(lines[0])
                prevname = lines[1]
                file.close()                    
            except IOError:
                file = open('highscores.txt', 'w')
                writescore = str(score) + "\n"
                file.write(writescore)
                writename = name + "\n"
                file.write(writename)
                file.close()

            # If the score is higher than the previous, a new score will be written
            if score > prevhighscore:
                file = open('highscores.txt', 'w')
                writescore = str(score) + "\n"
                file.write(writescore)
                writename = name + "\n"
                file.write(writename)
                file.close()
                
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            # Fire a bullet if the user clicks the mouse button
            bullet = Bullet()
            
            # Set the bullet so it is where the player is
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y + 145
            
            # Add the bullet to the lists
            all_sprites_list_two.add(bullet)
            bullet_list_two.add(bullet)  
            
            # Play shooting sound
            fire_sound.play()
            
        elif score == 65:
            
            # Get the final score 
            try:
                file = open('highscores.txt', 'r')
                lines = file.readlines()
                prevhighscore = int(lines[0])
                prevname = lines[1]
                file.close()                    
            except IOError:
                file = open('highscores.txt', 'w')
                writescore = str(score) + "\n"
                file.write(writescore)
                writename = name + "\n"
                file.write(writename)
                file.close()

            # If the score is higher than the previous, a new score will be written
            if score >= prevhighscore:
                file = open('highscores.txt', 'w')
                writescore = str(score) + "\n"
                file.write(writescore)
                writename = name + "\n"
                file.write(writename)
                file.close()     
            
            # Sends the player to the end screen.
            level_two = False
                            
        # Make the cursor invisible        
        pygame.mouse.set_visible(0)  
        
        
    for bullet in bullet_list_two:
        # See if it hit a block
        block_hit_list_two = pygame.sprite.spritecollide(bullet, block_list_two, True)
 
        # For each block hit, remove the bullet and add to the score
        for enemytwo in block_hit_list_two:
            bullet_list_two.remove(bullet)
            all_sprites_list_two.remove(bullet)
            
            score += 1
            print(score)
            
            # Plays a sound when an arrow collides with an enemy
            hit_sound.play()
        
        # Remove the bullet if it flies up off the screen
        if bullet.rect.x > 2000:
            bullet_list_two.remove(bullet)
            all_sprites_list_two.remove(bullet) 
                                    
    # Set the screen background
    screen.blit(main_background_image, [0, 0]) 
    
    # Prints the level that the player is on
    text = font.render("LEVEL TWO", True, WHITE)
    screen.blit(text, [800, 30])
    
    # Update and draw sprites
    all_sprites_list_two.update()
    
    all_sprites_list_two.draw(screen)
    
    # Score
    scoretext = "Score: " + str(score)
    text = font.render(scoretext, True, WHITE)
    screen.blit(text, [40, 40])
    
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
end_screen = True
play_victory_sound = 1
# ------ End Screen -------
while not done and end_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            victory_sound.stop()
            done = True
            
    # Plays the victory sound
    victory_sound.play()       
    
    # Display the image and flip  
    screen.blit(end_screen_image, [0, 0])
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()