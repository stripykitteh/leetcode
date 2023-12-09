class Solution:
    def rankTeams(self, votes: list[str]) -> str:
        l = len(votes)
        lv = len(votes[0])
        memo = {}
        for p in range(lv):
            for k in memo:
                memo[k] *= 1001
            for i in range(l):
                c = votes[i][p]
                memo[c] = memo.get(c, 0) + 1
                print(memo)
                
            if len(memo) != lv:
                continue
            s = sorted(memo.items(), key=lambda x: -x[1])
            if all(s[i][1] != s[i+1][1] for i in range(lv-1)):
                return ''.join([_[0] for _ in s])

        s.sort(key=lambda x: (-x[1],ord(x[0])))
        return ''.join([_[0] for _ in s])

if __name__ == '__main__':

    votes = ["BAC","ACB","ABC","ACB","BAC"]
    # votes = ["ABC","CBA"]

    #votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]    

    print(Solution().rankTeams(votes))
