from setuptools import setup, find_packages

setup(
    name='McQueen',
    version='0.3.2',
    url="https://github.com/hpcao299/McQueen",
    description='A collection of information-gathering tools',
    packages=find_packages(),
    install_requires=['dnspython', 'requests', 'argparse', 'beautifulsoup4'],
    python_requires='>=3.6',
    license='MIT',
    classifiers=[
        'Programming Language :: Python'
        'Programming Language :: Python :: 3',
        'Topic :: Security',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
    ],
)