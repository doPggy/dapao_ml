import target_encode_cy
import numpy as np
import timeit
import pandas as pd



# print(timeit.timeit('target_encode_cy.target_mean_cy_v2(np.array([[1, 2, 3, 4],[2, 3, 4 ,5]]))',
#         setup='import target_encode_cy;import numpy as np',
#         number = 10 ))
# print(timeit.timeit('zyt.mountain_is_trash_v1(np.array([[1, 2, 3, 4],[2, 3, 4 ,5]]))', setup='import zyt;import numpy as np', number = 10 ))
# print(timeit.timeit('zyt.mountain_is_trash_v1(np.array([[1, 2, 3, 4],[2, 3, 4 ,5]]))', setup='import zyt;import numpy as np', number = 10 ))
# print(timeit.timeit('zyt.mountain_is_trash_v2(np.array([[1, 2, 3, 4],[2, 3, 4 ,5]]))', setup='import zyt;import numpy as np', number = 10 ))
# print(timeit.timeit('zyt.mountain_is_trash_v3(np.array([[1, 2, 3, 4],[2, 3, 4 ,5]]))', setup='import zyt;import numpy as np', number = 10 ))
y = np.random.randint(2, size=(5000, 1))
x = np.random.randint(10, size=(5000, 1))
data = pd.DataFrame(np.concatenate([y, x], axis=1), columns=['y', 'x'])
print(target_encode_cy.target_mean_cy_v3(data, 'y', 'x').base)

