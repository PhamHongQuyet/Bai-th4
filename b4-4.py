ds=input('Danh sach:').split()
# in cả dãy vừa nhập
print(ds[::-1])
# in dãy vừa nhập, mỗi phần tử trên mỗi dòng
for so in ds:
    print(so[::-1])
