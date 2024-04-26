"""
https://leetcode.com/problems/design-twitter/description/
"""

class Twitter: #My solution

    def __init__(self):
        self.feed = [] #[[userId, tweetId]] - a central feed is kept for later filtering
        self.links = {} #{followerId: {followeeId}}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed.append([userId, tweetId])
        

    def getNewsFeed(self, userId: int) -> List[int]: #Time complexity O(10 * k) where k is the number followees for userId
        res = []
        for tweet in self.feed[::-1]: #the central feed is reverse to append the recent tweets first
            if tweet[0] == userId:
                res.append(tweet[1])

            if userId in self.links and tweet[0] in self.links[userId]:
                res.append(tweet[1])

            if len(res) == 10:
                break

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.links:
            self.links[followerId].add(followeeId)
        else:
            self.links[followerId] = set()
            self.links[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.links:
            self.links[followerId].remove(followeeId)
        

class Twitter:

    def __init__(self):
        self.count = 0 #used to keep a central track of the timing of tweets
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:  #Time complexity O(k + 10logk) where k is the number followees for userId, if 10 were larger, this solution becomes more efficient
        res = []
        maxHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]: #the most recent tweet from each followee is compared for recency
            if followeeId in self.tweetMap: #need to make sure the followee actually has tweets
                index = len(self.tweetMap[followeeId]) - 1
                count, tweet = self.tweetMap[followeeId][index]
                maxHeap.append([count, tweet, followeeId, index - 1]) #index - 1 is appended to keep track of the next most recent tweet from that followeeId

        heapq.heapify(maxHeap)

        while maxHeap and len(res) < 10:
            count, tweet, followeeId, index = heapq.heappop(maxHeap)
            res.append(tweet)
            if index >= 0: #to prevent the index going out of range
                count, tweet = self.tweetMap[followeeId][index]
                heapq.heappush(maxHeap, [count, tweet, followeeId, index - 1]) #the recent most recent tweet is pushed for comparison

        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
      
