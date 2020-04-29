letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Build dictionary with the letters of the alphabet and their
# corresponding points
letter_to_points = {letter:points for letter, points in zip(letters, points)}
letter_to_points[' '] = 0

# Calculate total points for the word
def score_word(word):
  word = word.upper()
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total

# test score_word()
brownie_points = score_word('brownie')
print(brownie_points)

# list of words per player so far
player_to_words = {'player1':['blue', 'tennis', 'exit'], 'wordNerd':['earth', 'eyes', 'machine'], 'Lexi Con': ['eraser', 'belly', 'husky'], 'Prof Reader': ['zap', 'coma', 'period']}

player_to_points = {}

# calculate the current points for each player
def update_point_totals():
  for player, words in player_to_words.items():
    word_total = 0
    for word in words:
      word_total += score_word(word)
      player_to_points[player] = word_total

# add new word to player
def play_word(player, word):
  player_to_words[player] += word
  update_point_totals()
  print(player_to_points)

# test play word function
play_word('player1', 'menezunda')
