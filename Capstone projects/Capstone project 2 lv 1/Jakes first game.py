import pygame
import random

pygame.init()

#define screen size

screen_width = 1000
screen_height = 1000

#create screen

screen = pygame.display.set_mode((screen_width,screen_height))

#create player and give it image saved in folder as well as enemy

player = pygame.image.load("player.jpg")
enemy = pygame.image.load("enemy.png")
enemy2 = pygame.image.load("monster.jpg")
enemy3 = pygame.image.load("image.png")
prize = pygame.image.load("prize.jpg")

#get the width and hight of the above images in order to detect boundary.

image_height = player.get_height()
image_width = player.get_width()
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()


print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))


#store the position of the player and enemy as variable.

playerXPosition = 100
playerYPosition = 50

#make the enemy start off screen and at random y position.

enemyXPosition = screen_width
enemyYPosition = random.randint(0, screen_height - enemy_height)

enemy2XPosition = 400
enemy2YPosition = 70

enemy3XPosition = 600
enemy3YPosition = 800

prizeXPosition = 700
prizeYPosition = 70

#check if up or down key is pressed.

keyUp = False
keyDown = False
keyLeft = False
keyRight = False

#create game loop to refresh/update the screen window and apply changes to represent real time game play.

while 1:

    screen.fill(0) #this clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition)) #draws image selected to point specified on screen.
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))

    pygame.display.flip() #updates screeen

    for event in pygame.event.get(): #loops through events in the game.

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN: #Checks if down key is pressed.

            if event.key == pygame.K_UP:
                keyUp = True #Test if key pressed is one we want.

            if event.key == pygame.K_DOWN:
                keyDown = True

            if event.key == pygame.K_LEFT:
                keyLeft = True

            if event.key == pygame.K_RIGHT:
                keyRight = True

        if event.type == pygame.KEYUP: #checks if up key is pressed.

            if event.key == pygame.K_UP:
                keyUp = False

            if event.key == pygame.K_DOWN:
                keyDown = False

            if event.key == pygame.K_LEFT:
                keyLeft = False

            if event.key == pygame.K_RIGHT:
                keyRight = False

      
              

            

# Check key pressed values and move image accordingly.

    if keyUp == True:
        if playerYPosition > 0 : #ensure user does not move image above the window.
            playerYPosition -= 1
              
    if keyDown == True:
        if playerYPosition < screen_height - image_height:
            playerYPosition += 1 #ensure player does not move image bllow screen.

    if keyLeft == True:
        if playerXPosition > 0 :
            playerXPosition -= 1

    if keyRight == True:
        if playerXPosition < screen_width - image_width:
            playerXPosition += 1


# Check for collision with enemy.
# Add bounding boxes around images.
# Test if these boxes intercept. If they do there is a collision.

     #bounding box for player:

    playerBox = pygame.Rect(player.get_rect())

    playerBox.top = playerYPosition
    playerBox.left = playerXPosition #updates playerbox position.

     #bounding box for enemy:

    enemyBox = pygame.Rect(enemy.get_rect())

    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition #updates enemy box position.

    enemy2Box = pygame.Rect(enemy.get_rect())

    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    enemy3Box = pygame.Rect(enemy3.get_rect())

    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    #bounding box for prize.

    prizeBox = pygame.Rect(prize.get_rect())

    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition 

     #test colliosn of Boxes:

    if playerBox.colliderect(enemyBox):

         #display "you lose"

        print("You lose!")

         #quit game and exit window:

        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy2Box):

         #display "you lose"

        print("You lose!")

         #quit game and exit window:

        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy3Box):

         #display "you lose"

        print("You lose!")

         #quit game and exit window:

        pygame.quit()
        exit(0)   

      #if the enemy is off screen user wins:


    if playerBox.colliderect(prizeBox):

        #display "you win"

        print("YOU WIN!")

        #quit game and exit window:

        pygame.quit()
        exit(0)

    if enemyXPosition < 0 - enemy_width:



          #display "you win!"

        print("You win!")

          #Quit and exit

        pygame.quit()

        exit(0)


       #make enemy approach player.

    enemyXPosition -= 0.15

    enemy3YPosition -= 0.15

       #=======================game loop logic ends here. ===============================

     

         

            
        




