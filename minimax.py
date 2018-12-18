def minimax(state, depth, player):
    if player == MAX:
      best = [-1, -1, -infinity]
    else:
      best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
      score = evaluate(state)
      return [-1, -1, score]

    for cell in empty_cells(state):
      x, y = cell[0], cell[1]
      state[x][y] = player
      score = minimax(state, depth - 1, -player)
      state[x][y] = 0
      score[0], score[1] = x, y

      if player == MAX:
        if score[2] > best[2]:
          best = score
      else:
        if score[2] < best[2]:
          best = score

    return best
