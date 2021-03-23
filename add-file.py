import argparse
import pathlib
import sqlite3


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('package_name')
    parser.add_argument('href')
    parser.add_argument('hash_name')
    parser.add_argument('hash_value')
    return parser.parse_args()


def main():
    args = parse_args()
    cnx = sqlite3.connect(pathlib.Path('packages.db').resolve())
    with cnx:
        cnx.execute('''
            insert into packages (name, hash_name, hash_value, href)
            values (:name, :hash_name, :hash_value, :href)
        ''', {
            'name': args.package_name,
            'hash_name': args.hash_name,
            'hash_value': args.hash_value,
            'href': args.href
        })
    cnx.close()


if __name__ == '__main__':
    main()
