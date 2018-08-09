from redis import StrictRedis

redis_ = StrictRedis(host='localhost', port=6379, db=0)
redis_.set('name', 'Bob')
print(redis_.get('name'))

#此外，还可以
from redis import ConnectionPool
pool = ConnectionPool(host='localhost', port=6379, db=0)
redis__ = StrictRedis(connection_pool=pool)
redis_.set('name', 'Bob')
print(redis_.get('name'))