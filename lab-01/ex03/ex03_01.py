def tinh_tong_so_chan(lst):
    tong = 0
    for so in lst:
        if so % 2 == 0:
            tong += so
    return tong


input_list = input("Nhap danh sach so nguyen (cach nhau boi dau phay): ")
numbers = list(map(int,input_list.split(",")))

tong_chan = tinh_tong_so_chan(numbers)
print("Tong cac so chan trong danh sach la:", tong_chan)