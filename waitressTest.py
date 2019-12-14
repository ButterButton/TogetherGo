from waitress import serve
import test
serve(test.app, host='127.0.0.1', port=80)