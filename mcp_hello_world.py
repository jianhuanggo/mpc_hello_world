from typing import Optional

class HelloWorldContext:
    """Context class that maintains the state and behavior for hello world operations"""
    def __init__(self):
        self._greeting = "Hello World"
        self._name = None
        self._cursor_position = 0
        
    @property
    def greeting(self):
        return self._greeting
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        
    @property
    def cursor_position(self):
        return self._cursor_position
    
    @cursor_position.setter
    def cursor_position(self, value: int):
        self._cursor_position = max(0, value)

class HelloWorldModel:
    """Model class that implements the business logic"""
    def __init__(self, cursor_position: int = 0):
        self.context = HelloWorldContext()
        self.context.cursor_position = cursor_position
    
    def display_hello_world(self) -> str:
        """
        Function to display a simple Hello World message
        Returns:
            str: The hello world message
        """
        return self.context.greeting + "!"
    
    def display_hello_world_with_name(self, name: str) -> str:
        """
        Function to display Hello World with a given name
        
        Args:
            name (str): The name to be displayed in the greeting
        Returns:
            str: The personalized hello world message
        """
        self.context.name = name
        return f"{self.context.greeting}, {self.context.name}!"
    
    def get_cursor_position(self) -> int:
        """Get the current cursor position"""
        return self.context.cursor_position
    
    def set_cursor_position(self, position: int):
        """Set the cursor position"""
        self.context.cursor_position = position

def main():
    # Create model instance with initial cursor position
    model = HelloWorldModel(cursor_position=0)
    
    # Test the first function
    print("Testing first function:")
    result = model.display_hello_world()
    print(result)
    
    # Test the second function
    print("\nTesting second function:")
    result = model.display_hello_world_with_name("Alice")
    print(result)
    
    # Demonstrate cursor position tracking
    print(f"\nCurrent cursor position: {model.get_cursor_position()}")
    model.set_cursor_position(10)
    print(f"Updated cursor position: {model.get_cursor_position()}")

if __name__ == "__main__":
    main() 