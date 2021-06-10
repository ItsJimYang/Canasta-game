import random
import pickle

def setup():
    font = loadFont("Marion-Bold-48.vlw")
    textFont(font)
    size(1000, 700)
    global currentInterface
    currentInterface = 0
    global keyInput
    keyInput = ""
    global InterfaceList
    InterfaceList = [MenuScreen, WelcomeScreen, HelpScreen, quitScreen, GameRuleScreen, HowToPlayScreen, HighScoreScreen, PauseScreen, QuickHelpScreen, CanastaGame, EndScreen]
    # global buttonLink
    # buttonLink = [[goBackButton], [playButton], [helpButton], [quitButton, quitInGameButton], [gameRuleButton], [howToPlayButton], [highScoreButton], [pauseButton, toPauseButton], [quickHelpButton], [resumeInGameButton]]
    global allCardImage
    allCardImage = loadImage("Cards.jpg")
    global arrowPointer
    arrowPointer = loadImage("Arrow Pointer.svg")
    global allImg
    allImg = loadImageFile("Images.txt")
    global playerInputList, currentInputBox
    global allButton, allButtonLink
    allButton = loadButtonFile("Buttons.txt")
    print(allButton)
    allButtonLink = loadButtonLink("Button Link.txt")
    print(allButtonLink)
    print(allButtonLink[7][0][0])
    playerInputList = allButton[1]
    # for c in playerInputList:
    #     c[8] = True
    # playerInputList = [studentNumberEnterField1, studentFirstNameEnterField1, studentLastNameEnterField1, studentNumberEnterField2, studentFirstNameEnterField2, studentLastNameEnterField2, studentNumberEnterField3, studentFirstNameEnterField3,studentLastNameEnterField3,studentNumberEnterField4,studentFirstNameEnterField4,studentLastNameEnterField4]
    currentInputBox = 0
    global currentPlayerIndex
    currentPlayerIndex = 0
    global cardSelected
    cardSelected = []
    global playerinfodic
    playerinfodic = readingdic()
    global datelist
    datelist = [0,0,0]
    datelist[0] = day() 
    datelist[1] = month()   
    datelist[2] = year()
    global studentNum
    studentNum = ""
    global names
    names = ""
    global inout
    inout = False
    global displaything
    displaything = ["","","","","","","",""]
    global displaynum
    displaynum = 0
    global highscorelist
    highscorelist = [["",0,""],["",0,""],["",0,""],["",0,""],["",0,""]]
    global inputedkey
    inputedkey = ""
    global possiblekey
    possiblekey = "1234567890qwertyuiopasdfghjklzxcvbnm "
    global mclicked
    mclicked = False
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def loadButtonFile(fileName):
    fileList = []
    file = open(fileName)
    for line in file:
        tempList = line.strip("\n").split("/")    
        for i in range(len(tempList)):
            tempList[i] = tempList[i].split(",")
            for j in range(1,8):
                tempList[i][j] = int(tempList[i][j])
            tempList[i].append(False)
            # if fileName != "Button Link.txt":
            #     tempList[i].append(False)
            # else:
            #     tempList[i].append(True)
        fileList.append(tempList)
    file.close()
    return fileList

def loadButtonLink(fileName):
    fileList = []
    file = open(fileName)
    for line in file:
        tempList = line.strip("\n").split("/")    
        for i in range(len(tempList)):
            tempList[i] = tempList[i].split(",")
            for j in range(1,8):
                tempList[i][j] = int(tempList[i][j])
            tempList[i].append(False)
            # if fileName != "Button Link.txt":
            #     tempList[i].append(False)
            # else:
            #     tempList[i].append(True)
        fileList.append(tempList)
    file.close()
    return fileList
# loadImageFile(): load image info from a text file into a list
def loadImageFile(fileName):
    fileList = []
    file = open(fileName)
    for line in file:
        tempList = line.strip("\n").split("/")    
        for i in range(len(tempList)):
            tempList[i] = tempList[i].split(",")
            for j in range(1,5):
                tempList[i][j] = int(tempList[i][j])
        fileList.append(tempList)
    file.close()
    return fileList

#loadTextFile(): load image info from a text file into a list
def loadTextFile(fileName):
    fileList = []
    file = open(fileName)
    for line in file:
        tempList = line.strip("\n").split(",")
        for i in range(1, 5):
            tempList[i] = int(tempList[i])
        fileList.append(tempList)
    file.close()
    return fileList

