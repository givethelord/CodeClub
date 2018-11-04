#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @Site    :
# @File    : 排序算法.py
# @Software: PyCharm

"""
-----------------------------------------------------
思路：

-----------------------------------------------------
"""


"""比较排序"""


def bubble_sort(list_sort):
    """冒泡排序

        1. 比较相邻的元素，如果前一个比后一个大，就把它们两个调换位置
        2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
        3. 针对所有的元素重复以上的步骤，除了最后一个。
        4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较

        分类 -------------- 内部比较排序
        数据结构 ---------- 数组
        最差时间复杂度 ---- O(n^2)
        最优时间复杂度 ---- 如果能在内部循环第一次运行时,使用一个旗标来表示有无需要交换的可能,可以把最优时间复杂度降低到O(n)
        平均时间复杂度 ---- O(n^2)
        所需辅助空间 ------ O(1)
        稳定性 ------------ 稳定
    """
    count = 0
    N = len(list_sort)
    for i in range(N):  # 每次最大元素就像气泡一样"浮"到数组的最后
        for j in range(N - i - 1):  # 依次比较相邻的两个元素,使较大的那个向后移
            count += 1  # 统计判断次数
            if list_sort[j] > list_sort[j + 1]:
                list_sort[j], list_sort[j + 1] = list_sort[j + \
                    1], list_sort[j] # 如果前一个大于后一个，交换位置

    print("执行次数为%d" % count)
    return list_sort


def cocktail_sort(list_sort):
    """鸡尾酒排序

    鸡尾酒排序，也叫定向冒泡排序，是冒泡排序的一种改进。此算法与冒泡排序的不同处在于从低到高然后从高到低，而冒泡排序则仅从低到高去比较序列里的每个元素。他可以得到比冒泡排序稍微好一点的效能

    分类 -------------- 内部比较排序
    数据结构 ---------- 数组
    最差时间复杂度 ---- O(n^2)
    最优时间复杂度 ---- 如果序列在一开始已经大部分排序过的话,会接近O(n)
    平均时间复杂度 ---- O(n^2)
    所需辅助空间 ------ O(1)
    稳定性 ------------ 稳定
    """

    N = len(list_sort)
    left = 0
    right = N - 1
    count = 0

    while (left < right):

        for i in range(right):  # 前半轮,将最大元素放到后面
            count += 1  # 统计判断次数
            if list_sort[i] > list_sort[i + 1]:
                list_sort[i], list_sort[i + 1] = list_sort[i + \
                    1], list_sort[i] # 如果前一个大于后一个，交换位置

        right -= 1

        for j in range(right, left, -1):  # 后半轮,将最小元素放到前面
            count += 1  # 统计判断次数
            if list_sort[j] < list_sort[j - 1]:
                list_sort[j], list_sort[j - 1] = list_sort[j -
                                                           1], list_sort[j] # 如果前一个大于后一个，交换位置

        left += 1

    print("执行次数为%d" % count)
    return list_sort


def selection_sort(list_sort):
    """选择排序

    一种简单直观的排序算法。它的工作原理很容易理解：初始时在序列中找到最小（大）元素，放到序列的起始位置作为已排序序列；
    然后，再从剩余未排序元素中继续寻找最小（大）元素，放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

    分类 -------------- 内部比较排序
    数据结构 ---------- 数组
    最差时间复杂度 ---- O(n^2)
    最优时间复杂度 ---- O(n^2)
    平均时间复杂度 ---- O(n^2)
    所需辅助空间 ------ O(1)
    稳定性 ------------ 不稳定
    """

    N = len(list_sort)
    count = 0

    for i in range(N - 1):  # i为已排序序列的末尾
        min_index = i
        for j in range(i + 1, N):  # 未排序序列
            count += 1  # 统计判断次数
            if list_sort[min_index] > list_sort[j]:
                min_index = j  # 找出未排序序列中的最小值

        if min_index != i:
            # 交换位置
            list_sort[min_index], list_sort[i] = list_sort[i], list_sort[min_index]

    print("执行次数为%d" % count)
    return list_sort


