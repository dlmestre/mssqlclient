import argparse


class Arguments:

    @staticmethod
    def get_args() -> dict:
        parser = argparse.ArgumentParser()
        return Arguments._set_arguments(parser)

    @staticmethod
    def _set_arguments(parser) -> dict:
        parser._action_groups.pop()
        required = parser.add_argument_group('required arguments')
        optional = parser.add_argument_group('optional arguments')
        required.add_argument('--format', required=True)
        required.add_argument('--query', required=True)
        optional.add_argument('--config_file', required=False)
        optional.add_argument('--plain', type=Arguments._str2bool, nargs='?', const=True, default=False)
        return vars(parser.parse_args())

    @staticmethod
    def _str2bool(v) -> bool:
        if isinstance(v, bool):
           return v
        if v.lower() in ('yes', 'true', 't', 'y', '1'):
            return True
        elif v.lower() in ('no', 'false', 'f', 'n', '0'):
            return False
        else:
            raise argparse.ArgumentTypeError('Boolean value expected.')
