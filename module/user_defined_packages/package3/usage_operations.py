"""
Purpose: Scripts for usage of operations.py
"""

import sys

# this below results in not creating python byte code for this script
sys.dont_write_bytecode=True

import operations
print(f"{operations.factorila(10)   =}")
print(f"{operations.fibanoci(10)    =}")
print()

from operations import fibanoci
print(f"{fibanoci(9)    =}")
print()

# wildcart impot we can import whatever functions we want 
from operations import*
print(f"{factorila(10)  =}")
print(f"{fibanoci(10)   =}")

# help(operations)
# print()