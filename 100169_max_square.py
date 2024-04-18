import numpy as np

from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:

        hSizes = []
        vSizes = []

        hFences.sort()
        vFences.sort()
        
        for i in range(len(hFences)):
            hSizes.append(hFences[i] - 1) if hFences[i] - 1 not in hSizes else hSizes
            hSizes.append(m - hFences[i]) if m - hFences[i] not in hSizes else hSizes
            for j in range(0,i):
                hSizes.append(hFences[i] - hFences[j]) if hFences[j] - hFences[i] not in hSizes else hSizes
        hSizes.append(m - 1)
        hSizes.sort(reverse = True)
        
        for i in range(len(vFences)):
            vSizes.append(vFences[i] - 1) if vFences[i] - 1 not in vSizes else vSizes
            vSizes.append(n - vFences[i]) if n - vFences[i] not in vSizes else vSizes
            for j in range(0,i):
                vSizes.append(vFences[i] - vFences[j]) if vFences[j] - vFences[i] not in vSizes else vSizes                
        vSizes.append(n - 1)
        vSizes.sort(reverse = True)
 
        #print(hSizes, vSizes)

        max_size = next((a for a in hSizes if a in vSizes), None)

        if max_size is not None:
            return max_size**2 % 1000000007
        else:
            return -1
                

if __name__ == '__main__':

    m = 8959
    n = 8405
    hFences = [7929,4465,8596,5003,1691,3558,1548,4899,3816,2435,4931,7054,154,8113,2419,842,3872,1866,4886,2404,339,391,6710,16,4045,5821,6344,7725,6333,5764,8642,3079,8771,3488,6289,11,6392,2461,4640,8790,4100,1326,7949,2686,7910,6416,171,8912,7683,5883,2088,5562,4753,7952,7206,7126,4742,77,3820,8415,8580,3276,5515,89,8487,5923,967,6293,2411,4535,4453,6334,5386,1965,6435,2977,6352,5274,6921,2310,1088,6422,6956,40,3325,7566,1718,3392,6358,8144,2756,750,5986,2933,2429,8677,6699,8160,3576,1724,8115,4177,2287,1822,4621,3417,1104,1677,3145,3735,22,4930,3990,4368,7827,250,1658,4926,722,2443,5568,6576,704,2807,4096,2767,2867,5845,3486,6306,5771,4092,3045,1673,7036,7853,3570,8359,3187,257,5544,1028,8172,6787,2763,2959,6892,4528,1841,974,4797,3627,4779,6205,3723,2777,3829,956,1615,8394,6378,8324,7564,8262,1610,2373,2002,1203,7523,1451,6186,3370,619,3854,6453,5917,3371,4713,4495,1062,1212,1165,2563,3773,5218,1538,3393,4922,6480,2188,6248,4065,5991,6719,4596,6812,3797,4697,372,838,1545,3038,5254,8275,4195,5437,3003,6985,7652,5076,1637,5987,7108,7425,7175,146,6071,5967,8582,7995,8349,4876,1690,5378,110,8541,8470,7521,4652,884,113,8507,3597,532,7169,5577,7983,6282,6281,5185,1559,1710,542,4285,1467,4441,2108,7061,6960,4684,6045,341,5423,7993,3505,5312,2951,8038,1493,7905,6945,6855,3654,1850,1533,2545,7506,6267,3885,6542,4159,8231,3781,2647,1536,8241,6369,6313,5179,2828,8723,6926,923,3985,8187,5851,4803,5061,418,98,3127,8049,7548,6773,2527,2258,4536,3481,4238,6152,8196,153,2376,1755,3552,8407,7140,5288,6097,8319,2390,1384,7701,5720,666,6201,1853,3137,1418,3179,4481,4521,2808,6257,4906,1202,7454,6374,6753,5248,5475,2442,1460,2724,7724,7504,424,4909,3090,6827,8043,73,8635,2033,5171,8774,7886,7534,8033,2832,392,1703,415,5128,8298,792,7535,3521,8877,3533,6697,4951,5191,4511,1667,984,7784,8655,3784,2843,6016,4998,6999,3874,754]
    vFences = [858,8030,8350,3160,2167,5909,4099,5295,1098,6722,2204,286,2962,5162,4051,3181,4744,4440,6808,6075,7662,3269,7049,3091,1719,1913,5863,7830,1167,4700,6713,3067,3919,3928,1990,4740,4175,5521,876,1982,4729,2246,7436,6172,7902,7423,5596,2886,2799,6423,5840,3571,2656,3072,7869,7018,5900,6525,3327,3870,3864,2717,1210,1804,3758,7417,2099,3534,5018,5201,3616,1878,6441,3698,244,4091,4231,6336,5303,7522,364,4398,7153,8118,4390,2369,7316,6338,6103,1729,1184,8150,6481,4606,7035,6770,1514,1088,5279,7397,6438,8297,5587,7406,3730,7822,2271,2533,1964,4269,5387,5526,2430,703,2509,4487,5000,7884,7429,138,5649,4090,2411,2697,7950,7526,5157,2897,4225,7925,806,1128,6520,7742,428,7989,753,3491,6507,2036,3811,3443,7971,8060,2404,2622,3036,2906,6404,658,2224,1269,6940,2978,7301,2004,4988,8061,5829,1765,2504,6862,6417,1824,5044,1648,6488,2394,7237,2364,2454,7537,3985,2424,3670,3488,2564,7271,4268,6790,4650,7583,1478,7698,6615,2762,2358,7724,8340,6848,7485,4058,1206,6975,5530,2606,1526,6190,1583,4350,2457,5514,6133,4002,6222,6317,5502,2737,4079,8244,4814,6402,407,2663,3360,7788,7862,7611,1922,2785,357,620,2001,1638,4471,1584,5170,2531,4366,7594,2803,4928,1691]
    
    print(Solution().maximizeSquareArea(m,n,hFences,vFences))



        
