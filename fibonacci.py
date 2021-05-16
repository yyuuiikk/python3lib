
if __name__ == "__main__":
    f = [0, 1]
    n = 50  # ループの上限値
    for i in range(2, n):
        f.append(f[i-1] + f[i-2])
    print(f)
