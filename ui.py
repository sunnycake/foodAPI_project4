
"""functions in this file handles 
    communication between the application and the user"""

def get_search_term():
    search_recipe = input('Search for a recipe: ').strip()
    return search_recipe

  
def message(msg):
    """ Prints a message for the user
     :param msg: the message to print"""
    print(msg)
    
def get_non_empty_string(question):
    """accepts only alpha characers for an answer """
    answer = input(question)
    while True:
        if answer.isalpha() == False:
            message("Please use alpha characters only!") 
            answer = input(question)
        else:
            return answer


def get_id():
    """ Ask for ID, validate to ensure is positive integer
    :returns: the ID value """
    while True:
        try:
            id = int(input('Enter art work ID: '))
            if id > 0:
                return id
            else:
                message('Please enter a positive number.')

        except ValueError:
            message('Please enter a number.')

            
def save_or_not_save():
    """ Ask user to enter 'save' or 'not save'
     :returns: True if user enters 'save' or False if user enters 'not save' """
    while True:
        response = input('Enter \'save\' if you wish to save this data: \'not save\' if you are not interested: ')
        if response.lower() == "save":
            return True
        elif response.lower() == "not save":
            return False
        else:
            message('Type \'save\' or \'not save\'')

