from mssqlcli.arguments import Arguments
from mssqlcli.config import Configuration
from mssqlcli.formats import Formatter
from mssqlcli.storage import Storage
import sys


def main():
    arguments = Arguments.get_args()
    config = Configuration(arguments['config_file'])
    data = Storage.query(config, arguments['query'])
    sys.stdout.write(Formatter(arguments['format'], data, arguments['plain']))


if __name__ == "__main__":
    main()
