# ÖRNEK 1
import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Executed {func.__name__} in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@log_execution_time
def process_data(data):
    time.sleep(2)  # Simulating a time-consuming process
    return f"Processed {len(data)} records"

print(process_data([1, 2, 3, 4, 5]))

print("#"*70)

# ÖRNEK 2
def log_params(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_params
def multiply(a, b):
    return a * b

@log_params
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

if __name__ == "__main__":
    print(multiply(3, 4))
    print(greet("Alice"))
    print(greet("Bob", greeting="Hi"))

