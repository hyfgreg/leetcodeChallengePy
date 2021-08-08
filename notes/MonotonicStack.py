"""
单调递增栈：单调递增栈就是从栈底到栈顶数据是从大到小
单调递减栈：单调递减栈就是从栈底到栈顶数据是从小到大

现在有一组数10，3，7，4，12。从左到右依次入栈，则如果栈为空或入栈元素值小于栈顶元素值，则入栈；否则，如果入栈则会破坏栈的单调性，则需要把比入栈元素小的元素全部出栈。单调递减的栈反之。

10入栈时，栈为空，直接入栈，栈内元素为10。

3入栈时，栈顶元素10比3大，则入栈，栈内元素为10，3。

7入栈时，栈顶元素3比7小，则栈顶元素出栈，此时栈顶元素为10，比7大，则7入栈，栈内元素为10，7。

4入栈时，栈顶元素7比4大，则入栈，栈内元素为10，7，4。

12入栈时，栈顶元素4比12小，4出栈，此时栈顶元素为7，仍比12小，栈顶元素7继续出栈，此时栈顶元素为10，仍比12小，10出栈，此时栈为空，12入栈，栈内元素为12。
————————————————
版权声明：本文为CSDN博主「lucky52529」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/lucky52529/article/details/89155694
"""


class MonotonicStack:
    # 这里实现的是[单调递增栈]
    # 当入栈元素比栈顶元素大的时候，栈顶元素要出栈，直到栈顶元素比入栈元素大
    def __init__(self):
        self.stack = []

    def push(self, val):
        if not self.stack or self.stack[-1] > val:
            self.stack.append(val)
        else:
            while self.stack:
                if self.stack[-1] < val:
                    self.stack.pop()
                else:
                    break
            self.stack.append(val)

    def pop(self):
        if self.stack:
            return self.stack.pop()


if __name__ == '__main__':
    nums = [10, 3, 7, 4, 12]
    ms = MonotonicStack()
    for num in nums:
        ms.push(num)
        print(ms.stack)
