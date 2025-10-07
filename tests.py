import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "functions"))
from run_python_file import run_python_file

def test_run_python_file():
    print("Testing run_python_file function...")
    
    # Test 1: Run main.py
    print("\n1. Testing run_python_file(calculator, main.py):")
    result1 = run_python_file("calculator", "main.py")
    print(f"Result: {result1}")
    
    # Test 2: Run main.py with arguments
    print("\n2. Testing run_python_file(calculator, main.py, ['3 + 5']):")
    result2 = run_python_file("calculator", "main.py", ["3 + 5"])
    print(f"Result: {result2}")
    
    # Test 3: Run tests.py
    print("\n3. Testing run_python_file(calculator, tests.py):")
    result3 = run_python_file("calculator", "tests.py")
    print(f"Result: {result3}")
    
    # Test 4: Try to run file outside working directory (should return error)
    print("\n4. Testing run_python_file(calculator, ../main.py):")
    result4 = run_python_file("calculator", "../main.py")
    print(f"Result: {result4}")
    
    # Test 5: Try to run non-existent file (should return error)
    print("\n5. Testing run_python_file(calculator, nonexistent.py):")
    result5 = run_python_file("calculator", "nonexistent.py")
    print(f"Result: {result5}")

if __name__ == "__main__":
    test_run_python_file()
