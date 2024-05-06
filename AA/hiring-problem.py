# The hiring problem simulates a hiring agency that interviews and hires candidates on your behalf, there is an interview cost ci and a hiring cost ch attached to each of them, at any point the best candidate is hired, we need to compute the total cost incurred by the company
import random

def hiring_problem(candidates):
    hiring_cost = 10
    interview_cost = 5
    pay_per_day  = 2
    current_best = 0
    days_worked = 1
    candidates_interviewed = 0
    cost = 0  
    for candidate in candidates:
        if candidate > current_best:
            current_best = candidate
            hiring_new_cost = interview_cost + hiring_cost
            firing_current_cost = days_worked * pay_per_day
            cost += hiring_new_cost + firing_current_cost  
            days_worked = 0
        else:
            cost += interview_cost
            days_worked += 1
        candidates_interviewed += 1
    return cost, candidates_interviewed


# Worst Case
# candidates = [1,2,3,4,5,6,7,8,9,10]
# Best Case
# candidates = [10,9,8,7,6,5,4,3,2,1]
# Average Case
candidates = random.sample(range(1, 11), 10)
print(candidates)
cost, candidates_interviewed = hiring_problem(candidates)
print("Total cost:", cost)
print("Candidates interviewed:", candidates_interviewed)
# The formula cost should be equal to or greater than equal to total cost ????
formula_cost = 10*5 + candidates_interviewed*10
print(formula_cost)
