so_gio_lam = float(input("Nhập số giờ làm: "))
luong_mot_gio = float(input("Nhập lương một giờ: "))
gio_tieu_chuan = 44
gio_vuot_chuan = so_gio_lam - gio_tieu_chuan

thuc_linh = gio_tieu_chuan * luong_mot_gio + gio_vuot_chuan * luong_mot_gio * 1.5
thuc_linh = round(thuc_linh, 2)
print("Lương thực lĩnh là: ", thuc_linh)