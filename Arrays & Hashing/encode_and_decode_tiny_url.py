class Codec:  #Time complexity O(1), Space complexity O(1)
    
    def __init__(self):
        self.encodeMap = {}
        self.decodeMap = {}
        self.base = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.encodeMap:
            shortUrl = self.base + str(len(self.encodeMap) + 1)
            self.encodeMap[longUrl] = shortUrl
            self.decodeMap[shortUrl] = longUrl
        return self.encodeMap[longUrl]

    def decode(self, shortUrl: str) -> str:
        return self.decodeMap[shortUrl]



class MyCodec: #Same complexity as above

    def __init__(self):
        self.count = 0
        self.encodeMap = {}
        self.decodeMap = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        url = f"http://tinyurl.com/{str(self.count)}"
        self.encodeMap[longUrl] = url
        self.decodeMap[url] = longUrl
        self.count += 1
        return url
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decodeMap[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
