# Alexander Holmes
# 10/16/22
# CRN: 10235
# CIS 226: Advanced Python Programming
# Total time it took to complete --- 4 hours ---

import PySimpleGUI as sg

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
                [sg.B("Enter", key='binary_search')],
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
                    help_section = ''' '''

                    sg.popup(help_section, title="Help")
                    print("A popup should display. If not," + \
                        "there is documentation to reference at the top of the program.")

        
                elif event =='About':
                    about_content = '' +\
                        'Design: \n\n' +\
                        'Develop: \n\n' +\
                        'Test: There are no tests.\n\n'+\
                        'Document: '
                
                    sg.popup(about_content, title="About")


                elif event == 'enter_list':
                    self.validate_list(event, values)
                    self.window['current_list'].update("Your current list is: {}".format(values['user_list']))

                    pass

                elif event =='binary_search':
                    
                    search_value = int(values['search_value'])

                    self.window['search_results'].update(self.binary_search(search_value, result))

                    pass

                elif event == 'merge_sort':
                    ''' Merge sort button is pressed, sorts user list and updates window to show sorted list'''
                    
                    user_list = values['user_list'].split(",")
                    map_object = map(int, user_list)
                    listofint = list(map_object)

                    result = self.merge_sort(listofint)
                    self.window['sorted_list'].update("Your current sorted list is: {}".format(result))

                    pass

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
                
            string = str(("The value {} is at index {}, found in {} steps\n".format(search_value, middle, step)))

            return string


        def merge_sort(self, array):
            ''' Sorts a given array with merge sort O(n log(n))'''
            if len(array) <= 1:
                return array

            midpoint = int(len(array) / 2)    

            left, right = self.merge_sort(array[:midpoint]), self.merge_sort(array[midpoint:])

            return self.merge(left,right)

        def merge(self, left, right):
            print(left,right)
            results = []
            #swaps = 0
            left_pointer = right_pointer = 0
            
            while left_pointer < len(left) and right_pointer < len(right):

                if left[left_pointer] < right[right_pointer]:

                    results.append(left[left_pointer])
                    left_pointer += 1
                    #swaps += 1

                else:
                    results.append(right[right_pointer])
                    right_pointer += 1
                    #swaps += 1


            results.extend(left[left_pointer:])
            results.extend(right[right_pointer:])

            return results #,swaps 
            # results is a list, swaps would be an int, I have tried converting
            # both to same type, as well as using self.swaps as I would somehow need to keep track of the swaps
            # with also recurssively calling the function in merge_sort.
            

    # Instantiate our class and run it
    sort_gui = SortGUI()
    sort_gui.run()
    

if __name__ == '__main__':
    main()