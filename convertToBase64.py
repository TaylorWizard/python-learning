import base64

two_col_layout_f = ''
three_col_layout_f = ''

with open('./img/two-col-layout.png', 'rb') as two_col:
    two_col_layout_f = base64.b64encode(two_col.read())

with open('./img/three-col-layout.png', 'rb') as three_col:
    three_col_layout_f = base64.b64encode(three_col.read())

with open('./img/new-img.png', 'wb') as img:
    imgData = base64.b64decode(two_col_layout_f)
    print('imgData: {0}'.format(imgData))
    img.write(imgData)

with open('./img/new-two-layout.txt', 'wb') as txt:
    txt.write(two_col_layout_f)

with open('./img/new-three-layout.txt', 'wb') as text:
    text.write(three_col_layout_f)

print(two_col_layout_f)
