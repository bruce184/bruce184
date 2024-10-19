# Lấy thư viện về 
import random 

gioi_han = input('Nhập giới hạn: ') # nhập giới hạn số 

if gioi_han.isdigit(): # kiểm tra nếu 'ý nghĩa' của nó là số 
    gioi_han = int(gioi_han) # đảm bảo, đổi nó thành số 

    if gioi_han <= 0: # kiểm tra nếu nó nhỏ hon 0 
        print('Nhập số lớn hơn 0: ') # báo kêu nhập lại, lớn hơn 0
        quit() # lệnh thoát khỏi phần code này
        # LƯU Ý: khác với break là ngắt code hoàn toàn 
else: 
    print('Hãy nhập 1 số lần này:') # nhập lại, phải là SỐ
    quit() 


so_ngau_nhien = random.randint(0, gioi_han) # nếu là randint thì lấy luôn đuôi
so_lan_doan = 0

while True: # khởi tạo vòng lặp 
    so_lan_doan += 1 # ít nhất sẽ có 1 lần đoán, nên số lần đoán sẽ tăng lên 1
    so_doan = input('Đoán số: ') # Nhập số muốn đoán
    if so_doan.isdigit(): # như trên, để đảm bảo nó là kiểu số
        so_doan = int(so_doan)

    else: 
        print('Hãy nhập 1 số lần này:') # khi nhập sai trước đó 
        continue 

    if so_doan == so_ngau_nhien: # nếu giống 
        print('Đoán đúng!')  # báo đún
        break    # ngắt vòng lặp -> .xuất dòng 37
    elif so_doan > so_ngau_nhien: # nếu lớn hơn hay thấp hơn thì xuất thông báo 
        print('Thấp hơn')
    else: 
        print('Cao hơn')

print(f'Bạn đã đoán đúng trong {so_lan_doan} đoán') # xuất thông báo sau khi đoán đún