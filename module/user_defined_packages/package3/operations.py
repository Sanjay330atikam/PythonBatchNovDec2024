"""
Purpose: Functions with math operations
  --factorial
  --fibannoci
"""

def factorila(n):
    result = 1
    for i in range(1,n+1):
        result *-i

    return result


def fibanoci(n):
    a,b =0,1
    series = []
    for _ in range(n+1):
        series.append(a)
        a, b = b, a+b
    return series


if __name__ == "__main__":
    print(f"{factorila(10)  =}")
    print(f"{fibanoci(10)   =}")
