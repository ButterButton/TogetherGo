from waitress import serve
import test
serve(test.app, host='0.0.0.0', port=8080)