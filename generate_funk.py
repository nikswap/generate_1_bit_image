import random

operators = ['*','//','+','-','~']
vars = ['x','y']

def get_a_funk():
    no_of_ops = random.randint(2,10)
    res = []
    res2 = ''
    for i in range(no_of_ops):
        op = random.choice(operators)
        var1 = random.choice(vars)
        var2 = random.choice(vars)
        if op in '~':
            t = var1
            var1 = random.choice(operators)
            while var1 in '~':
                var1 = random.choice(operators)
            res.append(t+var1+op+var2)
        else:
            res.append(op.join([var1,var2]))
    #print(res)
    for i in range(0,len(res)-1,2):
        op = random.choice(operators)
        op2 = random.choice(operators)
        #Lazy fix. This should be able to ~ as well
        while op2 in '~':
            op2 = random.choice(operators)
        #print(op,op2,op in '~')
        if op in '~':
            res2 += res[i]+op2+op+res[i+1]+op2
        else:
            res2 += res[i]+op+res[i+1]+op2
        
    if res2[-1] == '/':
        res2 = res2[:-1]
    return res2[:-1]

if __name__ == '__main__':
    for i in range(10):
        print(get_a_funk())