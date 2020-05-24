load_file_in_context("script.py")

try:
  class graph_vertex:
    def __init__(self, name, x, y):
      self.name = name
      self.position = (x, y)
  a = graph_vertex("A", 0, 1)
  b = graph_vertex("B", 1, 0)
  graph = {a: set([(b, 2)]), b: set([(a, 2)])}
  a_star(graph, a, b)
except TypeError:
  fail_tests("Did change all instances of `paths_and_distances[some_variable_name]` to `paths_and_distances[some_variable_name][0]`?")

pass_tests()
