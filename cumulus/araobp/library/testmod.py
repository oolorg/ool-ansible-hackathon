from ansible.module_utils.basic import * 

def main():
    module = AnsibleModule(
        argument_spec = dict(
            state     = dict(default='present', choices=['present', 'absent']),
            name      = dict(required=True)
        )
    )
    state = module.params['state']
    name = module.params['name']
    module.exit_json(msg='{} {}'.format(state, name))


if __name__ == '__main__':
    main()
