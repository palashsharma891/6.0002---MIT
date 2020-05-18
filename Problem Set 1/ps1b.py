# EXCEPT FOR THE MEMOIZATION, I HONESTLY DO NOT UNDERSTAND HOW THIS IS 
# ANY DIFFERENT FROM GREEDY, BECAUSE WE ARE TAKING THE HEAVUEST EGG FIRST
# IF YOU KNOW WHY, PLEASE HELP ME OUT!



###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # Analogy to 0/1 Knapsack.
    # Value is the
    # Weight is the actual weight(kilograms, pounds, etc.)
    # Weight limit is targest_weight
    
    # ITERATIVE
    egg_weights = sorted(egg_weights, reverse=True)
    result = 0
    total_eggs = 0
    available_weight = target_weight
    for weight in egg_weights:
        if available_weight > 0:            
            num_eggs = available_weight // weight # number of eggs with weight*number <= available weight
            #print(num_eggs) # debugging
            total_eggs = total_eggs + num_eggs
            remaining_weight = available_weight % weight
            #print(remaining_weight, 'oo') # debugging
            available_weight = remaining_weight
            
        else: # stop if knapsack is full
            break
        
    return total_eggs

    # RECURSIVE
    egg_weights = tuple(sorted(egg_weights, reverse=True))    
    
    total_eggs = 0
    available_weight = target_weight
    
    if egg_weights in memo: # MEMOIZATION
        return memo[egg_weights]

    elif len(egg_weights) == 1: # since we are guaranteed to have an egg of value 1
        return egg_weights[0] * target_weight

    else:
        num_eggs = available_weight // egg_weights[0] # number of eggs with weight*number <= available weight
        #print(num_eggs) #debugging
        remaining_weight = available_weight % egg_weights[0]
        #print(remaining_weight, 'oo') # debugging
        available_weight = remaining_weight
        memo[egg_weights[0]] = num_eggs
        total_eggs = total_eggs + memo[egg_weights[0]] + dp_make_weight(egg_weights[1:], remaining_weight, memo)
    
    return total_eggs  

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25, 35)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
