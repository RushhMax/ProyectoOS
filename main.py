from app.process_manager import ProcessManager
from app.cpu import CPU
from app.process import Process
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

@app.route('/add_process', methods=['POST'])
def add_process():
    """Handle the request to add a new process."""
    # Get data from the form
    name = request.form.get('name')
    arrival_time = int(request.form.get('arrival_time'))
    priority = int(request.form.get('priority'))
    service_time = int(request.form.get('service_time'))

    # Create the new process
    new_process = Process(pid=len(manager.get_processes()) + 1, name=name, arrival_time=arrival_time, service_time=service_time, priority=priority)
    manager.add_process(new_process)

    # Render the updated processes list and return it
    return render_template('process-list.html', processes=manager.get_processes())

@app.route('/delete_process', methods=['POST'])
def delete_process():
    """Handle the request to delete a process."""
    # Get the process id to delete
    pid = int(request.form.get('pid'))

    # Delete the process
    manager.delete_process(pid)

    # Render the updated processes list and return it
    return render_template('process-list.html', processes=manager.get_processes())

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
