#------------------------------------------------------------
#把矩阵原地顺时针旋转90度
#2018-9-5
#------------------------------------------------------------
class Solution(object):
    def rotate(self, matrix):
        if matrix:
            rows = len(matrix)
            cols = len(matrix[0])
            for i in range(rows // 2):
                for j in range(cols):
                    matrix[i][j], matrix[rows - i -1][j] = matrix[rows -i -1][j], matrix[i][j]
            for i in range(rows):
                for j in range(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
matrix = [[5,1,9,11],
          [2,4,8,10],
          [13,3,6,7],
          [15,14,12,16]
          ]
if __name__ == '__main__':
    w =Solution()
    w.rotate(matrix)
    print(matrix)