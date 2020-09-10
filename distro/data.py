"""
The Distro data. Names, versions, and any other information.

The DATA variable is a Python LIST of DICTs, each dict is required, at a minimum:

- a 'name' key of type String
- either a 'version' key of type String OR a 'versions' key of type List (of strings)

If no 'flavour' key is provided, the default will be 'Linux'

Any other key/value pair will be added as is to the Distro object
"""

DATA = [
    # Ubuntu (source: http://releases.ubuntu.com/)
    {'name': 'precise', 'versions': ['12.04', '12.04.5'], 'full_name': 'Precise Pangolin', 'flavour': 'Ubuntu'},
    {'name': 'trusty', 'versions': ['14.04', '14.04.6'], 'full_name': 'Trusty Thar', 'flavour': 'Ubuntu'},
    {'name': 'xenial', 'versions': ['16.04', '16.04.6'], 'full_name': 'Xenial Xerus', 'flavour': 'Ubuntu'},
    {'name': 'bionic', 'versions': ['18.04', '18.04.2'], 'full_name': 'Bionic Beaver', 'flavour': 'Ubuntu'},
    {'name': 'cosmic', 'versions': ['18.10'], 'full_name': 'Cosmic Cuttlefish', 'flavour': 'Ubuntu'},
    {'name': 'disco', 'versions': ['19.04'], 'full_name': 'Disco Dingo', 'flavour': 'Ubuntu'},
    {'name': 'fossa', 'versions': ['20.04'], 'full_name': 'Focal Fossa', 'flavour': 'Ubuntu'},
    {'name': 'gorilla', 'versions': ['20.10'], 'full_name': 'Groovy Gorilla', 'flavour': 'Ubuntu'},

    # Debian (source: https://www.debian.org/releases/)
    {'name': 'squeeze', 'version': '6', 'flavour': 'Debian'},
    {'name': 'wheezy', 'version': '7', 'flavour': 'Debian'},
    {'name': 'jessie', 'version': '8', 'flavour': 'Debian'},
    {'name': 'stretch', 'version': '9', 'flavour': 'Debian'},
    {'name': 'buster', 'version': '10', 'flavour': 'Debian'},
    {'name': 'bullseye', 'version': '11', 'flavour': 'Debian'},

    # Mint (source: https://en.wikipedia.org/wiki/Linux_Mint_version_history)
    {'name': 'ada', 'version': '1.0', 'flavour': 'Mint'},
    {'name': 'barbara', 'version': '2.0', 'flavour': 'Mint'},
    {'name': 'bea', 'version': '2.1', 'flavour': 'Mint'},
    {'name': 'bianca', 'version': '2.2', 'flavour': 'Mint'},
    {'name': 'cassandra', 'version': '3.0', 'flavour': 'Mint'},
    {'name': 'celena', 'version': '3.1', 'flavour': 'Mint'},
    {'name': 'daryna', 'version': '4', 'flavour': 'Mint'},
    {'name': 'elyssa', 'version': '5', 'flavour': 'Mint'},
    {'name': 'felicia', 'version': '6', 'flavour': 'Mint'},
    {'name': 'gloria', 'version': '7', 'flavour': 'Mint'},
    {'name': 'helena', 'version': '8', 'flavour': 'Mint'},
    {'name': 'isadora', 'version': '9', 'flavour': 'Mint'},
    {'name': 'julia', 'version': '10', 'flavour': 'Mint'},
    {'name': 'katya', 'version': '11', 'flavour': 'Mint'},
    {'name': 'lisa', 'version': '12', 'flavour': 'Mint'},
    {'name': 'maya', 'version': '13', 'flavour': 'Mint'},
    {'name': 'nadia', 'version': '14', 'flavour': 'Mint'},
    {'name': 'olivia', 'version': '15', 'flavour': 'Mint'},
    {'name': 'petra', 'version': '16', 'flavour': 'Mint'},
    {'name': 'qiana', 'version': '17', 'flavour': 'Mint'},
    {'name': 'rebecca', 'version': '17.1', 'flavour': 'Mint'},
    {'name': 'rafaela', 'version': '17.2', 'flavour': 'Mint'},
    {'name': 'rosa', 'version': '17.3', 'flavour': 'Mint'},
    {'name': 'sarah', 'version': '18', 'flavour': 'Mint'},
    {'name': 'serena', 'version': '18.1', 'flavour': 'Mint'},
    {'name': 'sonya', 'version': '18.2', 'flavour': 'Mint'},
    {'name': 'sylvia', 'version': '18.3', 'flavour': 'Mint'},
    {'name': 'tara', 'version': '19', 'flavour': 'Mint'},
    {'name': 'tessa', 'version': '19.1', 'flavour': 'Mint'},
    {'name': 'tina', 'version': '19.2', 'flavour': 'Mint'},
    {'name': 'tricia', 'version': '19.3', 'flavour': 'Mint'},
    {'name': 'ulyana', 'version': '20', 'flavour': 'Mint'},

    # Mac OS X (source: https://en.wikipedia.org/wiki/MacOS#Release_history)
    {'name': 'cheetah', 'version': '10.0', 'full_name': 'Mac OS X 10.0 Cheetah', 'flavour': 'MacOS'},
    {'name': 'puma', 'version': '10.1', 'full_name': 'Mac OS X 10.1 Puma', 'flavour': 'MacOS'},
    {'name': 'jaguar', 'version': '10.2', 'full_name': 'Mac OS X 10.2 Jaguar', 'flavour': 'MacOS'},
    {'name': 'panther', 'version': '10.3', 'full_name': 'Mac OS X 10.3 Panther', 'flavour': 'MacOS'},
    {'name': 'tiger', 'version': '10.4', 'full_name': 'Mac OS X 10.4 Tiger', 'flavour': 'MacOS'},
    {'name': 'leopard', 'version': '10.5', 'full_name': 'Mac OS X 10.5 Leopard', 'flavour': 'MacOS'},
    {'name': 'snow leopard', 'version': '10.6', 'full_name': 'Mac OS X 10.6 Snow Leopard', 'flavour': 'MacOS'},
    {'name': 'lion', 'version': '10.7', 'full_name': 'Mac OS X 10.7 Lion', 'flavour': 'MacOS'},
    {'name': 'mountain lion', 'version': '10.8', 'full_name': 'OS X 10.8 Mountain Lion', 'flavour': 'MacOS'},
    {'name': 'mavericks', 'version': '10.9', 'full_name': 'OS X 10.9 Mavericks', 'flavour': 'MacOS'},
    {'name': 'yosemite', 'version': '10.10', 'full_name': 'OS X 10.10 Yosemite', 'flavour': 'MacOS'},
    {'name': 'el capitan', 'version': '10.11', 'full_name': 'OS X 10.11 El Capitan', 'flavour': 'MacOS'},
    {'name': 'sierra', 'version': '10.12', 'full_name': 'macOS 10.12 Sierra', 'flavour': 'MacOS'},
    {'name': 'high sierra', 'version': '10.13', 'full_name': 'macOS 10.13 High Sierra', 'flavour': 'MacOS'},
    {'name': 'mojave', 'version': '10.14', 'full_name': 'macOS 10.14 Mojave', 'flavour': 'MacOS'},
    {'name': 'catalina', 'version': '10.15', 'full_name': 'macOS 10.15 Catalina', 'flavour': 'MacOS'},
    {'name': 'big sur', 'version': '11.0', 'full_name': 'macOS 11 Big Sur', 'flavour': 'MacOS'},

    # Android (source: https://en.wikipedia.org/wiki/Android_version_history)
    {'name': 'cupcake', 'version': '1.5', 'full_name': 'Android 1.5 Cupcake', 'flavour': 'Android'},
    {'name': 'donut', 'version': '1.6', 'full_name': 'Android 1.6 Donut', 'flavour': 'Android'},
    {'name': 'eclair', 'version': '2.0', 'full_name': 'Android 2.0 Eclair', 'flavour': 'Android'},
    {'name': 'froyo', 'version': '2.2', 'full_name': 'Android 2.2 Froyo', 'flavour': 'Android'},
    {'name': 'gingerbread', 'version': '2.3', 'full_name': 'Android 2.3 Gingerbread', 'flavour': 'Android'},
    {'name': 'honeycomb', 'version': '3.0', 'full_name': 'Android 3.0 Honeycomb', 'flavour': 'Android'},
    {'name': 'ice cream sandwich', 'version': '4.0', 'full_name': 'Android 4.0 Ice Cream Sandwich', 'flavour': 'Android'},
    {'name': 'jelly bean', 'version': '4.1', 'full_name': 'Android 4.1 Jelly Bean', 'flavour': 'Android'},
    {'name': 'kitkat', 'version': '4.4', 'full_name': 'Android 4.4 KitKat', 'flavour': 'Android'},
    {'name': 'lollipop', 'version': '5.0', 'full_name': 'Android 5.0 Lollipop', 'flavour': 'Android'},
    {'name': 'marshmallow', 'version': '6.0', 'full_name': 'Android 6.0 Marshmallow', 'flavour': 'Android'},
    {'name': 'nougat', 'version': '7.0', 'full_name': 'Android 7.0 Nougat', 'flavour': 'Android'},
    {'name': 'oreo', 'version': '8.0', 'full_name': 'Android 8.0 Oreo', 'flavour': 'Android'},
    {'name': 'pie', 'version': '9', 'full_name': 'Android 9 Pie', 'flavour': 'Android'},
]
