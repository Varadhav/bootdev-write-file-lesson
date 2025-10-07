# Calculator main module
import sys

def main():
    print("Calculator application")
    if len(sys.argv) > 1:
        print(f"Arguments received: {sys.argv[1:]}")
        # Simple calculation example
        try:
            result = eval(sys.argv[1])
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error calculating: {e}")
    return "Hello from main.py"

if __name__ == "__main__":
    main()
