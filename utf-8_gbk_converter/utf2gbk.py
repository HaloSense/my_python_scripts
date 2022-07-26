# Convert a file (with encoding format UTF-8) into another file (encoding format GBK).

source_name = 'source.txt'
result_name = 'result.txt'

source = open(source_name, 'r', encoding = 'utf-8')
result = open(result_name, 'w+', encoding = 'utf-8')

lines = source.readlines()
for line in lines:
    res_line = line.encode('utf-8').decode('gbk')
    result.write(res_line)
    # print(res_line)

source.close()
result.close()
