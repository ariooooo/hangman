def hangman(word):
    wrong=0
    stages=["",
            "_______     ",
            "|           ",
            "|     |     ",
            "|     0     ",
            "|   / | \   ",
            "|    / \    ",
            "|　　　　　 "
            ]
    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print("welcome to the hangman!")

while wrong<len(stages)-1:
    print("\n")
    msg="guess a letter"
    char=input(msg)
    if char in rletters:
        cind=rletters.index(char)
        rletters[cind]='$'
    else:
        wrong +=1
    print(" ".join(board))
    e=wrong +1
    print(" ".join(stages[0:e]))
    if "_" not in board:
        print("you win!")
        print(" ".join(board))
        win=True
        break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("you lose!correct answer is{}.".format(word))

hangman("cat")
