# Alexander Holmes
# 9/27/22
# CRN: 10235
# CIS 226: Advanced Python Programming
# Total time it took to complete --- 4 hours ---

import PySimpleGUI as sg
import random


'''
The Documentation for this program can be found in the About that work menu option.

How to play.
This program is a game of Heads or Tails. In order to play the game first enter in your name in the corresponding field, then decide if you would 
like to pick heads or tails. You will then flip a coin using the 'Flip Coin' button to determine if you or the computer won or not.
If you get confused along the way you can reference the Help option in the menu.'''


def main():
    class HeadsOrTails:
        """Class that defines Heads or Tails GUI"""
        def __init__(self):
            '''The layout defines what the page initially will look like.'''
            layout = [
                [sg.T("Enter your name:")],
                [sg.I(key='user_name')],
                [sg.T("Heads or Tails?")],
                [sg.I(key='user_choice')],
                [sg.B('Flip Coin')],
                [sg.StatusBar("Ready", key='StatusBar')],
                [sg.Menu([['File', ['View Log', 'Save Log as']],
                    ['Quit and Help', ['Quit', 'Help' ]],
                    ['About that work', 'About']], key='-MenuBar-')],
            ]

            self.window = sg.Window('Heads Or Tails', layout)


        def run(self):
            """Start the program"""
            self._run_loop()    # Start the Event Loop
            self.window.close() # After that is done, close the window


        def _run_loop(self):
            """Run the Event Loop"""
            log = []
            while True:
                event, values = self.window.read()
                print(event, values)   # For Debugging purposes
                if event == sg.WINDOW_CLOSED or event == 'Quit':    # If user wishes to quit, close program.
                    break

                # Flip the coin, store and display if its a loss or win.
                elif event == 'Flip Coin':
                    self.window['StatusBar'].update("Flipping"),    # Statusbar Flipping
                    win_or_lose = self.on_flip(event, values)       # Stores if the user won or lost current round.
                    log.append(win_or_lose)                         # Appends the rounds data to the Log
                    self.window['StatusBar'].update("Ready"),       # Statusbar Ready
                    

                # View the Logs of the total wins and losses.
                elif event == 'View Log':
                    print("press")
                    sg.popup(log, title="Log")

                # Save the win and loss log in a text file.
                elif event == 'Save Log as': 
                    with open('logs.txt', 'w') as my_data_file:
                        my_data_file.write(str(log))

                # Displays Help screen 
                elif event == 'Help':
                    help_section = '''In order to play the game first enter in your name in the corresponding field, then decide if you would like to pick heads or tails. You will then flip a coin using the 'Flip Coin' button to determine if you or the computer won or not. 
                    
Menu options
-------------------
File -> View log shows you the previous history of your games.
File -> Save Log As saves the log history.
Quit -> Allows you to quit
About that work -> About shows how the program was created'''



                    sg.popup(help_section, title="Help")
                    print("A popup should display. If not," + \
                        "there is documentation to reference at the top of the program.")

        
                elif event =='About':
                    about_content = '' +\
                        'Design: The program was to implement the common game Heads or Tails using Python and PySimpleGui.The program was designed' +\
                            ' to be as simple as possible for the end user.\n\n' +\
                        'Develop: To develop the program it was necessary in understanding how PySimpleGui worked, using '+\
                            'their documentation to understand how to update, display, or capture values and keys.\n\n' +\
                        'Test: There are no tests.\n\n'+\
                        'Document: The heads_or_tails.py file contains the whole program and display. With using ' +\
                            'PySimpleGUI I was able to create a loop that infinitely runs whilst the program is running that defines the window'+\
                            'which can be updated and adjusted according to the users needs. '
                
                    sg.popup(about_content, title="About")


        def on_flip(self, event, values):
            ''' Flips a coin, displays who won.'''

            result = random.randint(0,1)    # Random number 0 or 1, heads or tails respectively
            if result == 0:
                result = "Heads"
            else:
                result = "Tails"

            sg.popup("You picked: " + values['user_choice'])
            sg.popup("You flipped: " + result)
            self.window['StatusBar'].update("Declaring Winner!"),

            if values['user_choice'] == result:
                sg.popup("Congratulations " + values['user_name'] + " You win!")
                win_or_loss = "Win" # variable keeping track of win or loss 
                                    # in order to update the logs
            else:
                sg.popup("Congratulations " + values['user_name'] + " You Lost!")
                win_or_loss = "Loss"

            return win_or_loss


    # Instantiate our class and run it
    heads_or_tails = HeadsOrTails()
    heads_or_tails.run()

if __name__ == '__main__':
    main()