import random
import pygame
from com.AI_Project.app import green


# class Food:
#     def __init__(self, display, width, height, block_size, img, snake_list, food_thickness=10):
#         self.display = display
#         self.width = width
#         self.height = height
#         self.block_size = block_size
#         self.food = img
#         self.food_thickness = food_thickness
#
#         self.random_food_x = random.randint(0, self.width / self.block_size - 1) * 10
#         self.random_food_y = random.randint(0, self.height / self.block_size - 1) * 10
#
#         while [self.random_food_x, self.random_food_y] in snake_list:
#             self.random_food_x = random.randint(0, self.width / self.block_size - 1) * 10
#             self.random_food_y = random.randint(0, self.height / self.block_size - 1) * 10
#
#     # To get the food
#     def update_food_position(self, snake_list):
#         self.random_food_x = random.randint(0, self.width / self.block_size - 1) * 10
#         self.random_food_y = random.randint(0, self.height / self.block_size - 1) * 10
#
#         while [self.random_food_x, self.random_food_y] in snake_list:
#             self.random_food_x = random.randint(0, self.width / self.block_size - 1) * 10
#             self.random_food_y = random.randint(0, self.height / self.block_size - 1) * 10
#
#     # get the food
#     def get_food_position(self):
#         return self.random_food_x, self.random_food_y
#
#     # display the food on the board
#     def display(self):
#         self.display.blit(self.food, [self.random_food_x, self.random_food_y, self.food_thickness, self.food_thickness])
#
# this is the apple object of the snake game
class Food:

    def __init__(self, gameDisplay, display_width, display_height, block_size, img, snake_list, food_thickness=10):
        self.gameDisplay = gameDisplay
        self.display_width = display_width
        self.display_height = display_height
        self.block_size = block_size
        self.food = img
        self.food_thickness = food_thickness

        self.random_food_x = random.randint(0, self.display_width / self.block_size - 1) * 10
        self.random_food_y = random.randint(0, self.display_height / self.block_size - 1) * 10

        while [self.random_food_x, self.random_food_y] in snake_list:
            self.random_food_x = random.randint(0, self.display_width / self.block_size - 1) * 10
            self.random_food_y = random.randint(0, self.display_height / self.block_size - 1) * 10

    # method to get the new apple
    def update_food_position(self, snake_list):
        self.random_food_x = random.randint(0, self.display_width / self.block_size - 1) * 10
        self.random_food_y = random.randint(0, self.display_height / self.block_size - 1) * 10

        while [self.random_food_x, self.random_food_y] in snake_list:
            self.random_food_x = random.randint(0, self.display_width / self.block_size - 1) * 10
            self.random_food_y = random.randint(0, self.display_height / self.block_size - 1) * 10

    # get the apple
    def get_food_position(self):
        return self.random_food_x, self.random_food_y

    # display the apple to the pygame board
    def display(self):
        self.gameDisplay.blit(self.food, [self.random_food_x, self.random_food_y, self.food_thickness,
                                          self.food_thickness])


class Snake:
    def __init__(self, gameDisplay, display_width, display_height, img, x, y, block_size=10):
        self.gameDisplay = gameDisplay
        self.display_width = display_width
        self.display_height = display_height
        self.head = img
        self.snake_length = 3
        self.snake_list = [[x, y]]
        self.block_size = block_size
        self.eaten = False
        self.direction = "right"

    # check if the snake is still alive
    def is_alive(self):
        if self.snake_list[-1][0] >= self.display_width or self.snake_list[-1][0] < 0 or self.snake_list[-1][
            1] >= self.display_height \
                or self.snake_list[-1][1] < 0:
            return False
        elif self.snake_list[-1] in self.snake_list[:-1]:
            return False
        else:
            return True

    # check if snake eats the apple
    def eat_apple(self, random_food_x, random_food_y):
        if self.snake_list[-1][0] == random_food_x and self.snake_list[-1][1] == random_food_y:
            self.snake_length += 1
            return True
        else:
            return False

    # display the score to the pygame board
    def display_score(self):
        from com.AI_Project.app import black, pygame
        score = self.snake_length - 3
        text = pygame.font.SysFont("Comic Sans MS", 15).render("Score: " + str(score), True, black)
        self.gameDisplay.blit(text, [0, 0])

    # return the snake head position
    def get_snake_head(self):
        return self.snake_list[-1][0], self.snake_list[-1][1]

    # move the snake by one step based on the snake's direction
    def update_snake_list(self, rand_apple_x, rand_apple_y):
        if self.direction == "left":
            lead_x_change = -self.block_size
            lead_y_change = 0
        elif self.direction == "right":
            lead_x_change = self.block_size
            lead_y_change = 0
        elif self.direction == "up":
            lead_y_change = -self.block_size
            lead_x_change = 0
        elif self.direction == "down":
            lead_y_change = self.block_size
            lead_x_change = 0

        snake_head = []
        snake_head.append(self.snake_list[-1][0] + lead_x_change)
        snake_head.append(self.snake_list[-1][1] + lead_y_change)
        self.snake_list.append(snake_head)

        if self.eat_apple(rand_apple_x, rand_apple_y):
            self.snake_length += 1
            self.eaten = True

        if len(self.snake_list) > self.snake_length:
            del self.snake_list[0]

    # display the snake to the board
    def display(self):
        from com.AI_Project.app import pygame, green
        self.gameDisplay.blit(self.head, (self.snake_list[-1][0], self.snake_list[-1][1]))

        for XnY in self.snake_list[:-1]:
            pygame.draw.rect(self.gameDisplay, green,
                             [XnY[0], XnY[1], self.block_size, self.block_size])


