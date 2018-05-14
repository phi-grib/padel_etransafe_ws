from subprocess import Popen, PIPE, STDOUT

PADEL_PATH = 'opt/api'


def start_nailgun():
    """
    starts nailgun server
    """
    print('...starting nailgun')
    
    cmd = ['java',
           '-classpath',
           'nailgun-server-0.9.3-SNAPSHOT.jar',
           'com.martiansoftware.nailgun.NGServer']

    proc = Popen(cmd, stdout=PIPE, stderr=STDOUT)


def add_cp_nailgun():
    """
    adds PaDEL lib and PaDEL jar with main to nailgun classpath
    """
    print('...adding claspath to nailgun server')
    cmd = 'ng ng-cp lib/*.jar PaDEL-Descriptor.jar'

    proc = Popen(cmd,
                 stdout=PIPE,
                 stdin=PIPE,
                 stderr=PIPE,
                 shell=True)

    stdout, stderr = proc.communicate()

    if stdout:
        print(stdout)
    if stderr:
        print(stderr)
