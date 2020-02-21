# Disruptor like library in python

WIP

# Testing

## Command Line

```
$ python -m pytest
```

### Dependencies
```
$ pytest --version
This is pytest version 5.3.2, imported from /home/troy/anaconda3/lib/python3.7/site-packages/pytest/__init__.py
setuptools registered plugins:
  pytest-remotedata-0.3.2 at /home/troy/anaconda3/lib/python3.7/site-packages/pytest_remotedata/plugin.py
  pytest-doctestplus-0.5.0 at /home/troy/anaconda3/lib/python3.7/site-packages/pytest_doctestplus/plugin.py
  pytest-openfiles-0.4.0 at /home/troy/anaconda3/lib/python3.7/site-packages/pytest_openfiles/plugin.py
  pytest-arraydiff-0.3 at /home/troy/anaconda3/lib/python3.7/site-packages/pytest_arraydiff/plugin.py
  hypothesis-4.54.2 at /home/troy/anaconda3/lib/python3.7/site-packages/hypothesis/extra/pytestplugin.py
  pytest-astropy-header-0.1.1 at /home/troy/anaconda3/lib/python3.7/site-packages/pytest_astropy_header/display.py
```

## VSCode

Create a .env file in the root of the project and add something like the following

```
PYTHONPATH=/home/troy/development/python/disruptor
```