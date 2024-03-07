"""
This type stub file was generated by pyright.
"""

def transpose(a, b=...):
    """Compute the transpose of 'a' and store it into 'b', if given,
    and return it. If 'b' is not given, allocate a new array
    and return that.

    This implements the algorithm documented in
    http://devblogs.nvidia.com/parallelforall/efficient-matrix-transpose-cuda-cc/

    :param a: an `np.ndarray` or a `DeviceNDArrayBase` subclass. If already on
        the device its stream will be used to perform the transpose (and to copy
        `b` to the device if necessary).
    """
    ...

