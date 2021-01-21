t = int(input())

for i in range(t):
    population_a, population_b, growth_a, growth_b = input().split()
    population_a = int(population_a)
    population_b = int(population_b)
    growth_a = float(growth_a)
    growth_b = float(growth_b)
    year = 0

    while (population_a <= population_b):
        count_population_a = int(population_a * (growth_a / 100.00))

        count_population_b = int(population_b * (growth_b / 100.00))

        year += 1
        population_a += count_population_a
        population_b += count_population_b
        if (year > 100):
            print('Mais de 1 seculo.')
            break

    if (year <= 100):
        print(f'{year} anos.')
