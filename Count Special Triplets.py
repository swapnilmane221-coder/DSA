class Solution(object):
    def specialTriplets(self, nums):

        i_dict = {}
        j_dict = {}
        MOD = 10**9 + 7
        res = 0

        for idx, num in enumerate(nums):
            if num & 1 == 0:
                if (num//2) in j_dict:
                    res = (res + j_dict[(num//2)])%MOD
            
            if num in j_dict:
                if (2*num) in i_dict:
                    j_dict[num] = (j_dict[num] + i_dict[2*num])%MOD
                else:
                    print("not possible  situation 1", num, "idx: ",idx)
            else:
                if (2*num) in i_dict:
                    j_dict[num] = (i_dict[2*num])%MOD

            if num not in i_dict:
                i_dict[num] = 0
            
            i_dict[num] += 1
        
        return res


        