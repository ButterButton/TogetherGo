from waitress import serve
import TogetherGoAPI
serve(TogetherGoAPI.app, host='0.0.0.0', port=8080)