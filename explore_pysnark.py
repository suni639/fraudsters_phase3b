# import pysnark
# from importlib import import_module

# submodules = ['libsnark', 'qaptools', 'zkinterface']  # Update this list based on the previous output

# for submodule in submodules:
#     module = import_module(f'pysnark.{submodule}')
#     print(f"Contents of {submodule}:", dir(module))

# import pysnark.libsnark as libsnark

# for attribute in dir(libsnark):
#     attr = getattr(libsnark, attribute)
#     if callable(attr):
#         print(f"Function: {attribute}")
#     elif isinstance(attr, type(libsnark)):
#         print(f"Module: {attribute} ->", dir(attr))

# import pysnark.qaptools as qaptools

# for attribute in dir(qaptools):
#     attr = getattr(qaptools, attribute)
#     if callable(attr):
#         print(f"Function: {attribute}")
#     elif isinstance(attr, type(qaptools)):
#         print(f"Module: {attribute} ->", dir(attr))


# import pysnark.zkinterface as zkinterface

# for attribute in dir(zkinterface):
#     attr = getattr(zkinterface, attribute)
#     if callable(attr):
#         print(f"Function: {attribute}")
#     elif isinstance(attr, type(zkinterface)):
#         print(f"Module: {attribute} ->", dir(attr))
