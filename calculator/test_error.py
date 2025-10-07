# Test script with both stdout and stderr
import sys

print("This goes to stdout")
print("Another stdout line", file=sys.stdout)

print("This goes to stderr", file=sys.stderr)
print("Another stderr line", file=sys.stderr)

# Exit with non-zero code to test exit code reporting
sys.exit(1)
