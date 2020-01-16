import random

obešenec=['''
                 _____
                |     |
                      |
                      |
                      |
                     _|_''', '''
                 _____
                |     |
                _     |
               (_)    |
                      |
                      |
                     _|_''', '''
                 _____
                |     |
                |     |
                _     |
               (_)    |
                |     |
                |     |
                     _|_''', '''
                 _____
                |     |
                |     |
                _     |
               (_)    |
               /|     |
                |     |
                     _|_''', '''
                 _____
                |     |
                _     |
               (_)    |
               /|\    |
                |     |
                     _|_''', ''' 
                 _____
                |     |
                _     |
               (_)    |
               /|\    |
                |     |
               /     _|_''', '''
                 _____
                |     |
                _     |
               (_)    |
               /|\    |
                |     |
               / \   _|_''','''
       ******************************
       ******************************
       
                     _
                    (_)
                    \|/      
    !!!_ZMAGOVALEC_! | !_!ZMAGOVALEC!!!!_       
                     |    
                    / \ 
                                       
       ******************************** 
       ******************************** ''']

looper=1
while looper==1:
    word_list="OTORINLARINGOLOG".split()    #V POVEDI SE PIŠE VSE SKUPAJ
    guessed_letters=[]


    def get_word():
        the_word=random.choice(word_list)
        return the_word
        
    word=get_word()
    word=word.upper()
    prazno='-' * len(word)  
    napačno=-1   
    pravilno=[]
    
    def get_guess():
        
        print()
        guess=input("Ugani črko - ")
        guess=guess.upper()
        print() 
        if guess in guessed_letters:
            print(" " + guess + " Beseda je bila že izbrana, poskusi še enkrat")
            get_guess()
        elif len(guess)!=1:
            print(" Izberi eno črko naenkrat")
            get_guess()
        elif guess not in 'ABCČDEFGHIJKLMNOPQRSŠTUVWXYZŽ ':
            print(" Izberi samo črke")
            get_guess()
        else:
            guessed_letters.append(guess)
        return guess

    running=True
    while running==True: 
        pravilno=[]  
        for i in range(len(word)):
           if word[i] in guessed_letters:
                prazno=prazno[:i] + word[i] + prazno[i+1:]                
                pravilno.append(i)
   
        print("\n" * 7)
    
        if napačno < 5:
            print(obešenec[napačno+1])
        else:
            print(obešenec[napačno+1])
            print(" PORAZ")
            running=False
            
        if len(pravilno)==len(word):
            
            
            print(obešenec[7])
            running=False
      

        print(" " + prazno + "") 
        
        print(" ", end=' ')
     
        for i in range(len(guessed_letters)):
             print("", end='')
             print(guessed_letters[i], end='')
         
        guess=get_guess()   
        if not guess in word:
            napačno=napačno+1
              
