
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']


_SERVICE = {
    'schema': {
        'label': {
            'type': 'string',
        },
        'name': {
            'type': 'string',
        },
    },
}


_DEPLOYMENT = {
    'schema': {
        'service_id': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'services',
            },
        },
        'version': {
            'type': 'string',
            'required': True,
        },
        'status': {
            'readonly': True,
            'default': None,
        },
        'outcome': {
            'readonly': True,
            'default': None,
        },
        'message': {
            'readonly': True,
        }
    },
}

_DEPLOYMENT_UPDATES = {
    'schema': {
        'deployment_id': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'deployments',
            },
        },
        'status': {
            'type': 'string',
            'allowed': ['INPROGRESS', 'DONE'],
            'required': True,
        },
        'outcome': {
            'type': 'string',
            'allowed': ['SUCCESS', 'FAILED'],
            'nullable': True,
            'default': None,
        },
        'message': {
            'type': 'string',
        }
    },
    'datasource': {
        'default_sort': [('_created', -1)],
    },
}


_ALARM = {
    'schema': {
        'service_id': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'services',
            },
        },
        'name': {
            'type': 'string',
            'required': True,
            },
        'description': {
            'type': 'string',
        },
        'status': {
            'readonly': True,
        },
        'reason': {
            'readonly': True,
        },
    },
}
_ALARM_UPDATES = {
    'schema': {
        'alarm_id': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'alarms',
            },
        },
        'status': {
            'type': 'string',
            'allowed': ['OK', 'ERROR'],
        },
        'reason': {
            'type': 'string',
        },
    },
    'datasource': {
        'default_sort': [('_created', -1)],
    }
}


DOMAIN = {
    'services': _SERVICE,

    'alarms': _ALARM,
    'alarm_updates': _ALARM_UPDATES,

    'deployments': _DEPLOYMENT,
    'deployment_updates': _DEPLOYMENT_UPDATES,
}
