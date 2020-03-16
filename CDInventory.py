#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# MBailey, 2020-Mar-13, added CD and DataProcessing classes, added code to main body, added code to FileIO and IO classes. Program runs successfully.
# MBailey, 2020-Mar-15 added docstrings and comments where necessary. 
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []
import pickle

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) getter and setter
        cd_title: (string) getter and setter
        cd_artist: (string) getter and setter
    methods:
        __str__: returns formatted string of data stored in attributes
    """
    #Fields
    cd_id: int
    cd_title: str
    cd_artist: str
    #Constructor
    def __init__(self, title, artist, cd_table):
        """constructor for CD class
        args: title (str)
              artist (str)
              cd_table (list), used for assigning sequential ID numbers
        returns: none"""
        #Attributes
        self.__cd_id = len(cd_table) + 1
        self.__cd_title = title
        self.__cd_artist = artist

    #Properties
    @property
    def cd_id(self):
        """getter for cd_id
        args: none
        returns: cd_id (int)
        """
        return self.__cd_id
    
    @cd_id.setter
    def cd_id(self, cd_idValue):
        """setter for cd_id
        args: cd_idValue (int)
        returns: none
        """
        if str(cd_idValue).isnumeric() == False:
            raise Exception('ID must be numeric') #This should not happen because ID number is set automatically, but wanted to build in an exception just in case
        else:
            self.__cd_id = cd_idValue
       
    @property
    def cd_title(self):
        """getter for cd_title
        args: none
        returns: cd_title (str)
        """
        return self.__cd_title.title()
    
    @cd_title.setter
    def cd_title(self, cd_titleValue):
        """setter for cd_title
        args: cd_titleValue (str)
        returns: none
        """
        self.__cd_title = cd_titleValue.title()
        
    @property
    def cd_artist(self):
        """getter for cd_artist
        args: none
        returns: cd_artist (str)
        """
        return self.__cd_artist
    
    @cd_artist.setter
    def cd_artist(self, cd_artistValue):
        """setter for cd_artist
        args: cd_artistValue (str)
        returns: none
        """
        self.__cd_artist = cd_artistValue
    #Methods
    def __str__(self):
        """returns formatted string of """
        return 'ID #{}: {} (by: {})'.format(self.cd_id, self.cd_title, self.cd_artist)

# -- PROCESSING -- #
class FileIO:
    """
    Processes data to and from file:
    properties:

    methods:
        save_file(file_name, cd_table): -> None
        read_file(file_name, cd_table): -> (a list of CD objects)
