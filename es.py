# from datetime import datetime
# from elasticsearch import Elasticsearch
#
# es=Elasticsearch()
# # 添加数据
# es.index(index="my-index", doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})
# # es.index(index="my_index",doc_type="test_type",id=1,body={"name":"python","addr":"深圳"})
# # 查询数据
# result=es.get(index="my-index", doc_type="test-type", id=42)['_source']
# # result = es.search(index="my_index",doc_type="test_type")
# # 打印所有数据
# # for item in result["hits"]["hits"]:
# #     print(item["_source"])
# print(result)
#tcp
# 1. 创建套芥子
import socket
# 创建套接字
tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 创建按
tcp_socket.connect(('127.0.0.1',8889))
#
data=input('qinghsuru')
tcp_socket.send(data.encode())