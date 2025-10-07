import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "functions"))
from write_file import write_file

def test_write_file():
    print("Testing write_file function...")
    
    # Test 1: Write to lorem.txt
    print("\n1. Testing write_file(calculator, lorem.txt, wait, this isn't lorem ipsum):")
    result1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(f"Result: {result1}")
    
    # Test 2: Write to pkg/morelorem.txt
    print("\n2. Testing write_file(calculator, pkg/morelorem.txt, lorem ipsum dolor sit amet):")
    result2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f"Result: {result2}")
    
    # Test 3: Try to write outside working directory (should return error)
    print("\n3. Testing write_file(calculator, /tmp/temp.txt, this should not be allowed):")
    result3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(f"Result: {result3}")

if __name__ == "__main__":
    test_write_file()
