import random

import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from retrogame.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.player_width = 75
        self.player_height = 75
        
        self.p_left_padding = 5
        self.p_right_padding = 5
        self.p_bottom_padding = 5
        
        self.surf = pygame.Surface((self.player_width, self.player_height))
        self.surf.fill((245,27,2))
        self.rect = self.surf.get_rect()
        
        # Position our player in center
        self.rect.left = (SCREEN_WIDTH/2)-(self.player_width/2)
        self.rect.top = (SCREEN_HEIGHT)-(self.player_height)
    
    def update(self, pressed_keys):
        # if pressed_keys[K_UP]:
            # # print("UP")
            # self.rect.move_ip(0, -5)
        # if pressed_keys[K_DOWN]:
            # # print("DN")
            # self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
            
        # Keep player on the screen
        if self.rect.left < self.p_left_padding:
            self.rect.left = self.p_left_padding
        if self.rect.right > SCREEN_WIDTH-self.p_right_padding:
            self.rect.right = SCREEN_WIDTH-self.p_right_padding
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT-self.p_bottom_padding:
            self.rect.bottom = SCREEN_HEIGHT-self.p_bottom_padding


class Stone(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_width = 75
        self.player_height = 75
        
        self.s_left_padding = 5
        self.s_right_padding = 5
        self.s_bottom_padding = 5
        
        self.surf = pygame.Surface((self.player_width, self.player_height))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0+self.s_left_padding, SCREEN_WIDTH-self.s_right_padding),
                random.randint(-20, -100),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()