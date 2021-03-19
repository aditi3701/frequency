freq_str = "Mississippi"
result = {}
for keys in freq_str:
    result[keys] = result.get(keys, 0) + 1
print ("Output : \n " +  str(result))
