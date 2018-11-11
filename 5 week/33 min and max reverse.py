arra = list(map(int, input().split()))
imin, imax = arra.index(min(arra)), arra.index(max(arra))
arra[imin], arra[imax] = arra[imax], arra[imin]
print(*arra)
