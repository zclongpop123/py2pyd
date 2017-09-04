#========================================
#    author: Changlong.Zang
#      mail: zclongpop123@163.com
#      time: Mon Sep 04 15:49:59 2017
#========================================
import sys, re, os
import distutils.core, distutils.extension
import Cython.Build
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def py2pyd(path):
    '''
    '''
    os.chdir(path)

    file_list = os.listdir(path)
    for f in file_list:
        if os.path.isdir(f):
            continue

        if not re.search('.py$', f):
            continue

        if re.match('setup.py', f):
            continue

        if re.match('__init__.py', f):
            continue

        if re.search('_rc.py', f):
            continue

        module_name = os.path.splitext(f)[0]
        extensions = [distutils.extension.Extension(module_name, [f])]
        distutils.core.setup(name=module_name, ext_modules=Cython.Build.cythonize(extensions))

        for ext in ('c', 'pyc'):
            f = '{0}.{1}'.format(module_name, ext)
            os.path.isfile(f) and os.remove(f)





if __name__ == '__main__':
    py2pyd(os.getcwd())