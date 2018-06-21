import redis

r = redis.Redis(host = '127.0.0.1', port = 6379)
#设置过期时间（秒）
#setex(name, value, time)
#设置过期时间（豪秒）
#psetex(name, time_ms, value)
r.setex('name', 'zhangsan', 60)
value = r.get('name')
r.close()
print(value)