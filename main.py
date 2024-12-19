from app.process_manager import ProcessManager
from app.core.Process import Process
from flask import Flask, render_template, request

app = Flask(__name__)
 
manager = ProcessManager()

@app.route('/', methods=['GET'])
def main():
    # Mostramos los procesos activos
    print("Procesos activos con informacion inicial random")

    #process_manager.generate_processes()

    # Imprime los procesos activos en la consola.
    manager.display_processes()


    # Renderiza la plantilla HTML principal mostrando los procesos actuales.
    return render_template('index.html', processes=manager.get_processes())

# GET REAL PROCESSES
@app.route('/get_real_processes', methods=['GET'])
def get_real_processes():

    # Obtiene los procesos reales del sistema.
    manager.get_real_processes()

    # Renderiza la plantilla HTML principal mostrando los procesos actuales.
    return render_template('process-list.html', processes=manager.get_processes())

@app.route('/get_simulated_processes', methods=['GET'])
def get_simulated_processes():
    """Handle the request to generate random processes."""
    # Generar procesos aleatorios
    manager.generate_processes(12)

    # Renderiza una lista actualizada de procesos.
    return render_template('process-list.html', processes=manager.get_processes())


# ELEGIR CADA ALGORITMO DE PLANIFICACIÓN POR CPU

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
        pid=manager.get_next_pid(),
        name=name,
        arrival_time=arrival_time,
        service_time=service_time,
        priority=priority
    )
    # Agrega el nuevo proceso al manager
    manager.add_process(new_process)    

    # Renderiza una lista actualizada de procesos.
    return render_template('process-list.html', processes=manager.get_processes(), cpus=manager.cpus)


@app.route('/delete_process', methods=['POST'])
def delete_process():
     """Handle the request to delete a process."""
     # Obtenemos el ID
     pid = int(request.form.get('pid'))

     # Elimina un proceso según su ID (pid).
     manager.delete_process(pid)

     # Renderiza una lista actualizada de procesos.
     return render_template('process-list.html', processes=manager.get_processes(), cpus=manager.cpus)


# SIMULAR
@app.route('/assign_processes', methods=['GET'])
def assign_processes():
    """Handle the request to assign processes to CPUs."""
    # Asignar procesos a las CPUs
    manager.assign_processes()

    # Renderiza una lista actualizada de procesos.
    return render_template('index.html', processes=manager.get_processes(), cpus=manager.cpus)

@app.route('/simulate', methods=['GET'])
def simulate():
    """Handle the request to simulate the CPU."""
    cpu_algorithms = [
        request.form.get("algorithm_cpu_1"),
        request.form.get("algorithm_cpu_2"),
        request.form.get("algorithm_cpu_3"),
        request.form.get("algorithm_cpu_4"),
    ]

    cpu_algorithms = ['fcfs', 'round_robin', 'sjf', 'priority']
    
    manager.setup_cpus(cpu_algorithms= cpu_algorithms)
    manager.assign_processes()

    """
    # Asignar procesos y ejecutar la simulación
    manager.assign_processes()
    manager.run_simulation()
    """

    # Renderiza una lista actualizada de procesos.
    return render_template('index.html', processes=manager.get_processes(), cpus=manager.cpus)

# def main():
#     # Crear instancia de ProcessManager
#     process_manager = ProcessManager(num_processes=12)
    
#     # Ejecutar la simulación
#     process_manager.simulate()

#     # Agregar un nuevo proceso
#     new_process = Process(
#         pid=100,
#         name="Process_100",
#         arrival_time=5,
#         service_time=10,
#         priority=3,
#         cpu=None,
#         memory=1024,
#         user="user",
#         status="READY"
#     )
#     process_manager.add_process(new_process)

#     # Reasignar procesos a las CPUs
#     process_manager.assign_processes()

#     # Eliminar un proceso por PID
#     process_manager.delete_process(100)

if __name__ == "__main__":
    app.run(debug=True)



# ruta para simular la asignación de procesos --------------------------------------------------------------------------
# """
# @app.route('/simulate', methods=['POST'])
# def simulate():
#     algorithm = request.form.get('algorithm')
#     manager.assign_processes(algorithm)

#     # Ejecutar procesos en cada CPU
#     for cpu in manager.cpus:
#         cpu.execute_processes(1)

#     manager.track_completed_processes()

#     # Mostrar resultados en la misma página
#     return render_template('index.html', processes=manager.get_processes(), cpus=manager.cpus, completed_processes=manager.completed_processes)

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

