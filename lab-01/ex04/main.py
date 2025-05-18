from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1 == 1):
    print("\nChuong trình quản lý sinh viên")
    print("1. Thêm sinh viên")
    print("2. Cập nhật sinh viên")
    print("3. Xóa sinh viên")
    print("4. Tìm kiếm sinh viên theo tên")
    print("5. Tìm kiếm sinh viên theo diểm trung bình")
    print("6. Tìm kiếm sinh viên theo chuyên ngành")
    print("7. Hiển thị danh sách sinh viên")
    print("0. Thoát")
    
    key = int(input("Nhập lựa chọn của bạn: "))
    if key == 1:
        qlsv.themSinhVien()
        print("\nThêm sinh viên thành công!")  
    elif key == 2:
        id = int(input("\nNhập ID sinh viên cần cập nhật: "))
        qlsv.updateSinhVien(id)
    elif key == 3:
        if qlsv.soLuongSinhVien() > 0:
            id = int(input("\nNhập ID sinh viên cần xóa: "))
            if qlsv.deleteByID(id):
                print("\nXóa sinh viên thành công!")
            else:
                print("\nKhông tìm thấy sinh viên với ID:", id)
        else:
            print("Danh sách sinh viên rỗng!")
    elif key == 4:
        name = input("Nhập tên sinh viên cần tìm kiếm: ")
        qlsv.findByName(name)
    elif key == 5:
        avgScore = float(input("Nhập điểm trung bình cần tìm kiếm: "))
        qlsv.findByAvgScore(avgScore)
    elif key == 6:
        major = input("Nhập chuyên ngành cần tìm kiếm: ")
        qlsv.findByMajor(major)
    elif key == 7:
        if(qlsv.soLuongSinhVien() > 0):
            print("\nDanh sách sinh viên:")
        qlsv.showSinhVien(qlsv.getListSinhVien())
    elif key == 0:
        print("Thoát chương trình!")
        break
    else :
        print("Lựa chọn không hợp lệ! Vui lòng chọn lại.")