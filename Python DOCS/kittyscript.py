def cat(arg1):
    if int(arg1) in range(1,4):
        print ('You have ' + arg1 + ' cats!\nAre\'t kittehs teh best?')
    elif int(arg1) in range(5,11):
        print ('You have ' + arg1 +' cats! \nWow! That is alot of kitties!')
    elif int(arg1) > 10:
        print ('You have ' + arg1 +' cats!\nThats a bit too many kittehs')
    else:
        try:
            print ('Aww, no kittehs?\nThat is a shame')
        except ValueError:
            print ('You need to select a number')
            
        

def ask():
    again = input('Do you want me to ask you again?/nAnswer y or n')
    while again == 'y':
        answer = input('how many cats do you have?')
        cat(answer)
    else:
        print ('Ok cats you later')

answer = input('how many cats do you have?')
cat(answer)    
ask()