def insertion_sort(list_sort, left, right):
    """插入排序

    1.从第一个元素开始，该元素可以认为已经被排序
    2.取出下一个元素，在已经排序的元素序列中从后向前扫描
    3.如果该元素（已排序）大于新元素，将该元素移到下一位置
    4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
    5.将新元素插入到该位置后
    6.重复步骤2~5


    分类 ------------- 内部比较排序
    数据结构 ---------- 数组
    最差时间复杂度 ---- 最坏情况为输入序列是降序排列的,此时时间复杂度O(n^2)
    最优时间复杂度 ---- 最好情况为输入序列是升序排列的,此时时间复杂度O(n)
    平均时间复杂度 ---- O(n^2)
    所需辅助空间 ------ O(1)
    稳定性 ------------ 稳定
    """

    count = 0

    for i in range(left + 1, right + 1):  # 类似抓扑克牌排序
        element = list_sort[i]  # 获取新元素：右手抓到一张扑克牌
        j = i - 1  # 拿在左手上的牌总是排序好的

        # 把新元素与排序的元素序列进行比较:将抓到的牌与手牌从右向左进行比较
        while j >= left and list_sort[j] > element:
            count += 1  # 统计判断次数
            list_sort[j + 1] = list_sort[j]  # 如果该手牌比抓到的牌大，就将其右移
            j -= 1

        # 直到该手牌比抓到的牌小(或二者相等)，将抓到的牌插入到该手牌右边(相等元素的相对次序未变，所以插入排序是稳定的)
        list_sort[j + 1] = element

    print("执行次数为%d" % count)
    return list_sort


def insertion_sort_dichotomy(list_sort):
    """二分插入排序

    二分法插入排序，简称二分排序，是在插入第i个元素时，对前面的0～i-1元素进行折半，先跟他们中间的那个元素比，
    如果小，则对前半再进行折半，否则对后半进行折半，直到left<right，然后再把第i个元素前1位与目标位置之间的所有元素后移，再把第i个元素放在目标位置上。

    分类 -------------- 内部比较排序
    数据结构 ---------- 数组
    最差时间复杂度 ---- O(n^2)
    最优时间复杂度 ---- O(nlogn)
    平均时间复杂度 ---- O(n^2)
    所需辅助空间 ------ O(1)
    稳定性 ------------ 稳定
    """

    N = len(list_sort)
    count = 0

    for i in range(1, N):  # 类似抓扑克牌排序
        element = list_sort[i]  # 获取新元素：右手抓到一张扑克牌
        left = 0  # 拿在左手上的牌总是排序好的，所以可以用二分法
        right = i - 1  # 手牌左右边界进行初始化

        while left <= right:
            count += 1  # 统计判断次数
            mid = (left + right) / 2  # 对前面的0～i-1元素进行折半
            if list_sort[mid] > element:
                right = mid - 1  # 如果小于中间元素，右边边界是中间左一位
            else:
                left = mid + 1  # 如果大于中间元素，左边边界是中间右边一位

        for j in range(i - 1, left - 1, -1):  # 将欲插入新牌位置右边的牌整体向右移动一个单位
            count += 1  # 统计判断次数
            list_sort[j + 1] = list_sort[j]

        list_sort[left] = element  # 将抓到的牌插入手牌

    print("执行次数为%d" % count)
    return list_sort


def shell_sort(list_sort):
    """希尔排序

    通过将比较的全部元素分为几个区域来提升插入排序的性能。这样可以让一个元素可以一次性地朝最终位置前进一大步。
    然后算法再取越来越小的步长进行排序，算法的最后一步就是普通的插入排序，但是到了这步，需排序的数据几乎是已排好的了

    分类 -------------- 内部比较排序
    数据结构 ---------- 数组
    最差时间复杂度 ---- 根据步长序列的不同而不同。已知最好的为O(n(logn)^2)
    最优时间复杂度 ---- O(n)
    平均时间复杂度 ---- 根据步长序列的不同而不同。
    所需辅助空间 ------ O(1)
    稳定性 ------------ 不稳定
    """

    N = len(list_sort)
    count = 0
    gap = N // 2  # 初始步长

    while gap > 0:  # gap循环减少插入排序

        for i in range(gap, N):  # 右边牌
            element = list_sort[i]
            j = i - gap

            while j >= 0 and list_sort[j] > element:  # 进行左边牌插入排序
                count += 1  # 统计判断次数

                list_sort[j + gap] = list_sort[j]
                j -= gap  # 按照gap的间隔

            list_sort[j + gap] = element  # 插入新的值

        gap = gap // 2  # 得到新的步长

    print("执行次数为%d" % count)
    return list_sort


