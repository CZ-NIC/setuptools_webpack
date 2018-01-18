import setuptools_webpack
from setuptools import setup


def main():
    setup(name='setuptools_webpack',
          version=setuptools_webpack.__version__,
          description='Plugin for setuptools to run webpack',
          long_description=open('README.md').read(),
          py_modules=['setuptools_webpack'],
          author='Jan Musilek',
          author_email='jan.musilek@nic.cz',
          url='https://github.com/CZ-NIC/setuptools_webpack',
          entry_points={
              "distutils.commands": [
                  "build_js = setuptools_webpack:build_js",
              ],
              "distutils.setup_keywords": [
                  "webpack_output_path = setuptools_webpack:check_webpack_output_path",
              ],
          },
          license='GPLv3',
          classifiers=[
              'Development Status :: 4 - Beta',
              'Intended Audience :: Developers',
              'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
              'Operating System :: OS Independent',
              'Programming Language :: Python :: 2',
              'Programming Language :: Python :: 2.6',
              'Programming Language :: Python :: 2.7',
              'Programming Language :: Python :: 3',
              'Programming Language :: Python :: 3.5',
              'Programming Language :: Python :: 3.6',
              'Topic :: Software Development :: Build Tools',
          ],
          )


if __name__ == '__main__':
    main()
