from mcp_hello_world import HelloWorldModel
from typing import Optional, Tuple

class CursorIntegration:
    def __init__(self):
        self.model = None
        self.current_position = 0
    
    def initialize_at_position(self, position: int) -> None:
        """
        Step 1: Initialize the model at a specific cursor position
        
        Args:
            position (int): The current cursor position in the editor
        """
        self.current_position = position
        self.model = HelloWorldModel(cursor_position=position)
    
    def insert_hello_world(self) -> Tuple[str, int]:
        """
        Step 2: Insert hello world at current cursor position
        
        Returns:
            Tuple[str, int]: The text to insert and the new cursor position
        """
        if not self.model:
            raise RuntimeError("Model not initialized. Call initialize_at_position first.")
        
        text = self.model.display_hello_world()
        new_position = self.current_position + len(text)
        self.model.set_cursor_position(new_position)
        return text, new_position
    
    def insert_hello_world_with_name(self, name: str) -> Tuple[str, int]:
        """
        Step 3: Insert personalized hello world at current cursor position
        
        Args:
            name (str): Name to include in the greeting
            
        Returns:
            Tuple[str, int]: The text to insert and the new cursor position
        """
        if not self.model:
            raise RuntimeError("Model not initialized. Call initialize_at_position first.")
        
        text = self.model.display_hello_world_with_name(name)
        new_position = self.current_position + len(text)
        self.model.set_cursor_position(new_position)
        return text, new_position

def example_usage():
    """
    Example of how to use the cursor integration
    """
    # Step 1: Create the integration instance
    integration = CursorIntegration()
    
    # Step 2: Initialize at current cursor position (e.g., position 10)
    integration.initialize_at_position(10)
    
    # Step 3: Insert hello world
    text, new_pos = integration.insert_hello_world()
    print(f"Inserted text: {text}")
    print(f"New cursor position: {new_pos}")
    
    # Step 4: Insert hello world with name
    text, new_pos = integration.insert_hello_world_with_name("Alice")
    print(f"Inserted text: {text}")
    print(f"New cursor position: {new_pos}")

if __name__ == "__main__":
    example_usage() 