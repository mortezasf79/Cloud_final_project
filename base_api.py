import os
import threading
from flask import Flask, jsonify, request
import database_module
import thread_functions
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)

# راه‌اندازی یک روت ساده
@app.route('/api/server', methods=['POST'])
def api():
    data = request.get_json()
    server_address = data['server_address']
    # database_module.cr_tb()
    database_module.ceate_table()
    database_module.insert_table(server_address)
    return jsonify(data)



@app.route('/api/server', methods=['GET'])
def get_server_data():
    server_id = request.args.get('id')
    data = database_module.show_info(server_id)
    return jsonify(data)



# راه‌اندازی یک روت با پارامتر
@app.route('/api/insert', methods=['GET'])
def api_with_parameter():
    data = {
        'message': f'Hello!'
    }
    database_module.insert_table()
    return jsonify(data)


# راه‌اندازی یک روت با پارامتر
@app.route('/api/start', methods=['GET'])
def api_with_parameter5():
    my_thread = threading.Thread(target=thread_functions.checking_function)
    my_thread.start()
    data = "Checking health of servers started..."
    return data


@app.route('/', methods=['GET'])
def api_with_parameter7():
    data = {
        'message': f'heloooooo'
    }
    return jsonify(data)



@app.route('/api/delete', methods=['GET'])
def api_with_parameter3():
    data = {
        'message': f'success!'
    }
    database_module.delete_table()
    return jsonify(data)



@app.route('/api/count', methods=['GET'])
def api_with_parameter4():
    data = {
        'message': f'Hello!'
    }
    database_module.count_of_server()
    return jsonify(data)



# راه‌اندازی یک روت با پارامتر
@app.route('/api/all', methods=['GET'])
def api_with_parameter1():
    
    data = database_module.getAllInfo()
    return jsonify(data)


if __name__ == '__main__':
    # app.run()
    # app.run(host='localhost', port=5000)
    app.run(debug=True,port=os.getenv('PORT'))