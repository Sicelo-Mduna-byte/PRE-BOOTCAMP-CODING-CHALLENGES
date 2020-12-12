def sum_of_multiples_of_3_and_10_below_1000():
    answer = 0
    for i in range(0,1000):
        if (i % 3 == 0 or i % 5 == 0):
            answer = answer + i
    return answer

print(sum_of_multiples_of_3_and_10_below_1000())
