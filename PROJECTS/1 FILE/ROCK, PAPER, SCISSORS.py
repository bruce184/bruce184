# Nhập thư viện 
import random

# Số lần thắng 
nguoi_thang = 0
may_thang = 0

# định nghĩa lựa chọn
lua_chon = ["rock", "paper", "scissors"]

while True:
    # kêu người chơi nhập
    nguoi_nhap = input("Nhập Rock/Paper/Scissors hoặc Q để không chơi: ").lower()
        # chọn 1 trong 3 để chơi
        # không muốn chơi nx sẽ xuất dòng 41, 42
    # nếu người chơi nhập 'q' sẽ kết thúc trò chơi
    if nguoi_nhap == "q":
        break

    # trường hợp, khi nhập ko trong lựa chọn 
    if nguoi_nhap not in lua_chon:
        # tiếp tục hỏi lại, đến khi nhập đún 
        continue

    so_chon = random.randint(0, 2)  # 
    # rock: 0, paper: 1, scissors: 2
    may_choi = lua_chon[so_chon]
    print("Máy chọn", may_choi + ".")

    # Các trường hợp 
        # Trường hợp 1
    if nguoi_nhap == "rock" and may_choi == "scissors":
        print("Bạn thắng!")
        nguoi_thang += 1
        
        # Trường hợp 2
    elif nguoi_nhap == "paper" and may_choi == "rock":
        print("Bạn thắng!")
        nguoi_thang += 1

        # Trường hợp 3
    elif nguoi_nhap == "scissors" and may_choi == "paper":
        print("Bạn thắng!")
        nguoi_thang += 1

        # Trường hợp 4
    else:
        print("Bạn thua!")
        may_thang += 1

print(f"Bạn thắng {nguoi_thang} lần.")
print(f"Máy thắng {may_thang} lần.")