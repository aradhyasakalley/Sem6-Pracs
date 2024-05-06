# Accounting method assumes a arbitary cost for every possible operartion higher or lower than the actual cost, and if the assumed cost is greater than the cost needed teh rest is stored as credit and used for the operations that have lesser assumed cost than the actual ones.
# At any point the sum of assumed (amortized) costs is greater than or equal to the sum of actual costs

# As opposed to the actual cost 1
push_amor_cost = 2
push_actual_cost = 1
# As opposed to the actual cost 1 
pop_amor_cost = 0  
pop_actual_cost = 1

def push(stack,n,cost,credit):
    for i in range(n):
        stack.append(i)
        if push_amor_cost >= push_actual_cost:
            cost += push_amor_cost
            credit += (push_amor_cost-push_actual_cost)
            print('Credit added : ',credit)
        else:
            cost += push_amor_cost
            credit -= push_actual_cost
            print('Credit consumed : ')
    return stack,cost,credit
    
def multipop(stack,n,cost,credit):
    for i in range(n):
        m = int(input('Enter the number of elements to multipop : '))
        for i in range(min(m,len(stack))):
            stack.pop()
            if pop_amor_cost >= pop_actual_cost:
                cost += pop_amor_cost
                credit += (pop_amor_cost-pop_actual_cost)
                print('Credit added : ',credit)
            else:
                cost += pop_amor_cost
                credit -= pop_actual_cost
                print('Credit consumed : ',credit)
    return stack,cost,credit

stack = []
cost = 0
op = 0
credit = 0

n = int(input('Enter the number of elements to push : '))
op += n
stack,cost,credit = push(stack,n,cost,credit)
print(f'Stack after {n} push operations : ',stack)
print(f'Cost after {n} push operations : ',cost)
print(f'Credit after push operations : ',credit)


n = int(input('Enter the number of Multipop opeartions : '))
op += n
stack,cost,credit = multipop(stack,n,cost,credit)
print(f'Stack after {n} multipops : ',stack)
print(f'Cost after {n} multipops : ',cost)
print(f'Credit after multipops operations : ',credit)

amortized_cost = cost/op
print('Amortized Cost per operation : ',amortized_cost)

