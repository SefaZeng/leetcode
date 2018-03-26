class Solution:
    def findMedianSortedArrays(self, num1, num2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(num1), len(num2)
        if m > n:
            num1, num2, m, n = num2, num1, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and num2[j-1] > num1[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and num1[i-1] > num2[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = num2[j-1]
                elif j == 0: max_of_left = num1[i-1]
                else: max_of_left = max(num1[i-1], num2[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = num2[j]
                elif j == n: min_of_right = num1[i]
                else: min_of_right = min(num1[i], num2[j])

                return (max_of_left + min_of_right) / 2.0