#createPlayerInfoList(): loads the information of the players into a list
def createPlayerInfoList(targetList):
    allInfo = []
    print(targetList)
    for i in range(0, 12, 3):
        # nameList = targetList[i][0].encode('ascii').split(" ")
        # nameList.insert(0, targetList[i-1][0].encode('ascii'))
        nameList = [targetList[i][0].encode('ascii'), targetList[i+1][0].encode('ascii'), targetList[i+2][0].encode('ascii')]
        allInfo.append(nameList)
    return allInfo

#addCardToSelectedList(): adding the selected card into the list of selected cards
def addCardToSelectedList(currentPlayer):
    selectedList = []
    for c in currentPlayer.cardsInHand:
        if c[4]:
            selectedList.append(c)
        if c[4] == False and c in selectedList:
            selectList.remove(c)
    return selectedList

#buildButton(): create the button boxes
def buildButton(buttonInfo):
    if buttonInfo[7] != 255:
        stroke(buttonInfo[7])
        strokeWeight(2)
        rect(buttonInfo[1], buttonInfo[2], buttonInfo[3], buttonInfo[4]) 
        noStroke()
    fill(buttonInfo[5])
    textSize(buttonInfo[6])
    text(buttonInfo[0], buttonInfo[1] + buttonInfo[3]/2 - textWidth(buttonInfo[0])/2 , (buttonInfo[2] + buttonInfo[2] + buttonInfo[4])/2 + buttonInfo[6] / 2)
    noFill()
#=====================================================
# checks if the mouse is over the button
# Receives the information of the button(in a list)
# returns true if the mouse is hoovering over the button
def mouseOverButton(buttonList):
    if buttonList[8] and mouseX >= buttonList[1] and mouseX <= buttonList[1] + buttonList[3] and mouseY >= buttonList[2] and mouseY <= buttonList[2] + buttonList[4]:
        return True
    
def readinput(keyin):
    global currentInterface
    global keyInput 
    global currentInputBox
    global playerInputList
    global allPlayerInfo
    global playerinfodic
    global displaything
    global displaynum
    global studentNum
    global names
    global inout
    global inputedkey

    if currentInputBox % 3 != 0:
        if keyin in "abcdefghijklmnopqrstuvwxyz " and len(keyInput) <= 10:
            keyInput += keyin
            names += keyin
            WelcomeScreen.buttonList[currentInputBox][0] = keyInput.upper()
        if keyin == "BACKSPACE" and len(keyInput) > 0:
            keyInput = keyInput[:-1]
            names += names[:-1]
            WelcomeScreen.buttonList[currentInputBox][0] = keyInput.upper()      
        if keyin == "ENTER" and currentInputBox % 3 == 1:
            currentInputBox += 1
            keyInput = ""  
        if keyin == "ENTER" and len(keyInput) > 0 and currentInputBox % 3 == 2:
            currentInputBox += 1
            inout = inlist(studentNum, playerinfodic)
            date = str(datelist[0]) + "/" + str(datelist[1]) + "/" + str(datelist[2])
            if inout == True:
                displaything[displaynum] = str(playerinfodic[studentNum][0][1])
                displaything[displaynum+1] = str(playerinfodic[studentNum][0][2])
                playerinfodic[studentNum][0][2] = date
            if inout == False:
                displaything[displaynum] = "0"
                displaything[displaynum+1] = "DNE"
                playerinfodic[studentNum] = []
                playerinfodic[studentNum].append([names, 0, date])
                keyInput = ""
                studentNum = ""
                names = ""
                displaynum += 2
                inout = False
    else:
        if keyin in "1234567890" and len(keyInput) < 6:
            keyInput += keyin
            print(keyInput)
            studentNum += keyin        
            WelcomeScreen.buttonList[currentInputBox][0] = keyInput.encode('ascii')
        if keyin == "BACKSPACE" and len(keyInput) > 0:
            keyInput = keyInput[:-1]
            studentNum = names[:-1]
            WelcomeScreen.buttonList[currentInputBox][0] = keyInput
        if keyin == "ENTER":
            if len(keyInput) == 6:
                currentInputBox += 1
                keyInput = ""
            else:
                print("You must enter 6-digit student number to continue")  
                
    if keyin == "ENTER" and all(c[0] != "" for c in WelcomeScreen.buttonList) :
        print("all inputs are complete")
        print("all player info ready")
        InterfaceList[currentInterface].turnOffButton()
        Canasta.loadPlayerInfo()
        Canasta.prepGame()
        currentInterface = 9
    inputedkey = ""

