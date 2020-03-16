## Prometheus Installation Playbook

Created to install Prometheus and manage the hosts within Prometheus through a pipeline

### Usage
The prometheus configuration that this playbook relies on is hosted within another repository and can be specified within the vars file.

By default, the configuration from the master branch will be deployed and this can be overridden by providing a `branch` variable into the `extra-vars` at run-time.

__Example__
```bash
# Note you'd need to create and specify your own hosts file here if choosing to run this playbook through the command-line
ansible-playbook -i hosts --extra-vars '{"branch": "dev"}'
```

Additonally, this works very well with Ansible Tower if one would choose to go that route as you could define your own inventory and credentials within the user interface.

