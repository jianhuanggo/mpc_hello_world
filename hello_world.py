def display_hello_world():
    """
    Function to display a simple Hello World message
    """
    print("Hello World!")

def display_hello_world_with_name(name):
    """
    Function to display Hello World with a given name
    
    Args:
        name (str): The name to be displayed in the greeting
    """
    print(f"Hello World, {name}!")

# Example usage
if __name__ == "__main__":
    # Test the first function
    print("Testing first function:")
    display_hello_world()
    
    # Test the second function
    print("\nTesting second function:")
    display_hello_world_with_name("Alice") 