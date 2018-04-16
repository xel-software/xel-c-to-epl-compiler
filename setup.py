import os, sys
try:
    from setuptools import setup
    from setuptools.command.install import install as _install
    from setuptools.command.sdist import sdist as _sdist
except ImportError:
    from distutils.core import setup
    from distutils.command.install import install as _install
    from distutils.command.sdist import sdist as _sdist


def _run_build_tables(dir):
    from subprocess import call
    call([sys.executable, '_build_tables.py'],
         cwd=os.path.join(dir, 'ctoepl'))


class install(_install):
    def run(self):
        _install.run(self)
        self.execute(_run_build_tables, (self.install_lib,),
                     msg="Build the lexing/parsing tables")


class sdist(_sdist):
    def make_release_tree(self, basedir, files):
        _sdist.make_release_tree(self, basedir, files)
        self.execute(_run_build_tables, (basedir,),
                     msg="Build the lexing/parsing tables")


setup(
    # metadata
    name='c-to-epl',
    description='C to ePL Converter in Python',
    long_description="""
        C to ePL Converter in Python
    """,
    license='BSD',
    version='1.0',
    author='Xeline Software Development Team',
    maintainer='Xeline Software Development Team',
    author_email='junk@mailinator.com',
    url='https://github.com/xel-software/c-to-epl',
    download_url = 'https://github.com/xel-software/c-to-epl/archive/1.0.tar.gz',
    platforms='Cross Platform',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=['ctoepl', 'ctoepl.ply'],
    package_data={'ctoepl': ['*.cfg']},
    entry_points={
    'console_scripts': [
        'c_to_epl=ctoepl:main',
    ],
},
    cmdclass={'install': install, 'sdist': sdist},
)
