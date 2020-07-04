import argparse
import pathlib
import ruamel.yaml


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('package_name')
    parser.add_argument('href')
    parser.add_argument('hash_name')
    parser.add_argument('hash_value')
    return parser.parse_args()


def main():
    args = parse_args()
    packages_file = pathlib.Path('packages.yaml').resolve()
    yaml = ruamel.yaml.YAML(typ='safe')
    package_data = yaml.load(packages_file)
    packages = package_data.get('packages')
    package = packages.get(args.package_name, {})
    files = package.get('files', [])
    files.append({
        'href': args.href,
        'hash_name': args.hash_name,
        'hash_value': args.hash_value
    })
    package['files'] = files
    packages[args.package_name] = package
    package_data['packages'] = packages
    print(f'Writing to {packages_file} ...')
    yaml.default_flow_style = False
    yaml.indent(mapping=2, sequence=4, offset=2)
    yaml.dump(package_data, packages_file)


if __name__ == '__main__':
    main()
