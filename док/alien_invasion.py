import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf
from button import Button
from scoreboard import Scoreboard


def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Draw start button
    play_button = Button(ai_settings, screen, "Играть")
    
    # Make a ship, bullets, aliens and stats
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            gf.update_ship(ai_settings, ship)
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        
run_game()
