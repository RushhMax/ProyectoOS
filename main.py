from app.process_manager import ProcessManager
from app.core.Process import Process
from flask import Flask, render_template, request

app = Flask(__name__)
 
manager = ProcessManager()

@app.route('/', methods=['GET'])
def main():
    # Mostramos los procesos activos
    print("Procesos activos con informacion inicial random")

    # Imprime los procesos activos en la consola.
    manager.display_processes()

    # Renderiza la plantilla HTML principal mostrando los procesos actuales.
    return render_template('index.html', processes=manager.get_processes(), cpus=manager.cpus)

# GET REAL PROCESSES
@app.route('/get_real_processes', methods=['GET'])
def get_real_processes():

    # Obtiene los procesos reales del sistema.
    manager.get_real_processes()

    # Renderiza la plantilla HTML principal mostrando los procesos actuales.
    return render_template('process-list.html', processes=manager.get_processes(), cpus=manager.cpus)

@app.route('/get_simulated_processes', methods=['GET'])
def get_simulated_processes():
    """Handle the request to generate random processes."""
    # Generar procesos aleatorios
    manager.generate_processes(12)

    # Renderiza una lista actualizada de procesos.
    return render_template('process-list.html', processes=manager.get_processes(), cpus=manager.cpus)


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
    """Handle the request to simulate the CPU."""

    cpu_algorithms = ['fcfs', 'round_robin', 'sjf', 'priority']
    
    manager.setup_cpus(cpu_algorithms= cpu_algorithms)
    manager.assign_processes()
    # Renderiza una lista actualizada de procesos.
    return render_template('index.html', processes=manager.get_processes(), cpus=manager.cpus)

@app.route('/simulate', methods=['GET'])
def simulate():

    cpu_algorithms = [
        request.form.get("algorithm_cpu_1"),
        request.form.get("algorithm_cpu_2"),
        request.form.get("algorithm_cpu_3"),
        request.form.get("algorithm_cpu_4"),
    ]

    cpu_algorithms = ['fcfs', 'round_robin', 'sjf', 'priority']

    manager.set_algorithm(0, cpu_algorithms[0])
    manager.set_algorithm(1, cpu_algorithms[1])
    manager.set_algorithm(2, cpu_algorithms[2])
    manager.set_algorithm(3, cpu_algorithms[3])

    manager.run_simulation()

    """
    # Asignar procesos y ejecutar la simulación
    manager.assign_processes()
    manager.run_simulation()
    """

    # Renderiza una lista actualizada de procesos.
    return render_template('index.html', processes=manager.get_processes(), cpus=manager.cpus)

if __name__ == "__main__":
    app.run(debug=True)
