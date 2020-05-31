try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': "Exercise 47 from LPTHW",
    'author': 'Luis C.',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'luisco28@gmail.com',
    'version': '0.1',
    'install_requires': ['none'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'Exercise 47'
}

setup(**config)