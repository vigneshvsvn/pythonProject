"""
If we want to access package. Then our module and package should be in same  current directory where our Module is there.

To overcome: Means I need to access package from anywhere from my system. Then we need to install

syntax:

Way 1:

Step 1: setup script need to create with name setup.py  on same folder where package available
	from setuptools import setup
	setup(name='vehicleLoan',
	  version='0.1',
	  packages=['vehicleLoan']
	  )

step 2: pip install .

Now we can use this package from anywhere.

"""