def mousefunctions():
    global currentInterface
    global keyInput
    global playerInputList, currentInpsutBox
    global cardSelected
    global numCardSelected
    global activePlayer
    global currentPlayerIndex
    global mouseOverCardIndex
    global allButtonLink
    print(allButtonLink)
    for c in allButtonLink:
        for i in c:
            if mouseOverButton(i) and i[8] == True:
                print(allButtonLink.index(c))
                if allButtonLink.index(c) == 3: 
                    exit()
                    print("Game Ended")
                if allButtonLink.index(c) == 0:
                    keyInput = ""
                InterfaceList[currentInterface].turnOffButton()
                currentInterface = allButtonLink.index(c)
                
    for c in WelcomeScreen.buttonList:
        if mouseOverButton(c):
            currentInputBox = WelcomeScreen.buttonList.index(c)
            
    if currentInterface == 9:
        cardSelected = addCardToSelectedList(activePlayer)
        numCardSelected = len(cardSelected) 
       
        if mouseOverCardIndex != -1:
            Canasta.updateCard(activePlayer)
            Canasta.updateCardLocation(activePlayer)
            
        leng = len(CanastaGame.buttonList)
        for i in range (leng):
            if mouseOverButton(CanastaGame.buttonList[i]):
                if i == 0:
                    activePlayer.addCardToMeld()
                if i == 1:
                    activePlayer.createMeld()
                if i == 2:
                    activePlayer.goingout()
                    #activePlayer.scoreonscreen = activePlayer.checkscore()
                if i == 3:
                    activePlayer.discardCard()
                    activePlayer.drawfrompile = False
                if i == 4 and activePlayer.drawfrompile == False:
                    print("Getting card from the deck")
                    activePlayer.getCard(Canasta.cardPile.cards)
                    activePlayer.drawfrompile = True
                if i == 5 and activePlayer.drawfrompile == False:
                    print("Getting card from the dicard pile")
                    activePlayer.getCardFromDis(Canasta.discardPile.cards)
                    activePlayer.drawfrompile = True        
#=======================================================

#readingdic(): reads a dictionary from a file and returns it
def readingdic():
    with open('report.txt', 'rb') as handle:
        dictionary = pickle.loads(handle.read())
    return dictionary

#dumpingdic(dict): dumps the dictionary into a file
def dumpingdic(dict):
    f = open("report.txt","wb")
    pickle.dump(dict,f)
    f.close()
    
# find the top 5 players from all the players
def topfive (playerdictionary, highscorelist):
    for i in playerdictionary:
        for j in range (len(highscorelist)):
            if playerdictionary[i][0][1] > highscorelist[j][1] and i != highscorelist[0][2] and i != highscorelist[1][2] and i != highscorelist[2][2] and i != highscorelist[3][2] and i != highscorelist[4][2]:
                highscorelist.insert(j,[playerdictionary[i][0][0],playerdictionary[i][0][1],i])
                highscorelist.pop(5)
                break
    return highscorelist

#checks if the player is new
def inlist (studentNum, playerdictionary):
    for i in playerdictionary:
        if i == studentNum:
            return True
    return False
        
# displays scores and dates of each player onto the screen
def displayscore():
    a = 0
    for i in range (0, len(displaything), 2):
        textSize(25)
        fill(255)
        text(displaything[i], 800, 280 + a * 100)
        text(displaything[i+1], 900, 280 + a * 100)
        a += 1
        
        
        
        
        
        
        
        

def ablebuttonlink(starting, ending):
    global allButtonLink
    
    for i in range (starting,ending+1, 1):
        allButtonLink[i][0][8] = True
        
        
        
        
        
        
        
        
        
        
        
        
    
#------------------------------------------------------------------------------------------------
class Card:
    def __init__(self, value, suit):
        self.value = int(value)
        self.suit = int(suit)
        self.x = 172
        self.y = 600
        self.isSelected = False

#------------------------------------------------------------------------------------------------
class Deck:
    def __init__(self):
        self.cards = []

    #building a card deck
    def buildDeck(self):
        for s in range(4):
            for v in range(13):
                self.cards.append([v, s, 172, 600, False])
    #shuffling the cards in the deck
    def shuffle(self):
        random.shuffle(self.cards)
    # deal a card and pop the card from the deck
    def dealCard(self):
        return self.cards.pop(0)

