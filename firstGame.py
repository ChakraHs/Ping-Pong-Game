import pygame


# Function to read the maximum score from a file
def read_max_score():
    try:
        with open('max_score.txt', 'r') as file:
            max_score = int(file.read())
            return max_score
    except FileNotFoundError:
        # If the file doesn't exist, return a default value (e.g., 0)
        return 0
    except ValueError:
        # Handle the case where the file contains non-integer data
        print("Error: The file contains non-integer data.")
        return 0

# Function to write the maximum score to a file
def write_max_score(max_score):
    with open('max_score.txt', 'w') as file:
        file.write(str(max_score))

# Example usage:
# Read the max score
max_score = read_max_score()


# Initialize Pygame
pygame.init()

pygame.mixer.init()

pygame.mixer.music.load('C:/Users/hussi/Downloads/06.mp3')  # Replace with the actual path to your song

pygame.mixer.music.play()

# Set up display
width, height = 800, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My First Pygame Program")



# Function to reset the game state
def reset_game():
    global dx, dy, speedx, speedy,level, levelindice
    dx = 0
    dy = 0
    speedx = 0.6
    speedy = 0
    level=1
    levelindice=0


Running = True
start_page = True
game_over=False

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the circle parameters
circle_color = white
circle_radius = 20
circle_position = (width // 2, height // 2)

dx = 0
dy = 0

speedx = 0.6
speedy = 0

speed = 1  # Adjust the speed of movement

xrect1 = 100
yrect1 = 100
width_rect1 = 40
dyrect1 = 0
height_rect1 = 200


levelindice=1
level=levelindice//10+1

# Font setup
font = pygame.font.Font(None, 36)  # You can adjust the font size and style

level_text = font.render("level", True, white)


background_image = pygame.image.load('C:/Users/hussi/Desktop/gameDev/paygame/back.png')  # Replace with the actual path to your background image


# Main game loop
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                start_page = False
                game_over=False
                reset_game()


    # Start page
    if start_page:
        screen.fill(black)
        screen.blit(background_image, (0, -750))
        start_text = font.render("Press ENTER to Play", True, white)
        start_rect = start_text.get_rect(center=(width // 2, height // 2))
        screen.blit(start_text, start_rect)
        pygame.display.flip()
        continue  # Skip the rest of the loop until the user presses ENTER

    if game_over:
        screen.fill(black)
        start_text = font.render("GAME OVER! Press ENTER to Play", True, white)
        start_rect = start_text.get_rect(center=(width // 2, height // 2))
        screen.blit(start_text, start_rect)
        pygame.display.flip()
        continue  # Skip the rest of the loop until the user presses ENTER


    dx += speedx
    dy += speedy

    # screen.blit(level_text,start_rect)
    # pygame.display.flip()

    # Clear the screen
    screen.fill(black)
    screen.blit(background_image, (0,-750))


    pygame.draw.rect(screen, (160, 160, 160), (0, 0, width, 40))

    # Drawing a rectangle
    pygame.draw.rect(screen, (255, 0, 0), (xrect1, yrect1 + dyrect1, width_rect1, height_rect1))


    level=levelindice//10+1

    if(levelindice>max_score):
        max_score=levelindice

    # Assuming level and levelindice are defined
    text_line1 = font.render(f'Level: {level}', True, white)
    text_line2 = font.render(f'Score: {levelindice}', True, white)

    text_max_score = font.render(f'Max Score: {max_score}', True, white)

    # Adjust the Y-coordinate for each line
    y_pos_line1 = 10
    y_pos_line2 = 10
    y_pos_max_score = 10



    # Blit each line separately
    screen.blit(text_line1, (width // 2 - text_line1.get_width() // 2, y_pos_line1))
    screen.blit(text_line2, (10, y_pos_line2))
    screen.blit(text_max_score, (width - text_max_score.get_width()-10, y_pos_max_score))
    
    # Draw the circle
    pygame.draw.circle(screen, circle_color, (circle_position[0] + dx, circle_position[1] + dy), circle_radius)

    # Collision detection with the rectangle
    if (
        (circle_position[0] + dx - circle_radius) <= (xrect1 + width_rect1)
        and (circle_position[0] + dx + circle_radius) >= xrect1
        and (circle_position[1] + dy - circle_radius) <= (yrect1 + dyrect1 + height_rect1)
        and (circle_position[1] + dy + circle_radius) >= (yrect1 + dyrect1)
    ):
        speedx = -speedx * (4/3) if levelindice % 5 == 0 else -speedx
        levelindice+=1
        if (
            (circle_position[1] + dy) <= (yrect1 + dyrect1 + height_rect1 // 2)
            and (circle_position[0] + dx + circle_radius) < width
        ):
            speedy = -0.2
        elif (
            (circle_position[1] + dy) > (yrect1 + dyrect1 + height_rect1 // 2)
            and (circle_position[0] + dx + circle_radius) < width
        ):
            speedy = 0.2

    # Collision detection with the window edges
    if (circle_position[0] + dx - circle_radius) <= 0:
        # speedx = 0
        # # Display "Game Over" in the center of the screen
        # game_over_text = font.render("Game Over", True, (255, 255, 255))
        # text_rect = game_over_text.get_rect(center=(width // 2, height // 2))
        # screen.blit(game_over_text, text_rect)
        # # Update the display
        # pygame.display.flip()
        game_over=True

    if (circle_position[0] + dx + circle_radius) >= width:
        speedx = -speedx
        if (circle_position[1] + dy) <= (yrect1 + dyrect1 + height_rect1 // 2) and (
            circle_position[0] + dx + circle_radius
        ) < width:
            speedy = -0.2
        elif (circle_position[1] + dy) > (yrect1 + dyrect1 + height_rect1 // 2) and (
            circle_position[0] + dx + circle_radius
        ) < width:
            speedy = 0.2

    if (circle_position[1] + dy - circle_radius) <= 40 or (circle_position[1] + dy + circle_radius) >= height:
        speedy = -speedy

    # Movement controls for the rectangle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and yrect1 + dyrect1 > 40:
        dyrect1 -= speed
    if keys[pygame.K_DOWN] and yrect1 + dyrect1 + height_rect1 < height:
        dyrect1 += speed
    if keys[pygame.K_LEFT] and xrect1 > 0:
        xrect1 -= speed
    if keys[pygame.K_RIGHT] and xrect1 + width_rect1 < width:
        xrect1 += speed

    # Update the display                                                  
    pygame.display.flip()
    

write_max_score(max_score)
# Quit Pygame
pygame.quit()
