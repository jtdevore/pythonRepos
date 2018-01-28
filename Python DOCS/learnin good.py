correct = 21

running = True

while running:
    guess = (input('What is the best hand in Black Jack?'))

    if guess in ('21', 'twenty one', 'ace and king','ace and face card','ace and queen','ace and jack','ace and ten', 'ace and 10'): #guessed 21
        print ('Winner winner chicken dinner!')
        running=False
    
    elif guess in ('0', '1', '2', '3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty'):  #Here if guessed < than 21
        print ('''You havn't won many hands of black jack have you?''')

    elif guess in ('joker'): #hidden guess
        print ('The correct answer is any variation of 21')
   
    elif guess in ('dealer'): #hidden guess
        print ('Tip me good and I will stack the deck in your favor')
    
    else:  #if guessed anything other than numbers up to 21
        print ('Sorry, but you do know blackjack only has number and face cards right?')
        print ('Perhaps a game of go fish is more your speed')

else:
    print ('You must be a card shark!')



print ('Good, well at least now you know how the game works')
import time
time.sleep(2)

running = True

while running:
    gameon = (input('Are you ready to play a game of blackjack?'))

    if gameon in ('yes'): #user wants to play
        print ('Let us begin')
        print ('Draw a card')
        running=False
        
    elif gameon in ('no'):  #user doesnt want to play
        print ('''Fine then, I didn't want to play anyways''')

    else:
        print ('''You need to say either yes or no, I don't speak idiot.''')
    
import random
import os

deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4
def deal(deck):
    hand =[]
    for i in range (2):
        random.shuffle(deck)
        card=deck.pop()
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "k"
        if card == 14:card = "A"
        hand.append(card)
        
    return hand

def play_again():
    again = raw_input("Do you want to play again? (Y/N) : ").lower()
    if again == "y":
	    dealer_hand = []
	    player_hand = []
	    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
	    game()
    else:
	    print ("Bye!")
	    exit()
	    
def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total+= 10
        elif card == "A":
            if total >= 11: total+= 1
            else: total+= 11
        else:total += card
    return total

def hit (hand):
    card=deck.pop()
    if card == 11:card = "J"
    if card == 12:card = "Q"
    if card == 13:card = "K"
    if card == 14:card = "A"
    hand.append(card)
    return hand

def clear ():
    if os.name == 'nt':
        os.system("CLS")
    if os.name=='posix':
        os.system("clear")

def print_results(dealer_hand, player_hand):
    clear()
    print ('The dealer has a ') + str(dealer_hand) + ("for a total of ") + str(total(dealer_hand))
    print ('you have a ') + str(player_hand) + ("for a total of ") + str(total(player_hand))

def blackjack(dealer_hand, player_hand):
    if total(player_hand) == 21:
        print_results (dealer_hand, player_hand)
        print ("Congrats! You got a Blackjack!\n")
        play_again()
    elif total(dealer_hand) == 21:
        print_results (dealer_hand, player_hand)
        print ('Tough luck, dealer got Blackjack.\n')
        play_again()
                                
def score(dealer_hand, player_hand):
    if total(player_hand) == 21:
            print_results(dealer_hand, player_hand)
            print ("Congratulations! You got a Blackjack!\n")
	
    elif total(dealer_hand) == 21:
            print_results(dealer_hand, player_hand)		
            print ("Sorry, you lose. The dealer got a blackjack.\n")
	
    elif total(player_hand) > 21:
            print_results(dealer_hand, player_hand)
            print ("Sorry. You busted. You lose.\n")
	
    elif total(dealer_hand) > 21:
            print_results(dealer_hand, player_hand)			   
            print ("Dealer busts. You win!\n")
	
    elif total(player_hand) < total(dealer_hand):
            print_results(dealer_hand, player_hand)
            print ("Sorry. Your score isn't higher than the dealer. You lose.\n")
   	
    elif total(player_hand) > total(dealer_hand):
            print_results(dealer_hand, player_hand)			   
            print ("Congratulations. Your score is higher than the dealer. You win\n")

                        
def game():
    choice = 0
    clear()
    print ("Here we go!\n")
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    while choice != "q":
        print ("The dealer is showing a " + str(dealer_hand)
        print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))   
		blackjack(dealer_hand, player_hand)
		choice = raw_input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
		clear()
		if choice == "h":
			hit(player_hand)
			while total(dealer_hand) < 17:
				hit(dealer_hand)
			score(dealer_hand, player_hand)
			play_again()
		elif choice == "s":
			while total(dealer_hand) < 17:
				hit(dealer_hand)
			score(dealer_hand, player_hand)
			play_again()
		elif choice == "q":
			print ("Bye!")
			exit()
	
if __name__ == "__main__":
   game()
   
import time
    
time.sleep(2)  #Sets a 2 sec delay between program done

print ('Program Done')
