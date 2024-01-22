def e_approx(n):
    e_num = 1
    f_num = 1
    for i in range(1, n + 1):
        f_num *= i
        e_num += 1 / f_num
    return e_num

def main():
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print("n =", n, "Approximation:", approx_str)

main()