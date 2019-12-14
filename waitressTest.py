from waitress import serve
import MongoDB_API
serve(MongoDB_API.app, host='0.0.0.0', port=5000)