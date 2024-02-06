def rps(p1, p2):
    #your code here
    if (p1 == p2):
      return "Draw!"

    map = {
      'paperrock': "Player 1 won!",
      'rockscissors': "Player 1 won!",
      'scissorspaper': "Player 1 won!",
      'paperscissors': 'Player 2 won!',
      'rockpaper': 'Player 2 won!',
      'scissorsrock': 'Player 2 won!'
    }
    return map[p1+p2]

print(rps('scissors', 'rock'))
print(rps('scissors', 'paper'))