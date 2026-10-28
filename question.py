def rol(value, positions):
    print("\nROL - Rotate Left without Carry")
    print("Original:", format(value, '08b'))

    for i in range(positions):
        msb = (value >> 7) & 1
        value = ((value << 1) & 0xFF) | msb
        print("After rotation", i + 1, ":",
              format(value, '08b'))

    print("Final result:", format(value, '08b'))
    print("Unsigned decimal:", value)


def rcl(value, carry, positions):
    print("\nRCL - Rotate Left with Carry")
    print("Original:", format(value, '08b'))
    print("Initial carry:", carry)

    for i in range(positions):
        msb = (value >> 7) & 1
        value = ((value << 1) & 0xFF) | carry
        carry = msb

        print("After rotation", i + 1, ":",
              format(value, '08b'),
              "Carry =", carry)

    print("Final result:", format(value, '08b'))
    print("Final carry:", carry)
    print("Unsigned decimal:", value)


number = int('10110110', 2)

rol(number, 2)
rcl(number, 0, 2)