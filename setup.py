from setuptools import setup

setup(
    name='cloner',
    version='1.0',
    py_modules=['cloner'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        cloner=cloner:cli
    '''
)
