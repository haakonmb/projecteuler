fib_last = 1;
fib_current = 1;
sum_terms = 0;

def fib_seq():
    global fib_last;
    global fib_current;
    tmp = fib_last + fib_current;
    fib_last = fib_current;
    fib_current= tmp;
    return fib_current;

while(fib_current < 4000000):
    global sum_terms;
    term = fib_seq();
    if(term % 2 == 0):
        sum_terms += term;


print(sum_terms);

