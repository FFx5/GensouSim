class Relationship:
    def __init__(
        self,
        affinity=0,
        trust=0,
        respect=0,
        fear=0
    ):
        self.affinity = affinity
        self.trust = trust
        self.respect = respect
        self.fear = fear

    def modify(
        self,
        affinity=0,
        trust=0,
        respect=0,
        fear=0
    ):
        """Adjust relationship dimensions by the supplied amounts."""
        self.affinity += affinity
        self.trust += trust
        self.respect += respect
        self.fear += fear
