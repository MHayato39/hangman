#!/usr/bin/env python
# coding: utf-8

# In[17]:


import random


# In[15]:


def hangman(word):
    wrong = 0 # 何回間違えたか記録する
    stages = ["",
              "__________          ",
              "|                   ",
              "|         |         ",
              "|         O         ",
              "|        /|\        ",
              "|        / \        ",
              "|                   "
             ]
    rletters = list(word) # 答えなければならない残り文字を記録
    board = ["_"]*len(word) # 回答者に見せるヒント
    win = False # 回答者がゲームに勝ったかどうかを記録する
    print("ハングマンへようこそ") 
    
    while wrong < len(stages)-1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters: # 入力した文字が正解文字列に含まれていた場合
            cind = rletters.index(char) # 一致した文字が含まれる文字列のインデックス番号
            board[cind] = char # ヒント文字列の「_」を一致した箇所を正解文字で置き換える
            rletters[cind] = "$"
        else:               # 入力した文字が正解文字列に含まれていなかった場合
            wrong += 1
        
        print(" ".join(board)) # ヒント文字列の状態を表示
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
            
    if not win:
        print("ハングマンが完成した")
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け  正解は{}".format(word))


# In[49]:


list_hang = ["cat", "dog", "elephant", "python", "master"]
hang = list_hang[random.randint(0, 4)]
hangman(hang)

