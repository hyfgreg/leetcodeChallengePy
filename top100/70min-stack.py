"""155. 最小栈
中等
相关标签
premium lock icon
相关企业
提示
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

实现 MinStack 类:

MinStack() 初始化堆栈对象。
void push(int val) 将元素val推入堆栈。
void pop() 删除堆栈顶部的元素。
int top() 获取堆栈顶部的元素。
int getMin() 获取堆栈中的最小元素。


示例 1:

输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.


提示：

-231 <= val <= 231 - 1
pop、top 和 getMin 操作总是在 非空栈 上调用
push, pop, top, and getMin最多被调用 3 * 104 次

面试中遇到过这道题?
1/5
是
否
通过次数
918,989/1.5M
通过率
62.6%
相关标签
栈
设计
"""


class MinStack:

    def __init__(self):
        self.stk = []
        self.min_val = None

    def push(self, val: int) -> None:
        if not self.stk:
            self.stk.append(0)
            self.min_val = val
            return
        diff = val - self.min_val  # type:ignore
        self.stk.append(diff)
        if diff < 0:
            self.min_val = val

    def pop(self) -> None:
        if self.stk:
            diff = self.stk.pop()
            if diff < 0:
                self.min_val = self.min_val - diff
            if not self.stk:
                self.min_val = None

    def top(self) -> int:
        return self.stk[-1] + self.min_val if self.stk[-1] >= 0 else self.min_val

    def getMin(self) -> int:
        return self.min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
