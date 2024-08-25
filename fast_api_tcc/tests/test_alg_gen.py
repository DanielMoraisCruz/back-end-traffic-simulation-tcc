from GeneticAlgorithm import GeneticAlgorithm

velue_red = 60
velue_green = 60
velue_cycle = 120
limit_chenges = 2


def test_crossover_size(population):
    ga = GeneticAlgorithm(population)
    total_iterations = 10
    # Passando a população como pais para garantir que a função tenha dados para trabalhar
    new_population = ga.crossover(total_iterations, *population)
    assert len(new_population) == total_iterations


def test_crossover_structure(population):
    ga = GeneticAlgorithm(population)
    total_iterations = 10
    # Passando a população como pais para garantir que a função tenha dados para trabalhar
    new_population = ga.crossover(total_iterations, *population)

    assert len(new_population) == total_iterations
    # Verifica se cada indivíduo tem 3 semáforos e se cada semáforo tem as chaves corretas
    _test = 3
    for individual in new_population:
        assert len(individual) == _test
        for semaphore in individual:
            assert 'redDuration' in semaphore
            assert 'greenDuration' in semaphore
            assert 'cycleStartTime' in semaphore


def test_mutate_functionality(population):
    mutation_rate = 0.5
    ga = GeneticAlgorithm(population, mutation_rate=mutation_rate)
    individual = population[0]
    original = [dict(semaphore) for semaphore in individual]  # Cópia profunda para comparação
    mutated_individual = ga.mutate(individual)

    # Contar quantos semáforos foram mutados
    changes = sum(
        1
        for original_sem, mutated_sem in zip(original, mutated_individual)
        if original_sem['redDuration'] != mutated_sem['redDuration']
        or original_sem['greenDuration'] != mutated_sem['greenDuration']
        or original_sem['cycleStartTime'] != mutated_sem['cycleStartTime']
    )

    # As mutações devem ocorrer aproximadamente conforme a taxa de mutação definida
    expected_changes = len(individual) * mutation_rate
    tolerance = len(individual) * 0.5  # 50% de tolerância para variabilidade estocástica

    TEXT = f'Expected around {expected_changes} changes, got {changes}'
    assert abs(changes - expected_changes) <= tolerance, TEXT
