"""
DP实现 还真得琢磨琢磨 由于k的不固定性 每个位置所有的状态都很多
=============
一个初步的想法 从0开始遍历至结尾 dp存储每个节点触及时的k值(跳跃距离) set去重
假设节点1的k只有1，可以触及2或3，则2的set为[1],3的set[2]。
遍历节点2时, 可以触及3或4。则此时3的set为[2,1]，4的set为[2]。
=============
速度比回溯慢
目前猜测是回溯本身的判断有提前结束的功能，而这边暂时没有，故每次触及之后都判断一下试试。
============= 提前结束没啥用 再说吧 暂时速度确实不够理想
优化一下 dp数组可以和数值的map合并可以提高速度
"""


class Solution:
    def canCross(self, stones) -> bool:
        if not stones:
            return False

        dp = {}
        for v in stones:
            dp[v] = set()
        dp[0].add(0)

        last_set = dp[stones[-1]]

        def fn(v, k):
            if k <= 0:
                return
            v += k
            if v not in dp:
                return
            dp[v].add(k)

        for v in stones:
            for k in dp[v]:
                fn(v, k + 1)
                fn(v, k)
                fn(v, k - 1)
                if len(last_set) > 0:
                    return True

        return False


s = Solution()
print(s.canCross([0, 1, 3, 5, 6, 8, 12, 17]) is True)
print(s.canCross([0, 1, 2, 3, 4, 8, 9, 11]) is False)
