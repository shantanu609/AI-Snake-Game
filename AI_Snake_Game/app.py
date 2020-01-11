import pygame
import com.AI_Project.ReinforcementLearning as RL
import com.AI_Project.Main_Game
from com.AI_Project.ReinforcementLearning import Qlearning

from com.AI_Project.Main_Game import *

pygame.init()

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 155, 0)

display_width = 150
display_height = 150

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("snake game")
clock = pygame.time.Clock()
icon = pygame.image.load("food.png")
pygame.display.set_icon(icon)
img = pygame.image.load('snake.jpg')
img2 = pygame.image.load('food.png')
pygame.display.flip()

block_size = 10
FPS = 20

actions = ["up", "left", "right"]
snake_agent = Qlearning(actions, e=0.01)

snake_agent.loadQ()

# training
def training_game(times=10):
    s = []

    for i in range(times):
        print(i)

        pygame.event.pump()
        game_over = False

        # snake will start in the middle of the window
        lead_x = 70
        lead_y = 70

        # snakes default direction is right
        snake = RL_Snake(gameDisplay, display_width, display_height, img, lead_x, lead_y)
        food = Food(gameDisplay, display_width, display_height, block_size, img2, snake.snake_list)

        a_x, a_y = food.get_food_position()

        # get the initial state, and action will be "up" starting
        old_state = snake.get_state([a_x, a_y])
        action = "up"

        while not game_over:
            a_x, a_y = food.get_food_position()
            snake.update_snake_list(a_x, a_y)

            # snake if not dead or eats the food, reward will be -10
            # this is negative so that it will "encourage" the snake to move towards the food,
            # since that is the only positive award
            reward = -10

            # check if snake dies
            if snake.is_alive() is False:
                game_over = True

                # if snake dies, then reward is -100
                reward = -10
                s.append(snake.snake_length - 1)
            gameDisplay.fill(white)

            # if snake eats the food, make a random new food
            if snake.eaten is True:
                food.update_food_position(snake.snake_list)
                # if snake eats the food, reward is 500
                reward = 10
                # snake.snake_length = snake.snake_length + 1
                s.append(snake.snake_length)

            # get the new state, then we can update the Q table
            state = snake.get_state([a_x, a_y])
            snake_agent.updateQ(tuple(old_state), action, tuple(state), reward)

            # training will take a lot of time, so archive the Q table
            snake_agent.saveQ()

            # this part is using the snake position and apple
            # positin to use the Qlearning method to get the action
            a_x, a_y = food.get_food_position()
            old_state = snake.get_state([a_x, a_y])
            action = snake_agent.getA(tuple(state))
            snake.set_direction_by_action(action)

            print(action)

            food.display()
            snake.eaten = False
            snake.display()
            snake.display_score()
            pygame.display.update()
            clock.tick(FPS)

    print("Average score is: {}".format((sum(s) / len(s)) * 100))


if __name__ == "__main__":
    training_game()
# import pygame
# import random
# from com.AI_Project.ReinforcementLearning import Qlearning
# from com.AI_Project.Main_Game import *
#
# pygame.init()
#
# # colors
# black = (0, 0, 0)
# white = (255, 255, 255)
# red = (255, 0, 0)
# green = (0, 155, 0)
#
# # window size
# display_width = 500
# display_height = 500
#
# # all the pygame settings
# gameDisplay = pygame.display.set_mode((display_width, display_height))
# pygame.display.set_caption("Snake Game")
# clock = pygame.time.Clock()
# icon = pygame.image.load("food.png")
# pygame.display.set_icon(icon)
# img = pygame.image.load('snake.jpg')
# img2 = pygame.image.load('food.png')
# pygame.display.flip()
#
# block_size = 10
# # frame per second will control the game speed
# FPS = 20
#
# # set up for the Qlearning
# actions = ["up", "left", "right"]
# snake_agent = Qlearning(actions, e=0.01)
#
# # if it is the first time to train, there is no Q.txt to load
# # then comment out this line
# # snake_agent.loadQ()
#
#
# # training method
# def training_game(times=10):
#     # s list will store the score of each game
#     s = []
#     for i in range(times):
#         # print out the game number
#         print(i)
#
#         pygame.event.pump()
#         game_over = False
#
#         # snake will start in the middle of the game window
#         lead_x = 70
#         lead_y = 70
#
#         # snake default direction is right
#         snake = RL_Snake(gameDisplay, display_width, display_height, img, lead_x, lead_y)
#         food = Food(gameDisplay, display_width, display_height, block_size, img2, snake.snake_list)
#
#         a_x, a_y = food.get_food_position()
#
#         # get the initial state, and action will be "up" starting
#         old_state = snake.get_state([a_x, a_y])
#         action = "up"
#
#         while not game_over:
#
#             # based on the direction, we can work out the x, y changes to update the snake
#             a_x, a_y = food.get_food_position()
#             snake.update_snake_list(a_x, a_y)
#
#             # snake not die or eats the food, reward will be -10
#             # this is negative so that it will "encourage" the snake to
#             # move towards to the food, since that is the only positive award
#             reward = -10
#
#             # check if snake dies
#             if snake.is_alive() is False:
#                 game_over = True
#                 # if snake dies, award is -100
#                 reward = -100
#                 s.append(snake.snake_length - 1)
#
#             gameDisplay.fill(white)
#
#             # if snake eats the food, make a random new food
#             if snake.eaten is True:
#                 food.update_food_position(snake.snake_list)
#                 # if snake eats the food, reward is 500
#                 reward = 500
#
#             #############################################
#             # get he new state, then we can update the Q table
#             state = snake.get_state([a_x, a_y])
#             snake_agent.updateQ(tuple(old_state), action, tuple(state), reward)
#
#             # training will take a lot of time, so archive the Q table
#             snake_agent.saveQ()
#
#             # this part is using the snake position and food
#             # position to use the Qlearning method to get the action
#             a_x, a_y = food.get_food_position()
#             old_state = snake.get_state([a_x, a_y])
#             action = snake_agent.getA(tuple(state))
#             snake.set_direction_by_action(action)
#             #############################################
#
#             food.display()
#             snake.eaten = False
#             snake.display()
#             snake.display_score()
#             pygame.display.update()
#             clock.tick(FPS)
#     # after training is done, print out the average score
#     print("Average score is: {}".format(sum(s) / len(s)))
#
#
# if __name__ == "__main__":
#     training_game()