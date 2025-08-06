from collections import deque
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
preorder = []

node_info = {val: index for index, val in enumerate(inorder)}

def build_preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    visited_node = postorder[post_end]
    preorder.append(visited_node)

    index = node_info[visited_node]
    left_size = index - in_start

    build_preorder(in_start, index - 1, post_start, post_start + left_size - 1) #좌측 서브 트리
  
    build_preorder(index + 1, in_end, post_start + left_size ,post_end - 1) #우측 서브 트리

build_preorder(0, N-1, 0, N-1)
print(*preorder)