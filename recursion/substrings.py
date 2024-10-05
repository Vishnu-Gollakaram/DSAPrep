ans = []

def get_substring(s, sub):

    if s == "":
        ans.append(sub)
        return

    get_substring(s[1:], sub + s[0])
    get_substring(s[1:], sub)

get_substring(input("Enter the String: "), "")
print(ans)
