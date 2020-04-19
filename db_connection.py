import psycopg2
import config


def pg_stat_activity():
    try:
        conn = psycopg2.connect(dbname=config.DB_CONFIG['dbname'],
                                user=config.DB_CONFIG['user'],
                                host=config.DB_CONFIG['host'],
                                port=config.DB_CONFIG['port'],
                                password=config.DB_CONFIG['password']
                                )
        cursor = conn.cursor()
        cursor.execute('select * from pg_stat_activity')
        rows = cursor.fetchall()
        objects_list = []
        for row in rows:
            result = Stat_Activity(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],
                                   row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19])
            objects_list.append(result)
        return objects_list
    except (Exception, psycopg2.Error) as error:
        print(error)
    finally:
        if conn:
            cursor.close()
        conn.close()


class Stat_Activity:
    def __init__(self, datid, datname, pid, usesysid, usename, application_name, client_addr, client_hostname, client_port,  backend_start,
                 xact_start, query_start, state_change, wait_event_type, wait_event, state, backend_xid, backend_xmin, query, backend_type):
        self.datid = datid
        self.datname = datname
        self.pid = pid
        self.usesysid = usesysid
        self.usename = usename
        self.application_name = application_name
        self.client_addr = client_addr
        self.client_hostname = client_hostname
        self.client_port = client_port
        self.backend_start = backend_start
        self.xact_start = xact_start
        self.query_start = query_start
        self.state_change = state_change
        self.wait_event_type = wait_event_type
        self.wait_event = wait_event
        self.state = state
        self.backend_xid = backend_xid
        self.backend_xmin = backend_xmin
        self.query = query
        self.backend_type = backend_type







