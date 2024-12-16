from app.process_manager import ProcessManager
from app.cpu import CPU
from app.process import Process
from app.algorithms import fcfs, round_robin, sjf
from flask import Flask, render_template, request

app = Flask(__name__)

# Inicializamos la gestión de procesos 
manager = ProcessManager()
manager.start() 

"""
ruta principal para visualizar procesos ------------------------------------------------------------------------------
"""
@app.route('/', methods=['GET'])
def main():
     # Mostramos los procesos activos
    print("Procesos activos con informacion inicial random")

    # Imprime los procesos activos en la consola.
    manager.display_processes()

    # Renderiza la plantilla HTML principal mostrando los procesos actuales.
    return render_template('index.html', processes=manager.get_processes(), cpus=manager.cpus)


"""
ruta para agregar proceso -------------------------------------------------------------------------------------------
"""
@app.route('/add_process', methods=['POST'])
def add_process():
    """Handle the request to add a new process."""
    # Recibe datos de un formulario HTML
    name = request.form.get('name')
    arrival_time = int(request.form.get('arrival_time'))
    priority = int(request.form.get('priority'))
    service_time = int(request.form.get('service_time'))

    # crea una nueva instancia de Process.
    new_process = Process(
        pid=len(manager.get_processes()) + 1,
        name=name,
        arrival_time=arrival_time,
        service_time=service_time,
        priority=priority
    )
    # Agrega el nuevo proceso al manager
    manager.add_process(new_process)    

    # Renderiza una lista actualizada de procesos.
    return render_template('process-list.html', processes=manager.get_processes(), cpus=manager.cpus)

"""
ruta para eliminar proceso -------------------------------------------------------------------------------------------
"""
@app.route('/delete_process', methods=['POST'])
def delete_process():
    """Handle the request to delete a process."""
    # Obtenemos el ID
    pid = int(request.form.get('pid'))

    # Elimina un proceso según su ID (pid).
    manager.delete_process(pid)

    # Renderiza una lista actualizada de procesos.
    return render_template('process-list.html', processes=manager.get_processes(), cpus=manager.cpus)

"""
ruta para simular la asignación de procesos --------------------------------------------------------------------------
"""
@app.route('/simulate', methods=['POST'])
def simulate():
    algorithm = request.form.get('algorithm')
    manager.assign_processes(algorithm)

    # Ejecutar procesos en cada CPU
    for cpu in manager.cpus:
        cpu.execute_processes(1)

    manager.track_completed_processes()

    # Mostrar resultados en la misma página
    return render_template('index.html', processes=manager.get_processes(), cpus=manager.cpus, completed_processes=manager.completed_processes)

# @app.route('/simulate', methods=['POST'])
# def simulate():
#     """Handle the request to simulate the CPU."""
#     # Get the selected algorithm
#     algorithm = request.form.get('algorithm')

#     # Simulate the CPU with the selected algorithm
#     if algorithm == 'fcfs':
#         simulate_fcfs_logic(manager)
#     elif algorithm == 'round_robin':
#         round_robin(manager)

#     # Render the updated processes list and return it
#     return render_template('process-list.html', processes=manager.get_processes())

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
