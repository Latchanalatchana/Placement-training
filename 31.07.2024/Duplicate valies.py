def print_duplicates(lst):
    duplicates = set()
    seen = set()
    for num in lst:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    for dup in duplicates:
        print(dup)

if __name__ == "__main__":
    lst = list(map(int, input("Enter the list of integers separated by space: ").split()))
    print_duplicates(lst)
