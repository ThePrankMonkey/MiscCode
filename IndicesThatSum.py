# Matthew Hellmer
# 2017.06.14
# IndicesThatSum.py


#############
# Functions #
#############
def calculate_combinations(values, goal):
    # reset the global match variable
    global Matches
    Matches = []
    
    Get_Results(values, goal, [], 0, len(values))

    if Matches == []:
        # I assume we want to capture when a solution isn't found
        print("No combination exists")
        return None
    else:
        for match in Matches:
            print(match)
    print()
    return Matches


def Get_Results(values, goal, checks, cur, valMax):
    # Recursively search for matches
    global Matches
    total = 0
    for check in checks:
        total = total + values[check]
    if total == goal:
        Matches.append(checks)
    if total >= goal:
        # Terminates once it surpasses goal, as further calculations are wasteful
        return

    for num in range(cur, valMax):
        newChecks = checks[:]
        newChecks.append(num)
        Get_Results(values, goal, newChecks, num+1, valMax)



#############
# Test Data #
#############
# Test 1: [5, 5, 15, 10], 15
# Example 1
print("Test 1 Results:")
test1 = calculate_combinations([5, 5, 15, 10], 15)

# Test 2: [1, 2, 3, 4], 6
# Example 2
print("Test 2 Results:")
test2 = calculate_combinations([1, 2, 3, 4], 6)

# Test 3: [3, 4, 5, 5], 6
# No matches example
print("Test 3 Results:")
test3 = calculate_combinations([3, 4, 5, 5], 6)

# Test 4: [10, 10, 10, 10, 10, 10, 10, 10, 10, 10], 100
# Longer set example
print("Test 4 Results:")
test4 = calculate_combinations([10, 10, 10, 10, 10, 10, 10, 10, 10, 10], 100)