# extend the snake to facilitate the RL
class RL_Snake(Snake):
    # this one will return the state of the snake
    # the state is: with the direction snake is in
    # (what is in the left cell, what is in the above cell, what is in the right cell
    # , (diff of the position between target and the snake head))
    def get_state(self, target):
        head_x, head_y = self.get_snake_head()
        start = [head_x, head_y]

        if self.direction == "up":
            options = [[start[0] - self.block_size, start[1]], [start[0], start[1] - self.block_size],
                       [start[0] + self.block_size, start[1]]]
        elif self.direction == "right":
            options = [[start[0], start[1] - self.block_size], [start[0] + self.block_size, start[1]],
                       [start[0], start[1] + self.block_size]]
        elif self.direction == "down":
            options = [[start[0] + self.block_size, start[1]], [start[0], start[1] + self.block_size],
                       [start[0] - self.block_size, start[1]]]
        elif self.direction == "left":
            options = [[start[0], start[1] + self.block_size], [start[0] - self.block_size, start[1]],
                       [start[0], start[1] - self.block_size]]

        state = []

        for o in options:
            result = None
            if [o[0], o[1]] in self.snake_list or o[0] < 0 or o[0] >= self.display_width or o[1] < 0 or \
                    o[1] >= self.display_height:
                result = 1
            elif o == target:
                result = 2
            else:
                result = 0
            state.append(result)

        # until now, we will get what is in the left, up, right side of the snake head
        # 1 is something will get the snake die
        # 2 is the apple
        # 0 is empty space

        # quadrant is the difference of the position between target and snake head
        quadrant = [target[0] - start[0], target[1] - start[1]]

        if self.direction == "up":
            pass
        elif self.direction == "right":
            temp = quadrant[0]
            quadrant[0] = quadrant[1]
            quadrant[1] = -temp
        elif self.direction == "down":
            temp = quadrant[0]
            quadrant[0] = -quadrant[1]
            quadrant[1] = -temp
        elif self.direction == "left":
            temp = quadrant[0]
            quadrant[0] = -quadrant[1]
            quadrant[1] = temp
        state.append(tuple(quadrant))

        return state

    # method change the direction based on the action chosen
    def set_direction_by_action(self, action):
        look_up = {"up": 0, "right": 1, "left": -1}
        value = look_up[action]

        if self.direction == "up":
            if value != 0:
                self.direction = ("left" if value == -1 else "right")
            else:
                self.direction = "up"
        elif self.direction == "right":
            if value != 0:
                self.direction = ("up" if value == -1 else "down")
            else:
                self.direction = "right"
        elif self.direction == "down":
            if value != 0:
                self.direction = ("right" if value == -1 else "left")
            else:
                self.direction = "down"
        elif self.direction == "left":
            if value != 0:
                self.direction = ("down" if value == -1 else "up")
            else:
                self.direction = "left"
