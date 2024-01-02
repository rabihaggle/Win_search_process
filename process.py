from flask import Flask, jsonify
import psutil

app = Flask(__name__)


@app.route('/')
def hello_world():
    response = {
        'message': 'Hello, world'
    }
    return jsonify(response), 200


@app.route('/search_process/<name_process>', methods=['GET'])
def search_process(name_process):
    all_processes = psutil.process_iter(['pid', 'name'])
    for process_info in all_processes:
        if name_process.lower() in process_info.info['name'].lower():
            return jsonify({'status': 'success', 'message': f'El proceso {name_process} está en ejecución.'}), 200

    return jsonify({'status': 'error', 'message': f'El proceso {name_process} no está en ejecución.'}), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8080)
