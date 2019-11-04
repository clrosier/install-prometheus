import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_prometheus_endpoint(host):
    command = """curl --digest -L -D - http://localhost:9090 \
                 -u ansible:ansible"""

    cmd = host.run(command)
    assert 'HTTP/1.1 200 OK' in cmd.stdout
