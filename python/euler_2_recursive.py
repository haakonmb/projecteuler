#Max recursion depth exceeded. Could set it higher, but might get stack overflow. Recursion is not optimised for solving this problem. 
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

memo = {0:0, 1:1}
def fib(num):
    if not num in memo:
        memo[num] = fib(num-1) + fib(num-2)
    return memo[num]


print(fib(4000000))
