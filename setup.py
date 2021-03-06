from setuptools import setup


setup(
    name='Flask-SuRF-Allegrograph',
    version='0.1',
    url='https://github.com/SergioML9/flask-surf-allegrograph/',
    license='BSD',
    author='Sergio Muñoz',
    author_email='sergio.munoz@upm.es',
    description='Very short description',
    long_description=__doc__,
    packages=['flask_surf_allegrograph'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'SuRF @ git+https://github.com/franzlst/surfrdf@master',
        'surf.allegro_franz @ git+https://github.com/SergioML9/surfrdf-allegrofranz-plugin@main',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)