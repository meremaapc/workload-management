CREATE EXTENSION IF NOT EXISTS dblink;

CREATE OR REPLACE FUNCTION create_workload_management_database(_password text, _username text)
    RETURNS VOID AS $$ DECLARE db_name text = 'workload_management1';
BEGIN
    IF NOT EXISTS (SELECT FROM pg_database WHERE datname = db_name) THEN
        PERFORM dblink_connect('host=localhost user=postgres password=' || _password || ' dbname=' || current_database());
        PERFORM dblink_exec('CREATE DATABASE ' || db_name);
    END IF;
END
$$ language plpgsql;
