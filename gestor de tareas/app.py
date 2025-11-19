from flask import Flask,request, redirect, render_template

app = Flask(__name__)

#======================================================
#Estructura de datos
#======================================================
tareas=[]
siguiente_id=1

def agregar_tarea(texto):
    global siguiente_id
    tareas.append({
        'id':siguiente_id,
        'texto':texto,
        'hecho':False
    })
    siguiente_id+=1

def completar_tarea(id):
    for tarea in tareas:
        if tarea['id']==id:
            tarea['hecho']=True
            break

#======================================================
#Rutas
#======================================================
@app.route('/agregar',methods=['POST'])
def agregar():
    texto_tarea=request.form.get('texto_tarea')

    if texto_tarea:
        agregar_tarea(texto_tarea)

        return redirect ('/')


@app.route('/completar/<int:id>')
def completar(id):
    completar_tarea(id)
    return redirect ('/')





@app.route('/')
def index():
    return "hola mundo"

if __name__ == '__main__':
    app.run(debug=True)
