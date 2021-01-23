import copy
import time
start_time = time.time()

# double count for i = 5 and i = 7 because they have same condition
# unnecessary second while loop after first loop condition not met - waste of time
def trapping_water(inputs):
    vol = 0
    record = []
    max = len(inputs)
    for i in range(len(inputs) - 1):
        if i == 0:
            continue
        # running loop
        k = copy.copy(i) - 1
        j = copy.copy(i) + 1

        while inputs[i] >= inputs[k] and k >= 0:
            k -= 1
            if k == -1:
                break
        # end for k loop
        # give a condition only if k > 0
        if k != -1:
            # start of j loop
            while inputs[i] >= inputs[j] and j <= len(inputs):
                j += 1
                if j == max:
                    break
            if not (k > 0 and j < len(inputs)):
                continue
            else:
                if k not in record:
                    left_bar = inputs[k]
                    right_bar = inputs[j]
                    vol += (j - k - 1) * (min(right_bar, left_bar) - inputs[i])
                    record.append(k)
                else:
                    pass
        else:
            print("k was -1")
            pass
    print(vol)
    return vol


inputs = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
trapping_water(inputs)
print("--- %s seconds ---" % (time.time() - start_time))
