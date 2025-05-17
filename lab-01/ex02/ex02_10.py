def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
intput_str = input("Nhập một chuỗi: ")
print("Chuỗi đảo ngược là:", dao_nguoc_chuoi(intput_str))