#
# class Snake:
#     def __init__(self, display, width, height, img, x, y, block_size=10):
#         self.display = display
#         self.width = width
#         self.height = height
#         self.head = img
#         self.snake_length = 1
#         self.snake_list = [[x, y]]
#         self.block_size = block_size
#         self.eaten = False
#         self.direction = "right"
#
#     # check if the snake is still alive
#     def is_alive(self):
#         if self.snake_list[-1][0] >= self.width or self.snake_list[-1][0] < 0 or self.snake_list[-1][1] >= self.height \
#                 or self.snake_list[-1][1] < 0:
#             return False
#         elif self.snake_list[-1] in self.snake_list[:-1]:  # if it hits itself
#             return False
#
#         else:
#             return True
#
#     # check if the snake has eat the food
#     def eat_food(self, rand_food_x, rand_food_y):
#         if self.snake_list[-1][0] == rand_food_x and self.snake_list[-1][1] == rand_food_y:
#             return True
#         else:
#             return False
#
#     # score of the game
#     def display_score(self):
#         from com.AI_Project.app import black
#         score = self.snake_length - 1
#         text = pygame.font.SysFont("Comic Sans MS", 15).render("score:" + str(score), True, black)
#         self.display.blit(text, [0, 0])
#
#     # return the snake head position
#     def get_snake_head(self):
#         return self.snake_list[-1][0], self.snake_list[-1][1]
#
#     # snakes movement based on direction
#     def update_snake_list(self, rand_food_x, rand_food_y):
#         if self.direction == "left":
#             lead_x_change = -self.block_size
#         elif self.direction == "right":
#             lead_x_change = self.block_size
#             lead_y_change = 0
#
#         elif self.direction == "up":
#             lead_y_change = -self.block_size
#             lead_x_change = 0
#
#         elif self.direction == "down":
#             lead_y_change = self.block_size
#             lead_x_change = 0
#
#         snake_head = []
#         snake_head.append(self.snake_list[-1][0] + lead_x_change)
#         snake_head.append(self.snake_list[-1][1] + lead_y_change)
#         self.snake_list.append(snake_head)
#
#         if self.eat_food(rand_food_x, rand_food_y):
#             self.snake_length += 1
#             self.eaten = True
#
#         if len(self.snake_list) > self.snake_length:
#             del self.snake_list[0]
#
#     # display the snake on the board
#     def display(self):
#
#         self.display.blit(self.head, (self.snake_list[-1][0], self.snake_list[-1][1]))
#
#         for i in self.snake_list[:-1]:
#             pygame.draw.rect(self.display, green, [i[0], i[1], self.block_size, self.block_size])
#
#
# class RL_snake(Snake):
#
#     def get_state(self, target):
#         head_x, head_y = self.get_snake_head()
#         start = [head_x, head_y]
#
#         if self.direction == "up":
#             options = [[start[0] - self.block_size, start[1]], [start[0], start[1] - self.block_size],
#                        [start[0] + self.block_size, start[1]]]
#
#         elif self.direction == "right":
#             options = [[start[0], start[1] - self.block_size], [start[0] + self.block_size, start[1]],
#                        [start[0], start[1] + self.block_size]]
#
#         elif self.direction == "down":
#             options = [[start[0] + self.block_size, start[1]], [start[0], start[1] + self.block_size],
#                        [start[0] - self.block_size, start[1]]]
#
#         elif self.direction == "left":
#             options = [[start[0], start[1] + self.block_size], [start[0] - self.block_size, start[1]],
#                        [start[0], start[1] - self.block_size]]
#
#         state = []
#
#         for i in options:
#             result = None
#             if [i[0], i[1]] in self.snake_list or i[0] < 0 or i[0] >= self.width or i[1] < 0 or i[1] >= self.height:
#                 result = 1
#
#             elif i == target:
#                 result = 2
#
#             else:
#                 result = 0
#                 state.append(result)
#
#             # difference between the position and the target
#             difference = [target[0] - start[0], target[1] - start[1]]
#
#             if self.direction == "up":
#                 pass
#
#             elif self.direction == "right":
#                 temp = difference[0]
#                 difference[0] = difference[1]
#                 difference[1] = -temp
#
#             elif self.direction == "down":
#                 temp = difference[0]
#                 difference[0] = -difference[1]
#                 difference[1] = -temp
#
#             elif self.direction == "left":
#                 temp = difference[0]
#                 difference[0] = -difference[1]
#                 difference[1] = temp
#             state.append(tuple(difference))
#
#             return state
#
#     # this method changes the direction based on the action
#
#     def set_directions_by_action(self, action):
#         look_up = {"up": 0, "right": 1, "left": -1}
#         value = look_up[action]
#
#         if self.direction == "up":
#             if value != 0:
#                 self.direction = ("left" if value == -1 else "right")
#             else:
#                 self.direction = "up"
#
#         elif self.direction == "right":
#             if value != 0:
#                 self.direction = ("up" if value == -1 else "down")
#             else:
#                 self.direction = "right"
#
#         elif self.direction == "down":
#             if value != 0:
#                 self.direction = ("right" if value == -1 else "left")
#             else:
#                 self.direction = "down"
#
#         elif self.direction == "left":
#             if value != 0:
#                 self.direction = ("down" if value == -1 else "up")
#             else:
#                 self.direction = "left"
