import AP_03_ordenacao as alg
import time
import random
import sys

sys.setrecursionlimit(10000)

runs = 100
sample_sizes = [100, 500, 1000, 5000]
algorithms = ["selection_sort", "divide_and_conquer_sort", "quick_sort"]
scenarios = ["Random", "Worst Case"]

benchmark_results = {
    algo: {
        scenario: {size: 0.0 for size in sample_sizes} 
        for scenario in scenarios
    } 
    for algo in algorithms
}

def print_ascii_table(data):
    first_algo = list(data.keys())[0]
    first_scenario = list(data[first_algo].keys())[0]
    sizes = list(data[first_algo][first_scenario].keys())
    
    algo_width = 24
    scenario_width = 11
    col_width = 9
    
    header = f"| {'Algorithm':<{algo_width}} | {'Scenario':<{scenario_width}} "
    for size in sizes:
        header += f"| N={size:<{col_width-2}} "
    header += "|"
    
    separator = "-" * len(header)
    
    print(separator)
    print(header)
    print(separator)
    
    for algo, scenarios in data.items():
        for scenario, times in scenarios.items():
            row = f"| {algo:<{algo_width}} | {scenario:<{scenario_width}} "
            for size in sizes:
                time_val = times.get(size, 0)
                row += f"| {time_val:<{col_width}.6f} "
            row += "|"
            print(row)
        print(separator)

def random_test_cases(n, k):
    return [[random.randint(1, n+1) for _ in range(n)] for _ in range(k)]

def benchmarking(func, test_cases, alg_name, scenario):
    runs = len(test_cases)
    total_time = 0.0

    for i in range(runs):
        status_text = f"{alg_name} ({scenario}) Testing - {i + 1}/{runs}"    
        print(f"\r{status_text.ljust(60)}", end="", flush=True)

        data = test_cases.pop()
        start_time = time.perf_counter()
        func(data)
        end_time = time.perf_counter()
        total_time += (end_time - start_time)

    return total_time / runs

def benchmark_algorithms(algorithms, sample_sizes, runs, benchmark_results):
    for size in sample_sizes:   
        master_random_cases = [random_test_cases(size, runs) for _ in range(runs)]
        master_worst_cases = [list(range(size, 0, -1)) for _ in range(runs)]

        for alg_name in algorithms:
            func = getattr(alg, alg_name)
            
            random_data = [case.copy() for case in master_random_cases]
            worst_case_data = [case.copy() for case in master_worst_cases]
            
            benchmark_results[alg_name]["Random"][size] = benchmarking(func, test_cases=random_data, alg_name=alg_name, scenario="Random")
            benchmark_results[alg_name]["Worst Case"][size] = benchmarking(func, test_cases=worst_case_data, alg_name=alg_name, scenario="Worst Case")

    print("")
    print_ascii_table(benchmark_results)

# Test
benchmark_algorithms(algorithms, sample_sizes, runs, benchmark_results)