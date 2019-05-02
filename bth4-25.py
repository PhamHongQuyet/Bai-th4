values=input("nhap mot chuoi cac so, cach nhau boi dau phay:")
numbers=[x for x in values.split(",") if int(x)%2!=0]
print(",".join(numbers))
