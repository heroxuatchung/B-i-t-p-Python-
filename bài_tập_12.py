#nhập 1 số có 2 chữ số hàng đơn vị và số hàng chục
a = int(input("nhập 1 số có 2 chữ số: "))
HangChuc = a//10
HangDV = a%10
print(f"Hàng chục: {HangChuc}, "f"Hàng đơn vị: {HangDV}")