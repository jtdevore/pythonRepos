#! python3

correct = 21

running = True

while running:
    guess =int(input('What is the best hand in Black Jack?'))

    if guess ==correct: #guessed 21
        print ('Winner winner chicken dinner!')
        running=False
    
    elif guess <correct:  #Here if guessed < than 21
        print ('''You havn't won many hands of black jack have you?''')
    
    else:  #Only here if guessed >21
        print ('Sorry, but you are a fool')

else:
    print ('You must be a card shark!')
    
import time
time.sleep(2)  #Sets a 2 sec delay between program done

print ('Program Done')
