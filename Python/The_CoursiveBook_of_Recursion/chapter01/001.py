result = [(lambda r: lambda n: 1 if n < 2 else r(r)(n-1) + r(r)(n-2))((lambda r: lambda n: 1 if n < 2 else r(r)(n-1) + r(r)(n-2)))(n) for n in range(37)]
