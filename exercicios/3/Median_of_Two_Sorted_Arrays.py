class Solution(object):
    def findMedianSortedArrays(self,nums1, nums2):
        tamNums1, tamNums2 = len(nums1), len(nums2)
        if tamNums1 > tamNums2:
            nums1, nums2, tamNums1, tamNums2 = nums2, nums1, tamNums2, tamNums1

        valMin, valMax, meio = 0, tamNums1, (tamNums1 + tamNums2 + 1) // 2

        while valMin <= valMax:
            i = (valMin + valMax) // 2
            j = meio - i
            if i < tamNums1 and nums2[j-1] > nums1[i]:
                valMin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                valMax = i - 1
            else:
                if i == 0: 
                    maxEsq = nums2[j-1]
                elif j == 0: 
                    maxEsq = nums1[i-1]
                else: 
                    maxEsq = max(nums1[i-1], nums2[j-1])

                if (tamNums1 + tamNums2) % 2 == 1:
                    return maxEsq

                if i == tamNums1: 
                    minDir = nums2[j]
                elif j == tamNums2: 
                    minDir = nums1[i]
                else: 
                    minDir = min(nums1[i], nums2[j])

                return (maxEsq + minDir) / 2.0
            