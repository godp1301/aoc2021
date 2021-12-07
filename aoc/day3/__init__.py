def most_common_bit_of(values):
    return '0' if len([b for b in values if b == '0']) > len([b for b in values if b == '1']) else '1'


def gamma_rate_of(binary_numbers):
    mcb = []
    for i, v in enumerate(binary_numbers):
        mcb.append([b for b in v])

    v_list = list(zip(*mcb))
    return "".join([most_common_bit_of(v) for v in v_list])