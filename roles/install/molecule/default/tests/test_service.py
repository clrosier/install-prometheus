import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_service_file_exists(host):
    service_file = host.file('/etc/systemd/system/prometheus.service')

    assert service_file.exists
    assert service_file.user == 'root'
    assert service_file.group == 'prometheus'


def test_prometheus_running_and_enabled(host):
    prometheus = host.service('prometheus')
    assert prometheus.is_running
    assert prometheus.is_enabled
