"""
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""
# i = 1  # 先定义一个变量
# while i < 10:  # 准备分两部分,前5次空格按1递减,*按奇数递增   后5次空格按1递增,*按奇数递减
#     if i <= 5:
#         print(" " * (5 - i), "*" * (i * 2 - 1))  # 5次空格递减,5次奇数递增
#     else:
#         print(" " * (i - 5), "*" * ((10-i) * 2 - 1))  # 5次空格递增, 5次奇数递减
#     i += 1  # 保证循环跳出条件



# i = 1
# while i < 10:
#     if i <= 5:
#         print(" " * (5 - i), "*" * ((i * 2) - 1))
#     else:
#         print((" " * (i - 5)), "*" * ((10 - i) * 2 - 1))
#         # if i == 8:
# #         #     print(" " * 4, "*")
# #         #     break
# #     i += 1


"""
最简单的是
"""

print("""
     *
    ***
   *****
  *******
 *********
  *******
   *****
    ***
     *""")
