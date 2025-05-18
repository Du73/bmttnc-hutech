from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []
    
    def generateId(self):
        maxId = 1
        if(self.soLuongSinhVien() > 0):
            maxId = self.listSinhVien[0]._id
            for sv in  self.soLuongSinhVien():
                if(maxId < sv._id):
                    maxId = sv._id
                maxId += 1
        return maxId
    def soLuongSinhVien(self):
        return len(self.listSinhVien)
    
    
    def themSinhVien(self):
       svId = self.generateId()
       name = input("Nhập tên sinh viên: ")
       sex = input("Nhập giới tính: ")
       major = input("Nhập chuyên ngành: ")
       avgScore = float(input("Nhập điểm trung bình: "))
       sv =SinhVien(svId, name, sex, major, avgScore)
       self.xepLoaiHocLuc(sv)
       self.listSinhVien.append(sv)
       print("Thêm sinh viên thành công!")
       
    def updateSinhVien(self, ID):
        sv: SinhVien = self.findByID(ID)
        if (sv!= None):
            name = input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính: ")
            major = input("Nhập chuyên ngành: ")
            avgScore = float(input("Nhập điểm trung bình: "))

            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._avgScore = avgScore
            self.xepLoaiHocLuc(sv)
        else:
            print("Không tìm thấy sinh viên với ID:", ID)
        print("Cập nhật sinh viên thành công!")
        
    def sortByiD(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)
            

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)
        
    def sortByAvgScore(self):
        self.listSinhVien.sort(key=lambda x: x._avgScore, reverse=False)
        
    def findByID(self, ID):
        searchResult = None
        if(self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if(sv._id == ID):
                    searchResult = sv
                    return searchResult
                
    def findByName(self, keyword):
        listSV = []
        if(self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if(keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
            return listSV
        
        
        
    def deleteByID(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if(sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        else:
            print("Không tìm thấy sinh viên với ID:", ID)
        return isDeleted
    
    def xepLoaiHocLuc(self, sv: SinhVien):
        if(sv._avgScore >= 8):
            sv._hocLuc = "Giỏi"
        elif(sv._avgScore >= 6.5):
            sv._hocLuc = "Khá"
        elif(sv._avgScore >= 5):
            sv._hocLuc = "Trung bình"
        else:
            sv._hocLuc = "Yếu"
            
    def showSinhVien(self, listSV):
        print("{:<8} {:18} {:<8} {:<8} {:<8} {:<8}".format("ID", "Tên", "Giới tính", "Chuyên ngành", "Điểm TB", "Học lực"))
        if(listSV.__len__() >0):
            for sv in listSV:
                print("{:<8} {:18} {:<8} {:<8} {:<8} {:<8}".format(sv._id, sv._name, sv._sex, sv._major, sv._avgScore, sv._hocLuc))
            print("\n")
            
    def getListSinhVien(self):
        return self.listSinhVien