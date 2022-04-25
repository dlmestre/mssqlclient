from mssqlcli.arguments import Arguments
from mssqlcli.config import Configuration
from mssqlcli.formats import Formatter
from mssqlcli.storage import Storage


def main():
    arguments = Arguments.get_args()
    config = Configuration(arguments['config_file'])
    data = Storage.query(arguments['query'], config)
    return Formatter(arguments['format'], data, arguments['plain'])


if __name__ == "__main__":
    main()
