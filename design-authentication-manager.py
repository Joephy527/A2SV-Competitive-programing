class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokenTimeMap = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokenTimeMap[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if (tokenId in self.tokenTimeMap and
            self.tokenTimeMap[tokenId] > currentTime):
            self.tokenTimeMap[tokenId] = currentTime + self.timeToLive 

    def countUnexpiredTokens(self, currentTime: int) -> int:
        validToken = 0
        
        for token in self.tokenTimeMap:
            if self.tokenTimeMap[token] > currentTime:
                validToken += 1

        return validToken

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
