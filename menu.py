import pygame
import sys

from pygame.locals import *

class Menu:
    '''Menu class that creates a menu and lists interactive menu options'''
    
    screen_resolution = (800, 600)
    background = pygame.image.load("resources/images/space.png")
    
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
        title_font = pygame.font.Font("resources/fonts/3Dventure.ttf", 80)
        menu_font = pygame.font.Font("resources/fonts/3Dventure.ttf", 30)
        title = title_font.render("PING!", False, font_colour)
        start_option = menu_font.render("Start", False, font_colour)
        settings_option = menu_font.render("Settings", False, font_colour)
        quit_option = menu_font.render("Quit", False, font_colour)
        
        #Add hover coordinates.
        hover_start = start_option.get_rect()
        hover_settings = settings_option.get_rect()
        hover_quit = quit_option.get_rect()
        hover_start.x, hover_start.y = 300, 270
        hover_settings.x, hover_settings.y = 300, 290
        hover_quit.x, hover_quit.y = 300, 320
        
        #Initialise a variable to indicate mouse position at click.
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
            screen.blit(self.background, (0, 0))
            screen.blit(title, (300, 180))
            screen.blit(start_option, (320, 260))
            screen.blit(settings_option, (320, 290))
            screen.blit(quit_option, (320, 320))
            #Implement changes to display on hover.
            if hover_start.collidepoint(pygame.mouse.get_pos()):
                hover = menu_font.render('>', False, (255, 255, 255))
                screen.blit(hover, (300, 260))
            elif hover_settings.collidepoint(pygame.mouse.get_pos()):
                hover = menu_font.render('>', False, (255, 255, 255))
                screen.blit(hover, (300, 290)) 
            elif hover_quit.collidepoint(pygame.mouse.get_pos()):
                hover = menu_font.render('>', False, (255, 255, 255))
                screen.blit(hover, (300, 320))
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
        
    def get_settings(self):
        '''Returns the settings menu when called by user'''
        #TODO: Finish implementation of get_settings
        self.settings = True
        
        pygame.init()
        font_colour = (255, 255, 255)
        screen = pygame.display.set_mode(self.screen_resolution) 
        
        #Create the objects to be displayed.
        settings_font = pygame.font.Font("resources/fonts/3Dventure.ttf", 30)
        return_option = settings_font.render("Go Back", False, font_colour)
        hover_back = return_option.get_rect()
        hover_back.x, hover_back.y = 300, 250
        
        #Initialise a variable to indicate mouse position at click.
        mouse_clicked = 0, 0
        
        #Begin displaying the settings menu.
        display_settings = self.settings
        while display_settings:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    display_settings = False
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    mouse_clicked = pygame.mouse.get_pos()                
            pygame.event.pump()
            screen.fill((0, 0, 0))
            screen.blit(self.background, (0, 0))
            #Add objects and their interactions.
            screen.blit(return_option, (340, 250))
            if hover_back.collidepoint(pygame.mouse.get_pos()):
                hover = settings_font.render('>', False, (255, 255, 255))
                screen.blit(hover, (320, 250))
            else:
                hover = settings_font.render('', False, (255, 255, 255))            
            if hover_back.collidepoint(mouse_clicked):
                display_settings = False
                self.settings = False
                pygame.quit()
                self.display_menu()
                break
            #Update screen display
            pygame.display.update() 
            pygame.display.flip()
        
#Uncomment the following for in-class display of the menu.
#check_menu_display = Menu()
#check_menu_display.display_menu()
