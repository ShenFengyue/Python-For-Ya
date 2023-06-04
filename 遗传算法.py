'''
以下为Python遗传算法示例
'''

import random

# 设置种群大小和基因长度
POPULATION_SIZE = 10
GENE_LENGTH = 5

# 设置交叉概率和变异概率
CROSSOVER_RATE = 0.7
MUTATION_RATE = 0.1

# 初始化种群
def create_population():
    population = []
    for i in range(POPULATION_SIZE):
        chromosome = [random.randint(0, 1) for _ in range(GENE_LENGTH)]
        population.append(chromosome)
    return population

# 计算适应度
def calculate_fitness(chromosome):
    return sum(chromosome)

# 选择
def selection(population):
    fitness_list = [calculate_fitness(chromosome) for chromosome in population]
    total_fitness = sum(fitness_list)
    probability_list = [fitness / total_fitness for fitness in fitness_list]
    roulette_wheel = []
    cum_probability = 0
    for probability in probability_list:
        cum_probability += probability
        roulette_wheel.append(cum_probability)
    selected_population = []
    for _ in range(POPULATION_SIZE):
        random_number = random.random()
        for i in range(len(roulette_wheel)):
            if random_number <= roulette_wheel[i]:
                selected_population.append(population[i])
                break
    return selected_population

# 交叉
def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        crossover_point = random.randint(0, GENE_LENGTH - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2
    else:
        return parent1, parent2

# 变异
def mutation(chromosome):
    mutated_chromosome = chromosome.copy()
    for i in range(GENE_LENGTH):
        if random.random() < MUTATION_RATE:
            mutated_chromosome[i] = 1 - mutated_chromosome[i]
    return mutated_chromosome

# 遗传算法主函数
def genetic_algorithm():
    # 创建初始种群
    population = create_population()

    # 迭代
    for _ in range(100):
        # 选择
        selected_population = selection(population)

        # 交叉
        offspring_population = []
        for i in range(0, POPULATION_SIZE, 2):
            parent1, parent2 = selected_population[i], selected_population[i+1]
            child1, child2 = crossover(parent1, parent2)
            offspring_population.append(child1)
            offspring_population.append(child2)

        # 变异
        mutated_population = [mutation(chromosome) for chromosome in offspring_population]

        # 生成下一代种群
        population = mutated_population

    # 找到适应度最高的个体
    fitness_list = [calculate_fitness(chromosome) for chromosome in population]
    best_index = fitness_list.index(max(fitness_list))
    best_chromosome = population[best_index]

    return best_chromosome

# 测试
best_chromosome = genetic_algorithm()
print("最优个体：", best_chromosome)
