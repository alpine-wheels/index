import jinja2
import pathlib
import re
import ruamel.yaml


def normalize(name):
    return re.sub(r'[-_.]+', '-', name).lower()


def name_from_href(href: str) -> str:
    _, _, name = href.rpartition('/')
    return name


def main():
    jinja_env = jinja2.Environment(autoescape=jinja2.select_autoescape(['html']), keep_trailing_newline=True,
                                   loader=jinja2.FileSystemLoader('_templates'), trim_blocks=True)
    jinja_env.filters['name_from_href'] = name_from_href
    jinja_env.filters['normalize'] = normalize
    packages_file = pathlib.Path('packages.yaml').resolve()
    yaml = ruamel.yaml.YAML(typ='safe')
    packages = yaml.load(packages_file)
    for name, data in packages.get('packages').items():
        package_template = jinja_env.get_template('package.html')
        package_rendered = package_template.render(name=name, package=data)
        out_dir = pathlib.Path(normalize(name))
        out_dir.mkdir(exist_ok=True)
        out_file = out_dir / 'index.html'
        with out_file.open('w') as f:
            f.write(package_rendered)
    index_template = jinja_env.get_template('index.html')
    index_rendered = index_template.render(packages=packages.get('packages'))
    out_file = pathlib.Path('index.html')
    with out_file.open('w') as f:
        f.write(index_rendered)


if __name__ == '__main__':
    main()
