

if __name__ == "__main__":
    """
    線形探索

    1つ1つの要素を順に調べていく探索方法
    計算量：O(N)
    """

    # カンマ区切りで探索する数を入力
    user_input = input("input numbers:\n").strip()
    target = input("input target number:\n").strip()

    is_exist = False
    user_input = user_input.split(',')
    for input_num in user_input:
        if input_num == target:
            is_exist = True
    if is_exist is True:
        print('target is exist')
    else:
        print('target is not exist')

