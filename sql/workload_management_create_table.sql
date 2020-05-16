BEGIN;

CREATE SCHEMA IF NOT EXISTS wm;

CREATE TABLE IF NOT EXISTS wm.metrics (
                                          id SERIAL PRIMARY KEY,
                                          name varchar(16) unique,
                                          threshold smallint,
                                          priority smallint,
                                          CONSTRAINT priority_check CHECK (priority <= 100),
                                          CONSTRAINT threshold_check CHECK (threshold <= 100)
);

CREATE OR REPLACE FUNCTION wm.init_insert_metrics()
    RETURNS VOID AS
$$ DECLARE table_size smallint;
BEGIN
    table_size = (SELECT count(*) FROM wm.metrics);
    if table_size = 0 then
        INSERT INTO wm.metrics(name, threshold, priority)
        VALUES ('pcpu', 75, 50),
               ('pmem', 75, 50);
    end if;
END
$$ language plpgsql;

SELECT wm.init_insert_metrics();

CREATE TABLE IF NOT EXISTS wm.cluster_statistic (
    cpu_usage float,
    ram_usage float,
    date timestamp
);

COMMIT;
