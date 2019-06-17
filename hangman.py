import random

words = ["cat", "dog", "bird", "fish", "three", "seven"]
answer = words[random.randint(0, len(words) - 1)]

def hangman(word):
    # 変数wrongはプレイヤーが間違えた回数をカウントする変数
    wrong = 0
    stages = ["",
              "________        ",
              "|               ",
              "|       |       ",
              "|       0       ",
              "|      /|\      ",
              "|      / \      ",
              "|               "
              ]
    # 変数rlettersは答えなければいけない残りの文字
    rletters = list(word)
    # 変数boardはプレイヤーに見せるヒントを記録
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}.".format(word))


hangman(answer)
