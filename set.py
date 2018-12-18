bri = {'China', 'Russia', 'Greek'}

bric = bri.copy()

bric.add('Iran')
bric.add('Iraq')

print(bri.intersection(bric))
print(bri & bric)
print('convergence of bri and bric is ',bri | bric) # convergence
print(bric.issuperset(bri))

lyst = [1,2,3]
lyst[1],lyst[2] = lyst[2], lyst[1]
print(lyst)