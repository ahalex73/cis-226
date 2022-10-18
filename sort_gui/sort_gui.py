# Alexander Holmes
# 10/16/22
# CRN: 10235
# CIS 226: Advanced Python Programming
# Total time it took to complete --- 4 hours ---



'''
This program allows the user to enter in a list (Ex: 1,19,28,19) and sort and search through it.
Implementations of both merge sort to sort the list and binary search to search for a given
value inside of that sorted list are present in this program.

How to use 
1. Enter in your list.
2. Press 'Merge sort' to sort your list in ascending order.
3. Enter a search value you would like to look for in your list.
4. Hit 'Search' to search for your given value in your list.
'''

import PySimpleGUI as sg

total_swaps = 0

def main():
    class SortGUI:
        """Class that defines Heads or Tails GUI"""
        def __init__(self):
            '''The layout defines what the page initially will look like.'''
            layout = [
                [sg.T("Enter a List you would like to search or sort through:")],
                [sg.I(key='user_list')],

                [sg.B('Enter', key = 'enter_list')],
                [sg.T("Your current list is:", key='current_list')],
                [sg.T("Your current sorted list is:", key='sorted_list')],

                [sg.B('Merge sort', key='merge_sort')],
                [sg.T("Number of Swaps:"), sg.T(key="swaps")],
                [sg.T("Enter a value that you would like to search for:")],
                [sg.I(key='search_value')],
                [sg.B("Search", key='binary_search')],
                [sg.T("Search results:", key='search_results')],
                
                
                [sg.StatusBar("Welcome to Alex's Sort Gui!", key='StatusBar')],
                [sg.Menu(
                    [['Quit and Help', ['Quit', 'Help' ]],
                    ['About that work', 'About']], key='-MenuBar-')],
            ]

            self.window = sg.Window('Sort Gui - Alexander Holmes', layout)


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

                # Displays Help screen 
                elif event == 'Help':
                    ''' Help page dropdown content'''
                    help_section = ''' '''

                    sg.popup(help_section, title="Help")
                    print("A popup should display. If not," + \
                        "there is documentation to reference at the top of the program.")

        
                elif event =='About':
                    ''' About page dropdown content '''
                    about_content = '' +\
                        'Design: \n\n' +\
                        'Develop: \n\n' +\
                        'Test: There are no tests.\n\n'+\
                        'Document: '
                
                    sg.popup(about_content, title="About")


                elif event == 'enter_list':
                    ''' Enters, validates, and stores user list.'''

                    self.validate_list(event, values)
                    self.window['current_list'].update("Your current list is: {}".format(values['user_list']))

                    

                elif event =='binary_search':
                    ''' Handles the enter button for searching a value using binary search '''
                    
                    search_value = int(values['search_value'])
                    self.window['search_results'].update(self.binary_search(search_value, result))

                    

                elif event == 'merge_sort':
                    ''' Merge sort button is pressed, sorts user list and updates window to show sorted list'''
                    
                    user_list = values['user_list'].split(",")
                    map_object = map(int, user_list)
                    listofint = list(map_object)

                    result = self.merge_sort(listofint)
                    self.window['swaps'].update(total_swaps)
                    self.window['sorted_list'].update("Your current sorted list is: {}".format(result))

                    
        def validate_list(self, events, values):
            ''' Handle when enter button is pressed'''
            user_list = values['user_list']
            self.window['current_list'].update("Your current list is:{}".format(user_list))

            return



        def binary_search(self, search_value, array):
            ''' Search through array with binary sort O(log n)'''
            start = 0
            end = len(array)-1
            found = False
            step = 0
            comparisons = 0

            while found != True and start <= end:   
                # while we havent found search value and we havent crossed start and end markers
                # Calculate midway between start and end marker
                middle = int((start + end) / 2)

                if array[middle] == search_value:
                    # Then we found the value
                    comparisons += 1
                    found = True
                
                elif array[middle] < search_value:
                    # Value is to the right of our search
                    start = middle + 1
                    step += 1
                    comparisons += 1
                else:
                    # Value is to the left of our search
                    end = middle - 1
                    step += 1
                    comparisons += 1

            # handling if integer was not found in list
            if found == False:
                return str("The integer was not found.")
                
            # if found, return a string stating where it is and in how many steps
            string = str(("The value {} is at index {}, found in {} steps\n".format(search_value, middle, step)))

            return string


        def merge_sort(self, array):
            ''' Sorts a given array with merge sort O(n log(n))'''
            # handles if array is too small
            if len(array) <= 1:
                return array

            midpoint = int(len(array) / 2)    

            # initializes and recursively calls a left and right array 
            # the left is from the 0 index to midpoint and the right is up to midpoint to end
            left, right = self.merge_sort(array[:midpoint]), self.merge_sort(array[midpoint:])

            return self.merge(left,right)

        def merge(self, left, right):
            ''' Merges the two arrays given from merge_sort function'''

            print(left,right)
            results = []
            global total_swaps
            left_pointer = right_pointer = 0    # index pointers used to compare values
            
            # while there are still numbers left inside each seperate array to compare,
            # continue to evaluate and swap them.
            while left_pointer < len(left) and right_pointer < len(right):

                if left[left_pointer] < right[right_pointer]:

                    results.append(left[left_pointer])
                    left_pointer += 1
                    total_swaps += 1

                else:
                    results.append(right[right_pointer])
                    right_pointer += 1
                    total_swaps += 1

    
            results.extend(left[left_pointer:])
            results.extend(right[right_pointer:])

            return results 
            

    # Instantiate our class and run it
    sort_gui = SortGUI()
    sort_gui.run()
    

if __name__ == '__main__':
    main()