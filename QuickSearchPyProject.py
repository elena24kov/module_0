#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def find_nb_bisection(nb_to_find):
    # Function implements bisection method to find a randomly allocated number 
    # from 1 to 100 inclusive.
    # First, lower and upper bounds of the search interval 
    # are set to 1 and 100 correspondingly.
    # On each step, the search interval is halved.
    count = 0
    lower_bound = 1
    upper_bound = 100
    while count < 101: # algorythm certainly completes in less than 100 iterations
        count += 1
        cut_point = int((lower_bound + upper_bound)/2)
        if cut_point == nb_to_find:
            break # loop stops when number is found
        # determine part of the search interval to eliminate
        elif cut_point < nb_to_find:
            lower_bound = cut_point + 1
        else:
            upper_bound = cut_point - 1
    return count
        
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # RANDOM SEED is fixed to reproduce the experiment
    random_array = np.random.randint(1,101, size=(1000))
    avg = 0
    for i in range(1000):
        count_ls.append(game_core(random_array[i]))
        avg += count_ls[i]/1000
    score = int(np.mean(count_ls))
    min_attempts = np.min(count_ls)
    max_attempts = np.max(count_ls)
    print("Статистика эксперимента:")
    print(f" Среднее число попыток: {avg}")
    print(f" Было не менее {min_attempts} и не более {max_attempts} попыток")
    print("Требуемый результат:")
    print(f" Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(find_nb_bisection)


# In[ ]:




