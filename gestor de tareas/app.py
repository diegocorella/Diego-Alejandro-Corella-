from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# =============================
#   ESTRUCTURA DE DATOS
# =============================

tareas = []
siguiente_id = 1


def agregar_tarea(texto):
    global siguiente_id
    tareas.append({
        'id': siguiente_id,
        'texto': texto,
        'hecho': False
    })
    siguiente_id += 1


def completar_tarea(id):
    for tarea in tareas:
        if tarea['id'] == id:
            tarea['hecho'] = True
            break


# =============================
#           RUTAS
# =============================

@app.route('/')
def index():
    return render_template("index.html", tareas=tareas)


@app.route('/agregar', methods=['POST'])
def agregar():
    texto = request.form.get("texto_tarea")

    if texto and texto.strip() != "":
        agregar_tarea(texto.strip())

    return redirect('/')


@app.route('/completar/<int:id>')
def completar(id):
    completar_tarea(id)
    return redirect('/')


# =============================
#      EJECUTAR APLICACIÓN
# =============================
if __name__ == '__main__':
    app.run(debug=True)
