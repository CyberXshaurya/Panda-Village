import pygame
from enum import Enum

class PandaState(Enum):
    WALKING = 1
    RUNNING = 2
    JUMPING = 3
    SLEEPING = 4
    EATING = 5
    TRACKING_MOUSE = 6
    REACTING_TO_CLICKS = 7

class Panda:
    def __init__(self):
        self.state = PandaState.SLEEPING
        self.position = (0, 0)

    def walk(self):
        self.state = PandaState.WALKING
        print("Panda is walking.")

    def run(self):
        self.state = PandaState.RUNNING
        print("Panda is running.")

    def jump(self):
        self.state = PandaState.JUMPING
        print("Panda is jumping.")

    def sleep(self):
        self.state = PandaState.SLEEPING
        print("Panda is sleeping.")

    def eat(self):
        self.state = PandaState.EATING
        print("Panda is eating.")

    def track_mouse(self):
        self.state = PandaState.TRACKING_MOUSE
        print("Panda is tracking the mouse.")

    def react_to_click(self):
        self.state = PandaState.REACTING_TO_CLICKS
        print("Panda is reacting to clicks.")

    def draw(self, surface):
        # Placeholder for drawing logic using pygame
        pygame.draw.rect(surface, (255, 255, 255), (self.position[0], self.position[1], 50, 30))
        print("Panda drawn on the surface.")

# Example usage:
# panda = Panda()
# panda.walk()
# panda.draw(surface)