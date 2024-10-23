import random


# Định nghĩa hàm con: random số bất kỳ từ 1-6
def rut():
  gia_tri_nho_nhat = random(1, 100) # 50 
  gia_tri_lon_nhat = random(1, 100)
  lac = random.randint(gia_tri_nho_nhat, gia_tri_lon_nhat)

  return lac


# player = input('Enter the number of nguoi_choi (1-4): ')
while True:
  nguoi_choi = input('Nhap so nguoi (2-4): ') # nhập số lượng người chơi
  if nguoi_choi.isdigit():    # khi ý nghĩa của nó là số: số '4' và số 'bốn'
    nguoi_choi = int(nguoi_choi) # đổi nó thành số tự nhiên
    if 2 <= nguoi_choi <= 4:  # nếu thỏa đk từ 2-4 người chơi
      break                # ngắt vòng lặp này
    else: print('Phai 2 đến 4 nguoi choi') # xuất thông báo nhắc nhở
  else: print('So nguoi choi khong hop le') # xuất error khi string của mình ko phải là số
print(nguoi_choi)


# giới hạn điểm số tối đa/người chơi
diem_toi_da = 50
  # khởi tạo số điểm mỗi người chơi khi bắt đầu là 0
diem_nguoi_choi = [0 for _ in range(nguoi_choi)] # ko phải len(nguoi_choi)


# code 'chơi'
while max(diem_nguoi_choi) < diem_toi_da:
  for thu_tu_nguoi_choi in range(nguoi_choi): # chạy qua từng người chơi
    print(f'Nguoi choi {thu_tu_nguoi_choi + 1} bat dau') # thông báo người chơi thứ n bđ chơi
    print(f'Tong cong diem cua nguoi choi {thu_tu_nguoi_choi + 1} : {diem_nguoi_choi[thu_tu_nguoi_choi]}\n')
    diem_hien_tai = 0 # khởi tạo điểm số = 0

    while True: 
      lua_chon = input ('Ban co muon rut bai (y/n): ') # hỏi chơi ko
        # lower() là hàm định dạng văn bản viết hoa thành viết thường 
      if lua_chon.lower() != 'y': # nếu trả lời khác 'yes'
        break # ngắt vòng lặp (chơi)

      gia_tri = rut() # lắc
      if gia_tri == 1: # nếu lắc số 1
        print ('Ban rut so 1. Lượt het') # xuất thông báo
        diem_hien_tai = 0 # điểm số thành 0
        break # ngắt vòng lặp
      else:
        diem_hien_tai += gia_tri # cộng vào điểm số hiện tại
        print (f'Ban rut {gia_tri}') # xuất thông báo đã lắc đc giá trị gì
      print(f'Diem hien tai cua ban la {diem_hien_tai}') # xuất ra điểm số hiện tại

    diem_nguoi_choi[thu_tu_nguoi_choi] += diem_hien_tai # điểm số tổng cộng ng chơi có
    print(f'Tong cong diem cua ban la {diem_nguoi_choi[thu_tu_nguoi_choi]}') # xuất thông báo

# Tìm ra người chiến thắng 
diem_cao_nhat = max(diem_nguoi_choi) # tìm số điểm cao nhất 
nguoi_thang = diem_nguoi_choi.index(diem_cao_nhat) # xác định chỉ số người có điểm cao nhất 
print(f'Nguoi choi {nguoi_thang + 1} chien thang voi so diem:{diem_cao_nhat}') # xuất thông báo
