from typing import List

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        ret_val = ""
   
        results = {}
        num_votes = len(votes)
        num_teams = len(votes[0])
            
        # build the dictionary of vote counts
        for vote in votes:
            for index in range(num_teams):
                if vote[index] in results:
                    results[vote[index]] += max(num_votes,2) ** (num_teams - index - 1)
                else:
                    results[vote[index]] = max(num_votes,2) ** (num_teams - index - 1)                    

        #print(sorted(results.items(), key=lambda item: (item[1],-ord(item[0])), reverse=True))
            
        for i in sorted(results.items(), key=lambda item: (item[1],-ord(item[0])), reverse=True):
            ret_val += i[0]

        return ret_val

if __name__ == '__main__':

    # votes = ["ABC","ACB","ABC","ACB","ACB"]
    # votes = ["ABC","CBA"]

    votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]    

    print(Solution().rankTeams(votes))
 
