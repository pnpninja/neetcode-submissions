class Twitter:

    def __init__(self):
        self.timer = 0
        self.follower_map = defaultdict(Set)
        self.tweet_map = defaultdict(List)
        self.most_recent_size = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map.setdefault(userId,[])
        self.tweet_map[userId].insert(0, [self.timer, tweetId])
        self.timer+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        # Get list of tweets made by user themself
        users_to_analyze = self.follower_map.setdefault(userId,set())
        users_to_analyze.add(userId)
        # Iterate through tweets of followees
        for user in users_to_analyze:
            if user not in self.tweet_map:
                continue
            for [tweetTime, tweetId] in self.tweet_map[user]:
                if len(heap) < self.most_recent_size:
                    heapq.heappush(heap,(tweetTime, tweetId))
                else:
                    topTweetTime, _ = heap[0]
                    if tweetTime > topTweetTime:
                        heapq.heappop(heap)
                        heapq.heappush(heap,(tweetTime, tweetId))
        ans = []
        while len(heap) > 0:
            _, tweetId = heapq.heappop(heap)
            ans.insert(0,tweetId)
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_map.setdefault(followerId, set())
        self.follower_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follower_map:
            return
        if followeeId not in self.follower_map[followerId]:
            return
        self.follower_map[followerId].remove(followeeId)
