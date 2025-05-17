def xoa_phan_tu(lst, index):
    if 0 <= index < len(lst):
        del lst[index]
    else:
        print("Chỉ số không hợp lệ")
    return lst

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key_to_delete = input("Nhập khóa cần xóa: ")
if key_to_delete in my_dict:
    del my_dict[key_to_delete]
else:
    print("Khóa không tồn tại trong từ điển")
print("Từ điển sau khi xóa:", my_dict)