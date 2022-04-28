"""Để mở và đọc file chúng ta có 1 số chế dộ cơ bản
chế độ 'r': mở để đọc, ko ghi
chế độ 'w': Mở để đọc và có chính sửa nd file

chọn lựa tham số mã hoá, đây là cách dữ liệu thường ghi xuống theo chuẩn mã hoá quốc tế
_> chuẩn cơ bản thường gặp là UTF8
"""

# fopen = open('data.txt',"r", encoding="UTF-8")

"""ĐỌc file có tương tác nhiều dòng
-> Xuất ra các dòng trong file

    Để đọc từng dòng trong file ta dùng vòng lặp for, mặc định mỗi dòng trong file đều kết thúc bằng ký tự \n
    
"""

fopen2 = open('data2.txt',"r", encoding="utf-8")
# str = fopen2.read()
cnt = 0

for line in fopen2:
    print(line)
    tmpstr = line.split(" ")
    cnt += len(tmpstr)
print("so luong tu la", cnt)
