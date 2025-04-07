import setuptools
#with open("README.md", "r") as fh:
#    long_description = fh.read()
setuptools.setup(
     name='spork-testing',  
     version='0.0.1',
     scripts=['test'] ,
     author="spork1on",
     author_email="diegobavutti@gmail.com",
#     long_description=long_description,
   long_description_content_type="text/markdown",
     packages=setuptools.find_packages(),
 )
