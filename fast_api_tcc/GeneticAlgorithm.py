import random

# {
#     avgTime: number,
#     carsTotal: number
#     simulatedTime: number,
#     avgSpeed: number,
#     occupationRate: number,
#     iterateNext: boolean,
# }


class GeneticAlgorithm:
    def __init__(self, population: list, selecteds: int = 2, mutation_rate: float = 0.1):
        self.results = []
        self.population = population
        self.mutation_rate: float = mutation_rate
        self.selecteds: int = selecteds

    def crossover(self, total_iterations: int, *parent: list):
        new_population = []

        # Copiando a população original para a nova população
        new_population.extend(self.population)

        while len(new_population) < total_iterations:
            child = []
            for i in range(3):
                all_reds = [par_[i]['redDuration'] for par_ in parent]
                all_greens = [par_[i]['greenDuration'] for par_ in parent]
                all_cycles = [par_[i]['cycleStartTime'] for par_ in parent]
                child.append({
                    'redDuration': random.choice(all_reds),
                    'greenDuration': random.choice(all_greens),
                    'cycleStartTime': random.choice(all_cycles),
                })

            new_population.append(child)
        return new_population

    def mutate(self, individual):
        for semaphore in individual:
            if random.random() < self.mutation_rate:
                semaphore['redDuration'] = random.randint(1, 60)
            if random.random() < self.mutation_rate:
                semaphore['greenDuration'] = random.randint(1, 60)
            if random.random() < self.mutation_rate:
                semaphore['cycleStartTime'] = random.randint(1, 120)
        return individual
