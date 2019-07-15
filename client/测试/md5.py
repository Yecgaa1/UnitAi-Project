import hashlib
path="C:/Users/Administrator/Downloads/Anaconda3-2019.03-Windows-x86_64.exe"
#md5=hashlib.md5(open(path, 'rb').read()).hexdigest()
f = open(path,'rb')
md5_obj = hashlib.md5()
while True:
    d = f.read(8096)
    if not d:
      break
    md5_obj.update(d)
hash_code = md5_obj.hexdigest()
f.close()
md5 = str(hash_code).lower()
print(md5)