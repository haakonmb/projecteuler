#Max recursion depth exceeded. Could set it higher, but might get stack overflow. Recursion is not optimised for solving this problem. 
memo = {0:0, 1:1}
def fib(num):
    if not num in memo:
        memo[num] = fib(num-1) + fib(num-2)
    return memo[num]


print(fib(4000000))
