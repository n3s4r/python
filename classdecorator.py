import time  # Import the time module to measure execution time

class LogExecutionTime:  # Define a class for the decorator
    def __init__(self, func):  # Initialize the decorator with the function to be decorated
        self.func = func  # Store the function to be decorated

    def __get__(self, instance, owner):  # Define the descriptor method to handle instance methods
        return lambda *args, **kwargs: self(instance, *args, **kwargs)  # Return a lambda that passes the instance

    def __call__(self, *args, **kwargs):  # Make the class instance callable
        instance = args[0]  # Extract the instance from the arguments
        start_time = time.time()  # Record the start time
        result = self.func(instance, *args[1:], **kwargs)  # Call the original function with its arguments
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the execution time
        print(f"Execution time of {self.func.__name__}: {execution_time:.4f} seconds")  # Log the execution time
        return result  # Return the result of the original function call

# Example usage:

class ExampleClass:  # Define an example class to demonstrate the decorator
    @LogExecutionTime  # Apply the decorator to the method
    def example_method(self):  # Define a method in the class
        for _ in range(1000000):  # A sample computation to add some delay
            pass  # Do nothing

# Instantiate the example class and call the decorated method
example = ExampleClass()  # Create an instance of the ExampleClass
example.example_method()  # Call the decorated method to see the execution time log
