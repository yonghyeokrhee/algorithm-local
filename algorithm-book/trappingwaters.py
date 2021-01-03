import copy

# double count for i = 5 and i = 7 because they have same condition

def trapping_water(inputs):
    vol = 0
    for i in range(len(inputs)):
        if i == 0:
            continue
        k = copy.copy(i) - 1
        while inputs[i] >= inputs[k] and k >= 0:
            k -= 1
        j = copy.copy(i) + 1
        while inputs[i] >= inputs[j] and j <= len(inputs):
            j += 1

        if k < 0 or j > len(inputs):
            continue
        else:
            left_bar = inputs[k]
            right_bar = inputs[j]
            vol += (j- k -1) * (min(right_bar, left_bar) - inputs[i])
    print(vol)
    return vol


inputs = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
trapping_water(inputs)
