#--------------------------------------------------------
#题目：给一个url地址，写一份下载脚本，并打印进度条。
#2018-8-28
#--------------------------------------------------------
import requests
from tqdm import tqdm
def get_file(url,name):
    resp = requests.get(url=url)
    content_size = int(resp.headers['Content-Length'])/1024
    with open(name, 'wb') as f:
        print('total', content_size, 'k')
        for data in tqdm(interable = resp.iter_content(1024),total = content_size,unit = 'k'):
            f.write(data)
        print('file name'+name)

if __name__ == '__main__':
    url = 'https://files.pythonhosted.org/packages/0e/07/b73f3a6f494fa2dae322cd49097d9db11b12a68c4793423771db943c8d91/Pillow-4.0.0-cp27-cp27m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl'
    #url = "http://10.0.251.224:8081/text.zip"
    name = url.split('/')[-1]
    get_file(url,name)