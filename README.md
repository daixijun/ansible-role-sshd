Role Name
=========

[![Build Status](https://travis-ci.com/daixijun/ansible-role-sshd.svg?branch=master)](https://travis-ci.com/daixijun/ansible-role-sshd)

配置sshd

Requirements
------------

* RHEL/Centos 7

Role Variables
--------------

```yaml
sshd_port: 22   # 端口
sshd_manage_user: sysadmin # 管理员账号
sshd_pubkeys: []  # 公钥文件路径
```

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: daixijun.sshd
      sshd_manage_user: sysadmin
      sshd_pubkeys:
        - /tmp/test.pub
```

License
-------

BSD

Author Information
------------------

Xijun Dai <daixijun1990@gmail.com>
