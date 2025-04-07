# Ansible Playbook Deployment output:

```bash
tjann@fedora:~/DevOps-Course/ansible$ ansible-playbook playbooks/dev/main.yaml | tail -n 50
[WARNING]: Platform linux on host yandex_vm is using the discovered Python
interpreter at /usr/bin/python3.10, but future installation of another Python
interpreter could change the meaning of that path. See
https://docs.ansible.com/ansible-
core/2.18/reference_appendices/interpreter_discovery.html for more information.

PLAY [install Docker] **********************************************************

TASK [Gathering Facts] *********************************************************
ok: [yandex_vm]

TASK [docker : Install Docker & compose] ***************************************
included: /home/tjann/DevOps-Course/ansible/roles/docker/tasks/install_docker.yml for yandex_vm

TASK [docker : Install prerequisites] ******************************************
ok: [yandex_vm]

TASK [docker : Add Docker official GPG key] ************************************
ok: [yandex_vm]

TASK [docker : Add Docker repository] ******************************************
ok: [yandex_vm]

TASK [docker : Update package cache] *******************************************
changed: [yandex_vm]

TASK [docker : Install Docker] *************************************************
ok: [yandex_vm]

TASK [docker : Ensure Docker is running] ***************************************
ok: [yandex_vm]

TASK [docker : Install Docker Compose] *****************************************
included: /home/tjann/DevOps-Course/ansible/roles/docker/tasks/install_compose.yml for yandex_vm

TASK [docker : Install Docker Compose] *****************************************
ok: [yandex_vm]

PLAY RECAP *********************************************************************
yandex_vm                  : ok=10   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```
# Inventory Details

## Inventory list

```bash
tjann@fedora:~/DevOps-Course/ansible$ ansible-inventory -i inventory/default_aws_ec2.yml --list
{
    "_meta": {
        "hostvars": {
            "yandex_vm": {
                "ansible_host": "89.169.129.233",
                "ansible_ssh_private_key_file": "~/.ssh/yandex_vm",
                "ansible_user": "tjann"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    },
    "ungrouped": {
        "hosts": [
            "yandex_vm"
        ]
    }
}
```

## Inventory Structure

```bash
tjann@fedora:~/DevOps-Course/ansible$ ansible-inventory -i inventory/default_aws_ec2.yml --graph
@all:
  |--@ungrouped:
  |  |--yandex_vm
```


