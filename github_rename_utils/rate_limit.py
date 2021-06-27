class InMemoryRateLimitStore:
    def __init__(self, callback=None):
        self.values = {}
        self.callback = callback

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
    
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        if self.callback:
            self.callback(self.values)
