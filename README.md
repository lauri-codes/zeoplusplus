# zeoplusplus
Python wrapper for the Zeo++ library.

## Rebuilding Cython wrapper
The cython wrapper definitions live inside src/zeoplusplus. The package comes
with prebuilt C++ binding code created with Cython, but these bindings can be
recreated with:

```sh
python setup.py build_ext --inplace
```
