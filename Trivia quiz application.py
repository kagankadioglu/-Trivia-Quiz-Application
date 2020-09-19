mainmenudict={1:"- Set prize for the next competition.",2:"- Display questions for the next competition.",3:"- Add new question to the next competition",4:"- Delete a question from the next competition.",5:"- See users data.",6:"- Log out."}
kisiler={'abbas':[5.4,5557],'betul':[3.2,5466],'omer':[6.4,551]}
odul=10000
q = {1:['What color are Zebras?',[{'White with black stripes:':'True','Black with white stripes':'False','Black with red stripes':'False'}]],2:['Where was the old Campus of Sehir University?',[{'Levent:':'False','Altunizade':'True','Maltepe':'False'}]],3:['What is the capital of Turkey?',[{'Ankara:':'True','Istanbul':'False','Konya':'False'}]] }
def welcome():
    print('--- Welcome to Sehir Hadi:) - --')
    while True:
        global giris
        giris = raw_input('Please type your phone number in order to sign in:\n')
        for i in kisiler:
            if giris == str(kisiler[i][1]):                                                       # checking number in database or not
                print 'Checking' + ' ' + giris
                print 'welcome' + ' ' + i
                print 'Competition will start soon.. be ready :)'
                global currentp
                currentp=str(i)
                yarisma()                                                                         # if in going to game
        if giris == '**':
             mainmenu()                                                                           # going to admin menu
        else:
            print giris + ' ' + 'is not a valid phone number, please try again!'
def yarisma():
    import random
    players = []
    for i in kisiler:
        players.append(i)
    qn=1
    if qn in q:
        for i in q:
            print 'Total Players: ' + str(len(players)) + str(' *************************')
            print '---' + 'Q' + str(i) + ': ' + str(q[qn][0]) + '---'
            sum = 1
            qn+=1
            for v in (q[i][1]):                                                  # display key and and value of question one by one...
                for key, value in v.items():
                    print '   Ans ' + str(sum) + '- ' + str(key)
                    mm=(v.values())
                    mm2=mm.index('True')
                    mm2+=1
                    sum += 1
            cevap=raw_input('Your answer')
            if cevap == str(mm2):                                                  # checking input index true or false(answer true or false)
                print 'True'
                sum=1
                for v in (q[i][1]):
                    for key, value in v.items():
                        print '   Ans ' + str(sum) + '- ' + str(key) + str(value)
                        sum+=1
                def background(rasgele):
                    playerss = random.randint(1, 3)
                    if str(playerss) != str(mm2):
                        del kisiler[rasgele]                                         # choose random value and apply to list I prefered map module for apply for all list and delete person who cannot know true answer
                        players.remove(rasgele)
                map(background, players)
            else:
                print 'Incorrect!'
                sum = 1
                for v in (q[i][1]):
                    for key, value in v.items():
                        print '   Ans ' + str(sum) + '- ' + str(key) + str(value)
                        sum+=1
                players.remove(currentp)                                             # remove from list and dictinary becasue it sellect wrong answer
                del kisiler[currentp]
                def background(rasgele):
                    playerss = random.randint(1, 3)
                    if str(playerss) != str(mm2):
                        del kisiler[rasgele]
                        players.remove(rasgele)                                     # choose random value and apply to list I prefered map module for apply for all list and delete person who cannot know true answer
                map(background, players)
                break

    import math
    print '--' + 'Total winners' + ' ' + str(len(players))
    print '--' + 'Total distributed prize:' ' ' + str(odul)
    bolum= odul/len(players)                                                                      # odulu kisi sayisina bolmek icin
    for k in kisiler:
       print k + ' ' + '-->'+ str((kisiler[k][0])) + ' ' + 'Current Balance:' + ' ' + str((float((kisiler[k][0]))+float(bolum)))    # add prize people who answer all question true
    welcome()
def mainmenu():
    print "Please choose one of the following services:"
    for key in mainmenudict:
        print "\t"+str(key)+".",mainmenudict[key]                                                    # displaying to admin menu. wait for input from people
    while True:
        choice = int(raw_input("Your Choice: "))
        if choice == 1:
            return choice1()
        if choice == 2:
            return choice2()
        if choice == 3:
            return uc()
        if choice == 4:
            return Choice4()
        if choice == 5:
            return Choice5()
        if choice == 6:
            welcome()
        else:
            print "Please choose a valid menu number!"
def choice1():
    global odul
    odul = raw_input('Please type the total prize of the next competition:')                # change to prize from default value
    print 'Setting prize...'
    print 'Going back to Admin Menu...'
    print ''
    mainmenu()
def choice2():
    for i in q:
        print '---' + 'Q' + str(i) + ': ' + str(q[i][0]) + '---'
        sum = 1
        for v in (q[i][1]):
            for key,value in v.items():                                                     # for value and displaying list in dictinary
                print '   Ans ' + str(sum) + '- ' + str(key) + '>>>>>' + str(value)         # displaying key and value of question
                sum+=1
    mainmenu()
def uc():
    def secimler():
        newq = raw_input('Please type the question:')                                     # take input from user for create new question
        newt = raw_input('Please type the CORRECT answer:')
        newf1 = raw_input('Please type an incorrect answer:')
        newf2 = raw_input('Please type an incorrect answer:')
        mx=[]
        for i in q:
            mx.append(int(i))                                                              # return question number
        q[max(mx)+1]= [newq,[{newt:'True'},{newf1:'False'},{newf2:'False'}] ]              # max function for add plus one question number...  set dictionary True and false value
        mainmenu()
    secimler()
def Choice4():
    for i in q:
        print 'Q' + str(i) + '. ' + str(q[i][0])
    delete = raw_input('Please type the number of the question to be deleted:')
    q.pop(int(delete))                                                                    # delete spesific key
    print 'Q' + delete + ' ' 'has been deleted successfully!!'
    print ' '
    mainmenu()
def Choice5():
    print 'Displaying user Data'
    for i in kisiler:
        print i + ', ' + 'Balance ' + str(kisiler[i][0]) + ', ' +'Number ' + str(kisiler[i][1])           # for cycle for display all data in dictinary
    print ''
    print 'Going back to the Admin menu..'
    mainmenu()
welcome()