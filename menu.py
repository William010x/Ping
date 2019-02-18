class Menu:
    '''Menu class that creates a menu and lists interactive menu options'''
    
    screen_resolution = (400, 300)
    
    def __init__(self):
        '''Initialises an new instance of Menu'''
        self.start = False
        self.settings = False
        
    def display_menu(self):
        '''Displays menu objects on user's screen'''
        #TODO: Finish implementation of display_menu
        
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