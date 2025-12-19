from flask import Flask, jsonify
from flask_cors import CORS  # <--- NEW IMPORT
import ctypes
import os

app = Flask(__name__)
CORS(app)  # <--- ALLOW FRONTEND CONNECTIONS

# --- Load the C Library ---
so_file = os.path.abspath("pc.so")
c_lib = ctypes.CDLL(so_file)

# --- Configure C Return Types ---
c_lib.produce_item.restype = ctypes.c_int
c_lib.consume_item.restype = ctypes.c_int

# Initialize buffer in C
c_lib.init_buffer()

# MUST MATCH C CODE BUFFER_SIZE
BUFFER_SIZE = 5 

def get_c_buffer():
    ArrayType = ctypes.c_int * BUFFER_SIZE
    c_array = ArrayType()
    c_lib.get_buffer_state(c_array)
    return list(c_array)

@app.route('/status', methods=['GET'])
def status():
    return jsonify({
        "buffer": get_c_buffer(),
        "capacity": BUFFER_SIZE,
        "count": len([x for x in get_c_buffer() if x != -1])
    })

@app.route('/produce', methods=['POST'])
def produce():
    import random
    item = random.randint(10, 99)
    success = c_lib.produce_item(item)
    current_buffer = get_c_buffer()
    
    if success == 1:
        return jsonify({"status": "success", "produced": item, "buffer": current_buffer})
    else:
        return jsonify({"error": "Buffer is FULL", "buffer": current_buffer}), 409

@app.route('/consume', methods=['GET'])
def consume():
    item = c_lib.consume_item()
    current_buffer = get_c_buffer()
    
    if item != -1:
        return jsonify({"status": "success", "consumed": item, "buffer": current_buffer})
    else:
        return jsonify({"error": "Buffer is EMPTY", "buffer": current_buffer}), 409

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
