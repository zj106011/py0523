from redis import Redis, ConnectionPool


def _init_():
    pools=ConnectionPool(host='127.0.0.1',port='6379',db='10',max_connections=1000)
    redis_=Redis(connection_pool=pools,decode_responses=True)
    return redis_
SESS={
    'SECRET_KEY':'10086',
    'SESSION_TYPE':'redis',
    'SESSION_REDIS':_init_(),
    'SESSION_KEY_PREFIX':'Flask'
}