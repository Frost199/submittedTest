
U = 6  # 1 0 1 1 1 1 0
L = 3  # 1 0 0 1 0 1 1
C = [2, 0, 1, 2, 1, 2, 1]


def checker(u, l, c):
    u_counter = []
    l_counter = []
    valid = u + l
    if valid > sum(c) or valid < sum(c):
        return "IMPOSSIBLE"
    else:
        for i in c:
            if i == 2:
                if sum(u_counter) >= u:
                    u_counter.append(0)
                else:
                    u_counter.append(1)
                if sum(l_counter) >= l:
                    l_counter.append(0)
                else:
                    l_counter.append(1)
            if i == 1:
                if l > u:
                    if sum(l_counter) >= l:
                        l_counter.append(0)
                        u_counter.append(1)
                    else:
                        l_counter.append(1)
                        u_counter.append(0)
                else:
                    if sum(u_counter) >= u:
                        u_counter.append(0)
                        l_counter.append(1)
                    else:
                        u_counter.append(1)
                        l_counter.append(0)

            if i == 0:
                u_counter.append(0)
                l_counter.append(0)

        u_counter_string = ''.join(str(i) for i in u_counter)
        l_counter_string = ''.join(str(i) for i in l_counter)

        return "{}, {}".format(u_counter_string, l_counter_string)


print(checker(U, L, C))
