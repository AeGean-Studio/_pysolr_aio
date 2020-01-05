try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='pysolr_aio',
    use_scm_version=True,
    description='Lightweight Python client for Apache Solr',
    author='Daniel Lindsley',
    author_email='daniel@toastdriven.com',
    long_description=open('README.rst', 'r').read(),
    py_modules=['pysolr_aio'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Programming Language :: Python :: 3',
    ],
    url='https://github.com/AeGean-Studio/pysolr_aio',
    license='BSD',
    install_requires=['httpx>=0.10.0'],
    extras_require={'solrcloud': ['kazoo>=2.5.0']},
    setup_requires=['setuptools_scm'],
    python_requires='>=3.6',
)
