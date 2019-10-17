def reorder_list(v, cols):
    n = len(v)
    mod = n % cols
    rows = n // cols
    v_new = [0 for i in range(n)]
    for i in range(mod):
        for j in range(rows + 1):
            v_new[j * cols + i] = v[i * (rows + 1) + j]
    for i in range(0, cols - mod):
        for j in range(rows):
            if mod * (rows + 1) + i * rows + j < n:
                if  j * cols + i + mod < n :
                    v_new[j * cols + i + mod] = v[mod * (rows + 1) + i * rows + j]
    return v_new
