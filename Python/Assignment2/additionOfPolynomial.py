# Function to add two polynomials
def add_polynomials(poly1, poly2):
    max_len = max(len(poly1), len(poly2))
    
    poly1 = [0] * (max_len - len(poly1)) + poly1
    poly2 = [0] * (max_len - len(poly2)) + poly2
    
    result = [poly1[i] + poly2[i] for i in range(max_len)]
    return result

def display_polynomial(poly):
    terms = []
    for i, coef in enumerate(poly):
        if coef != 0:
            power = len(poly) - i - 1
            if power == 0:
                terms.append(f"{coef}")
            elif power == 1:
                terms.append(f"{coef}x")
            else:
                terms.append(f"{coef}x^{power}")
    print(" + ".join(terms))

print("Enter coefficients of the first polynomial (highest power to lowest):")
poly1 = list(map(int, input().split()))

print("Enter coefficients of the second polynomial (highest power to lowest):")
poly2 = list(map(int, input().split()))

result = add_polynomials(poly1, poly2)

print("The resulting polynomial after addition is:")
display_polynomial(result)


# Enter coefficients of the first polynomial (highest power to lowest):
# 3 2 1
# Enter coefficients of the second polynomial (highest power to lowest):
# 5 4 0 2

# The resulting polynomial after addition is:
# 5x^3 + 7x^2 + 2x + 3