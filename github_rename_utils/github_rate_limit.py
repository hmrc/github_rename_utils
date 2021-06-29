class InMemoryRateLimitStore:
    def __init__(self):
        self.values = {}

    def put(self, resource, cost, reset_at):
        self.values[resource] = {
            "cost": self.values[resource]["cost"] + cost,
            "reset_at": max([self.values[resource]["reset_at"], reset_at])
        } if resource in self.values else {
            "cost": cost,
            "reset_at": reset_at
        }

    def reset(self):
        self.values = {}