#------------------------------------------------------------------------------------------------            
class Player:
    def __init__(self, studentNumber, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.studentNumber = studentNumber
        self.scoreonscreen = 0
        self.cardsInHand = []
        self.meld = []
        self.drawfrompile = False
        self.discard = False
        self.takecard = False
        self.score = [[[7,8,9,10,11,12],10], [[3,4,5,6],5],[[2],5], [[0],20], [[1],20]]

    # takes in an additional list as the reference from which the player will be taking card from    
    def getCard(self, targetPile):
        if len(targetPile) == 0:
            print("You can't take cards from an empty deck")
            return 0
        print("Taking card from the pile")
        lista = []
        lista.append(targetPile.pop())
        self.cardsInHand = insertcard(lista,self.cardsInHand)

    #checking if a player can get cards from the discard pile and getting the cards from the discard pile if valid
    def getCardFromDis(self, targetPile):
        samenum = 0
        if len(targetPile) == 0:
            print("You can't take cards from an empty deck")
            return 0
        print("Taking card from the discard")
        if len(self.meld) >= 1:
            for i in range(len(self.meld)):
                if self.meld[i][0][0] == targetPile[0][0]:
                    self.takecard = True
        for j in range (len(self.cardsInHand)):
            if self.cardsInHand[j][0] == targetPile[0][0]:
                samenum += 1
        if samenum >= 2:
            self.takecard = True
        if self.takecard == True:
            self.cardsInHand = insertcard(targetPile,self.cardsInHand)
            for x in range (len(targetPile)-1, -1, -1):
                targetPile.pop(x)
            # lengthpile = len(targetPile)-1
            # for i in range(lengthpile, -1, -1):
            #     self.cardsInHand.append(targetPile[i])
            #     targetPile.pop(i)    
        if self.takecard == False:
            print("you can't take the cards from this pile")
        self.takecard = False
    #check if a meld can be created and creating a meld if it's valid            
    def createMeld(self):
        global currentPlayerIndex
        numCardSelected = len(cardSelected) 
        if  numCardSelected != 0:
            cardvalue = cardSelected[0][0]
        isSameCards = True
        # isSameCards = all(c[0] == cardSelected[0][0] for c in cardSelected)
        for i in range (numCardSelected):
            if cardSelected[i][0] != cardvalue:
                isSameCards = False
        if isSameCards and numCardSelected >= 3:
            self.meld.append(cardSelected)
            print("The cards have been added to the meld of the player")
            print("Created new meld with card " + str(cardSelected[0][0] + 1))
            print("The card has been added to your melds, your meld now has " + str(len(cardSelected)) + " cards")
            
            for c in cardSelected:
                self.cardsInHand.remove(c)
            if currentPlayerIndex == 0 or currentPlayerIndex == 1:
                Canasta.playerList[currentPlayerIndex + 2].meld.append(cardSelected)
            else:
                Canasta.playerList[currentPlayerIndex - 2].meld.append(cardSelected)
        else:
            print("You can only create a meld with three or more cards that share the same value")
    #checks if the player can go out            
    def goingout(self):
        global currentInterface
        canasta = False
        for i in self.meld:
            if len(i) >= 7:
                canasta = True
        if len(self.cardsInHand) == 1 and canasta == True:
            for j in self.meld:
                if j[0][0] == self.value:
                    self.addCardToMeld
                    return 
            self.discardCard
            self.scoreonscreen += 200
            currentInterface = 10
            
        else:
            print("can't go out")
    #checks if a card can be added to the meld and adding the card if it's valid            
    def addCardToMeld(self):
        global currentPlayerIndex
        isSameCards = all(c[0] == cardSelected[0][0] for c in cardSelected)
        if isSameCards and numCardSelected != 0:
            for sublist in self.meld:
                if cardSelected[0][0] == sublist[0][0]:
                    for c in cardSelected:
                        sublist.append(c)
                        self.cardsInHand.remove(c)
                    print("The card has been added to your melds, your meld now has " + str(len(sublist)) + " cards")
                else:
                    print("You don't have any melds with the selected cards")
        if currentPlayerIndex == 0 and currentPlayerIndex == 1:
            Canasta.playerlist[currentPlayerIndex + 2].meld = self.meld
        if currentPlayerIndex == 2 and currentPlayerIndex == 3:
            Canasta.playerlist[currentPlayerIndex - 2].meld = self.meld
        else:
            print("You have to select the same cards to add them to a meld")
    #checks if the player can discard a card and discard the card if it's valid                
    def discardCard(self):  
        global currentPlayerIndex
        if len(cardSelected) == 1  and len(self.cardsInHand) != 1:
            Canasta.discardPile.cards.insert(0, cardSelected[0])
            self.cardsInHand.remove(cardSelected[0])
            if currentPlayerIndex != 3:
                currentPlayerIndex += 1
            else:
                currentPlayerIndex = 0
            
        else:
            print("You can only discard one card at a time")
    #returns the scores for each player
    def checkscore(self):
        score = 0
        for i in self.meld:
            if len(i) < 7:
                for x in self.score:
                    for j in x[0]:
                        if i[0][0] == j and i[0][0] != 2:
                            score += x[1]
                        elif i[0][0] == 2 and (i[0][1] == 0 or i[0][1] == 1):
                            score += 5
            elif len(i) == 7:
                natural = True
                first = i[0]
                for j in i:
                    if j[0] != first[0]:
                        natural = False
                if natural:
                    score += 500
                else:
                    score += 300
        for i in self.cardsInHand:
            if i[0] == 2 and (i[1] == 2 or i[1] == 3):
                score += 200
            for x in self.score:
                for j in x[0]:
                    if i[0] == j and i[0] != 2:
                        score -= x[1]
        return score
#------------------------------------------------------------------------------------------------
class Game:
    def __init__(self):
        self.playerList = []
        self.cardPile = Deck()
        self.discardPile = Deck()
    #buiding the decks for the players
            
    def prepGame(self):
        self.cardPile.buildDeck()
        self.cardPile.buildDeck()
        self.cardPile.shuffle()
        for c in self.playerList:
            for i in range(13):
                c.cardsInHand.append(self.cardPile.dealCard())
            c.cardsInHand = sortcard(c.cardsInHand)
        # Sort player cards

        
    #load player's information     
    def loadPlayerInfo(self):
        allPlayerInfo = createPlayerInfoList(WelcomeScreen.buttonList)
        print("This is the info of the four players")
        print(allPlayerInfo)
        print(playerInputList)
        
        for subList in allPlayerInfo:
            self.playerList.append(Player(subList[0], subList[1], subList[2]))
    # update the card that the player chose            
    #================================================    
    def updateCard(self, currentPlayer):
        currentPlayer.cardsInHand[mouseOverCardIndex][4] = not(currentPlayer.cardsInHand[mouseOverCardIndex][4])       
           
    #==================================================
    # update the location of the card if the card is selected or deselected       
    def updateCardLocation(self, currentPlayer):
        if currentPlayer.cardsInHand[mouseOverCardIndex][4]:
            currentPlayer.cardsInHand[mouseOverCardIndex][3] -= 30
        else:
            currentPlayer.cardsInHand[mouseOverCardIndex][3] = 600

# playButton = ["PLAY", 150, 250, 200, 50, 255, 48, 255, False]
# helpButton = ["HELP", 150, 350, 200, 50, 255, 48, 255, False]
# highScoreButton = ["HIGH SCORE", 150, 450, 200, 50, 255, 48, 255, False]
# quitButton = ["QUIT", 150, 550, 200, 50, 255, 48, 255, False]

# goBackButton = ["GO BACK", 875, 0, 100, 50, 255, 24, 255, False]
# gameRuleButton = ["GAME RULE", 200, 200, 200, 50, 255, 30, 255, False]
# howToPlayButton = ["HOW TO PLAY", 650, 200, 200, 50, 255, 30, 255, False]

# pauseButton = ["", 1230, 0, 50, 50, 255, 30, 255, False]

# resumeInGameButton = ["RESUME", 540, 250, 200, 50, 0, 30, 255, False]
# quickHelpButton = ["QUICK HELP", 550, 350, 200, 50, 0, 30, 255, False]
# quitInGameButton = ["QUIT", 550, 450, 200, 50, 0, 30, 255, False]
# toPauseButton = ["TO PAUSE", 1150, 0, 100, 50, 255, 25, 255, False]

# studentNumberEnterField1 = ["", 50, 250, 125, 50, 255, 25, 254, False]
# studentFirstNameEnterField1 = ["", 250, 250, 200, 50, 255, 25, 254, False]
# studentLastNameEnterField1 = ["", 500, 250, 200, 50, 255, 25, 254, False] 
# studentNumberEnterField2 = ["", 50, 350, 125, 50, 255, 25, 254, False]
# studentFirstNameEnterField2 = ["", 250, 350, 200, 50, 255, 25, 254, False]
# studentLastNameEnterField2 = ["", 500, 350, 200, 50, 255, 25, 254, False] 
# studentNumberEnterField3 = ["", 50, 450, 125, 50, 255, 25, 254, False]
# studentFirstNameEnterField3 = ["", 250, 450, 200, 50, 255, 25, 254, False]
# studentLastNameEnterField3 = ["", 500, 450, 200, 50, 255, 25, 254, False] 
# studentNumberEnterField4 = ["", 50, 550, 125, 50, 255, 25, 254, False]
# studentFirstNameEnterField4 = ["", 250, 550, 200, 50, 255, 25, 254, False]
# studentLastNameEnterField4 = ["", 500, 550, 200, 50, 255, 25, 254, False] 

# addToMeldButton = ["ADD TO MELD", 172, 520, 190, 50, 0, 25, 255, False]
# createMeldButton = ["CREATE MELD", 500, 520, 200, 50, 0, 25, 255, False]
# goOutButton = ["GO OUT", 820, 520, 110, 50, 0, 25, 255, False]
# discardButton = ["DISCARD", 1000, 520, 130, 50, 0, 25, 255, False]
# getCardFromDeckButton = ["", 553, 300, 72, 96, 0, 25, 255, False]
# getCardFromDiscardButtton = ["", 655, 300, 72, 96, 0, 25, 0, False]

#-------------------------------------------------------------------------------------------------

class Interface:
    
    def __init__(self, imageList, textList, buttonList):
        self.imageList = imageList
        self.textList = textList
        self.buttonList = buttonList
    # display the image onto the screen
    def displayImage(self):
        for c in self.imageList:
            eachImg = loadImage(c[0])
            image(eachImg, c[1], c[2], c[3], c[4])
    #display the buttons onto the screen
    def displayButton(self):
        for c in self.buttonList:
            buildButton(c)
            c[8] = True
    #displace the texts onto the screen        
    def displayText(self):
        leng = len(self.textList)
        for i in range(leng):
            fill(self.textList[i][3])
            textSize(self.textList[i][4])
            text(self.textList[i][0], self.textList[i][1], self.textList[i][2])
            noFill()
    #deactivate the buttons                
    def turnOffButton(self):
        for c in self.buttonList:
            c[8] = False
    
    def turnOnButton(self):
        for c in self.buttonList:
            c[8] = True
    
    #display the cards in the player's hand       
    # def displayCard(self, currentPlayer):
    #     global allCardImage
    #     leng = len(currentPlayer.cardsInHand)
    #     for i in range(leng):
    #         cardImage = allCardImage.get(73 * currentPlayer.cardsInHand[i][0], 99 * currentPlayer.cardsInHand[i][1], 72, 96)
    #         # card position start at (32, 0)
    #         image(cardImage, (width - 72 * leng)/2 + 36 * i, currentPlayer.cardsInHand[i][3], 72, 96)
            
    def displayCard(self, currentPlayerslist):
        global allCardImage
        global currentPlayerIndex

        for i in range (len(currentPlayerslist)-1, currentPlayerIndex, -1):
            leng = len(currentPlayerslist[i].cardsInHand)
            for j in range(leng):
                cardImage = allCardImage.get(73 * currentPlayerslist[i].cardsInHand[j][0], 99 * currentPlayerslist[i].cardsInHand[j][1], 72, 96)
                image(cardImage, (width - 72 * leng)/2 + 72 * j, currentPlayerslist[i].cardsInHand[j][3] - i * 30, 72, 96)  
        for i in range (0, currentPlayerIndex+1, +1):
            leng = len(currentPlayerslist[i].cardsInHand)
            for j in range(leng):
                cardImage = allCardImage.get(73 * currentPlayerslist[i].cardsInHand[j][0], 99 * currentPlayerslist[i].cardsInHand[j][1], 72, 96)
                image(cardImage, (width - 72 * leng)/2 + 72 * j, currentPlayerslist[i].cardsInHand[j][3] - (currentPlayerIndex - i) * 30, 72, 96)  
        
    #display the top card on the discard pile        
    def displayDiscardPile(self):
        if len(Canasta.discardPile.cards) != 0:
            discardPileCard = Canasta.discardPile.cards[0]
            discardPileImage = allCardImage.get(73 * discardPileCard[0], 99 * discardPileCard[1], 72, 96)
            image(discardPileImage, 630, 175, 72, 96)    
        else:
            stroke(0)
            strokeWeight(2)
            rect(630, 175, 72, 96)
    #display the meld already created onto the screen
    def displayMeld(self, currentPlayer):
        leng = len(currentPlayer.meld)
        if leng != 0:
            for i in range(leng):
                meldCard = currentPlayer.meld[i][0]
                meldCardImage = allCardImage.get(73 * meldCard[0], 99 * meldCard[1], 72, 96)
                image(meldCardImage, 170 + 90 * i, 320, 72, 96)
                numCardInMeld = len(currentPlayer.meld[i])
                textSize(20)
                fill(0)
                text(str(numCardInMeld), 205 + 90 * i, 315)
                noFill()
    #show any red three the player has on the screen                 
    def showRedThree(self, currentPlayer):
        for i in currentPlayer.cardsInHand:
            if (i[1] == 2 and i[0] == 2) or (i[1] == 3 and i[0] == 2):
                displayImage = allCardImage.get(73 * i[0], 99 * i[1], 72, 96)
                image(displayImage, 100, 100, 72, 96)   
    #checks if the player's mouse is over the card            
    def mouseOverCard(self, currentPlayer):
        leng = len(currentPlayer.cardsInHand)
        for c in currentPlayer.cardsInHand:
            if mouseX > (width - 72 * leng)/2 + 72 * currentPlayer.cardsInHand.index(c) and mouseX < (width - 72 * leng)/2 + 72 * (currentPlayer.cardsInHand.index(c)+1) and mouseY > c[3] and mouseY < c[3]+96:
                return currentPlayer.cardsInHand.index(c)  
        return -1
    #display the score for the player
    def displayScore(self, currentPlayer):
        textAlign(CENTER)
        textSize(25)
        fill(255)
        text(currentPlayer.firstName + " " + currentPlayer.lastName, 500, 100)
        text(str(currentPlayer.scoreonscreen), 500, 150) 
        textAlign(BASELINE)
        fill(0)
    # display the score for each player when the game is finished    
    def score(self):
        textSize(40)
        fill(0)
        text("Game Over", 520, 50)
        textSize(32)
        text("First name", 100, 200)
        text("Last name" , 550, 200)
        text("Scores", 950, 200)
        for i in range (4):
            text(Canasta.playerList[i].firstName, 100, 300 + 100*i)
        for i in range (4):
            text(Canasta.playerList[i].lastName, 550, 300 + 100*i)
        for i in range (4):
            text(Canasta.playerList[i].scoreonscreen, 950, 300 + 100*i)
#-------------------------------------------------------------------------------------------------------------------------------
WelcomeScreenText = loadTextFile("Welcome Screen Text.txt")
HelpScreenText = loadTextFile("Help Screen Text.txt")
GameRuleScreenText = loadTextFile("Game Rule Screen Text.txt")
GamePlayScreenText = loadTextFile("Game Play Screen Text.txt")
HighScoreScreenText = loadTextFile("High Score Screen Text.txt")
QuickHelpScreenText = loadTextFile("Quick Help Screen Text.txt")
global allImg
allImg = loadImageFile("Images.txt")
global allButton
global playerInputList
allButton = loadButtonFile("Buttons.txt")
playerInputList = allButton[1]
MenuScreen = Interface(allImg[0], [], allButton[0])
WelcomeScreen = Interface(allImg[1], WelcomeScreenText, playerInputList)
HelpScreen = Interface(allImg[2], HelpScreenText, allButton[3])
quitScreen = Interface([], [], [])
GameRuleScreen = Interface(allImg[2], GameRuleScreenText, allButton[2])
HowToPlayScreen = Interface(allImg[2], GamePlayScreenText, allButton[2]) 
HighScoreScreen = Interface(allImg[3], HighScoreScreenText, allButton[2])
PauseScreen = Interface(allImg[5], [], allButton[5])
QuickHelpScreen = Interface(allImg[2], QuickHelpScreenText, allButton[6])
EndScreen = Interface([], [], allButton[2]) 

CanastaGame = Interface(allImg[4], [], allButton[7])
Canasta = Game()

def draw():
    background(250)
    global playerInputList
    global keyInput
    global currentPlayerIndex
    global activePlayer
    global mouseOverCardIndex
    global currentInputBox
    global cardSelected
    global highscorelist
    global mclicked
    global inputedkey
    global allButton
    global allButtonLink
    InterfaceList[currentInterface].displayImage() 
    InterfaceList[currentInterface].displayText()
    InterfaceList[currentInterface].displayButton()
    
    # print(currentInterface)
    if currentInterface != 9 or currentInterface != 7:
        for i in range (10):
            allButtonLink[i][0][8] = False
    
    if currentInterface == 0:
        ablebuttonlink(1,3)
        allButtonLink[6][0][8] = True
        
    if currentInterface == 2 or currentInterface == 4 or currentInterface == 5 or currentInterface == 6:
        allButtonLink[0][0][8] = True
        #print(allButtonLink)
        
    if currentInterface == 2:
        allButtonLink[0][0][8] = True
        allButtonLink[4][0][8] = True
        allButtonLink[5][0][8] = True
    
    if currentInterface == 7:
        allButtonLink[9][0][8] = True
        allButtonLink[8][0][8] = True
    
    if mclicked  == True:
        mousefunctions()
        mclicked = False
    
    if currentInterface != 1 and currentInterface != 10 and currentInterface != 6:
        keyInput = ""
    
    if currentInterface == 1:
        if currentInputBox % 3 == 0 and len(playerInputList[currentInputBox][0]) == 6:
            currentInputBox += 1
            keyInput = ""
        readinput(inputedkey)
        displayscore()
                
    if currentInterface == 10:
        EndScreen.score()
    
    if currentInterface == 6:
        highscorelist = topfive(playerinfodic,highscorelist)
        for i in range (len(highscorelist)):
            textSize(40)
            fill(255)
            text(highscorelist[i][0], 300, 250 + i* 80)
            text(highscorelist[i][1], 900, 250 + i* 80)
           
    if currentInterface == 9:
        allButtonLink[7][0][8] = True
        activePlayer = Canasta.playerList[currentPlayerIndex]
        activePlayer.scoreonscreen = activePlayer.checkscore()
        mouseOverCardIndex = CanastaGame.mouseOverCard(activePlayer)
        CanastaGame.displayDiscardPile()
        CanastaGame.displayCard(Canasta.playerList)
        CanastaGame.displayMeld(activePlayer)
        CanastaGame.showRedThree(activePlayer)
        CanastaGame.displayScore(activePlayer)
    
def mouseClicked():
    global mclicked
    mclicked = True 

def keyTyped():
    global inputedkey
    global possiblekey

    if key.lower() in possiblekey:
        inputedkey = key
    if key == BACKSPACE :
        inputedkey = "BACKSPACE"   
    if key == ENTER and len(keyInput) > 0:
        inputedkey = "ENTER"

#reads an array of cards. Then sort the cards according to the number and return the sorted arr
def sortcard(arr):
     leng = len(arr)
     for i in range(leng - 1):
         minValueIdx = i
         for j in range(i+1, leng):
             if arr[j][0] < arr[minValueIdx][0]:
                 minValueIdx = j
         arr.insert(i, arr.pop(minValueIdx))
     return arr
 
# reads an array containing selected cards and an array containing cards in hand. Insert the selected cards and return the new cards in hand array
def insertcard(newcards, cardsinhand):
    for i in range (len(newcards)):
        for j in range (len(cardsinhand)):
            if newcards[i][0] < cardsinhand[j][0]:
                cardsinhand.insert(j,newcards[i])
                break
            elif j == len(cardsinhand)-1:
                cardsinhand.append(newcards[i])
    return cardsinhand

#-------------------------------------------------------------------------------------------------
# Create a new indirect array from student number and first,last name combination
# take in a dictionary
# return a two dimensional indirect array
def indirectArray(dict):
    allNames = []
    for c in dict.values():
        allNames.append(c[0] + c[1])
    allNumbers = dict.keys()    
    inArray = [[i, i] for i in range(len(allNames))]
    switch  = False
    for j in range (1, len(inArray)):
        switch  = True
        limit = len(allNames)- j
        for i in range (limit):
            if allNames[inArray[i][1]] > allNames[inArray[i+1][1]]:
                inArray[i][1] , inArray[i+1][1] = inArray[i+1][1] , inArray[i][1]
                switch = False
            if allNumbers[inArray[i][0]] > allNumbers[inArray[i+1][0]]:
                inArray[i][0] , inArray[i+1][0] = inArray[i+1][0] , inArray[i][0]
                switch = False
        if switch:
            break
    return inArray

# Find any file on the computer, takes in the name and the root, return the path of the file
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

# Load the target pickle file into a data structure depending on the content of the file
# take in the name of the pickle file
# return the data being loaded
def pickleIn(fileName):
    pickle_in = open(fileName, "rb")
    targetData = pickle.load(pickle_in)
    pickle_in.close()
    return targetData

# Dump the target data into a pickle file
# take in the target data and the name of the pickle file
# returns nothing
def pickleOut(target, fileName):
    pickle_out = open(fileName, "wb")
    pickle.dump(target, pickle_out)
    pickle_out.close()
    return

# Load file origin to a player dictionary
# takes in nothing
# returns the player dictionary
def loadStudentDictionary():
    try:
        return pickleIn("Student Dictionary.pickle") 
    except:
        print("dictionary pickle not found")
        try:
            f = find("setup.txt", "/Users")
            file = open(f)
            newDict = {}
            for line in file:
                tempList = line.strip("\n").split(",")
                newDict[tempList.pop(0)] = tempList
            file.close()
            return newDict
        except:
            print("setup.txt not found")
            print("Can't run game")
            raise IOError
#allStudentDict = loadStudentDictionary()

# Load or create indirect array from student dictionary
# Takes in the student dictionary
# returns the indirect array
def loadStudentIndirectArray(dict):
    try:
        return pickleIn("Student Indirect Array.pickle") 
    except:
        print("indirect array pickle not found")
        newIndirectArray = indirectArray(dict)
        return newIndirectArray
#allStudentIndirect = loadStudentIndirectArray(allStudentDict)
