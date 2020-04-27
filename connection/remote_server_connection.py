import paramiko
import config


def connect():
    key = paramiko.RSAKey.from_private_key_file(config.REMOTE_SERVER_CONFIG["key"])
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    print("Start connection to host", config.REMOTE_SERVER_CONFIG["host"], sep=" ")

    client.connect(
        hostname=config.REMOTE_SERVER_CONFIG['host'],
        username=config.REMOTE_SERVER_CONFIG['user'],
        pkey=key)

    print("Successfully connected to host", config.REMOTE_SERVER_CONFIG["host"], sep=" ")

    return client
