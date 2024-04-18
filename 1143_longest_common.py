from typing import List
from functools import cache

class Solution:    
    @cache
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        set1 = set(text1)
        set2 = set(text2)
        common = set1.intersection(set2)
        if not common:
            return 0
        set1_drop = ''.join(list(set1.difference(common)))
        text1_table = str.maketrans("X","X",set1_drop)
        text1_drop = text1.translate(text1_table)
        set2_drop = ''.join(list(set2.difference(common)))
        text2_table = str.maketrans("X","X",set2_drop)
        text2_drop = text2.translate(text2_table)

        acc = 0
        while len(text1_drop) >= 1:
            # by convention make text1_drop the shorter string
            if len(text1_drop) > len(text2_drop):
                tmp = text2_drop
                text2_drop = text1_drop
                text1_drop = tmp
            if len(text1_drop) == 1:
                acc += 1
            if text1_drop[-1] == text2_drop[-1]:
                text1_drop = text1_drop[:-1]
                text2_drop = text2_drop[:-1]
                acc += 1
            else:
                
            acc = acc + self.longestCommonSubsequence(text1_drop[:-1],text2_drop[:-1],acc+1,text1_drop[-1])
        else:
            return max(self.longestCommonSubsequence(text1_drop[:-1],text2_drop), \
            self.longestCommonSubsequence(text2_drop[:-1],text1_drop))

        return acc
    
if __name__ == '__main__':

    text1,text2 = "abcde","ace"
    print(Solution().longestCommonSubsequence(text1,text2))
    text1,text2 = "abc","abc"
    print(Solution().longestCommonSubsequence(text1,text2))
    text1,text2 = "abc","def"
    print(Solution().longestCommonSubsequence(text1,text2))    
    text1,text2 = "oxcpqrsvwf","shmtulqrypy"
    print(Solution().longestCommonSubsequence(text1,text2))
    text1,text2 = "abcdefghijklmnopqrstuvwxyz","aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"
    print(Solution().longestCommonSubsequence(text1,text2))
    text1,text2 = "fcvafurqjylclorwfoladwfqzkbebslwnmpmlkbezkxoncvwhstwzwpqxqtyxozkpgtgtsjobujezgrkvevklmludgtyrmjaxyputqbyxqvupojutsjwlwluzsbmvyxifqtglwvcnkfsfglwjwrmtyxmdgjifyjwrsnenuvsdedsbqdovwzsdghclcdexmtsbexwrszihcpibwpidixmpmxshwzmjgtadmtkxqfkrsdqjcrmxkbkfoncrcvoxuvcdytajgfwrcxivixanuzerebuzklyhezevonqdsrkzetsrgfgxibqpmfuxcrinetyzkvudghgrytsvwzkjulmhanankxqfihenuhmfsfkfepibkjmzybmlkzozmluvybyzsleludsxkpinizoraxonmhwtkfkhudizepyzijafqlepcbihofepmjqtgrsxorunshgpazovuhktatmlcfklafivivefyfubunszyvarcrkpsnglkduzaxqrerkvcnmrurkhkpargvcxefovwtapedaluhclmzynebczodwropwdenqxmrutuhehadyfspcpuxyzodifqdqzgbwhodcjonypyjwbwxepcpujerkrelunstebopkncdazexsbezmhynizsvarafwfmnclerafejgnizcbsrcvcnwrolofyzulcxaxqjqzunedidulspslebifinqrchyvapkzmzwbwjgbyrqhqpolwjijmzyduzerqnadapudmrazmzadstozytonuzarizszubkzkhenaxivytmjqjgvgzwpgxefatetoncjgjsdilmvgtgpgbibexwnexstipkjylalqnupexytkradwxmlmhsnmzuxcdkfkxyfgrmfqtajatgjctenqhkvyrgvapctqtyrufcdobibizihuhsrsterozotytubefutaxcjarknynetipehoduxyjstufwvkvwvwnuletybmrczgtmxctuny","nohgdazargvalupetizezqpklktojqtqdivcpsfgjopaxwbkvujilqbclehulatshehmjqhyfkpcfwxovajkvankjkvevgdovazmbgtqfwvejczsnmbchkdibstklkxarwjqbqxwvixavkhylqvghqpifijohudenozotejoxavkfkzcdqnoxydynavwdylwhatslyrwlejwdwrmpevmtwpahatwlaxmjmdgrebmfyngdcbmbgjcvqpcbadujkxaxujudmbejcrevuvcdobolcbstifedcvmngnqhudixgzktcdqngxmruhcxqxypwhahobudelivgvynefkjqdyvalmvudcdivmhghqrelurodwdsvuzmjixgdexonwjczghalsjopixsrwjixuzmjgxydqnipelgrivkzkxgjchibgnqbknstspujwdydszohqjsfuzstyjgnwhsrebmlwzkzijgnmnczmrehspihspyfedabotwvwxwpspypctizyhcxypqzctwlspszonsrmnyvmhsvqtkbyhmhwjmvazaviruzqxmbczaxmtqjexmdudypovkjklynktahupanujylylgrajozobsbwpwtohkfsxeverqxylwdwtojoxydepybavwhgdehafurqtcxqhuhkdwxkdojipolctcvcrsvczcxedglgrejerqdgrsvsxgjodajatsnixutihwpivihadqdotsvyrkxehodybapwlsjexixgponcxifijchejoxgxebmbclczqvkfuzgxsbshqvgfcraxytaxeviryhexmvqjybizivyjanwxmpojgxgbyhcruvqpafwjslkbohqlknkdqjixsfsdurgbsvclmrcrcnulinqvcdqhcvwdaxgvafwravunurqvizqtozuxinytafopmhchmxsxgfanetmdcjalmrolejidylkjktunqhkxchyjmpkvsfgnybsjedmzkrkhwryzan"
    print(Solution().longestCommonSubsequence(text1,text2))
