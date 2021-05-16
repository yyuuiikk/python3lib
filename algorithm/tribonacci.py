
if __name__ == "__main__":
    f = [0, 0, 1]
    n = 50  # ループの上限値
    for i in range(3, n):
        f.append(f[i-1] + f[i-2] + f[i-3])
    print(f)
