from setuptools import setup, find_packages

setup(
    name='pystats',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
    ],
    author='Hevardhan',
    author_email='hevardhan2004@gmail.com',
    description='A package for SMA crossover, MACD, and Heiken Ashi strategies',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/hevardhan/pystats',  # Your GitHub URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
