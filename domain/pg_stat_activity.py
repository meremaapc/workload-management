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