"""
    # TODO Add code to process data from a file
    # TODO Add code to process data to a file
    @staticmethod
    def read_file(file_name, cd_table):
        """Function to manage data ingestion from file to a list of dictionaries
        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table. One line in the file represents one dictionary row in table.
        Args:
            file_name (string): name of file used to read the data from
            cd_table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
        Returns:
            cd_table (list of dict): 2D data structure read from the binary file.
        """
        try:
            cd_table.clear()  # this clears existing data and allows to load data from file
            with open(file_name, 'rb') as objFile:
                cd_table = pickle.load(objFile)
                print('Data successfully loaded from file.')
            return cd_table
        except FileNotFoundError:
            print(file_name, 'was not found.')
            return cd_table #must return this so that function returns a list, cannot assign None to a list type variable
        except EOFError:
            print(file_name, 'is empty.')
            return cd_table

    @staticmethod
    def save_file(file_name, cd_table):
        """
        Function to save table to a file. Includes error handling.
        Args: cd_table (list): name of list used to store dictionaries
              file_name (string): the name of the .txt file where data will be written.
        Returns: none
        """
        try:
            with open(file_name, 'wb') as objFile:
                pickle.dump(cd_table, objFile)
            print('Data successfully saved to file.')
        except:
            print('Error encountered while saving. Please try again.')

class DataProcessor:
    
    @staticmethod
    def add_cd(new_cd, cd_table):
        """
        Creates dictionary from data received in IO.user_cd_input. Appends dictionary to cd_table.
        Args: cd_table (list): name of list used to store dictionaries
              new_cd (CD object): 
        Returns: none
        
        try:
            for row in cd_table:
                if row['ID'] == intID:
                    raise DuplicateIDError()
            cd_dict = {'ID': intID, 'Title': strTitle, 'Artist': strArtist}
            cd_table.append(cd_dict)
        except DuplicateIDError as e:
            print('You entered a duplicate ID number, therefore your CD entry was not added to the inventory.\nPlease enter a unique ID number.\n')
            print (e.__str__)
        """
        cd_table.append(new_cd)
        
    @staticmethod
    def delete_cd(cd_table, IDnumber):
        """
        Function to delete a CD's dictionary based on user's choice of which ID number to delete. 
        Loops through the 'ID' key's value in each dictionary and checks if it is equal to the user's input.
        Renumbers all ID numbers after deletion.
        Args: table (list): name of list used to store dictionaries
              IDnumber (int): user's input of which ID to delete
        Returns: none
        """
        intRowNr = -1
        blnCDRemoved = False
        for row in cd_table:
            intRowNr += 1
            if row.cd_id == IDnumber:
                del cd_table[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
        for i in range(len(cd_table)): #These two lines renumber all ID numbers after deletion so that ID numbers are sequential
            cd_table[i].cd_id = i + 1
            
# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODO add docstring
    # TODO add code to show menu to user
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user
        Args:
            None.
        Returns:
            None.
        """
        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')
    # TODO add code to captures user's choice
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection
        Args:
            None.
        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x
        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    # TODO add code to display the current data on screen
    @staticmethod
    def show_inventory(cd_table):
        """Displays current inventory table
        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.
        Returns:
            None.
        """
        print('======= The Current Inventory: =======')
        for row in cd_table:
            print(row.__str__()) #Simply prints formatted string returned by __str__ method
        print('======================================')
        
    # TODO add code to get CD data from user
    @staticmethod
    def get_int_input(input_string):
        """ Gets an integer input from the user
        Args:
            input_string (string): String displayed prompting user for input
        Returns:
            user_int_input (int): Integer value given by the user
        """
        correctID = False
        while correctID == False:
            try:
                user_int_input = int(input(input_string).strip()) #Structured error handling for when ID is not an int
                correctID = True
                return user_int_input
            except ValueError:
                print('You entered an invalid ID. Please enter an integer.')
                
    @staticmethod
    def user_cd_input():
        """Gathers user input for fields of the new CD
        Args:
            None.
        Returns:
            intID (int): ID for the new CD
            strTitle (string): Title of the new CD
            strArtist (string): Artist of the new CD
        """
        #intID = IO.get_int_input("Enter ID: ")  #The get_int_input() function contains error handling in case input is a non-integer
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()

        return strTitle, strArtist


# -- Main Body of Script -- #
# TODO Add Code to the main body
# Load data from file into a list of CD objects on script start
try:    #Try to read in file, if it exists
    lstOfCDObjects = FileIO.read_file(strFileName, lstOfCDObjects) #loads file contents into memory, stored in lstOfCDObjects
    print('Welcome back to your CD Inventory')
except:#If file does not exist, continue anyways
    print('Welcome to your CD Inventory! An existing inventory file was not found.\nLet\'s create a new inventory.\n')
# Display menu to user
while True:
    choice = IO.menu_choice()
    # show user current inventory
    if choice == 'i':
        IO.show_inventory(lstOfCDObjects)
    # let user add data to the inventory
    elif choice == 'a':
         new_cd = CD(*IO.user_cd_input(), lstOfCDObjects)
         DataProcessor.add_cd(new_cd, lstOfCDObjects)
         IO.show_inventory(lstOfCDObjects)
    # let user save inventory to file
    elif choice == 's':
        FileIO.save_file(strFileName, lstOfCDObjects)
    # let user load inventory from file
    elif choice == 'l':
        FileIO.read_file(strFileName, lstOfCDObjects)
    # let user delete CD from inventory
    elif choice == 'd':
        IO.show_inventory(lstOfCDObjects)
        intIDDel = IO.get_int_input('Enter the ID you would like to delete: ')
        DataProcessor.delete_cd(lstOfCDObjects, intIDDel)
        IO.show_inventory(lstOfCDObjects)
    # let user exit program
    elif choice == 'x':
        break
    else:
        print('General error while making menu choice.')

