import os
from typing import List
from mcp.server.fastmcp import FastMCP

TEXT_DIR = "text_files"
os.makedirs(TEXT_DIR, exist_ok=True)

# Initialize FastMCP server
mcp = FastMCP("textops")

@mcp.tool()
def create_file(filename: str, content: str = "") -> str:
    """
    Create a new .txt file with given content.
    
    Args:
        filename: Name of the file (without extension)
        content: Initial content to write
        
    Returns:
        Status message
    """
    filepath = os.path.join(TEXT_DIR, f"{filename}.txt")
    if os.path.exists(filepath):
        return f"File '{filename}.txt' already exists."

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    return f"File '{filename}.txt' created successfully."

@mcp.tool()
def append_to_file(filename: str, content: str) -> str:
    """
    Append content to an existing .txt file.
    
    Args:
        filename: Name of the file (without extension)
        content: Text to append
        
    Returns:
        Status message
    """
    filepath = os.path.join(TEXT_DIR, f"{filename}.txt")
    if not os.path.exists(filepath):
        return f"File '{filename}.txt' does not exist."

    with open(filepath, "a", encoding="utf-8") as f:
        f.write("\n" + content)
    
    return f"Appended content to '{filename}.txt'."

@mcp.tool()
def read_file(filename: str) -> str:
    """
    Read and return the content of a .txt file.
    
    Args:
        filename: Name of the file (without extension)
        
    Returns:
        File contents or error
    """
    filepath = os.path.join(TEXT_DIR, f"{filename}.txt")
    if not os.path.exists(filepath):
        return f"File '{filename}.txt' does not exist."
    
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

@mcp.tool()
def delete_file(filename: str) -> str:
    """
    Delete a .txt file.
    
    Args:
        filename: Name of the file (without extension)
        
    Returns:
        Status message
    """
    filepath = os.path.join(TEXT_DIR, f"{filename}.txt")
    if not os.path.exists(filepath):
        return f"File '{filename}.txt' does not exist."
    
    os.remove(filepath)
    return f"File '{filename}.txt' has been deleted."

if __name__ == "__main__":
    mcp.run(transport="stdio")
