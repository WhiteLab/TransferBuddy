import argparse
import requests

from eve import Eve


def producer():
    eve_settings = {
        'MONGO_HOST': 'localhost',
        'MONGO_PORT': 27017,
        'MONGO_DBNAME': 'tbuddy',
        'DOMAIN': {
            'people': {},
            'things': {}
        }
    }

    app = Eve(settings=eve_settings)
    app.run(port=8080)


def subscriber(endpoint, runner_path):
    response = requests.get(endpoint)
    print(response.json())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--producer', action='store_true', help='Run in producer mode')
    parser.add_argument('--rsync-module-location', help='Full path to root of data rsync module')
    parser.add_argument('--port', type=int, help='Port to run REST API')

    parser.add_argument('--subscriber', action='store_true', help='Run in subscriber mode')
    parser.add_argument('--endpoint', help='REST API endpoint to reach out to')
    parser.add_argument('--runner', help='Path to Python file to execute transfer')
    args = vars(parser.parse_args())

    if args['producer']:
        producer()
    elif args['subscriber']:
        subscriber(
            endpoint=args['endpoint'],
            runner_path=args['runner']
        )
