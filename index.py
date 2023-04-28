import random

def getRandomNumber():
    return random.randint(1, 3)

def getGbb():
    num = getRandomNumber()
    if num == 1:
        return "묵"
    elif num == 2:
        return "찌"
    else:
        return "빠"

while True:
    userInput = input("묵(1), 찌(2), 빠(3)를 입력하세요. 종료하려면 q를 입력하세요.")
    if userInput == "q":
        print("게임을 종료합니다.")
        break
    elif userInput not in ["1", "2", "3"]:
        print("잘못된 입력입니다. 다시 입력해주세요.")
        continue

    userCoice = ""
    if userInput == "1":
        userChoice = "묵"
    elif userInput == "2":
        userChoice = "찌"
    elif userInput == "3":
        userChoice = "빠"

    computerChoice = getGbb()

    print("사용자:"+ userChoice , "컴퓨터:"+ computerChoice)

    if userChoice == computerChoice:
        print("비겼습니다.")
    elif (userChoice == "묵" and computerChoice == "찌") or (userChoice == "찌" and computerChoice == "빠") or (userChoice == "빠" and computerChoice == "묵"):
        print("사용자가 이겼습니다")
    else:
        print("컴퓨터가 이겼습니다")
