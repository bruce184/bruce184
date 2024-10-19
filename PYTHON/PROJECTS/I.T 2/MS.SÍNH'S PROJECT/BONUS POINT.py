# NHẬP THÔNG TIN
def nhap():
    ds_thisinh = []
    sl = int(input('Nhập số lượng thí sinh: '))
    for i in range(sl):
        while True: 
            sbd = input(f'Nhập Số báo danh thí sinh {i+1} (4 ký tự): ')
            if len(sbd) == 4:
                break
            else: 
                print('Số báo danh không hợp lệ!')
                
        math = float(input(f'Nhập điểm Toán của thí sinh {i+1}: '))
        literature = float(input(f'Nhập điểm Văn của thí sinh {i+1}: '))
        english = float(input(f'Nhập điểm Tiếng Anh của thí sinh {i+1}: '))
        thisinh = {
            'SBD': sbd, 
            'Toán': math,
            'Văn': literature,
            'Anh': english,
            'ĐTB': (math + literature + english) / 3,
            'Tổng điểm': math + literature + english
        }
        ds_thisinh.append(thisinh)
    return ds_thisinh


# HIỂN THỊ DS
def display(ds_thisinh):
    print('{:<5} {:<6} {:<6} {:<6} {:<6} {:<12}'.format('SBD', 'Toán', 'Văn', 'Anh', 'ĐTB', 'Tổng điểm'))
    for thisinh in ds_thisinh:
        print('{:<5} {:<6} {:<6} {:<6} {:<6.2f} {:<12.2f}'.format(
            thisinh['SBD'], thisinh['Toán'], thisinh['Văn'], thisinh['Anh'], thisinh['ĐTB'], thisinh['Tổng điểm']
        ))       
    print('\n')


# HIỂN THỊ DS THÍ SINH ĐTB >= 5 ĐIỂM 
def dtb_5(ds_thisinh):
        # dictionary comprehension
    ds_dtb_5 = {thisinh['SBD']: thisinh['ĐTB'] for thisinh in ds_thisinh if thisinh['ĐTB'] >= 5}
    if ds_dtb_5: 
        print('Danh sách thí sinh có Điểm trung bình >= 5:')
        for sbd, dtb in ds_dtb_5.items():
            print(f'SBD: {sbd} | ĐTB: {dtb:.2f}')
    else: 
        print('Không có thí sinh thuộc hạng mục này!')
    print('\n')


# HIỂN THỊ DS CÓ TỔNG ĐIỂM >= 20 ĐIỂM 
def td_20(ds_thisinh):
    ds_tongdiem_20 = [thisinh for thisinh in ds_thisinh if thisinh['Tổng điểm'] >= 20]
    if ds_tongdiem_20:
        print(f'Danh sách thí sinh có tổng điểm >= 20 điểm:')
        display(ds_tongdiem_20)
    else: 
        print('Không có thí sinh thuộc hạng mục này!')
    # print('\n')


# HIỂN THỊ DS LỚP CỬ NHÂN TÀI NĂNG (TỔNG ĐIỂM >= 27 ĐIỂM)
def td_27(ds_thisinh):
    ds_tongdiem_27 = [thisinh for thisinh in ds_thisinh if thisinh['Tổng điểm'] >= 27]
    if ds_tongdiem_27:
        print('Danh sách thí sinh được vào lớp Cử nhân Tài năng (tổng điểm >= 27 điểm):')
        display(ds_tongdiem_27)
    else: 
        print('Không có thí sinh thuộc hạng mục này!')
    # print('\n')



# HIỂN THỊ DS BỊ ĐIỂM LIỆT 
def diem_liet(ds_thisinh):
    ds_diemliet = [(thisinh['SBD'], thisinh['Toán'], thisinh['Văn'], thisinh['Anh']) for thisinh in ds_thisinh if 0 in (thisinh['Toán'], thisinh['Văn'], thisinh['Anh'])]
    if ds_diemliet:
        print('Danh sách thí sinh bị điểm liệt: ')
            # để xuất ra hết 
        for sbd, toan, van, anh in ds_diemliet:
            print(f'SBD: {sbd} | Toán: {toan} | Văn: {van} | Anh: {anh}')
    else: 
        print('Không có thí sinh thuộc hạng mục này!')
    print('\n')


# HIỂN THỊ DS CÓ ĐIỂM 3 MÔN CAO NHẤT 
def cao_nhat(ds_thisinh):
    if not ds_thisinh:
        print("Danh sách thí sinh trống!")
        return
    
    try: 
        max_toan = max(ds_thisinh, key = lambda x: x['Toán'])
        max_van = max(ds_thisinh, key = lambda x: x['Văn'])
        max_anh = max(ds_thisinh, key = lambda x: x['Anh'])
        print("Thí sinh có điểm Toán cao nhất:")
        print(f"SBD: {max_toan['SBD']} | Điểm Toán: {max_toan['Toán']}\n")
        print("Thí sinh có điểm Văn cao nhất:")
        print(f"SBD: {max_van['SBD']} | Điểm Văn: {max_van['Văn']}\n")
        print("Thí sinh có điểm Anh cao nhất:")
        print(f"SBD: {max_anh['SBD']} | Điểm Anh: {max_anh['Anh']}\n")
    except KeyError as e:
        print(f'Thiếu thông tin điểm cho môn {e}')
    except ValueError:
        print('Danh sách thí sinh không có dữ liệu hợp lệ!')


# MAIN 
danhsach_thisinh = nhap()
print('Danh sách thí sinh: ')
display(danhsach_thisinh)
dtb_5(danhsach_thisinh)
td_20(danhsach_thisinh)
td_27(danhsach_thisinh)
diem_liet(danhsach_thisinh)
cao_nhat(danhsach_thisinh)