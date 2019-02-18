import pygame
import sys

class Menu:
    '''Menu class that creates a menu and lists interactive menu options'''
    
    screen_resolution = (400, 300)
    
    def __init__(self):
        '''Initialises an new instance of Menu'''
        self.start = False
        self.settings = False
        
    def display_menu(self):
        '''Displays menu objects on user's screen'''
        #TODO: Implement hover on text and calls when an option is selected.
        
        pygame.init()
        font_colour = (255, 255, 255)
        screen = pygame.display.set_mode(self.screen_resolution)
        
        #Create the text to be displayed with the desired game font.
        title_font = pygame.font.Font("resources/fonts/3Dventure.ttf", 60)
        menu_font = pygame.font.Font("resources/fonts/3Dventure.ttf", 20)
        title = title_font.render("PING!", False, font_colour)
        start_option = menu_font.render("Start", False, font_colour)
        settings_option = menu_font.render("Settings", False, font_colour)
        quit_option = menu_font.render("Quit", False, font_colour)
        
        #Begin displaying the menu.
        menu_display = True
        while menu_display:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu_display = False
                    pygame.quit()
                    sys.exit()
            pygame.event.pump()
            screen.fill((0, 0, 0))
            screen.blit(title, (120, 80))
            screen.blit(start_option, (150, 150))
            screen.blit(settings_option, (150, 170))
            screen.blit(quit_option, (150, 190))            
            
            pygame.display.flip()        
        
    def start_game(self):
        '''Starts the game when called by user'''
        self.start = True
        #TODO: Finish implementation of start_game
        
    def get_settings(self):
        '''Returns the settings menu when called by user'''
        self.settings = True
        #TODO: Finish implementation of get_settings
    
    def quit_game(self):
        '''Exits user from the game'''
        #TODO: Finish implementation of quit_game
        
# Uncomment the following for in-class display of the menu.
# check_menu_display = Menu()
# check_menu_display.display_menu()
