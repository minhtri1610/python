# hãy vieets chương trình thêm tất cả các từ trong file data2.txt vào trong danh sach mywork

f = open('data2.txt')
ds = []
hcnt = 0
# fread = f.read()
for line in f:
    tmp = line.strip().split(" ")
    ds += tmp
print(ds)
print("tong so tu la", len(ds))
for key in ds:
    if key == 'hello':
        hcnt += 1
print("so tu hello la ", hcnt)

# trước khi phân tích dữ liệu cần phải làm sạch dữ liệu