height = int(input())
rise = int(input())
falt = int(input())
height -= rise
rise -= falt
print((height + (rise - height % rise) % rise) // rise + 1)
