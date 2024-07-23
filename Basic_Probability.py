xw = 5
xb = 4
x = xw+xb
pxw = xw/x
pxb = xb/x

yw = 7
yb = 6
y = yw+yb
pyw = yw/y
pyb = yb/y

newy = y+1

probbfromyifw = yb/newy
probbfromyifb = (yb+1)/newy

totalprob = probbfromyifb*pxb + probbfromyifw*pxw

print("Probability of getting black from Y : ",totalprob)
