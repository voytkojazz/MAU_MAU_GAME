#!/usr/bin/env python
# coding: utf-8



import random
import time
import os
import sys
CRED = '\033[91m'
CEND = '\033[0m'
CBLACK = '\33[30m'

CONGRATS = '''

 ▄████▄   ▒█████   ███▄    █   ▄████  ██▀███   ▄▄▄     ▄▄▄█████▓ █    ██  ██▓    ▄▄▄     ▄▄▄█████▓ ██▓ ▒█████   ███▄    █   ██████    
▒██▀ ▀█  ▒██▒  ██▒ ██ ▀█   █  ██▒ ▀█▒▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒ ██  ▓██▒▓██▒   ▒████▄   ▓  ██▒ ▓▒▓██▒▒██▒  ██▒ ██ ▀█   █ ▒██    ▒    
▒▓█    ▄ ▒██░  ██▒▓██  ▀█ ██▒▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░▓██  ▒██░▒██░   ▒██  ▀█▄ ▒ ▓██░ ▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒░ ▓██▄      
▒▓▓▄ ▄██▒▒██   ██░▓██▒  ▐▌██▒░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ ▓▓█  ░██░▒██░   ░██▄▄▄▄██░ ▓██▓ ░ ░██░▒██   ██░▓██▒  ▐▌██▒  ▒   ██▒   
▒ ▓███▀ ░░ ████▓▒░▒██░   ▓██░░▒▓███▀▒░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ ▒▒█████▓ ░██████▒▓█   ▓██▒ ▒██▒ ░ ░██░░ ████▓▒░▒██░   ▓██░▒██████▒▒   
░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   ░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒▒   ▓▒█░ ▒ ░░   ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░   
  ░  ▒     ░ ▒ ▒░ ░ ░░   ░ ▒░  ░   ░   ░▒ ░ ▒░  ▒   ▒▒ ░   ░    ░░▒░ ░ ░ ░ ░ ▒  ░ ▒   ▒▒ ░   ░     ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░▒  ░ ░   
░        ░ ░ ░ ▒     ░   ░ ░ ░ ░   ░   ░░   ░   ░   ▒    ░       ░░░ ░ ░   ░ ░    ░   ▒    ░       ▒ ░░ ░ ░ ▒     ░   ░ ░ ░  ░  ░     
░ ░          ░ ░           ░       ░    ░           ░  ░           ░         ░  ░     ░  ░         ░      ░ ░           ░       ░     
░                                                                                                                                     

'''

greetings = """

░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝

███╗░░░███╗░█████╗░██╗░░░██╗░░░░░░███╗░░░███╗░█████╗░██╗░░░██╗
████╗░████║██╔══██╗██║░░░██║░░░░░░████╗░████║██╔══██╗██║░░░██║
██╔████╔██║███████║██║░░░██║█████╗██╔████╔██║███████║██║░░░██║
██║╚██╔╝██║██╔══██║██║░░░██║╚════╝██║╚██╔╝██║██╔══██║██║░░░██║
██║░╚═╝░██║██║░░██║╚██████╔╝░░░░░░██║░╚═╝░██║██║░░██║╚██████╔╝
╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚═════╝░░░░░░░╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚═════╝░
"""


def clear():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')




SPADE = CBLACK + '\u2660' + CEND
HEART = CRED + '\u2665' + CEND
DIAMOND = CRED + '\u2666' + CEND
CLUB = CBLACK + '\u2663' + CEND
suits = [SPADE, HEART, DIAMOND, CLUB]


# # This is the implementation of Card Class

# 0 = чірва 1 = піка  2 = бубна 3 = хреста

class Card:
    #class variables for 4 different suits of cards and 13 different ranks of cards
    suits = suits
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9",'10', "J", "Q", "K", "A"]
    
    # when object of Card class is created it requeres index of suit and rank from their list as arguments
    def __init__(self, suit, rank):
        self.suite = Card.suits[suit]
        self.rank = Card.ranks[rank]
        
    def __str__(self):
        representation = f"|{self.rank}{self.suite}|"
        return representation
    
    def __lt__(self, other):
        return self.rank < other.rank
    
    def __eq__(self, other):
        return self.rank == other.rank


# # This is the implemenatation of Deck Class 



class Deck:
    def __init__(self):
        self.deck = []
        ### When new deck class object is implemented, this loop creates 52 cards and adds them to the deck.
        for suit_index in range(len(Card.suits)):
            for rank_index in range(len(Card.ranks)):
                self.deck.append(Card(suit_index, rank_index))
        ### Calling a method of Deck class to shuffle all the cards in the deck
        self.shuffle()
        
    def __len__(self):
        return len(self.deck)
    def __str__(self):
        for card in self.deck:
            return card
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def pop_card(self):
        return self.deck.pop()
        


