from flask import Flask,render_template, request
import os


app = Flask(__name__)


@app.route('/',defaults={'path': ' '})
@app.route('/<path:path>')
def page(path):
	path = request.path
	name1  = request.args.get('path',path)
	path_dir = os.getcwd()+'/templates/'+path
	if ('~' in path or '..' in path or '//' in path) :
		return error_403(403)
	if os.path.isfile(path_dir) and (path.endswith('.html')):
		return render_template(path,path=path)
	return error_404(404)

@app.errorhandler(404)
def error_404(error):
        return render_template('404.html'), 404


@app.errorhandler(403)
def error_403(error):
        return render_template('403.html'), 403

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')





