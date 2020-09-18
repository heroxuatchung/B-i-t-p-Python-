# Nhập vào tiền lương cơ bản, phụ cấp và số ngày  đi làm trong tháng và in ra lương chính thức
LuongCB = int(input("lương cơ bản: "))
PhuCap = int(input("phụ cấp: "))
SoNgay = int(input("Số ngày: "))
LuongChinh = ((LuongCB + PhuCap)/22)*SoNgay
print(f"Lương Chính: {LuongChinh}")
