def gen_par(n):
    if n & 1:
        return False
    gen_braces(n, "", 0, 0, n // 2)
    return True

def gen_braces(n, pattern, op, cl, max_op):
    if n == 0:
        print(pattern)
        return
    
    if op < max_op:
        gen_braces(n - 1, pattern + "(", op + 1, cl, max_op)

    if cl < op:
        gen_braces(n - 1, pattern + ")", op, cl + 1, max_op)

if not gen_par(int(input("Enter number of input paranthesis: "))):
    print("Cannot generate balanced paranthesis for odd number of braces")