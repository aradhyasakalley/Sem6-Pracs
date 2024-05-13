# In potential method we look at the state before and after and compute the potential change between the current and previous states, based on the potential function given

def potential_change(final,initial):
    return (2*final-initial)

# for each push operation size increases and hence
def push(stack,n,cost,potential):
    initial = len(stack)
    for i in range(n):
        stack.append(i)
        final = len(stack)
        potential += potential_change(final,initial)
        initial = final
        cost += 1
    return stack,cost,potential
    
def multipop(stack,n,cost,potential):
    for i in range(n):
        m = int(input('Enter the number of elements to multipop : '))
        initial = len(stack)
        for i in range(min(m,len(stack))):
            stack.pop()
            final = len(stack)
            potential += potential_change(final,initial)
            initial = final
            cost += 1
    return stack,cost,potential


stack = []
cost = 0
potential = 0
op = 0
n = int(input('Enter the number of elements to push (Cost/push == 1) : '))
op += n
stack,cost,potential = push(stack,n,cost,potential)
print(f'Stack after {n} push operations : ',stack)
print(f'Potential after {n} push operations : ',potential)

n = int(input('Enter the number of Multipop opeartions : '))
op += n
stack,cost,potential = multipop(stack,n,cost,potential)
print(f'Stack after {n} multipops : ',stack)
print(f'Cost after {n} multipops : ',cost)
print(f'Potential after {n} multipops : ',potential)

amortized_cost = potential/op
print('Amortized Cost per operation : ',amortized_cost)    
