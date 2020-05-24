load_file_in_context("script.py")

try:
  class graph_vertex:
    def __init__(self, name, x, y):
      self.name = name
      self.position = (x, y)
  a = graph_vertex("A", 0, 1)
  b = graph_vertex("B", 1, 4)
  d = heuristic(a, b)
  if d != 10:
    fail_tests("Does the function return the sum of `x_distance` squared and `y_distance` squared?")
except TypeError as e:
  fail_tests(e)

pass_tests()