"""归并排序

递归法（Top-down） 一个大问题分割成小问题分别解决，然后用所有小问题的答案来解决整个大问题
1.申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列
2.设定两个指针，最初位置分别为两个已经排序序列的起始位置
3.比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置
4.重复步骤3直到某一指针到达序列尾
5.将另一序列剩下的所有元素直接复制到合并序列尾

迭代法（Bottom-up） 首先进行是两两归并，然后四四归并，然后是八八归并，一直下去直到归并了整个数组。
原理如下（假设序列共有n个元素）：

1.将序列每相邻两个数字进行归并操作，形成ceil(n/2)个序列，排序后每个序列包含两/一个元素
2.若此时序列数不是1个则将上述序列再次归并，形成ceil(n/4)个序列，每个序列包含四/三个元素
3.重复步骤2，直到所有元素排序完毕，即序列数为1

分类 -------------- 内部比较排序
数据结构 ---------- 数组
最差时间复杂度 ---- O(nlogn)
最优时间复杂度 ---- O(nlogn)
平均时间复杂度 ---- O(nlogn)
所需辅助空间 ------ O(n)
稳定性 ------------ 稳定
"""


def merge(left, right):  # 合并两个已排好序的数组
    result = []    # 辅助空间O(n)

    while left and right:  # 左右比大小，小的放入新列表
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left:  # 多余的左边元素直接放入
        result += left
    if right:  # 多余的右边元素直接放入
        result += right
    return result


def merge_sort_recursion(list_sort):
    """递归实现的归并排序(自顶向下)

    """

    N = len(list_sort)
    if N <= 1:  # 当待排序的序列长度为1时，递归开始回溯，进行merge操作
        return list_sort

    mid = N // 2
    left = list_sort[:mid]
    right = list_sort[mid:]
    left = merge_sort_recursion(left)
    right = merge_sort_recursion(right)
    return merge(left, right)


def merge_sort_iteration(list_sort):
    """非递归(迭代)实现的归并排序(自底向上)

    """
    N = len(list_sort)

    i = 2
    while i <= N:  # 每隔i拆分两个数组进行比较
        result = []
        for j in range(0, N, i):
            right = i + j if i + j < N else N - 1
            mid = j + i / 2

            result += merge(list_sort[j:mid], list_sort[mid:right])
        list_sort = result
        i *= 2
    return list_sort


"""
堆排序是指利用堆这种数据结构所设计的一种选择排序算法。
堆是一种近似完全二叉树的结构（通常堆是通过一维数组来实现的），并满足性质：以最大堆（也叫大根堆、大顶堆）为例，其中父结点的值总是大于它的孩子节点。

1.由输入的无序数组构造一个最大堆，作为初始的无序区
2.把堆顶元素（最大值）和堆尾元素互换
3.把堆（无序区）的尺寸缩小1，并调用heapify(A, 0)从新的堆顶元素开始进行堆调整
4.重复步骤2，直到堆的尺寸为1

分类 -------------- 内部比较排序
数据结构 ---------- 数组
最差时间复杂度 ---- O(nlogn)
最优时间复杂度 ---- O(nlogn)
平均时间复杂度 ---- O(nlogn)
所需辅助空间 ------ O(1)
稳定性 ------------ 不稳定
"""


