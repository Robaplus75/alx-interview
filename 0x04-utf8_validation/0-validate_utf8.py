#!/usr/bin/python3
""" UTF 8 Validation project"""


def validUTF8(data):
    """
    utf 8 validator
    """
    first_mask = 1 << 7
    num_b = 0
    second_mask = 1 << 6

    for i in data:

        m_byte = 1 << 7

        if num_b == 0:

            while m_byte & i:
                num_b += 1
                m_byte = m_byte >> 1

            if num_b == 0:
                continue

            if num_b == 1 or num_b > 4:
                return False

        else:
            if not (i & first_mask and not (i & second_mask)):
                    return False

        num_b -= 1

    if num_b == 0:
        return True

    return False
