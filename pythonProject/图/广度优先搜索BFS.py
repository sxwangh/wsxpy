# breadth-first search BFS 广度优先搜索

# 1.python的deque（双向）队列详解
# 可见deque是标准库collections中的
# 这其中最好用的是deque,他的操作很像list
# 同时相比于list实现的队列，deque实现拥有更低的时间和空间复杂度。list实现在出队（pop）和插入（insert）时的空间复杂度大约为O(n)，deque在出队（pop）和入队（append）时的时间复杂度是O(1)。
# 所以deque更有优越性 而且deque既可以表示队列 又可以表示栈 实在是太方便了
# https://www.cnblogs.com/ranzhong/p/12438841.html

from collections import deque


def search(name):
    queue = deque()  # 创建一个队列
    queue += graph[name]  # name的邻居加到队列中
    visited = []  # 是否被访问过
    while queue:
        person = queue.popleft()
        if person not in visited:
            if check_person(person):
                print(person + 'is the check person')
                return True
            else:
                queue += graph[person]
                visited.append(person)  # 将这个人标记为 已查过
    return False


# 检查这个人是不是卖芒果的
def check_person(name):
    return name[-1] == 'm';
