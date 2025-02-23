import numpy as np
import random

# Bước 1: Tạo lớp NST
class Chromosome:
    def __init__(self, genes):
        self.genes = genes
        self.cost = self.calculate_cost()

    def calculate_cost(self):
        cost = 0
        for i in range(len(self.genes) - 1):        # Duyệt từng thành phố
            cost += distance_matrix[self.genes[i]][self.genes[i+1]]
        cost += distance_matrix[self.genes[-1]][self.genes[0]]  # Quay lại thành phố ban đầu
        return cost
    
# Bước 2: Khởi tạo quần thể (mỗi chromosome là một hành trình qua các thành phố)
def initialize_population(population_size, num_cities):
    population = []     # Lưu trữ quần thể (chứa nhiều cá thể - giải pháp)
    for _ in range(population_size):
        genes = list(range(num_cities))
        random.shuffle(genes)
        population.append(Chromosome(genes))
    return population

# Bước 3: Chọn lọc các chromosomes tốt nhất trong quần thể để tiến hành giao phối
def selection(population):
    population.sort(key=lambda x: x.cost)
    return population[:len(population)//2]
    # Chỉ lấy nửa đầu tốt nhất để thực hiện tiếp

# Bước 4: Lai ghép
def crossover(parent1, parent2, pc):
    if random.random() < pc:
        genes1, genes2 = parent1.genes[:len(parent1.genes)//2], parent2.genes[len(parent2.genes)//2:]
        child_genes = genes1 + genes2
        return Chromosome(child_genes)
    else:
        return random.choice([parent1, parent2])

# Bước 5: Đột biến
def mutate(chromosome, pm):
    # Hoán đổi vị trí 2 gen trong chuỗi gen của nó  
    if random.random() < pm:
        idx1, idx2 = random.sample(range(len(chromosome.genes)), 2) # Chọn ngẫu nhiên
        chromosome.genes[idx1], chromosome.genes[idx2] = chromosome.genes[idx2], chromosome.genes[idx1]


# Bước 6: Thực hiện thuật toán GA
def genetic_algorithm(population_size, num_cities, num_generations, pc, pm):
    # Khởi tạo quần thể
    population = initialize_population(population_size, num_cities)     
    
    # Lặp qua số thế hệ
    for _ in range(num_generations):
        selected = selection(population)        # Lựa chọn phương pháp chọn lọc

        for _ in range(num_generations):
            selected = selection(population)
            offspring = []
            while len(offspring) < len(population) - len(selected):
                parent1, parent2 = random.sample(selected, 2)
                child = crossover(parent1, parent2, pc)
                mutate(child, pm)
                offspring.append(child)
            population = selected + offspring
        best_solution = min(population, key=lambda x: x.cost)
        return best_solution

if __name__ == "__main__":
    distance_matrix = [
        [0, 2, 9, 10, 1],  # Khoảng cách từ thành phố 0 đến các thành phố khác
        [1, 0, 6, 4, 8],  # Khoảng cách từ thành phố 1 đến các thành phố khác
        [2, 7, 0, 8, 3],  # Khoảng cách từ thành phố 2 đến các thành phố khác
        [3, 5, 8, 0, 2],  # Khoảng cách từ thành phố 3 đến các thành phố khác
        [10, 8, 4, 2, 0]  # Khoảng cách từ thành phố 4 đến các thành phố khác
    ]


    N = 10  # Kích thước quần thể
    generation = 100  # Số thế hệ
    pc = 0.7  # Xác suất lai ghép
    pm = 0.1  # Xác suất đột biến
    num_cities = 5  # Giả sử có 5 thành phố, cần cung cấp distance_matrix

    # Chạy thuật toán GA với các thông số đã cho
    best_solution = genetic_algorithm(N, num_cities, generation, pc, pm)

    print("Lời giải tốt nhất tìm được:")
    print("Hành trình:", best_solution.genes)
    print("Tổng khoảng cách:", best_solution.cost)
