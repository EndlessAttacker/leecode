class AuthenticationManager:

    def __init__(self, timeToLive):
        self.timeToLive = timeToLive
        self.map = {}

    def generate(self, tokenId, currentTime):
        self.map[tokenId] = self.timeToLive + currentTime
        

    def renew(self, tokenId, currentTime):
        if self.map[tokenId] and currentTime >= (self.map[tokenId]-self.timeToLive) and currentTime < self.map[tokenId]:
            self.map[tokenId] = currentTime +self.timeToLive


    def countUnexpiredTokens(self, currentTime:int)-> int:
        res = 0
        # print(self.map)
        for key,value in self.map.items():
            if currentTime >= (value-self.timeToLive) and currentTime < value:
                res += 1
        return res


obj = AuthenticationManager(5)
obj.generate("aaa", 2)
obj.renew("aaa", 1)
param_3 = obj.countUnexpiredTokens(6)
print(param_3)