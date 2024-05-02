from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    description = f.read()

setup(
    name='McQueen',
    version='0.5.0',
    author='Michael Cao',
    author_email='caohoangphuc2909@gmail.com',
    url="https://github.com/hpcao299/McQueen",
    description='A collection of information-gathering tools',
    packages=find_packages(),
    install_requires=['dnspython', 'requests', 'argparse', 'beautifulsoup4'],
    python_requires='>=3.6',
    license='MIT',
    classifiers=[
        'Programming Language :: Python',
        'Topic :: Security',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
    ],
    entry_points={
        'console_scripts': [
            'mcqueen = McQueen:interactive',
        ],
    },
    long_description=description,
    long_description_content_type='text/markdown'
)