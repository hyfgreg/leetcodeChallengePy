# -*- coding: utf-8 -*-
import typing
import attr


@attr.s
class KeyIndexCount:
    R = attr.ib(type="int", default=0)
    count = attr.ib(type="list", default=attr.Factory(list))

    def sort(self, a: dict) -> list:
        """
        :param a: key: str, value: int, 1-R，连续的
        :return:
        """
        N = len(a.keys())
        R = max(a.values())
        count = [0] * (R + 2)
        ret = [''] * N
        for name, r in a.items():
            count[r + 1] += 1

        # 最精妙的一步
        # 第i+1号的起始索引=第i号的起始索引+第i号的数量
        # 上一步的r+1操作后，count[i+1]就是第i号的数量， count[i]在加过之后就是起始索引，默认第1号的其实索引是0
        for i in range(R + 1):
            count[i + 1] += count[i]

        for name, r in a.items():
            ret[count[r]] = name
            count[r] += 1

        return ret


@attr.s
class LSD:
    def sort(self, a: list[str], w: int) -> list[str]:
        """
        R表示字母表的字符数量
        :param a: 字符串list
        :param w: 排序使用的倒数w位字符
        :return:
        """
        assert w > 0
        N = len(a)
        R = 128  # ascii, 那么索引其实是0-127，然后R+1就是129

        aux = [''] * N
        for i in range(w - 1, -1, -1):
            count = [0] * (R + 1)
            # 统计频率
            for text in a:
                ch = text[i]
                count[ord(ch) + 1] += 1

            # 计算起始索引
            for r in range(R):
                count[r + 1] += count[r]

            # 回写
            for text in a:
                ch = text[i]
                aux[count[ord(ch)]] = text
                count[ord(ch)] += 1
            a = aux[:]
        return aux


@attr.s
class MSD:
    R = attr.ib(type="int", default=128)  # ascii

    def sort(self, a: list[str]):
        self._sort(a, 0, len(a) - 1, 0)

    def _sort(self, a: list[str], lo: int, hi: int, d: int):
        """
        :param a: 要排序的字符串数组
        :param lo: 要排序的字符串数组的子数组的起始索引
        :param hi: 要排序的字符串数组的子数组的终止索引
        :param d:  用来排序的字符的索引(用来排序的第几位字符)
        :return:
        """
        if hi - lo <= 0:
            # print(lo, hi)
            return

        count = [0] * (self.R + 2)
        aux = [''] * (hi - lo + 1)

        # 统计频率
        for i in a[lo:hi + 1]:
            count[self._char_at(i, d) + 2] += 1  # +2， count[1]表示的-1(即超出了字符串范围，放在最前)的个数，count[2]表示第0号字符的个数...

        # 计算起始索引
        for r in range(self.R):
            # r == 0, count[r+1] = count[r+1] + count[r], see right, count[r+1]上一个r的数量，count[r]上一个r的索引
            count[r + 1] += count[r]
            # count[0] 表示的-1(即超出了字符串范围，放在最前)的索引, count[1]表示第0个字符索引...

        # 分类
        for i in a[lo:hi + 1]:
            aux[count[self._char_at(i, d) + 1]] = i
            count[self._char_at(i, d) + 1] += 1

        # 回写
        for i in range(hi - lo + 1):
            a[i + lo] = aux[i]
        print(lo, hi, d)
        print('aux', aux)
        print('a', a)
        # print(count)
        # 递归调用
        # start_index = lo
        # print("before while", lo, hi, d)
        # while start_index <= hi:
        #     end_index = count[self._char_at(a[start_index], d) + 1]
        #     print("start_index", start_index, 'end_index', end_index)
        #     self._sort(a, start_index, end_index - 1, d + 1)
        #     start_index = end_index
        for r in range(self.R):
            self._sort(a, lo + count[r], lo + count[r + 1] - 1, d + 1)

    def _char_at(self, a: str, i: int):
        # -1 表示超出了字符串范围，默认放在最前
        # 0~R-1， 表示是第几个字符
        if i >= len(a):
            return -1
        return ord(a[i])


def test_KIC():
    groups = {'Anderson': 2,
              'Brown': 3,
              'Davis': 3,
              'Garcia': 4,
              'Harris': 1,
              'Jackson': 3,
              'Johnson': 4,
              'Jones': 3,
              'Martin': 1,
              'Martinez': 2,
              'Miller': 2,
              'Moore': 1,
              'Robinson': 2,
              'Smith': 4,
              'Taylor': 3,
              'Thomas': 4,
              'Thompson': 4,
              'White': 2,
              'Williams': 3,
              'Wilson': 4}

    s = KeyIndexCount()
    print(groups)
    ret = s.sort(groups)
    print([i + ' ' + str(groups[i]) for i in ret])


def test_LSD():
    a = ['4PGC938',
         '2IYE230',
         '3CIO720',
         '1ICK750',
         '1OHV845',
         '4JZY524',
         '1ICK750',
         '3CIO720',
         '1OHV845',
         '1OHV845',
         '2RLA629',
         '2RLA629',
         '3ATW723']
    l = LSD()
    print(a)
    a = l.sort(a, len(a[0]))
    print(a)


def test_MSD():
    a = ['she',
         'sells',
         'seashells',
         'by',
         'the',
         'sea',
         'shore',
         'the',
         'shells',
         'she',
         'sells',
         'are',
         'surely',
         'seashells']
    m = MSD()
    print(a)
    m.sort(a)
    print(a)


if __name__ == '__main__':
    test_MSD()
