import jankenMethod

# じゃんけんゲームをする
janken = jankenMethod.Janken()
# 出す手を決定する
jankenPlayer = janken.selectJankenPlayer()
jankenCom = janken.selectJankenComputer()
# 勝敗を決める
result = janken.decideWinner(jankenPlayer,jankenCom)
# 勝敗メッセージを出力する。
print(janken.printResult(result))

