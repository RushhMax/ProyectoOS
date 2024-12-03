from app.process_manager import ProcessManager
from app.cpu import CPU
from app.algorithms import fcfs, round_robin
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Processes', methods=['GET'])
def processes():
    manager = ProcessManager()
    processes = manager.get_processes()

    # Mostramos los procesos activos
    print("Procesos activos con informacion inicial random")
    manager.randomize_processes()
    manager.display_processes()

    fcfs(processes)

    return render_template('index.html',processes=processes)

@app.route('/AddProcess', methods=['POST'])
def add_process():
    return render_template('add_process.html')

def main():
    # Inicializamos la gestión de procesos
    manager = ProcessManager()
    processes = manager.get_processes()

    # Mostramos los procesos activos
    print("Procesos activos:")
    manager.display_processes()

    # Simulamos 4 CPUs
    cpus = [CPU(i) for i in range(4)]

    # Seleccionamos algoritmo
    print("\nAsignando procesos con FCFS:")
    fcfs(processes, cpus)

    # Ejecutamos los procesos en cada CPU
    for cpu in cpus:
        cpu.execute_processes()

if __name__ == "__main__":
    app.run(debug=True)
