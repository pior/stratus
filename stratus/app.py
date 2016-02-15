import logging

from eve import Eve


app = Eve()

app.logger.setLevel(logging.DEBUG)
app.debug = True


def on_inserted_deployment_updates(items):
    for item in items:

        update = {}
        if 'status' in item:
            update['status'] = item['status']
        if 'outcome' in item and item['outcome']:
            update['outcome'] = item['outcome']
        if 'message' in item:
            update['message'] = item['message']

        app.data.update('deployments', item['deployment_id'], update, {})

app.on_inserted_deployment_updates += on_inserted_deployment_updates


if __name__ == '__main__':
    app.run()
