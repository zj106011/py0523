from redis import Redis,ConnectionPool

def _init_redis():
    pools = ConnectionPool(host='localhost',port='6379',password='123456',db='14',max_connections=1000)
    redis_ = Redis(connection_pool=pools,decode_responses=True)
    return redis_

SESS = {
    'SECRET_KEY':'10086',
    'SESSION_TYPE':'redis',
    'SESSION_REDIS':_init_redis(),
    'SESSION_KEY_PREFIX':'Flask'
}