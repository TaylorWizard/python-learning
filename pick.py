import pickle

shop_list_file = 'showlist.data'

shop_list = ['vegetable', 'virus', 'mango']

f = open(shop_list_file, 'wb')
pickle.dump(shop_list, f)
f.close()

del shop_list

f = open(shop_list_file, 'rb')
storedList = pickle.load(f)
print(storedList)
f.close()


