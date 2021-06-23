class AddingDict(dict):
  def __add__(self, other):
    result = self.copy()
    
    for key in other:
      result[key] = result[key] + other[key] if key in self else other[key]
    
    return result
