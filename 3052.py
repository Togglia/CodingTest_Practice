arr = []
for i in range(10):
    a = int(input("숫자 : "))
    if a%42 not in arr:
        arr.append(a%42)
print(len(arr))