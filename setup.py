from io import open
from setuptools import setup


with open('README.md', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

VERSION = 'v0.0.2'
DESCRIPTION = 'Simple calendar for telegram bot (aiogram v2.x)'


setup(
  author='Nik Bbt-t',
  author_email='bbt-pip@yandex.ru',
  name='SACalendar',
  packages=['SACalendar'],
  version=VERSION,
  license='MIT License',
  description=DESCRIPTION,
  long_description=LONG_DESCRIPTION,
  long_description_content_type='text/markdown',
  url='https://github.com/bbt-t/SACalendar',
  download_url='https://github.com/bbt-t/SACalendar/archive/refs/tags/v0.0.2.tar.gz',
  keywords=['async', 'aiogram', 'telegram', 'bot', 'calendar'],
  install_requires=[
          'aiogram',
      ],
  classifiers=[
    'Programming Language :: Python :: 3.10'
  ],
)
