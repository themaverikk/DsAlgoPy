from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        friend_circles = [0] * len(M)

        circle_number = 0
        for i in range(len(M)):
            if friend_circles[i] == 0:
                circle_number += 1
                self.mark_friend_circles(M, friend_circles, i, circle_number)

        return circle_number

    def mark_friend_circles(self, M, friend_circles, i, circle_number):
        friend_circles[i] = circle_number

        for j in range(len(M)):
            if M[i][j] == 1 and friend_circles[j] == 0:
                self.mark_friend_circles(M, friend_circles, j, circle_number)

#
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
