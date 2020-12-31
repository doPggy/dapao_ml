import zyt
import numpy as np
import timeit

print(zyt.woe_is_trash())
print(zyt.woe_is_trash())
print(zyt.woe_is_trash())

# print(zyt.mountain_is_trash(np.array([[1, 2, 3, 4],[2, 3, 4 ,5]])))

zyt.mountain_stone_is_trash([[1, 2, 3, 4],[2, 3, 4 ,5]])
# 不报错时间长
# print(timeit.timeit('zyt.mountain_is_trash_v1([[1, 2, 3, 4],[2, 3, 4 ,5]])', setup='import zyt', number = 10 ))
# 报错
# print(timeit.timeit('zyt.mountain_is_trash_v2([[1, 2, 3, 4],[2, 3, 4 ,5]])', setup='import zyt', number = 10 ))
# print(timeit.timeit('zyt.mountain_is_trash_v3([[1, 2, 3, 4],[2, 3, 4 ,5]])', setup='import zyt', number = 10 ))

print(timeit.timeit('zyt.mountain_is_trash_v1(np.array([[1, 2, 3, 4],[2, 3, 4 ,5]]))', setup='import zyt;import numpy as np', number = 10 ))
print(timeit.timeit('zyt.mountain_is_trash_v2(np.array([[1, 2, 3, 4],[2, 3, 4 ,5]]))', setup='import zyt;import numpy as np', number = 10 ))
print(timeit.timeit('zyt.mountain_is_trash_v3(np.array([[1, 2, 3, 4],[2, 3, 4 ,5]]))', setup='import zyt;import numpy as np', number = 10 ))