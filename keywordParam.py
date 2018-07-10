def keywordParam(name, auth=True, id=1):
    print('auth is {auth}, id is {id} and name is {name}'.format(auth=auth, id=id, name=name))

keywordParam('Su Xiaohun', id=9, auth=False)
