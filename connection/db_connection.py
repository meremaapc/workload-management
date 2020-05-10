import psycopg2


def connect(config):
    print('Connecting to database %s...' % config['dbname'])
    conn = psycopg2.connect(dbname=config['dbname'],
                            user=config['user'],
                            host=config['host'],
                            port=config['port'],
                            password=config['password']
                            )
    print('Connecting to database %s successfully' % config['dbname'])
    return conn
