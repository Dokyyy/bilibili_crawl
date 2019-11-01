import requests
import json
import random
from os import path


#随机获取一个headers
def get_headers():
    user_agents =  ['Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
                    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11']
    headers = {'User-Agent':random.choice(user_agents)}
    return headers

def getHTML(av, html):
    cur_path = path.dirname(__file__)  # 当前文件路径
    count=1
    fi = open(path.join(cur_path, './replies', av + '_replies.txt'), 'w', encoding='utf-8')
    while(True):
        url=html+str(count)
        url=requests.get(url, headers = get_headers())
        if url.status_code==200:
            cont=json.loads(url.text)
        else:
            break
        lengthRpy = 0
        if(cont['data']['replies'] is not None):
            lengthRpy = len(cont['data']['replies'])
        if count==1:
            try:
                lengthHot=len(cont['data']['hots'])
                print('lengthHot = ',lengthHot)
                for i in range(lengthHot):
                    # 热门评论内容
                    hotMsg=cont['data']['hots'][i]['content']['message']
                    print(cont['data']['hots'][i]['content']['message'])
                    fi.write(hotMsg + '\n')
                    leng=len(cont['data']['hots'][i]['replies'])
                    for j in range(leng):
                        # 热门评论回复内容
                        hotMsgRp=cont['data']['hots'][i]['replies'][j]['content']['message']
                        fi.write(hotMsgRp+'\n')
            except:
                pass
        if lengthRpy!=0:
            for i in range(lengthRpy):
                comMsg=cont['data']['replies'][i]['content']['message']
                fi.write(comMsg + '\n')
                #print('评论:', comMsg)
                if cont['data']['replies'][i]['replies'] is not None:
                    leng = len(cont['data']['replies'][i]['replies'])
                    for j in range(leng):
                        comMsgRp = cont['data']['replies'][i]['replies'][j]['content']['message']
                        fi.write(comMsgRp + '\n')
        else:
            break
        #print("第%d页写入成功！"%count)
        count += 1
    fi.close()
    print(count-1,'页评论写入成功！')