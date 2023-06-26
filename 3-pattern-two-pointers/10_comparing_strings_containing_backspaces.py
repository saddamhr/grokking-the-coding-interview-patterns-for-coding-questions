class Solution:
    def build_string(self,string):
      built_string = []
      for s in string:
        if s != '#':
          built_string.append(s)
        elif built_string:
          built_string.pop()
      return built_string

    def backspaceCompare(self, s: str, t: str) -> bool:

      return self.build_string(s) == self.build_string(t)