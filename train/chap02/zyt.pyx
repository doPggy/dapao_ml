# distutils: language=c++
import numpy as np
cimport numpy as cnp

cpdef woe_is_trash():
    cdef int w_count = 0;
    w_count += 1
    return w_count


cpdef mountain_is_trash_v1(matrix):
    cdef int m_count = 0;
    m_count += 1
    # print(matrix[1:])
    # cdef 需要 cnp 
    # 因为 cdef 就要 cython 中识别，而不是用 Python
    cdef cnp.ndarray arg = np.asfortranarray(matrix, dtype=np.float64)
    return arg

cpdef mountain_is_trash_v2(long[:, :] matrix):
    cdef int m_count = 0;
    m_count += 1
    # print(matrix[1:])
    # cdef 需要 cnp 
    # 因为 cdef 就要 cython 中识别，而不是用 Python
    cdef cnp.ndarray arg = np.asfortranarray(matrix, dtype=np.float64)
    return arg

cpdef mountain_is_trash_v3(cnp.ndarray[long, ndim = 2] matrix):
    cdef int m_count = 0;
    m_count += 1
    # print(matrix[1:])
    # cdef 需要 cnp 
    # 因为 cdef 就要 cython 中识别，而不是用 Python
    cdef cnp.ndarray arg = np.asfortranarray(matrix, dtype=np.float64)
    return arg

cpdef mountain_stone_is_trash(l):
    # 不存在类型强转，所以类型要一致
    # l = [[1, 2, 3]] 默认是 long
    cdef cnp.ndarray[long, ndim = 2] a = np.array(l)
    # 其实我这样也是可以的，但是有指定类型，效果会更好 官网也有说
    # cdef cnp.ndarray a = np.array(l)
    print(a.dtype)
    #print(a.shape)