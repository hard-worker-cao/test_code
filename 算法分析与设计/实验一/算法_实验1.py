# 计数排序

def find_num(nums , k):
    max_num = max(nums)
    min_num = min(nums)
    # 初始化数组
    count = [0] * (max_num - min_num + 1)
    for num in nums:
        count[num - min_num] += 1
    idx = len(count) - 1
    total = 0
    while(total < k):
        total +=count[idx]
        idx -=1
    return idx + min_num + 1


m = int(input(f'请输入这个数组的数字个数:'))
k = int(input(f'要查找第几大的数字'))
if k > m :
    print("输入有误")
else:
    array = list(map(int,input('请输入元素的值').split(",")))
    find_num(array,k)
    print(f'数组中第{k}大的数字是：{find_num(array,k)}')
