import sys
from app import create_application
from flask_twisted  import Twisted
from twisted.python import log


if __name__ == '__main__':
    app = create_application()
    twisted = Twisted(app)
    log.startLogging(sys.stdout)

    app.logger.info(f"Running the app...")
    app.run(debug=True, threaded=True, host='0.0.0.0', port=5001)