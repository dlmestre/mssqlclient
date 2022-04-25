import pymssql
from mssqlcli.config import Configuration


class Storage:

    @staticmethod
    def query(config, query) -> list:
        conn = pymssql.connect(
        config.server,
        config.get_username(),
        config.password,
        config.database,
        **Storage._kwargs(config)
        )
        cursor = conn.cursor(as_dict=True)
        cursor.execute(query)

        results = [row for row in cursor]
        return results

    @staticmethod
    def _kwargs(config: Configuration) -> dict:
        keys = ['port', 'pkey', 'key_filename', 'timeout', 'allow_agent', 'look_for_keys', 'compress', 'sock']
        kwargs = {}
        for key in keys:
            if hasattr(config, key):
                kwargs[key] = getattr(config, key)
        return kwargs
