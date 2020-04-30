BEGIN;

CREATE SCHEMA IF NOT EXISTS wm;

CREATE TABLE IF NOT EXISTS wm.metrics (
                                          id SERIAL PRIMARY KEY,
                                          name varchar(16) unique,
                                          priority smallint,
                                          CONSTRAINT priority_check CHECK (priority <= 100)
);

CREATE OR REPLACE FUNCTION wm.init_insert_metrics()
    RETURNS VOID AS
$$ DECLARE table_size smallint;
BEGIN
    table_size = (SELECT count(*) FROM wm.metrics);
    if table_size = 0 then
        INSERT INTO wm.metrics(name, priority)
        VALUES ('pcpu', 50),
               ('pmem', 50);
    end if;
END
$$ language plpgsql;

SELECT wm.init_insert_metrics();

COMMIT;
