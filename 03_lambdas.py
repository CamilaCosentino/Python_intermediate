##### Lambdas #####
# el concepto de lambdas son como función pero con una peculiariada muy concreta, son anónimas.
# se puede igualar a una variable.
sum_two_values = lambda first_value , second_value: first_value + second_value
print(sum_two_values(2,4))

multiply_values = lambda  first_value , second_value: first_value * second_value - 3
print(multiply_values(3,5))


def sum_three_values(three_value):
    return lambda first_value , second_value: first_value + second_value + three_value

print(sum_three_values(4)(4,4))

