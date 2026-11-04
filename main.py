import random 

# 가위 바위 보 게임 미니 프로젝트
user_name = input('이름을 입력하세요 : ')
user_score = 0
comp_score = 0
game_cnt = 0
game_list = []


def func1(num):
    if num == 1:
        result = '가위'
    elif num == 2:
        result = '바위'
    elif num == 3:
        result = '보'
    return result

while True:
    print('=' * 30)
    print('가위 / 바위 / 보 게임')
    print('=' * 30)
    print("1. 가위 / 2. 바위 / 3. 보")
    computer = random.randint(1, 3)
    user = input("번호를 입력하세요. : ")
    
    if user == 'q':
        print('게임을 종료합니다.')
        break

    if not user.isdecimal():
        print("숫자만 입력해주세요.")
        continue

    user = int(user)
    
    if user < 1 or user > 3:
        print('1과 3 사이의 수를 입력하세요')

    user1 = func1(user)
    computer1 = func1(computer)

    print('\n[게임결과]')
    print(f'{user_name}: {user1} vs 컴퓨터: {computer1}')

    if user == 1:        
        if computer == 1:
            result = '=> 비김'
            game_list.append('비김')
        elif computer == 2:
            result = '=> 패배'
            comp_score += 1
            game_list.append('패배')
        elif computer == 3:
            result = '=> 승리'
            user_score += 1
            game_list.append('승리')
    elif user == 2:
        if computer == 1:
            result = '=> 승리'
            user_score += 1
            game_list.append('승리')
        elif computer == 2:
            result = '=> 비김'
            game_list.append('비김')
        elif computer == 3:
            result = '=> 패배'
            comp_score += 1
            game_list.append('패배')
    elif user == 3:
        if computer == 1:
            result = '=> 패배'
            comp_score += 1
            game_list.append('패배')
        elif computer == 2:
            result = '=> 승리'
            user_score += 1
            game_list.append('승리')
        elif computer == 3:
            result = '=> 비김'
            game_list.append('비김')

    print(result, "\n")

    print(f'현재 스코어 {user_name} {user_score} : {comp_score} 컴퓨터\n')

    if len(game_list) > 1 and game_list[-2] == '승리' and game_list[-1] == '승리':
        print(f"{user_name}이 2연승입니다!")
    elif len(game_list) > 1 and game_list[-2] == '패배' and game_list[-1] == '패배':
        print("컴퓨터가 2연승입니다!")

    if user_score == 2:
        print(f'{user_score}:{comp_score}로 {user_name}이/가 승리했습니다.\n')
        print("승패 목록")
        for i in range(len(game_list)):
            print(f'{i+1}판 결과: {game_list[i]}')
        break
    elif comp_score == 2:
        print(f'3판 2선 최종 결과 {user_score}:{comp_score}로 컴퓨터가 승리했습니다. ')
        print("승패 목록")
        for i in range(len(game_list)):
            print(f'{i+1}판 결과: {game_list[i]}')        
        break
    
    retry = input('\n다시 도전 (yes/no) : ')
    if retry == 'no':
        print("게임을 종료합니다.")
        break
    elif retry == 'yes':
        print("\n게임을 재개합니다.\n")
        continue  

    
        





