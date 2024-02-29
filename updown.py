import random


def up_down_game():
    while True:  # 게임을 다시 시작할 수 있도록 외부 루프 추가
        random_number = random.randint(1, 100)  # 1부터 100 사이의 랜덤한 숫자를 선택합니다.
        num = 0  # 시도 횟수를 추적합니다.

        print("1부터 100까지의 숫자 중에서 하나를 맞춰보세요.")

        while True:
            num += 1
            user_input = input("추측한 숫자를 입력하세요: ")

            # 사용자 입력 검증
            try:
                guess = int(user_input)
            except ValueError:
                print("유효한 숫자를 입력해주세요.")
                continue

            # 범위 검증
            if guess < 1 or guess > 100:
                print("1에서 100 사이의 숫자를 입력해야 합니다.")
                continue

            # 업 & 다운 로직
            if guess < random_number:
                print("up")
            elif guess > random_number:
                print("down")
            else:
                print(f"정답입니다! {num}번 만에 맞췄어요.")
                break  # 정답을 맞췄을 때 내부 루프를 종료합니다.

        # 게임 재시작 여부 확인
        restart = input("다시 시작하시겠습니까? (y/n): ").lower()
        if restart != 'y':
            print("게임을 종료합니다.")
            break  # 'y'가 아닌 다른 입력을 받으면 외부 루프를 종료하여 게임을 종료합니다.


if __name__ == "__main__":
    up_down_game()

