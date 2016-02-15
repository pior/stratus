# Hack notes

## Entities

alarm:
    name
    description
    state
    old_state
    state_change
    state_reason
    

## Cloudwatch notes

Alarm payload:

    {u'AWSAccountId': u'123412341234',
    u'AlarmDescription': u'my-alarm-description',
    u'AlarmName': u'my-alarm-name',
    u'NewStateReason': u'Threshold Crossed: 1 datapoint (1459.0) was greater  than or equal to the threshold (0.0).',
    u'NewStateValue': u'ALARM',
    u'OldStateValue': u'INSUFFICIENT_DATA',
    u'Region': u'APAC - Sydney',
    u'StateChangeTime': u'2015-01-11T00:33:20.013+0000',
    u'Trigger': {u'ComparisonOperator': u'GreaterThanOrEqualToThreshold',
     u'Dimensions': [{u'name': u'InstanceId', u'value': u'i-af41ec91'}],
     u'EvaluationPeriods': 1,
     u'MetricName': u'NetworkIn',
     u'Namespace': u'AWS/EC2',
     u'Period': 60,
     u'Statistic': u'SUM',
     u'Threshold': 0.0,
     u'Unit': None}}
