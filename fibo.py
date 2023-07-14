def naive_fibonacci(n):
    '''Input:  n
    Output: F_n'''
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return naive_fibonacci(n-2) + naive_fibonacci(n-1)

def fibonacci_list(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else: 
        f_seq = [0,1]
        i = 2
        while (i <= n):
            f_seq.append(f_seq[i-2]+f_seq[i-1])
            i += 1
        return f_seq[-1]
    
def fibonacci_variable(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else: 
        f_nm2 = 0
        f_nm1 = 1
        i = 2
        while (i <= n):
            f_n = f_nm2 + f_nm1
            if i == n:
                return f_n 
            # We want to update to compute the next F_n. 
            # F_n => F_nm1
            # F_nm1 => F_nm2
            else: 
                f_nm2 = f_nm1
                f_nm1 = f_n
                i += 1

def f_tests(n=10):
    print(f"F_10 = {naive_fibonacci(n)} = {fibonacci_list(n)} = {fibonacci_variable(n)}") 

f_tests()