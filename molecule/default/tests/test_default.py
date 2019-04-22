import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_sudoer_file(host):
    f = host.file('/etc/sudoers.d/sysadmin')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.contains("^sysadmin")


def test_user(host):
    user = host.user("sysadmin")

    assert user.name == "sysadmin"
    assert user.group == "sysadmin"
    assert user.home == "/home/sysadmin"
    assert user.shell == "/bin/bash"


def test_sshd_socket(host):
    s = host.socket("tcp://0.0.0.0:22")

    assert s.is_listening
