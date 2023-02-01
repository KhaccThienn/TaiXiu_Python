import random

def rollNum():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    return dice1 + dice2 + dice3


def game():
    
    print("Chào mừng bạn đến với game tài xỉu!")
    print("Bạn có tổng số 10.000 đồng để đặt cược.")
    money = 10000
    
    while money > 0:
        print("\nBạn có thể chọn tài(T) hoặc xỉu (X).")
        print(f"Bạn đang có: {money}")
        choice = input("Hãy chọn tài hoặc xỉu: ")
        if choice == "T":
            bet = int(input("Hãy nhập số tiền cược: "))
            if bet > money:
                print("\tBạn không đủ tiền để đặt cược.")
            else:
                roll = rollNum()
                print(f"\tRoll ra: {roll}")
                if roll < 7:
                    print("\tBạn đã thắng. Số tiền của bạn tăng lên " + str(bet))
                    money += bet
                else:
                    print("\tBạn đã thua. Số tiền của bạn giảm xuống " + str(bet))
                    money -= bet
        elif choice == "X":
            bet = int(input("Hãy nhập số tiền cược: "))
            if bet > money:
                print("\tBạn không đủ tiền để đặt cược.")
            else:
                roll = rollNum()
                print(f"\tRoll ra: {roll} \n")
                if roll > 7:
                    print("\tBạn đã thắng. Số tiền của bạn tăng lên " + str(bet))
                    money += bet
                else:
                    print("\tBạn đã thua. Số tiền của bạn giảm xuống " + str(bet))
                    money -= bet
        else:
            print("Lựa chọn không hợp lệ.")
    print("Rất tiếc, bạn đã hết tiền đặt cược ! ");
    
game();
