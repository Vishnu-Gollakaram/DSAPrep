s = "ABC"
arr = []

def permute(s, ans):

    if len(s) == 1:
        arr.append(ans + s[-1])
        return

    permute(s[1:], ans + s[0])
    permute(s[1:], ans + s[0] + " ")

permute(s, "")
print(arr)