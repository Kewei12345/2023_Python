global PlayerScores

#2D list with player names and their scores
PlayerScores = [[""]*2 for i in range(11)]


def ReadHighScores():
    with open("HighScore.txt", 'r') as TextFile:
        for n in range(11):
            PlayerScores[n][0] = TextFile.readline().strip()
            PlayerScores[n][1] = TextFile.readline().strip()
    

def OutputHighScores():
    for i in range(11):
        print(PlayerScores[i][0], PlayerScores[i][1])


def AmendHighScores(Name, Score):
    for i in range(9, -1, -1):
        if Score > int(PlayerScores[i][1]) and Score > int(PlayerScores[i-1][1]):
            PlayerScores[i][1] = PlayerScores[i-1][1]
            PlayerScores[i][0] = PlayerScores[i-1][0]
        elif Score > int(PlayerScores[i][1]) and Score < int(PlayerScores[i-1][1]):
            PlayerScores[i][1] = Score
            PlayerScores[i][0] = Name
        else:
            break


def WriteTopTen():
    with open("NewHighScore.txt", "w") as NewFile:
        for n in range(10):
            NewFile.write(f"{PlayerScores[n][0]}\n")
            NewFile.write(f"{PlayerScores[n][1]}\n")
            pass


ReadHighScores()
OutputHighScores()


UserName = input("3 letter name: ")
while len(UserName) != 3:
    UserName = input("Invalid, 3 letter name: ")


UserScore = int(input("1 and 100,000 inclusive: "))
while 1 >= UserScore and UserScore <= 100000:
    UserScore = int(input("invalid, 1 and 100,000 inclusive: "))


AmendHighScores(UserName, UserScore)
OutputHighScores()
WriteTopTen()