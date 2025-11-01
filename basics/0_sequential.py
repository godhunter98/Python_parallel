from time import perf_counter



def sum_of_squares(n):
    return sum(i*i for i in range(n))

nums = [10_00_0000,20_00_0000,30_00_0000,40_00_0000] #large calculations

a = perf_counter()
results = [sum_of_squares(n) for n in nums] #runs sequentially
b = perf_counter() 
print(results,f"\nIt took {(b-a):.2f} seconds to run!")