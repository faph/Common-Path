from setuptools import setup
import versioneer

setup(
    name='commonpath',
    packages=['commonpath'],
    zip_safe=False,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass()
)