# # Implementation on Hand class (player)


class Hand(Deck):
    # class variable to track id of the player
    id = 1
    # When the Hand class object is initialized - it requires the label - name of the player
    def __init__(self, label):
        #every time when new Hand object is created it tooks id and with every new object - id increases by one
        self.id = Hand.id
        Hand.id +=1 
        self.label = label
        self.deck = []
        self.has_turn = False
        self.is_mau = False
        self.is_mau_mau = False
        self.win_count = 0
    def __str__(self):
        return self.label
    def add_card(self, card):
        self.deck.append(card)
    def pop_card_by_index(self, index):
        return self.deck.pop(index)
        
    




class Table:
    def __init__(self, players=[]):
        self.played_cards = []
        self.players = players
        self.deck = Deck()
        self.mao = False


    def show_rules(self):
        clear()
        with open('rules.txt', 'r') as rules:
            d = rules.read()
            print(d)
        go = 1
        while go != '':
            go = input('\n\n\n---press ENTER to continue')
        self.show_menu()

    def finish_game(self):
        sys.exit('\n\n---Thank you for playing MAU-MAU with us!')


    def show_winners(self):
        clear()
        results = {}
        for player in self.players:
            results[str(player)] = player.win_count
        for key, value in results.items():
            print(f'Player {key} won the game {value} times')
        go = 1
        while go != '':
            go = input('press ENTER to go back')
        self.show_menu()


    def show_menu(self):
        func_map = {
            '1': self.start_game,
            '2': self.show_rules,
            '3': self.show_winners,
            '4': self.finish_game
        }
        numbers = [1,2,3,4]
        options = ['Start game', 'Show rules', 'Show winners', 'Finish game']
        zipped = zip(numbers, options)
        for number, option in zipped:
            print(str(number) + '. ' + option)
        while True:
            ask = input('type the number of option you want to choose and press enter... ')
            if ask in func_map.keys():
                func_map[ask]()
                break
            elif ask not in func_map.keys():
                print('try again, this time enter number between 1 and 4... ')



    def create_player(self, name):
        new_player = Hand(name)
        ### this loop creates 6 Card objects and adds them to every player
        for _ in range(6):
            new_player.add_card(self.deck.pop_card())
        self.players.append(new_player)
        
        
    def start_game(self):
        ### creates amount of players between 2 and 6, gives them 6 cards and pops card from the deck to the table to start the round
        clear()
        print('You can create up to 6 players, minimum 2')
        amount = 0
        while amount < 2 or amount > 6:
            amount = int(input('How many players yout want to create?...  '))
        for _ in range(1, amount+1):
            name = input(f'input the name of player{_} \n')
            self.create_player(name)
        self.start_first_round()
        self.make_turn(0, True)
            
            
    def start_first_round(self):
        card_to_start = self.deck.pop_card()
        while card_to_start.rank == 'J' or card_to_start.rank == '7':
            card_to_start = self.deck.pop_card()
        self.played_cards.append(card_to_start)
    
    
    def show_last_card(self):
        print(f'\n:::CARD ON THE TABLE IS:::\n\n{self.played_cards[-1]}\n')
        
        
    def count_5(self):
        counter = 1
        while counter != 6:
            print(str(counter) + '...')
            time.sleep(1)
            counter += 1
        
    def show_player_cards(self, player_index):
        print('\n---Your cards are:---')
        cards = ''
        number = 0
        x = iter(self.players[player_index].deck)
        for _ in range(len(self.players[player_index].deck)):
            number += 1
            cards += str(number) + '----' + str(next(x)) + '      '
        ready = input('press ENTER when you are ready to see your cards\n')
        print("\n" + cards + '\n\n\n')
        
        
        
    def choose_card(self, player_index):
        while True:
            try:
                ask = int(input('type the number of card you want to choose... '))
                i = ask - 1
                break
            except:
                print('...you need to type only number...')
        choosen_card = self.players[player_index].pop_card_by_index(i)
        return choosen_card

            
        
    
    def ask_suite(self):
        print('Please type the number which corresponds to the suit that you want to ask for')
        number = 0
        for suite in suits:
            number += 1
            print(f'{number}. {suite}')
        
        while True:
            try:
                ask = int(input('...type the number...'))
                break
            except:
                print('only numbers are accepted')
        while ask > 4 or ask < 1:
            print('type number between 1 and 4 that corresponds to the suit that you want to ask for')
            self.ask_suite()
        i = ask - 1
        requested_suite = suits[i]
        return requested_suite
            
     
    
    def check_mau(self, player_index):
        player = self.players[player_index]

        if len(player.deck) == 1:
            player.is_mau = True
            print(f'!!! PLAYER {player.label} says: MAUUO! \n')
        elif len(player.deck) > 1:
            player.is_mau = False
        elif len(player.deck) == 0:
            player.is_mau_mau == True
            player.win_count += 1
            self.greet_winner(player_index)
            

    def show_mau_players(self):
        mau_players = [player for player in self.players if player.is_mau == True]
        s = 'PLAYERS WHO HAVE "MAO" ARE: '
        for mau_player in mau_players:
            s += str(mau_player) + ", "
        if len(mau_players) > 0:
            print(s + '\n')
        

    def greet_winner(self, player_index):
        clear()
        print(CONGRATS)
        print('\n\n\n\n')
        winner = self.players[player_index]
        print(f'\n--- --- --- PLAYER {winner} IS WINNER OF THIS ROUND --- --- ---\n')
        self.show_menu()


        
    def confirm_next_turn(self):
        response = '1'
        while response != '':
            response = input('When you are ready for next turn, press ENTER')
        return True
    
    
    
    def next_turn(self, player_index, took_seven, requested_suite=None, take_eight=False):
        clear()
        player_index += 1
        try:
            self.make_turn(player_index, took_seven, requested_suite=requested_suite, take_eight=take_eight)
        except IndexError:
            player_index = 0
            self.make_turn(player_index, took_seven, requested_suite=requested_suite, take_eight=take_eight)
         
        
        
    def eight_scenario(self, player_index):
        player_ranks = []
        player = self.players[player_index]
        last_played_card = self.played_cards[-1]
        for card in player.deck:
            player_ranks.append(card.rank)
        if '8' not in player_ranks:
            print('...you do not have any 8s cards, so you need to skip your turn...')
            self.confirm_next_turn()
            self.next_turn(player_index, False, take_eight=True) 
        
        

        if "8" in player_ranks:
            choosen_card = self.choose_card(player_index)
            if choosen_card.rank == '8':
                self.played_cards.append(choosen_card)
                self.show_player_cards(player_index)
                self.show_last_card()
                self.check_mau(player_index)
                self.confirm_next_turn()
                self.next_turn(player_index, False, take_eight=False)
        
            elif choosen_card.rank != '8':
                print('...You can only place 8 card over 8 card on the table...')
                print('you got penalty - skip turn and take one card from the deck...')
                shit = input('...type "shit" to continue and press ENTER...')
                while not shit == 'shit':
                    shit = input('...type "shit" to continue and press ENTER...')
                player.add_card(choosen_card)
                player.add_card(self.deck.pop_card())
                self.show_player_cards(player_index)
                self.show_last_card()
                self.confirm_next_turn()
                self.next_turn(player_index, False, take_eight=True)
            
        
          
    def junior_scenario(self, player_index, requested_suite):
        player_suites = []
        player_ranks = []
        player = self.players[player_index]
        
        for card in player.deck:
            player_suites.append(card.suite)
            player_ranks.append(card.rank)
        
        print(f'REQUESTED SUITE BY PLAYER WHO THROWED JUNIOR IS ---{requested_suite}--- \n')    
        
        if requested_suite not in player_suites and 'J' not in player_ranks:
            print('...unfortunately you do not have corresponding suite or "J"... you take one card from deck and skip your turn...')
            shit = input('...type "shit" to continue and press ENTER...')
            while not shit == 'shit':
                shit = input('...type "shit" to continue and press ENTER...')
            player.add_card(self.deck.pop_card())
            self.show_player_cards(player_index)
            self.confirm_next_turn()
            self.next_turn(player_index, True, requested_suite)
            
        else:
            choosen_card = self.choose_card(player_index)
            
            while not choosen_card.suite == requested_suite or choosen_card.rank == 'J':
                print('You must choose the card with the same rank. Becouse the last played card on the table is "J"')
                print( f'And requested_suite is {requested_suite}\n')
                self.players[player_index].add_card(choosen_card)
                self.show_player_cards(player_index)
                choosen_card = self.choose_card(player_index)
            
            self.played_cards.append(choosen_card)
            self.show_last_card()
            self.check_mau(player_index)
            self.confirm_next_turn()
            
            if choosen_card.rank == '7':
                self.next_turn(player_index, False, requested_suite=None)
            if choosen_card.rank == 'J':
                requested_rank = self.ask_suite()
                self.next_turn(player_index, True, requested_suite=requested_rank)
            else:
                self.next_turn(player_index, True, requested_suite=None)
            
            
        
        
        
    
    def regular_scenario(self, player_index):
        player_ranks = []
        player_suites = []
        last_played_rank = self.played_cards[-1].rank
        last_played_suite = self.played_cards[-1].suite
        player = self.players[player_index]
        
        for card in player.deck:
            player_ranks.append(card.rank)
            player_suites.append(card.suite)
        
        if (last_played_rank not in player_ranks) and (last_played_suite not in player_suites) and "J" not in player_ranks:
            print('...you do not have the card with corresponding suite or rank... you take one card from deck and skip turn...')
            self.players[player_index].add_card(self.deck.pop_card())
            shit = input('...type "shit" to continue and press ENTER...')
            while not shit == 'shit':
                shit = input('...type "shit" to continue and press ENTER...')
            self.show_player_cards(player_index)
            self.confirm_next_turn()
            self.next_turn(player_index, True)
            
        choosen_card = self.choose_card(player_index)
        
        if choosen_card.rank == 'J':
                self.played_cards.append(choosen_card)
                self.check_mau(player_index)
                requested_suite = self.ask_suite()
                if self.confirm_next_turn() == True:
                    took_seven = False
                    self.next_turn(player_index, took_seven, requested_suite=requested_suite)
        
        while not choosen_card.rank is last_played_rank and not choosen_card.suite is last_played_suite:
            print('\nYou must choose card with the SAME RANK or SAME SUITE...')
            self.players[player_index].add_card(choosen_card)
            self.show_player_cards(player_index)
            self.show_last_card()
            choosen_card = self.choose_card(player_index)
            
        self.played_cards.append(choosen_card)
        self.show_last_card()
        self.check_mau(player_index)
        self.confirm_next_turn()
        if choosen_card.rank == '7':
            self.next_turn(player_index, False)
        else:
            self.next_turn(player_index, True)
        
        
        
        
    
    def seven_scenario(self, player_index):
        played_ranks = []
        player_ranks = []
        player = self.players[player_index]
        for card in self.played_cards:
            played_ranks.append(card.rank)
        for card in player.deck:
            player_ranks.append(card.rank)
        last_four_ranks = played_ranks[-4:]
        amount_of_7 = last_four_ranks.count('7')
        if last_four_ranks[-2] != '7':
            amount_of_7 = 1
        
        if '7' not in player_ranks and 'J' not in player_ranks:
            for _ in range(amount_of_7 * 2):
                player.deck.append(self.deck.pop_card())
            print(f'becouse you dont have 7s or J cards you took {amount_of_7 * 2} cards from deck...')
            shit = input('...type "shit" to continue and press ENTER...')
            while not shit == 'shit':
                shit = input('...type "shit" to continue and press ENTER...')
            print('now your card are:')
            self.show_player_cards(player_index)
            self.check_mau(player_index)
            if self.confirm_next_turn() == True:
                took_seven = True
                self.next_turn(player_index, took_seven)    
                
        elif '7' in player_ranks or 'J' in player_ranks:
            choosen_card = self.choose_card(player_index)
            print(choosen_card)
            if choosen_card.rank != '7' and choosen_card.rank != 'J':
                print(f'You can only place 7s card or J over 7s card! You are taking {amount_of_7} cards!!! Have a nice day')
                for _ in range(amount_of_7 * 2):
                    player.deck.append(self.deck.pop_card())
                print('Now your cards are:')
                self.show_player_cards(player_index)
                took_seven = True
                self.check_mau(player_index)
                self.confirm_next_turn()
                self.next_turn(player_index, took_seven)
            elif choosen_card.rank == '7':
                self.played_cards.append(choosen_card)
                self.check_mau(player_index)
                if self.confirm_next_turn() == True:
                    took_seven = False
                    self.next_turn(player_index, took_seven)
            elif choosen_card.rank == 'J':
                self.played_cards.append(choosen_card)
                self.check_mau(player_index)
                requested_suite = self.ask_suite()
                if self.confirm_next_turn() == True:
                    took_seven = False
                    self.next_turn(player_index, took_seven, requested_suite=requested_suite)
                
                
                
                
    
    def make_turn(self, player_index, took_seven, requested_suite=None, take_eight=False):
        player = self.players[player_index]
        last_played_card = self.played_cards[-1]
        print(f'Turn is by player {player}')
        self.count_5()
        self.show_player_cards(player_index)
        self.show_mau_players()
        self.show_last_card()
        if last_played_card.rank == 'J':
            self.junior_scenario(player_index, requested_suite)
        elif last_played_card.rank == "8" and take_eight == False:
            self.eight_scenario(player_index)
        elif last_played_card.rank == '8' and take_eight == True:
            self.regular_scenario(player_index)
        elif last_played_card.rank == '7' and took_seven == False:
            self.seven_scenario(player_index)
        elif last_played_card.rank =='7' or last_played_card.rank != '7' and took_seven == True:
            if last_played_card.rank =='7':
                print('pss.. you do not need to put 7 or J, previous player had a nice day...')
            self.regular_scenario(player_index)
        
        
    

table = Table()



print(greetings)

table.show_menu()






