#!/usr/bin/env python

'''
Perform functional testing to validate configuration changes
'''

import argparse
import salteval
import yaml
import sys


def parse_test(config):
    '''
    Parser functional test
    '''
    with open(config, 'r') as _fh:
        yml = yaml.safe_load(_fh)

    return yml


def main(config):
    '''
    Execute functional tests
    '''
    test_results = {'SUCCESS': {}, 'FAILED': {}, 'OTHER': {}}
    test_cases = parse_test(config)

    for name, test in test_cases.items():
        for func, args in test.items():
            kwargs = {}

            for arg in args:
                kwargs.update(arg)

            try:
                successful = getattr(salteval, func)(**kwargs)
            except AttributeError:
                successful = False
                test_results['OTHER'].update(
                    {name: '`{0}` is not a valid test method'.format(func)}
                )

            if successful:
                test_results['SUCCESS'].update(
                    {name: ''}
                )
            else:
                test_results['FAILED'].update(
                    {name: ''}
                )

    return test_results


if __name__ == '__main__':
    # pylint: disable=C0103
    parser = argparse.ArgumentParser(
        description='Functonal Testing for Config Management'
    )

    parser.add_argument(
        '-c',
        '--config-test',
        dest='config',
        required=True,
        help=''
    )

    opts = parser.parse_args()

    sys.exit(main(opts.config))
