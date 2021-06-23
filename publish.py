import itertools
import jinja2
import pathlib
import re
import sqlite3


def normalize(name):
    return re.sub(r'[-_.]+', '-', name).lower()


def name_from_href(href: str) -> str:
    _, _, name = href.rpartition('/')
    return name


def get_name(row):
    return row['name']


def main():
    jinja_env = jinja2.Environment(autoescape=jinja2.select_autoescape(['html']), keep_trailing_newline=True,
                                   loader=jinja2.FileSystemLoader('_templates'), trim_blocks=True)
    jinja_env.filters['name_from_href'] = name_from_href
    jinja_env.filters['normalize'] = normalize
    packages_sql = pathlib.Path('packages.sql').resolve()
    cnx = sqlite3.connect(':memory:')
    cnx.row_factory = sqlite3.Row
    with packages_sql.open() as f:
        cnx.executescript(f.read())
    cur = cnx.execute('select name, hash_name, hash_value, href from packages order by name, href')
    packages = cur.fetchall()
    package_names = []
    for name, packages in itertools.groupby(packages, get_name):
        package_names.append(name)
        package_template = jinja_env.get_template('package.html')
        package_rendered = package_template.render(name=name, packages=packages)
        out_dir = pathlib.Path(normalize(name))
        out_dir.mkdir(exist_ok=True)
        out_file = out_dir / 'index.html'
        with out_file.open('w') as f:
            f.write(package_rendered)
    index_template = jinja_env.get_template('index.html')
    index_rendered = index_template.render(packages=package_names)
    out_file = pathlib.Path('index.html')
    with out_file.open('w') as f:
        f.write(index_rendered)


if __name__ == '__main__':
    main()
