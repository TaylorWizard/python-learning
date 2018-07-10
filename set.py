bri = {'China', 'Russia', 'Greek'}

bric = bri.copy()

bric.add('Iran')
bric.add('Iraq')

print(bri.intersection(bric))
print(bri & bric)
print('convergence of bri and bric is ',bri | bric) # convergence
print(bric.issuperset(bri))
