# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 12:47:50 2021

@author: krish
"""

from trello import TrelloClient
import random, requests
from trello.board import Board
from trello.base import TrelloBase
from trello.compat import force_str


api_key = '**************************************'
api_secret = '**********************************************************'


trelloboard = Board(name='python_trial')
#print(trelloboard.__repr__.__str__)
print(trelloboard.__repr__)



class Boards(TrelloBase):
    
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return force_str(u'<Board %s>' % self.name)
    
    
    
    




client = TrelloClient(
    api_key=api_key,
    api_secret=api_secret
)



all_boards = client.list_boards(board_filter = 'python_trial')
print(all_boards)


#myboard = all_boards[2]
#mylists = myboard.list_lists()
#print(list(mylists))
#print(type(myboard))



    



#lists = [str(li) for li in all_boards]
#print(lists)
#
#for li in mylists:
#    print(li.__dict__)


#b = Boards('python_trial')
#print(b)
##check = Boards('python_trial') in mylists
#
#temp = False
#
#for li in all_boards:
#    print(li, b)
#    
#    if li.__dict__['name'] == 'python_trial':
#        print(li.__dict__)
#        print(li.__dict__['name'])
#        temp = True
#        break
#print(temp)




def get_todo_item():
    to_do = []
    for card in mylists:
        cards = card.list_cards()
        if card.closed == False:
            for i in cards:
                to_do.append(i.name)
    return to_do[random.randint(0, len(to_do)-1)]



#todo_items = get_todo_item()
#print(todo_items)




def check_board_duplicacy_by_board_name(board_name):
    """
    to check if there is a board with the board name (input parameter)
    @parameters:
        board_name: name of the board of which we are checking its presence
    @returns:
        boolean value, if the board_name is already present, returns True else returns False
    """
    all_boards = client.list_boards()
    is_duplicate = False
    for board in all_boards:
        if board.__dict__['name'] == board_name:
            is_duplicate = True
            break
    return is_duplicate


def check_board_duplicacy_by_board_id(board_id):
    """
    to check if there is a board with the board id (input parameter)
    @parameters:
        board_id: id of the board of which we are checking its presence
    @returns:
        boolean value, if the board_id is already present, returns True else returns False
    """
    all_boards = client.list_boards()
    is_duplicate = False
    for board in all_boards:
        if board.__dict__['id'] == board_id:
            is_duplicate = True
            break
    return is_duplicate
    



def create_board(board_name):
    """
    creating a new board in a trello application
    @parameters:
        board_name: name of the board that has to be created in then application.
    @returns:
        returns the board_id of the new board. If the board is already present, it returns duplicate statement.
    """
    
    check = check_board_duplicacy_by_board_name(board_name)
    
    if check == False:
        url = "https://api.trello.com/1/boards/"
        querystring = {"name": board_name, "key": api_key, "token": api_secret}
        response = requests.request("POST", url, params=querystring)
        board_id = response.json()["shortUrl"].split("/")[-1].strip()
        return board_id
    else:
        return "the board is already present"



def get_boards():
    '''
    getting all boards in a given account.
    '''
    all_boards = client.list_boards()
    print(all_boards)
    return all_boards




b = create_board("python_trial")
print(b)


def get_board_id(board_name):
    """
    to get the board id of the board name in the trello board
    @parameters:
        board_name: the board_name of which we want to find the board_id of
    @returns:
        returns the board_id of a board_name if present, else it returns None
    """
    all_boards = client.list_boards()
    check = False
    board_id = None
    for board in all_boards:
        if board.__dict__['name'] == board_name:
            check = True
            board_id = board.__dict__['id']
            break

    print("check status")
    print(check)
    
    if check == True:
        return board_id
    else:
        return None


def get_board_name(board_id):
    """
    to get the board name of the board id in the trello board
    @parameters:
        board_id: the board_id of which we want to find the board_name of
    @returns:
        returns the board_name of a board_id if present, else it returns None
    """
    all_boards = client.list_boards()
    check = False
    board_name = None
    for board in all_boards:
        if board.__dict__['id'] == board_id:
            check = True
            board_name = board.__dict__['name']
            break

    print("check status")
    print(check)
    
    if check == True:
        return board_name
    else:
        return None




def get_board(board_name):
    all_boards = get_boards()
    check = False
    my_board = None
    for board in all_boards:
        if board.__dict__['name'] == board_name:
            print(board)
            check = True
            my_board = board
            break
    
    return my_board


def get_lists(board_name):
    """
    to get all the lists of a given card name.......
    @parameters:
        board_name: the name of a board from which we want to get all lists.
    @returns:
        all the lists from the board or else... None
        
    """
    my_board = get_board(board_name)
    print("my board to gegt lists is.........")
    print(my_board.__dict__)
    my_list = my_board.list_lists()
#    check = False
#    board_name = None
#    for board in all_boards:
#        if board.__dict__['name'] == board_name:
#            check = True
#            board_name = board
#            break
    
    return my_list
    
   
my_board_id = get_board_id('python_trial')
print(my_board_id)


def create_list(board_id, list_name):
    '''
    function to create new list with the board id
    @params:
        board_id: id of the trello board in which we want to create a new list
        list_name: the name of the new list we want to create.
    
    @returns:
        returns a new list id of the new list that is created/ a duplicit statement if 
        \any list with that name is created
    '''
    url = f"https://api.trello.com/1/boards/{board_id}/lists"
    querystring = {"name": list_name, "key": api_key, "token": api_secret}
    response = requests.request("POST", url, params=querystring)
    list_id = response.json()["id"]
    return list_id


def create_list_by_board_name(board_name, list_name):
    """
    function to create a new list in a given board with a given list_name
    @paramters:
        board_name: name of the trello board in which we want to create a list
        list_name: the name of the new list we want to create
    
    @returns:
        returns a new list id of the new list that is created/ a duplicit statement if 
        \any list with that name is created
    """
    mylists = get_lists(board_name)
    print(mylists)
    list_name_check = False
    if mylists is not None:
        for li in mylists:
            if li.__dict__['name'] == list_name:
                list_name_check = True
                break
        
    print("the list name check is %s", list_name_check)
    if list_name_check == False:
        board_id = get_board_id(board_name)
        
        if board_id is None:
            return "no board with name: %s .", board_name
        else:
            return create_list(board_id, list_name)
    else:
        return "there is alist with name %s.", list_name


create_list_by_board_name('python_trial', 'python_basics')


def get_list_id_from_list_name(board_name, list_name):
    my_lists = get_lists(board_name)
    my_list_id = None
    for mine in my_lists:
        if mine.__dict__['name'] == list_name:
            my_list_id = mine.__dict__['id']
            break;
    
    return my_list


def create_card(board_name, list_name, card_name):
    list_id = get_list_id_from_list_name(list_name)
    url = f"https://api.trello.com/1/cards"
    querystring = {"name": card_name, "idList": list_id, "key": api_key, "token": api_secret}
    response = requests.request("POST", url, params=querystring)
    card_id = response.json()["id"]
    return card_id
