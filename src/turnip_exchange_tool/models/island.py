from datetime import datetime


class Island(dict):
    def __getattr__(self, name):
        if name in self:
            return self[name]
        raise AttributeError(f"No such attribute: {name}")

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        raise AttributeError(f"No such attribute: {name}")

    # def __repr__(self):
    #     return f"<{self.__class__.__name__}: {self.name}>"

    def __str__(self):
        return super().__str__()

    def insertion_format(self):
        return (
            self.turnipCode,
            self.name,
            self.fruit,
            self.turnipPrice,
            self.hemisphere,
            self.watchlist,
            self.fee,
            self.islander,
            self.category,
            self.islandTime,
            self.creationTime,
            self.description,
            self.queued,
            self.patreon,
            self.discordOnly,
            self.patreonOnly,
            self.messageID,
            self.rating,
            self.ratingCount,
            self.live,
            self.thumbsupt,
            self.thumbsdown,
            self.heart,
            self.clown,
            self.poop,
            self.islandScore,
            str(datetime.now()),
        )
