from setuptools import setup, find_packages

setup(
    name='netapp_lib',
    description='NetApp clustered Data ONTAP Library',
    long_description='This library is slightly modified netapp-lib'
                     ' (part of netapp-flocker-driver'
                     ' https://github.com/NetApp/netapp-flocker-driver)'
                     ' that is required for Ansible storage/netapp modules',

    author='NetApp, Inc.',
    author_email='opensource@netapp.com',
    license='Apache 2.0',
    url='TBD',
    version='2018.10.30',
    # packages=['suit', 'suit.templatetags'],
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        "lxml",
        "oslo.log",
        "xmltodict",
    ],

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
    ],
)
