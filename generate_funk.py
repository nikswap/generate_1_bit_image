import random

operators = ['*','//','+','-']
vars = ['x','y']

def get_a_funk():
    no_of_ops = random.randint(2,10)
    res = []
    res2 = ''
    for i in range(no_of_ops):
        op = random.choice(operators)
        var1 = random.choice(vars)
        var2 = random.choice(vars)
        res.append(op.join([var1,var2]))
    for i in range(len(res)-1):
        op = random.choice(operators)
        op2 = random.choice(operators)
        res2 += res[i]+op+res[i+1]+op2
    if res2[-1] == '/':
        res2 = res2[:-1]
    return res2[:-1]

if __name__ == '__main__':
    for i in range(10):
        print(get_a_funk())