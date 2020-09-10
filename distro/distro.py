# -*- coding: utf-8 -*-


"""distro.distro: provides entry point main()."""

__version__ = '0.0.5'

import argparse
import sys

from distro.data import DATA


def main():
    """Main execution wrapper. Parsers CLI arguments, loads data, calls the search method and displays the results"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', type=str, default='text', help='Output format (text|json|csv)')
    parser.add_argument('-v', '--version', action='store_true', help='Show version')
    parser.add_argument('search_term', nargs='*', help='Search terms, it can be a string or field:string')
    args = parser.parse_args()

    if args.version:
        print('v' + __version__)
        sys.exit()

    distros = load()
    results = search(args.search_term, distros)

    if args.output == 'text':
        display_text(results)
    elif args.output == 'json':
        display_json(results)
    elif args.output == 'csv':
        display_csv(results)


def load():
    """Load data from distro/data.py, return a list of Distro() objects"""
    return [Distro(**dt) for dt in DATA]


def search(terms, distros):
    """Search for items in the list of Distro() objects using the provided search terms."""
    results = []

    for dist in distros:
        if all(t in dist.raw() for t in terms):
            results.append(dist)

    return results


def display_text(results):
    """Display search results in raw TEXT format"""
    for result in results:
        print(result)


def display_csv(results):
    """Display search results in CSV format"""
    for result in results:
        print(result.raw())


def display_json(results):
    """Display search results in JSON format"""
    print('NOT IMPLEMENTED')
    for result in results:
        print(result.raw())


class Distro:
    """Distro data wrapper class. Instantiate with a dict"""

    def __init__(self, **kwargs):
        self.data = kwargs

        if 'name' not in self.data.keys():
            raise Exception('Name is required')
        if 'version' not in self.data.keys() and 'versions' not in self.data.keys():
            raise Exception('Either version or list of versions required')
        if 'flavour' not in self.data.keys():
            self.data['flavour'] = 'Linux'

        if self.data.get('versions', None) is None:
            self.data['versions'] = list()
        elif isinstance(self.data.get('versions', None), str):
            self.data['versions'] = list(self.data['versions'])

        ver = self.data.pop('version', None)
        if ver is not None and ver not in self.data['versions']:
            self.data['versions'].append(ver)

    def __str__(self):
        lpad = max([len(key) for key, val in self.data.items()]) + 5
        out_str = ''
        for key, val in sorted(self.data.items()):
            out_str += '{}:'.format(key.replace('_', ' ').title()).ljust(lpad, ' ')
            if isinstance(val, list):
                out_str += '{}\n'.format(', '.join(val))
            else:
                out_str += '{}\n'.format(val)
        return out_str

    def raw(self):
        """Return data in simplified CSV format, all in lowercase"""
        out = list()
        for key, val in sorted(self.data.items()):
            if isinstance(val, list):
                out.append('{}:{}'.format(key, ','.join(val)))
            else:
                out.append('{}:{}'.format(key, val))
        return ','.join(out).lower()
