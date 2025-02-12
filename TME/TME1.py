import os

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def process_numbers_file(filename):
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found. Creating file with sample data...")
        with open(filename, "w") as f:
            f.write("10,20,30,17\n1,2,3,4,5\n50,60,33,22,6\n101,202,303,404,505\n")
        print(f"File '{filename}' created. Please rerun the script.")
        return
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    for i, line in enumerate(lines, 1):
        line = line.strip()
        if not line:
            continue  
        
        try:
            numbers = list(map(int, line.replace(" ", "").split(',')))
            total = sum(numbers)
            result = "Palindrome" if is_palindrome(total) else "Not a palindrome"
            print(f"Line {i}: {', '.join(map(str, numbers))} (sum {total}) - {result}")
        except ValueError:
            print(f"Line {i}: Invalid line format. Ensure numbers are comma-separated.")

if __name__ == "__main__":
    print("Checking sum palindrome from numbers.txt:")
    process_numbers_file("numbers.txt")
