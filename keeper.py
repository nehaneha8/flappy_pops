import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode((500, 800))
pygame.display.set_caption("Neha Flappy Bird")
clock = pygame.time.Clock()

big_font = pygame.font.SysFont("bahnschrift", 70)
small_font = pygame.font.SysFont("bahnschrift", 30)

def draw_floor(x):
    if x <= -970:
        x = 0

    screen.blit(floor_surface, (x, 700))
    screen.blit(floor_surface, (x + 435, 700))
    screen.blit(floor_surface, (x + 435+435, 700))

    return x - 1


def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(510,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(510,random_pipe_pos-250))
    return bottom_pipe, top_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 600:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

def check_collisions(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False

    if bird_rect.top <= 0 or bird_rect.bottom >= 750:
        return False

    return True

def show_score(score):
    # print(score)
    value = small_font.render("Score: " + str(score), True, (0,0,0))
    screen.blit(value, [10, 10])
    pygame.display.update()


def check_score(score, pipes):
    for pipe in pipes:
        if bird_rect.x == pipe.x:
            print("Yay!")
            return score+1

    return score


# GAME VARIABLES!

gravity = 0.35
bird_movement = 0
dead = False
game_active = True
score = 0



bg_surface = pygame.transform.scale2x(pygame.image.load('bg_5.png')).convert()

floor_surface = pygame.transform.scale2x(pygame.image.load('download.png')).convert()
floor_x_pos = 0

bird_surface = pygame.transform.scale_by(pygame.image.load('srini.jpeg'), 0.2).convert()
bird_surface.set_colorkey((0, 0, 0))
bird_rect = bird_surface.get_rect(center=(100, 400))

pipe_surface = pygame.transform.scale_by(pygame.image.load('pipe.png'), .35).convert()
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)
pipe_height = [200,400,600]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 10

            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list = []
                bird_rect.y = 400

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())


    screen.blit(bg_surface,(0,0))

    if game_active:
        # bird movement
        bird_movement += gravity
        bird_rect.centery += bird_movement
        screen.blit(bird_surface, bird_rect)

        # pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        score = check_score(score, pipe_list)
        # print(score)
        show_score(score)
        game_active = check_collisions(pipe_list)


    else:
        text1 = big_font.render(f"Game Over", True, (213, 50, 80))
        screen.blit(text1, [128, 800 / 3])

        text2 = small_font.render(f"Score: {score} Press SPACE to Restart", True, (0, 0, 0))
        screen.blit(text2, [100, 320])

        # score = 1






    # floor
    # score = 0
    floor_x_pos = draw_floor(floor_x_pos)


    pygame.display.update()
    clock.tick(120)




