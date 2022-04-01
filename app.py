import sys
import traceback

import connexion
from prometheus_flask_exporter import ConnexionPrometheusMetrics

import os
import logging

from util.serde import ComplexObjectJSONEncoder

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(name)s:%(levelname)s:%(message)s')

env = os.environ.get('ENVIRONMENT', 'development')
port = int(os.environ.get('API_PORT', '7101'))


def main():
    app = connexion.App(__name__, specification_dir='spec', server='tornado')
    app.app.json_encoder = ComplexObjectJSONEncoder
    app.add_api('api-specification.yaml', strict_validation=True, options={'swagger_ui': True})
    ConnexionPrometheusMetrics(app, group_by='url_rule')

    exception_logger = logging.getLogger('exception_logger')

    @app.app.errorhandler(Exception)
    def exception_handler(exc):
        for line in traceback.format_exception(*sys.exc_info()):
            exception_logger.error(line)
        return exc
    app.run(port=port)


if __name__ == '__main__':
    main()
