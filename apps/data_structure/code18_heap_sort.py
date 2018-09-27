# coding=utf-8 
# @Time : 2018/9/25 21:29 
# @Author : achjiang
# @File : code18_heap_sort.py


# 堆排序适用于记录数很多的情况
#与快速排序，归并排序 时间复杂一样都是n*log（n）


####################################################
####################################################
####################################################

from collections import deque

# 这里需要说明元素的存储必须要从1开始
# 涉及到左右节点的定位，和堆排序开始调整节点的定位
# 在下标0处插入0，它不参与排序
L = deque([49,38,65,97,76,13,27,49])
L.appendleft(0)

#L = [0,49,38,65,97,76,13,27,49]

def element_exchange(numbers,low,high):

    temp = numbers[low]

    # j 是low的左孩子节点(cheer!)
    i = low
    j = 2*i

    while j<=high:
        # 如果右节点较大，则把j指向右节点
        if j<high and numbers[j]<numbers[j+1]:
            j = j+1
        if temp<numbers[j]:
            # 将numbers[j]调整到双亲节点的位置上
            numbers[i] = numbers[j]
            i = j
            j = 2*i
        else:
            break
    # 被调整节点放入最终位置
    numbers[i] = temp

def top_heap_sort(numbers):

    length = len(numbers)-1

    # 指定第一个进行调整的元素的下标
    # 它即该无序序列完全二叉树的第一个非叶子节点
    # 它之前的元素均要进行调整
    # cheer up！
    first_exchange_element = int(length/2)

    #建立初始堆
    print (first_exchange_element)
    for x in range(first_exchange_element):
        element_exchange(numbers,first_exchange_element-x,length)

    # 将根节点放到最终位置，剩余无序序列继续堆排序
    # length-1 次循环完成堆排序
    for y in range(length-1):
        temp = numbers[1]
        numbers[1] = numbers[length-y]
        numbers[length-y] = temp
        element_exchange(numbers,1,length-y-1)

if __name__=='__main__':
    top_heap_sort(L)
    LL = []
    for x in range(1,len(L)):
        # print L[x],
        LL.append(L[x])
    print (LL)
##############################################
##############################################
##############################################
def build_maxheap(L,len):
    len_new = int(len/2)
    for i in range(len_new,0,-1):
        # print i
        adjustdown(L,i,len)
    return L

def adjustdown(L,low,high):  #这里只是把一个位于low位置上的数向下移动。
    temp = L[low]
    i = low
    j = 2 * i
    while j <= high:
        # if j <= high and L[j] < L[j+1]:#z这里的L[j+1]可能不存在，所有会有out of index 报错.
        #     j+=1
        if j <= high and j + 1 <= high:
            if L[j] < L[j+1]:
                j+=1
        if L[j]>temp:
            L[i] = L[j]
            i = j
            j = 2 * i
        else:
            break
    L[i] = temp
    # return L  #由于这里是中间列表，不要输出。
    # print L
# L = [0,49,38,65,97,76,13,67,47]
# L =  build_maxheap(L,8)
# del L[0]
# # print type(L)
# print "大根堆第一次：",L

len = len(L)-1
def Heap_sort(L,len):
    build_maxheap(L,len)
    for i in range(len,1,-1):
        L[i],L[1] = L[1],L[i]
        # print i
        # print L[len],L[1]
        adjustdown(L,1,i-1)
    return L
L = [49,38,65,97,76,13,67,47]
print ("原列表：" ,L)
L.insert(0,0)
L = Heap_sort(L,len)
del L[0]
print ("堆排序：",L)

#基本思路是：
#1 先从后到前进行小数下移的操作。这个后是指len（L）/2
#2 第一步完成后，最大的那个数就上移到了根节点。把这个根节点与最后一个元素交换位置，这时最后一个元素就在有序区里。则只需要将第一个元素再进行下移操作即可。
#3.循环第二步，直到只剩下根节点。
'''方法2'''

def  HeapSort(ls):
    def heapadjust(arr,start,end):  #将以start为根节点的堆调整为大顶堆
        temp=arr[start]
        son=2*start+1
        while son<=end:
            if son<end and arr[son]<arr[son+1]:  #找出左右孩子节点较大的
                son+=1
            if temp>=arr[son]:       #判断是否为大顶堆
                break
            arr[start]=arr[son]     #子节点上移
            start=son                     #继续向下比较
            son=2*son+1
        arr[start]=temp             #将原堆顶插入正确位置
#######
    n=len(ls)
    if n<=1:
        return ls
    #建立大顶堆
    root=n//2-1    #最后一个非叶节点（完全二叉树中）
    while(root>=0):
        heapadjust(ls,root,n-1)
        root-=1
    #掐掉堆顶后调整堆
    i=n-1
    while(i>=0):
        (ls[0],ls[i])=(ls[i],ls[0])  #将大顶堆堆顶数放到最后
        heapadjust(ls,0,i-1)    #调整剩余数组成的堆
        i-=1
    return ls
#########
x=input("请输入待排序数列：\n")
y=x.split()
arr=[]
for i in  y:
    arr.append(int(i))
arr=HeapSort(arr)
#print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i,end=' ')
