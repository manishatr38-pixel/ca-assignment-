def to_binary(n):
    """Convert a signed integer to 8-bit 2's complement."""
    return format(n & 0xFF, '08b')


def signed_value(binary):
    """Convert an 8-bit binary string to a signed integer."""
    value = int(binary, 2)
    if value >= 128:
        value -= 256
    return value


def subtract(a, b):
    # Subtraction: A - B = A + (-B)
    a_bin = to_binary(a)
    b_bin = to_binary(b)
    neg_b_bin = to_binary(-b)

    a_value = int(a_bin, 2)
    neg_b_value = int(neg_b_bin, 2)

    # Perform 8-bit addition
    total = a_value + neg_b_value
    result_bin = format(total & 0xFF, '08b')
    result = signed_value(result_bin)

    # Signed overflow occurs when same-sign operands
    # produce a result with a different sign.
    sign_a = int(a_bin[0])
    sign_neg_b = int(neg_b_bin[0])
    sign_result = int(result_bin[0])

    overflow = (
        sign_a == sign_neg_b and sign_result != sign_a
    )

    print("A =", a, "Binary:", a_bin)
    print("B =", b, "Binary:", b_bin)
    print("-B Binary:", neg_b_bin)
    print("Addition:", a_bin, "+", neg_b_bin)
    print("Result Binary:", result_bin)
    print("Result Decimal:", result)
    print("Overflow:", "Yes" if overflow else "No")
    print("-" * 40)


print("Expression 1: 45 - (+19)")
subtract(45, 19)

print("Expression 2: (-35) - (-12)")
subtract(-35, -12)