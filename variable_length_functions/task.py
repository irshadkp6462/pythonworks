def second_largest(*args):

    sorted_number=sorted(args,reverse=True)

    return sorted_number[1]

print(second_largest(23,45,56,47,12))

