from setuptools import setup, find_packages

VERSION = '1.1.1'

setup(
    name="mkdocs-ubuntu",
    version=VERSION,
    url='http://mkdocs.github.io/mkdocs-bootstrap/',
    license='MIT',
    description='Vanilla framework base Ubuntu theme for MkDocs',
    author='Youngbin Han',
    author_email='ybhan@ubuntu.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['mkdocs>=1.1'],
    python_requires='>=3.5',
    entry_points={
        'mkdocs.themes': [
            'ubuntu = mkdocs_ubuntu',
        ]
    },
    zip_safe=False
)