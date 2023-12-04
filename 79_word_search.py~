from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        '''
        domains are leaves of a tree
        iterate over all domain names
          iterate over the parts of the domain name (going from top to bottom,
          i.e., right to left)
            if domain is not in the tree, insert it as a child of the parent
            and initialise its count to zero
            add the count for the domain 
        '''
        domain_counts = {}
        return_list = []
        for domain in cpdomains:
            domain_pieces = domain.split()[1].split(".")
            print(domain_pieces)
            piece_str = ""
            for piece in reversed(domain_pieces):
                piece_str = "." + piece + piece_str
                # check if this key is new, if so initialise it
                if piece_str not in domain_counts:
                    domain_counts[piece_str] = 0
                    
                domain_counts[piece_str] += int(domain.split()[0])
                
        print(domain_counts)
        for domain in domain_counts:
            print(domain_counts[domain], domain[1:])
            return_list.append(str(domain_counts[domain]) + " " + domain[1:])
        return return_list

        
if __name__ == '__main__':

    cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    
    print(Solution().subdomainVisits(cpdomains))
 
