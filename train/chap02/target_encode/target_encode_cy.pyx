# %%cython -a -f --compile-args=-DCYTHON_TRACE=1
# %%cython -a --cplus
import numpy as np
cimport numpy as cnp 
cimport cython
from libcpp.map cimport map as mapcpp



@cython.boundscheck(False)
@cython.wraparound(False)
# 发现 pandas 瓶颈，换成 numpy
cpdef target_mean_cy_v3(data, str y_name, str x_name):
  cdef mapcpp[int, int] type_2_sum_dict   = mapcpp[int, int]()
  cdef mapcpp[int, int] type_2_count_dict = mapcpp[int, int]()
  cdef mapcpp[int, int].iterator it

  cdef Py_ssize_t i
  cdef Py_ssize_t x, y # 不得放到 for 里头用 cdef
  cdef cnp.ndarray[Py_ssize_t] n_y = data[y_name].values # values faster than to_numpy
  cdef cnp.ndarray[Py_ssize_t] n_x = data[x_name].values

  cdef Py_ssize_t nums  = n_x.shape[0] # 这个 2us 优化，一般
  #cdef cnp.ndarray[double] result = np.zeros(nums)
  cdef double[:] result = np.zeros(nums)
  for i in range(nums):
    x = n_x[i]
    y = n_y[i]
    it = type_2_sum_dict.find(x)
    if it != type_2_sum_dict.end():
      type_2_sum_dict[x]   += y
      type_2_count_dict[x] += 1
    else:
      type_2_sum_dict[x]   = y
      type_2_count_dict[x] = 1
  for i in range(nums):
    x = n_x[i]
    y = n_y[i]
    result[i]  = (type_2_sum_dict[x] - y) / (type_2_count_dict[x] - 1)
  return result

