import redis

def redis_node():
    node = redis.StrictRedis(host = '127.0.0.1', port = 6379)
    node.set("name_test", "name_test_value")
    print(node.get("name_test"))

redis_node()
