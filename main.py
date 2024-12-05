from app.process_manager import ProcessManager
from app.cpu import CPU
from app.algorithms import fcfs, round_robin, simulate_fcfs_logic
from flask import Flask, render_template, request

app = Flask(__name__)

# Inicializamos la gestión de procesos 
manager = ProcessManager()
# get processes, randomize processes, sort processes
manager.start() 

@app.route('/', methods=['GET'])
def main():
     # Mostramos los procesos activos
    print("Procesos activos con informacion inicial random")
    manager.display_processes()

    #fcfs(processes)

    return render_template('index.html',processes=manager.get_processes())

@app.route('/fcfs')
def simulate_fcfs():
    processes = [
        {"pid": 1, "burst_time": 5},
        {"pid": 2, "burst_time": 3},
        {"pid": 3, "burst_time": 8},
    ]
    completion_times = simulate_fcfs_logic(processes)
    return render_template('simulation_fcfs.html', results=completion_times)

@app.route('/AddProcess', methods=['POST'])
def add_process():
    return render_template('add_process.html')

# def main():
#     # Inicializamos la gestión de procesos
#     manager = ProcessManager()
#     processes = manager.get_processes()
#
#     # Mostramos los procesos activos
#     print("Procesos activos:")
#     manager.display_processes()
#
#     # Simulamos 4 CPUs
#     cpus = [CPU(i) for i in range(4)]
#
#     # Seleccionamos algoritmo
#     print("\nAsignando procesos con FCFS:")
#     fcfs(processes, cpus)
#
#     # Ejecutamos los procesos en cada CPU
#     for cpu in cpus:
#         cpu.execute_processes()
#
if __name__ == "__main__":
    app.run(debug=True)
