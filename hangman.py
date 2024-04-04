import random, sys

#교수대를 나타내는 상수 설정
HANGMAN_PICS = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""]

#맞출 단어
CATEGORY = 'Animals'
WORDS = 'ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE WOLF WOMBAT ZEBRA'.split()

def main():
    print('행맨 게임을 플레이 해 봅시다!')

    #새로운 게임을 위해 변수 셋업
    missedLetters =[] #틀린 글자 리스트
    correctLetters= [] #맞춘 글자 리스트 
    secretWord = random.choice(WORDS) #플레이어가 맞춰야 하는 단어.

    while True:
        drawHangman(missedLetters, correctLetters, secretWord)

        # 사용자가 예상한 글자 입력하기
        guess = getPlayerGuess(missedLetters + correctLetters)

        if guess in secretWord:
            #맞춘 글자를 correctLetters 에 추가
            correctLetters.append(guess)

            #플레이어가 이겼는지 검사
            foundAllLetters = True #플레이어가 이겼다는 가정으로 시작

            for secretWordLetter in secretWord:
                if secretWordLetter not in correctLetters:
                    #correctLetters 에 정답인 단어의 글자가 아직 없기에 
                    #플레이어가 이긴 것이 아님
                    foundAllLetters =False
                    break

            if foundAllLetters:
                print('맞습니다! 비밀의 단어는 바로 "{}" 입니다!'.format(secretWord))
                print('성공!')
                break

        else:
            #플레이어의 추측이 틀림
            missedLetters.append(guess)

            #플레이어가 기회를 다 써서 졌는지 확인 
            #(-1 은 HANGMAN_PIC 에서 교수대가 비어 있는 단계를 카운트하지 않기 때문)
            if len(missedLetters) == len(HANGMAN_PICS) -1:
                drawHangman(missedLetters, correctLetters, secretWord)
                print('기회를 모두 사용했습니다😭')
                print('비밀의 단어는"{}"였습니다ㅠㅠ'.format(secretWord))
                break

def drawHangman(missedLetters, correctLetters, secretWord):
    """비밀 단어에 대해 맞힌 글자와 틀린 글자와 함께 교수형 집행인의 현재 상태를 그림""" 
    print(HANGMAN_PICS[len(missedLetters)])
    print('비밀 단어의 종류는 : "{}" 입니다.'.format(CATEGORY))
    print()

    #틀린 글자들을 보여준다
    print('틀린 글자들 : ',end='')
    for letter in missedLetters:
        print(letter, end=' ')
    if len(missedLetters) == 0:
        print('아직 틀린 글자가 없습니다.')
    print()

    #정답 단어에 대해 한 글자당 한 칸식 빈칸을 표시한다
    blanks = ['_'] * len(secretWord)

    #맞춘 글자는 빈칸 대신 표현한다.
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks[i] = secretWord[i]

    #글자사이에 공백을 표시 
    print(' '.join(blanks))

def getPlayerGuess(alreadyGuessed):
    """플레이어가 입력한 문자를 반환한다. 
    이 함수는 플레이어가 이전에 추측하지 않은 문자를 입력했는지 확인한다."""
    while True: #플레이어가 유효한 글자를 입력할 때까지 계속 요청 
        print('글자를 맞춰보세요.👻')
        guess =input('> ').upper()
        if len(guess) != 1:
            print('한글자만 입력하세요.')
        elif guess in alreadyGuessed:
            print('이미 해당 글자를 입력했어요. 다른 글자를 골라보세요')
        elif not guess.isalpha():
            print('영문 소문자로 입력해주세요')
        else:
            return guess

#이 프로그램이 다른 프로그램에 임포트 된 것이 아니라면 게임이 플레이된다.
if __name__ =='__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit() #ctrl+c 누르면 종료