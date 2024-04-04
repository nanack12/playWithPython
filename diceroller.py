import random, sys

print(''' D&D 기반의 주사위 굴리기 프로그램

    굴릴 주사위의 종류와(면체) 굴릴 갯수를 다음과 같이 작성하세요
    [굴릴 주사위 갯수]d[주사위 면의 개수] 
    + , - 옵션을 추가할 수 있습니다.
    
    예시)
        3d6 --> 6면체 주사위를 3개 굴립니다.
        1d10+2 --> 10면체 주사위를 1번 굴리고, 2를 더합니다.
        2d38-1 --> 38면체 주사위를 2번 굴리고, 1을 뺍니다.
      
        QUIT --> 프로그램을 종료합니다.

''')
while True: #메인 프로그램 루프
    try:
        diceStr = input('> ') #주사위 문자열을 입력하기 위한 프롬프트
        if diceStr.upper() == 'QUIT':
            print('플레이해주셔서 감사합니다.')
            sys.exit()

        #주사위 문자열을 정리
        diceStr = diceStr.lower().replace(' ','')

        #입력된 주사위 문자열에서 "d" 찾기
        dIndex = diceStr.find('d')
        if dIndex == -1:
            raise Exception('d 를 입력하지 않았습니다.')
        
        #굴릴 주사위의 개수를 얻는다. 
        numberOfDice = diceStr[:dIndex]
        if not numberOfDice.isdecimal():
            raise Exception('굴릴 주사위의 개수를 입력하지 않았습니다.')
        numberOfDice = int(numberOfDice)

        #더하기 혹은 빼기 기호가 있는지 찾는다. 
        moIndex = diceStr.find('+')
        if moIndex == -1:
            moIndex = diceStr.find('-')

        #주사위 면의 수를 찾는다.
        if moIndex ==-1:
            numberOfSides = diceStr[dIndex + 1 :]
        else:
            numberOfSides = diceStr[dIndex + 1:moIndex]
        if not numberOfSides.isdecimal():
            raise Exception('주사위 면 수를 입력하지 않았습니다.')
        numberOfSides =int(numberOfSides)

        #조건부의 수를 찾는다. (예를 들어 "3d6 +1" 에서 1)
        if moIndex ==-1:
            moAmount =0
        else:
            moAmount = int(diceStr[moIndex +1:])
            if diceStr[moIndex] == '-':
                #조건부의 수를 음수로 변경한다:
                moAmount = -moAmount
        
        #주사위 굴리기를 시뮬레이션한다 : 
        rolls =[]
        for i in range(numberOfDice):
            rollResult = random.randint(1, numberOfSides)
            rolls.append(rollResult)

        #총합을 표시한다.
        print( '결과: ', sum(rolls)+ moAmount,'(주사위 : ', end='' )

        #굴린 각각의 주사위를 표시한다 :
        for i, roll in enumerate(rolls):
            rolls[i] = str(roll)
        print(', '.join(rolls), end='')

        #조건부의 수를 표시한다 :
        if moAmount != 0 :
            moSign = diceStr[moIndex]
            print(', {}{}'.format(moSign,abs(moAmount)), end='')
        print(')')

    except Exception as exc:
        #예외 사항이 발생하면 메세지 표기
        print('잘못된 값을 입력하셨습니다. 입력 형식은 "1d6" 또는 "3d10+2" 와 같아야 합니다.')
        print('입력된 값이 잘못된 이유는 다음과 같습니다: '+str(exc))
        continue    #주사위 문자열을 입력하는 프롬프트로 돌아감.