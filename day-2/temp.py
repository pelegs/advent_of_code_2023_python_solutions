import re

def sumGameIDs():
    gameID = 0
    gameIDSum = 0
    reds = 12
    greens = 13
    blues = 14
    file = open("p1_actual_str.txt", "r")
    gameIDRegex = "(\\d+(?=:))"
    setsRegex = "(?<=:)(.*)"
    redsRegex = "(\\d+)(?=\\sred)"
    greensRegex = "(\\d+)(?=\\sgreen)"
    bluesRegex = "(\\d+)(?=\\sblue)"

    for line in file:
        valid = True
        gameID = int(re.search(gameIDRegex, line).group(0))
        sets = re.search(setsRegex, line).group(0)
        sets = re.split(";", sets)
        for set in sets:
            currRed = re.search(redsRegex, set)
            if(currRed):
                currRed = int(currRed.group(0))
                if(currRed > reds): valid = False

            currGreen = re.search(greensRegex, set)
            if(currGreen):
                currGreen = int(currGreen.group(0))
                if(currGreen > greens): valid = False


            currBlue = re.search(bluesRegex, set)
            if(currBlue):
                currBlue = int(currBlue.group(0))
                if(currBlue > blues): valid = False
                
        if(valid):
            print(gameID)
            gameIDSum += gameID

    print("The sum of game IDs is: " + str(gameIDSum))

    file.close()

sumGameIDs()
