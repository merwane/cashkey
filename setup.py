import setuptools

with open("README.md", 'r') as fh:
    long_description = fh.read()

setuptools.setup(
        name = "cashkey",
        version = "0.0.2",
        author = "Merwane Draï",
        author_email = "merwanedr@gmail.com",
        description = "A bank on your $5 USB stick",
        long_description = long_description,
        long_description_content_type = "text/markdown",
        url = "https://github.com/merwane/cashkey",
        download_url='https://github.com/merwane/cashkey',
        packages = setuptools.find_packages(),
        classifiers = [
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            'Natural Language :: English',
            'Intended Audience :: End Users/Desktop'
            ],
        license='MIT',
        keywords=(
            'bitcoincash',
            'cryptocurrency',
            'wallet',
            'payment',
            'cli'
            ),
        install_requires=[
            "bitcash",
            "cryptography",
            "colorama",
            "halo",
            "qrcode"
            ],
        entry_points={
            'console_scripts': [
                'cashkey = cashkey.__main__:main'
                ]
            },
        )
