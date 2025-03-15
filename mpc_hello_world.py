from mpyc.runtime import mpc
import sys

async def display_hello_world():
    """
    Function to display a simple Hello World message in MPC setting
    """
    await mpc.output("Hello World!")

async def display_hello_world_with_name(name):
    """
    Function to display Hello World with a given name in MPC setting
    
    Args:
        name (str): The name to be displayed in the greeting
    """
    # In MPC, we treat the name as a secret shared string
    secret_name = mpc.input(name)
    name_revealed = await mpc.output(secret_name)
    await mpc.output(f"Hello World, {name_revealed}!")

async def main():
    # Initialize the MPC runtime
    await mpc.start()

    # Test the first function
    print("Testing first function:")
    await display_hello_world()
    
    # Test the second function
    print("\nTesting second function:")
    await display_hello_world_with_name("Alice")

    # Shutdown the MPC runtime
    await mpc.shutdown()

if __name__ == "__main__":
    mpc.run(main()) 