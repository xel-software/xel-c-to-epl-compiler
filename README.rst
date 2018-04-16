======================
C to ePL Compiler v1.0
======================


Introduction
============

What is the C to ePL Compiler
-----------------------------

**c-to-epl** is a coder converter that will allow you to convert your C algorithms to the ePL language usable on the XEL network. Since ePL does not allow for the usage of function return values or function arguments, c-to-epl will make your life a lot easier.

Known Problems
--------------

**c-to-epl** is still work-in-progress and may contain severe bugs. Furthermore, is does not yet support any of the following features:

- Does not allow the initialization for arrays
- You are allowed to use only one function call either standalone or in a variable initialization. Using function calls in more complex statements will fail
- No pointers
- No structs, no enums, no typedefs
- Many other things may fail: if you experience a bug, please feel free to submit an issue or a pull request