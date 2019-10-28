import pynlpir

pynlpir.open()

#读入中文文本
file = open('Chinese.txt')
text = file.read()

segments = pynlpir.segment(text,  pos_english=False)

result = []
for segment in segments:
   segment = segment.__str__()
   result.append(segment)

result_pynlpir = ''.join(result)
print(result_pynlpir)


pynlpir.close()