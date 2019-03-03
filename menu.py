import pygame
import sys

from pygame.locals import *

class Menu:
    '''Menu class that creates a menu and lists interactive menu options'''
    
    screen_resolution = (400, 300)
    
    def __init__(self):
        '''Initialises an new instance of Menu'''
        self.start = False
        self.settings = False
        
    def display_menu(self):
        '''Displays menu objects on user's screen'''
        #TODO: Add changes to make when menu objects are clicked.
        
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
        
        #Add hover coordinates.
        hover_start = start_option.get_rect()
        hover_settings = settings_option.get_rect()
        hover_quit = quit_option.get_rect()
        hover_start.x, hover_start.y = 150, 150
        hover_settings.x, hover_settings.y = 150, 170
        hover_quit.x, hover_quit.y = 150, 190
        
        #Initialise variable to indicate mouse position at click.
        mouse_clicked = 0, 0        
        
        #Begin displaying the menu.
        menu_display = True
        while menu_display:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu_display = False
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    mouse_clicked = pygame.mouse.get_pos()                 
            pygame.event.pump()
            screen.fill((0, 0, 0))
            screen.blit(title, (120, 80))
            screen.blit(start_option, (150, 150))
            screen.blit(settings_option, (150, 170))
            screen.blit(quit_option, (150, 190))
            #Implement changes to display on hover.
            if hover_start.collidepoint(pygame.mouse.get_pos()):
                hover = menu_font.render('>', False, (255, 255, 255))
                screen.blit(hover, (140, 150))
            elif hover_settings.collidepoint(pygame.mouse.get_pos()):
                hover = menu_font.render('>', False, (255, 255, 255))
                screen.blit(hover, (140, 170)) 
            elif hover_quit.collidepoint(pygame.mouse.get_pos()):
                hover = menu_font.render('>', False, (255, 255, 255))
                screen.blit(hover, (140, 190))
            else:
                hover = menu_font.render('', False, (255, 255, 255))
            #Check for clicks.
            if hover_quit.collidepoint(mouse_clicked):
                menu_display = False
                pygame.quit()
                sys.exit()
            elif hover_settings.collidepoint(mouse_clicked):
                menu_display = False
                pygame.quit()
                self.get_settings()
                break
            elif hover_start.collidepoint(mouse_clicked):
                menu_display = False
                self.start_game()
                break            
            #Update screen display
            pygame.display.update()            
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
        
#Uncomment the following for in-class display of the menu.
#check_menu_display = Menu()
#check_menu_display.display_menu()
