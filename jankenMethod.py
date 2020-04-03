import random

# じゃんけん処理クラス
class Janken():
    def __init__(self) :
        pass
    # プレイヤーの出す手を決める
    def selectJankenPlayer(self):
        return int(input('じゃんけん？「ぐー」なら1,「ちょき」なら2,「ぱー」なら3）＝'))

    # COMの出す手を決める。
    def selectJankenComputer(self):
        return random.randint(1, 3)

    # 勝者がどちらか判定する
    # あいこの場合→"0"
    # プレイヤーが勝利→"1"
    # COMが勝利→"2"
    def decideWinner(self, jankenPlayer,jankenCom):
        if jankenPlayer == jankenCom:
            return 0
        elif (jankenPlayer == 1) and (jankenCom == 2):
            return 1
        elif (jankenPlayer == 2) and (jankenCom == 3):
            return 1
        elif (jankenPlayer == 3) and (jankenCom == 1):
            return 1
        else:
            return 2
    # COMが勝利→"2"
    def printResult(self, result):
        if result == 0:
            resultMessage = "あいこ"
        elif result == 1:
            resultMessage = "勝ち"
        else:
            resultMessage = "負け"
        return resultMessage