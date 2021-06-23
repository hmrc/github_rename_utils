class RateLimit:
  def __init__(self, cost, reset_at):
    self.cost = cost
    self.reset_at = reset_at

  def __add__(self, other):
    return RateLimit(
      self.cost + other.cost,
      max([self.reset_at, other.reset_at])
    )

  def __eq__(self, other):
    if isinstance(other, RateLimit):
      return (
        self.cost == other.cost and
        self.reset_at == other.reset_at
      )
    return False
