from waitress import serve
import TogetherGoAPI
serve(TogetherGoAPI.app, host='localhost', port=9999)