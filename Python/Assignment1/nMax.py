def nMax(*args):
    if not args:
        return "No numbers provided"
    return max(args)

print(nMax(5, 10, 3, 8))
