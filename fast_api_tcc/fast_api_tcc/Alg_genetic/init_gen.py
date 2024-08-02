import random

from deap import algorithms, base, creator, tools


# Classe que encapsula o algoritmo genético
class GeneticAlgorithm:
    def __init__(self, num_simulations, num_agents, num_generations):
        self.num_simulations = num_simulations  # Número de simulações
        self.num_agents = num_agents  # Número de agentes em cada indivíduo
        self.num_generations = num_generations  # Número de gerações

        # Define o tipo de fitness e o tipo de indivíduo
        creator.create('FitnessMax', base.Fitness, weights=(1.0,))
        creator.create('Individual', list, fitness=creator.FitnessMax)

        # Cria a toolbox com as funções básicas
        self.toolbox = base.Toolbox()
        self.toolbox.register('attr_bool', random.randint, 0, 1)
        self.toolbox.register(
            'individual', tools.initRepeat, creator.Individual, self.toolbox.attr_bool, num_agents
        )
        self.toolbox.register('population', tools.initRepeat, list, self.toolbox.individual)
        self.toolbox.register('evaluate', self.evalOneMax)
        self.toolbox.register('mate', tools.cxTwoPoint)
        self.toolbox.register('mutate', tools.mutFlipBit, indpb=0.05)
        self.toolbox.register('select', tools.selTournament, tournsize=3)

        # Inicializa a população
        self.population = self.toolbox.population(n=num_simulations)

    # Função de avaliação que simplesmente soma os valores dos genes
    @staticmethod
    def evalOneMax(individual):
        return (sum(individual),)

    # Método principal que executa o algoritmo genético
    def run(self, simulation_results=None):
        # Se houver resultados de simulação, atualiza o fitness dos indivíduos
        if simulation_results:
            self.update_fitness(simulation_results)

        # Retorna os melhores indivíduos após todas as gerações
        return self.get_best_individuals()

    def execution(self):
        # Aplica cruzamento e mutação para criar novos indivíduos
        offspring = algorithms.varAnd(self.population, self.toolbox, cxpb=0.5, mutpb=0.2)
        # Avalia os novos indivíduos
        fits = map(self.toolbox.evaluate, offspring)
        for fit, ind in zip(fits, offspring):
            ind.fitness.values = fit
        # Seleciona os melhores indivíduos para a próxima geração
        self.population = self.toolbox.select(offspring, k=len(self.population))

    # Método para atualizar o fitness dos indivíduos com base nos resultados das simulações
    def update_fitness(self, simulation_results):
        for ind, result in zip(self.population, simulation_results):
            ind.fitness.values = result

    # Método para obter os melhores indivíduos da população
    def get_best_individuals(self):
        return sorted(self.population, key=lambda ind: ind.fitness.values, reverse=True)


# Exemplo de uso:
if __name__ == '__main__':
    num_simulations = 300  # Número de simulações
    num_agents = 100  # Número de agentes em cada indivíduo
    num_generations = 40  # Número de gerações

    # Inicializa o algoritmo genético
    ga = GeneticAlgorithm(num_simulations, num_agents, num_generations)

    # Suponha que recebemos alguns resultados de simulações anteriores
    simulation_results = [(random.random(),) for _ in range(num_simulations)]

    # Executar o algoritmo genético com os resultados de simulação fornecidos
    best_individuals = ga.run(simulation_results)

    # Obter os melhores indivíduos para a próxima simulação
    novos_parametros = [ind for ind in best_individuals]
    print('Novos parâmetros para a próxima simulação:', novos_parametros)
