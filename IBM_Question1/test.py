def num_solutions(math_problems, threshold, start_index=0):
    num_solutions = 1
    min_point = math_problems[start_index]
    max_point = math_problems[start_index]
    i = start_index + 1
    while i < len(math_problems):
        diff_min = math_problems[i] - min_point
        diff_max = math_problems[i] - max_point
        if diff_min >= threshold or diff_max >= threshold:
            break
        if i + 1 >= len(math_problems):
            i += 1
        elif math_problems[i+1] - min_point > math_problems[i+1] - max_point:
            i += 1
        else:
            i += 2
        min_point = min(min_point, math_problems[i])
        max_point = max(max_point, math_problems[i])
        num_solutions += 1
    return num_solutions


# It is a 2 player game
# Each player take turn picking a number from the array. 
# If a player picks an even number the array reverses the order. 
# Who ever has the most points wins
# Return the score of the fisrt player minus the score of the second player.
