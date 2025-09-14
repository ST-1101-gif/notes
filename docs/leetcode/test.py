

def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_len = len(nums1) + len(nums2)
        mid = (total_len + 1) // 2
        if total_len % 2 == 0:
            even = 1
        else:
            even = 0

        p1 = 0
        p2 = 0
        cur = 0
        midnum = 0

        while cur < mid:
            cur += 1
            if nums1[p1] <= nums2[p2]:
                midnum = nums1[p1]
                p1 += 1
                if p1 >= len(nums1):
                    break
            else:
                midnum = nums2[p2]
                p2 += 1
                if p2 >= len(nums2):
                    break
            

        if cur == mid:
            if even:
                if p1 < len(nums1) and p2 < len(nums2):
                    return (midnum + min(nums1[p1], nums2[p2])) / 2
                elif p1 < len(nums1):
                    return (midnum + nums1[p1]) / 2
                else:
                    return (midnum + nums2[p2]) / 2
            else:
                return mid

        if p1 < len(nums1):
            if even:
                return (nums1[p1 + mid - cur] + nums1[p1 + mid - cur + 1]) / 2
            else:
                return nums1[p1 + mid - cur]

        else:
            if even:
                return (nums2[p2 + mid - cur] + nums1[p2 + mid - cur + 1]) / 2
            else:
                return nums2[p2 + mid - cur]



 
print(findMedianSortedArrays([1,2],[3,4]))