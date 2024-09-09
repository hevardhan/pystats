from setuptools import setup, find_packages

setup(
    name='pystats',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here, e.g.:
        # 'numpy', 'pandas',
    ],
    author='Hevardhan',
    author_email='hevardhan2004@gmail.com',
    description='A brief description of your library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_library',  # Link to your repo
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify Python version support
)
