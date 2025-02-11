import math

def mod_inverse(num, p):
    for i in range(p):
        product = num * i
        if product % p == 1:
            return i
    return 0

def bsgs(generator, p, h, r):
    iter_limit = math.ceil(math.sqrt(r))
    g_m_inverse = mod_inverse(math.pow(generator, iter_limit), p)

    baby_steps_j = dict()

    for j in range(iter_limit):
        baby_steps_j[f"{j}"] = math.pow(generator, j) % p

    for i in range(iter_limit):
        giant_step = h * math.pow(g_m_inverse, i) % p
        if giant_step in baby_steps_j.values():
            for key in baby_steps_j.keys():
                if baby_steps_j[key] == giant_step:
                    return (int(key) + i * iter_limit) % r

if __name__=="__main__":
    print(mod_inverse(27, 11))
    print(bsgs(3, 11, 5, 5)) # should return 3
    print(bsgs(5, 23, 11, 22)) # should return 9