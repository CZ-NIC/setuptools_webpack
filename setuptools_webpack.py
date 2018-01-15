"""Plugin for setuptools providing running webpack bundler."""
import os

from setuptools import Command

__version__ = '0.1.1'


def check_webpack_output_path(dist, attr, value):
    """Check webpack output path.

    Webpack creates non-existent directories. There is nothing to check."""
    pass


class build_js(Command):
    """Custom command that runs webpack."""

    user_options = [
        ('build-lib=', 'd', "directory to \"build\" (copy) to"),
        ('config=', 'c', "webpack configuration file"),
        ]

    def initialize_options(self):
        self.build_lib = None
        self.config = 'webpack.config.js'

    def finalize_options(self):
        self.set_undefined_options('build', ('build_lib', 'build_lib'))

    def run(self):
        if self.distribution.webpack_output_path:
            output_path = os.path.join(self.build_lib, self.distribution.webpack_output_path)
            os.system("webpack --output-path '%s'" % output_path)