def heap_sort(list_sort):

    def sift_down(start, end):
        """最大堆调整"""
        root = start
        while True:
            child = 2 * root + 1  # Left(i) = 2i + 1，i 的左子节点下标
            if child > end:
                break
            if child + 1 <= end and list_sort[child] < list_sort[child + 1]:
                child += 1  # Right(i) = 2i + 2，i 的右子节点下标 如果有右坐标且大于左坐标
            if list_sort[root] < list_sort[child]:  # 父小于子，交换
                list_sort[root], list_sort[child] = list_sort[child], list_sort[root]
                root = child  # 当上级父节点与子节点交换后，调整子节点的子节点之间的大小
            else:
                break

    N = len(list_sort)

    # 创建最大堆：父结点的值总是大于它的孩子节点
    for i in range(
            N // 2 - 1, -1, -1):     # Parent(i) = floor(i/2)，i 的父节点下标，获取父节点位置
        sift_down(i, N - 1)

    # 堆排序
    for j in range(N - 1, 0, -1):
        # 把最大堆的父元素放入最后一位
        list_sort[0], list_sort[j] = list_sort[j], list_sort[0]
        sift_down(0, j - 1)  # 排除最后一位元素进行最大堆调整

    return list_sort


"""
快速排序使用分治策略(Divide and Conquer)来把一个序列分为两个子序列
1.从序列中挑出一个元素，作为"基准"(pivot).
2.把所有比基准值小的元素放在基准前面，所有比基准值大的元素放在基准的后面（相同的数可以到任一边），这个称为分区(partition)操作。
3.对每个分区递归地进行步骤1~2，递归的结束条件是序列的大小是0或1，这时整体已经被排好序了。

分类 ------------ 内部比较排序
数据结构 --------- 数组
最差时间复杂度 ---- 每次选取的基准都是最大（或最小）的元素，导致每次只划分出了一个分区，需要进行n-1次划分才能结束递归，时间复杂度为O(n^2)
最优时间复杂度 ---- 每次选取的基准都是中位数，这样每次都均匀的划分出两个分区，只需要logn次划分就能结束递归，时间复杂度为O(nlogn)
平均时间复杂度 ---- O(nlogn)
所需辅助空间 ------ 主要是递归造成的栈空间的使用(用来保存left和right等局部变量)，取决于递归树的深度，一般为O(logn)，最差为O(n)
稳定性 ---------- 不稳定
"""


def partition(list_sort, left, right):
    """分区函数"""

    pivot = list_sort[right]  # 每次都选择最后一个元素作为基准
    i = left - 1  # 小于基准的子数组最后一个元素的索引
    for j in range(left, right):
        if list_sort[j] < pivot:
            i += 1
            # 把小于等于基准的元素放到前一个子数组末尾
            list_sort[i], list_sort[j] = list_sort[j], list_sort[i]
    if pivot < list_sort[i + 1]:
        list_sort[right], list_sort[i + 1] = list_sort[i + \
            1], list_sort[right] # 最后把基准放到前一个子数组的后边，剩下的子数组既是大于基准的子数组
    return i + 1  # 返回基准的索引


def quick_sort(list_sort, left, right):
    if left < right:
        p = partition(list_sort, left, right)  # 基准的索引
        quick_sort(list_sort, left, p - 1)
        quick_sort(list_sort, p, right)
    return list_sort


"""非比较排序算法"""


def count_sort(list_sort):
    """计数排序

    1.统计数组A中每个值A[i]出现的次数，存入C[A[i]]
    2.从前向后，使数组C中的每个值等于其与前一项相加，这样数组C[A[i]]就变成了代表数组A中小于等于A[i]的元素个数
    3.反向填充目标数组B：将数组元素A[i]放在数组B的第C[A[i]]个位置（下标为C[A[i]] - 1），每放一个元素就将C[A[i]]递减

    分类 ------------ 内部非比较排序
    数据结构 --------- 数组
    最差时间复杂度 ---- O(n + k)
    最优时间复杂度 ---- O(n + k)
    平均时间复杂度 ---- O(n + k)
    所需辅助空间 ------ O(n + k)
    稳定性 ----------- 稳定
    """

    size = max(list_sort) + 1
    n = len(list_sort)
    c = [0] * size  # 计数数组初始化

    for i in range(n):  # 使C[i]保存着等于i的元素个数
        c[list_sort[i]] += 1

    for j in range(1, size):  # 使C[i]保存着小于等于i的元素个数，排序后元素i就放在第C[i]个输出位置上
        c[j] += c[j - 1]

    b = [0] * n  # 分配临时空间,长度为n，用来暂存中间数据
    for k in range(n - 1, -1, -1):  # 从后向前扫描保证计数排序的稳定性(重复元素相对次序不变)
        c[list_sort[k]] -= 1  # 把每个元素A[i]放到它在输出数组B中的正确位置上
        b[c[list_sort[k]]] = list_sort[k]  # 当再遇到重复元素时会被放在当前元素的前一个位置上保证计数排序的稳定性
    list_sort = b[:]  # 把临时空间B中的数据拷贝回A
    del b[:]  # 释放临时空间
    return list_sort


def lsd_radix_sort(list_sort):
    """基数排序

    将所有待比较正整数统一为同样的数位长度，数位较短的数前面补零。
    然后，从最低位开始进行基数为10的计数排序，一直到最高位计数排序完后，数列就变成一个有序序列

    分类 ------------- 内部非比较排序
    数据结构 ---------- 数组
    最差时间复杂度 ---- O(n * dn)
    最优时间复杂度 ---- O(n * dn)
    平均时间复杂度 ---- O(n * dn)
    所需辅助空间 ------ O(n * dn)
    稳定性 ----------- 稳定
    :param list_sort: 待排序列表
    :return: 返回升序列表
    """

    n = len(list_sort)
    length = len(str(max(list_sort)))  # 获取最大数的位数

    for i in range(1, length + 1):  # 从低位到高位依据第i位数字对A进行计数排序

        #  使用计数排序
        c = [0] * 10

        def d(x, y): return (x // 10 ** (y - 1)) % 10  # 获得元素x的第d位数字
        for j in range(n):  # 使C[j]保存着等于i的元素个数
            c[d(list_sort[j], i)] += 1

        for k in range(1, 10):  # 使C[i]保存着小于等于i的元素个数，排序后元素i就放在第C[i]个输出位置上
            c[k] += c[k - 1]

        b = [0] * n  # 分配临时空间,长度为n，用来暂存中间数据
        for z in range(n - 1, -1, -1):  # 从后向前扫描保证计数排序的稳定性(重复元素相对次序不变)
            index = d(list_sort[z], i)
            c[index] -= 1  # 把每个元素A[i]放到它在输出数组B中的正确位置上
            b[c[index]] = list_sort[z]  # 当再遇到重复元素时会被放在当前元素的前一个位置上保证计数排序的稳定性
        list_sort = b[:]
        del b[:]
    return list_sort

def bucket_sort(list_sort):
    """桶排序

    数组元素映射到有限数量个桶里，利用计数排序可以定位桶的边界，
    每个桶再各自进行桶内排序（使用其它排序算法或以递归方式继续使用桶排序）

    分类 ------------- 内部非比较排序
    数据结构 --------- 数组
    最差时间复杂度 ---- O(nlogn)或O(n^2)，只有一个桶，取决于桶内排序方式
    最优时间复杂度 ---- O(n)，每个元素占一个桶
    平均时间复杂度 ---- O(n)，保证各个桶内元素个数均匀即可
    所需辅助空间 ------ O(n + bn)
    稳定性 ----------- 稳定
    :param list_sort:
    :return:返回升序列表
    """
    n = len(list_sort)
    bn = 13  # 这里排序[0, 129]的元素，使13个桶就够了，也可以根据输入动态确定桶的数量
    c = [0] * bn
    s = lambda x: x // 10
    for i in range(n): # 利用计数排序确定各个桶的边界（分桶）
        c[s(list_sort[i])] += 1  # 使C[i]保存着i号桶中元素的个数

    for j in range(1,bn):  # 定位桶边界：初始时，C[i]-1为i号桶最后一个元素的位置
        c[j] += c[j - 1]
    b = [0] * n
    for k in range(n-1, -1, -1):  # 从后向前扫描保证计数排序的稳定性(重复元素相对次序不变)
        index = s(list_sort[k])  # 元素A[i]位于b号桶
        c[index] -= 1  # 把每个元素A[i]放到它在输出数组B中的正确位置上
        b[c[index]] = list_sort[k]  # 桶的边界被更新：C[b]为b号桶第一个元素的位置
    list_sort = b[:]
    del b[:]

    for w in range(bn):
        left = c[w]  # C[i]为i号桶第一个元素的位置
        right = n - 1 if w == bn -1 else c[w + 1] - 1   # C[i+1]-1为i号桶最后一个元素的位置
        print left,right
        if left < right:  # 对元素个数大于1的桶进行桶内插入排序
            insertion_sort(list_sort, left, right)

    return list_sort



if __name__ == "__main__":
    sort_list = [43, 34, 4, 15, 46, 37, 18, 22, 123, 32, 65, 3]
    list_num = len(sort_list)
    # print bubble_sort(sort_list)
    # print cocktail_sort(sort_list)
    # print selection_sort(sort_list)
    # print insertion_sort(sort_list, 0, list_num)
    # print insertion_sort_dichotomy(sort_list)
    # print shell_sort(sort_list)
    # print merge_sort_recursion(sort_list)
    # print merge_sort_iteration(sort_list)
    # print heap_sort(sort_list)
    # print quick_sort(sort_list, 0, len(sort_list) - 1)
    # print count_sort(sort_list)
    # print lsd_radix_sort(sort_list)
    print bucket_sort(sort_list)
