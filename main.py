import random
import os

# ランダムに配列を生成
# 3 * 10
def getRandomArr(x,y):
    arr = []
    for j in range(0,y):
        line = []
        for i in range(0,x):
            line.append(random.randint(0,1))
        arr.append(line)
    return arr

# 2次元配列を表示
# 0 = " "
# 1 = "*"
def viewArr(arr):
    for j in arr:
        line_str = "|"
        for i in j:
            if i == 0:
                line_str = line_str + " "
            if i == 1:
                line_str = line_str + "*"
        line_str = line_str + "|"
        print(line_str)

# 生き残った個体を融合する
# 個体数/1の確率で値が決まる
# それを設定した個体数作成
# 次の世代には前の世代の形質を受け継いだ子供ができる

# 前世代の形質を受け継いだ配列を生み出す
def getOldGenWinner(gen_arr, gen_population_result):
    # 個体ごと
    winner = []
    for index,g_p_result in enumerate(gen_population_result):
        if g_p_result == 1:
            winner.append(index)
    # for pop_cnt, i in enumerate(gen_arr):
    # 個体の配列
    result = []
    pop = []

    for i_cnt, i in enumerate(gen_arr[0]):
        line = []
        for j_cnt, j in enumerate(i):
            win = []
            for k in winner:
                win.append(gen_arr[k][i_cnt][j_cnt])
            line.append(win[random.randint(0, len(win)-1)])
        # print(line)
        pop.append(line)
    # print(winner)

    # return gen_arr
    for i in gen_population_result:
        result.append(pop)
    return result

# Q and A
def q_and_a(qa_str):
    while 1:
        qa = input(qa_str)
        if qa == "Y" or qa == "y":
            break
        if qa == "N" or qa == "n":
            break
    return qa


# 1世代の個体数の設定
gen_population = 5

gen_arr = []

gen = 0
while 1:
    print("第" + str(gen) + "世代")
    if gen == 0:
        for population in range(0,gen_population):
            # ランダム配列を取得(行,列)
            arr = []
            arr = getRandomArr(10,3)
            # viewArr(arr)
            gen_arr.append(arr)

    if gen > 0:
        gen_arr = getOldGenWinner(gen_arr, gen_population_result)

    gen_population_result = []
    for population in range(0,gen_population):
        viewArr(gen_arr[population])
        qa = q_and_a("Y or N")
        if qa == "Y" or qa == "y":
            gen_population_result.append(1)
        if qa == "N" or qa == "n":
            gen_population_result.append(0)
    
    # print(gen_population_result)
    # print("次の世代に移ります")
    # os.system("cls")
    gen = gen + 1

# 配列を表示
# viewArr(gen_arr[0])

