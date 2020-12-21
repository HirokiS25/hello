import setuptools

setuptools.setup(
    name='hello',
    version='0.0',
    author='y',
    author_email='hogehoge@hoge',
    description='Say',
    url='https://hoge.jp',
    packages=['hello_world'],
    package_dir={'hello_world': 'src/hello_world'},
    python_requires='>=3.8',
    entry_points={
        'console_scripts': ['hello = src.hello_world.say_hello:hello']
    }
)