def get_prev(num):
    if num == 0:
        return
    print(num)
    get_prev(num - 1)

get_prev(int(input("Enter num: ")))