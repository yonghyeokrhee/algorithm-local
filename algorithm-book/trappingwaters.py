import copy

# double count for i = 5 and i = 7 because they have same condition
# unnecessary second while loop after first loop condition not met - waste of time
def trapping_water(inputs):
    vol = 0
    record = []
    for i in range(len(inputs)):
        if i == 0:
            continue
        k = copy.copy(i) - 1
        while inputs[i] >= inputs[k] and k >= 0:
            k -= 1
        if k == -1:
            continue
        j = copy.copy(i) + 1
        try:
            while inputs[i] >= inputs[j] and j <= len(inputs):
                j += 1
        except IndexError as e:
            print('out of index')
            continue

        if not (k > 0 or j < len(inputs)):
            continue
        else:
            if k not in record:
                left_bar = inputs[k]
                right_bar = inputs[j]
                vol += (j- k -1) * (min(right_bar, left_bar) - inputs[i])
                record.append(k)
            else:
                pass
    print(vol)
    return vol


inputs = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
trapping_water(inputs)
