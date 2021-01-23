import copy
import time

start_time = time.time()


def trapping_water(inputs):
    # local variables
    vol = 0
    record = []
    end = len(inputs)

    # outer loop
    for i in range(len(inputs) - 1):
        if i == 0:
            print("skip 0 index")
            continue
        # running loop
        k = copy.copy(i) - 1
        j = copy.copy(i) + 1

        while inputs[i] >= inputs[k] and k >= 0:
            k -= 1
            if k == -1:
                print("k was -1")
                print("skip j inner loop and k was %s" % k)
                break
        # end for k loop
        # start of j inner loop
        else:
            print("=============")
            print("j inner loop started and i was %s" % i)
            while inputs[i] >= inputs[j] and j <= len(inputs):
                j += 1
                if j == end:
                    break
            if not (k > 0 and j < len(inputs)):
                continue
            else:
                if k not in record:
                    left_bar = inputs[k]
                    right_bar = inputs[j]
                    vol += (j - k - 1) * (min(right_bar, left_bar) - inputs[i])
                    record.append(k)

    print(vol)
    return vol


inputs = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
trapping_water(inputs)
print("--- %s seconds ---" % (time.time() - start_time))
