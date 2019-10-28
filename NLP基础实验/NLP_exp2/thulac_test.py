import thulac

file = open('Chinese.txt')
user_dict = file.read()
#thulac 分词
thu1 = thulac.thulac(seg_only=False)

text = thu1.cut(user_dict, text=True)

print(text)



