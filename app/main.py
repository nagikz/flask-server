from data.productos import productos
from flask import Flask, render_template, request, url_for, redirect
from form import LoginForm

# Inicializamos la aplicación
app = Flask(__name__)
app.config["SECRET_KEY"] = "mi_clave_secreta_super_segura"


# Ruta 1: Devuelve un HTML muy básico
@app.route("/")
def home():
    # return """
    #     <h1>¡Hola desde Flask en Docker!!!!</h1>
    #     <p>Este es tu primer servidor Python funcionando.</p>
    # """
    return render_template("index.html")


@app.route("/saludo/<name>")
def saludo(name):
    # return f"<h1>Bienvenido a Flask, {name}</h1>"
    return render_template("saludo.html", name=name)


@app.route("/multiplicar/<int:n1>/<int:n2>")
def multiplicar(n1, n2):
    return f"<p>Multiplicar {n1} x {n2} da resultado {n1 * n2}"


@app.route("/catalogo")
def catalogo():
    return render_template("catalogo.html", nombre="algo", lista_productos=productos)


@app.route("/catalogo/<int:idProducto>")
def producto(idProducto):
    return render_template(
        "producto.html", idProducto=idProducto, producto=productos[idProducto]
    )


@app.route("/contacto", methods=["GET"])
def contacto():
    return render_template("contacto.html")


@app.route("/contacto", methods=["POST"])
def contacto_post():
    nombre = request.form.get("nombre")
    mensaje = request.form["mensaje"]
    return render_template("contacto-data.html", nombre=nombre, mensaje=mensaje)


@app.route("/filtrar")
def filtrar():
    return render_template("filtrar.html")


@app.route("/filtrar-data", methods=["GET"])
def filtrar_data():
    precio_min = request.args.get("precio_min", type=float)
    print(f"Precio mínimo: {precio_min}")
    productos_filtrados = [
        producto for producto in productos if producto["precio"] >= precio_min
    ]
    print(f"Productos filtrados: {productos_filtrados}")
    # return render_template("filtrar-data.html")
    return render_template(
        "catalogo.html", nombre="Filtrado", lista_productos=productos_filtrados
    )


@app.route("/saludo/<name>")
def saludo(name):
    return f"<h1>Bienvenido a FLask, {name}</h1>"


@app.route("/multiplicar/<int:a>/<int:b>")
def multiplicar(a, b):
    return f"<h1>{a} x {b} = {a * b}</h1>"


@app.route("/catalogo/<int:id_producto>")
def catalogo(id_producto):
    productos = [
        {"nombre": "Teclado Mecánico", "precio": 10.99, "disponible": True},
        {"nombre": "Mouse Inalámbrico", "precio": 15.99, "disponible": False},
        {"nombre": "Monitor LED", "precio": 199.99, "disponible": True},
    ]

    return render_template(
        "catalogo.html",
        nombre="Juan",
        id_producto=id_producto,
        lista_productos=productos,
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    # validate_on_submit comprueba si la peticion es POST  y si se validan todos los campos
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print(f"El usuario es {email} con la contraseña {password}")

        return redirect(url_for("gracias"))

    return render_template("login.hmtl", form=form)


@app.route("/gracias")
def gracias():
    return render_template("gracias.html")


if __name__ == "__main__":
    # host='0.0.0.0' es VITAL en Docker para que el servidor sea accesible desde fuera del contenedor
    # debug=True hará que el servidor se reinicie automáticamente si cambias este archivo
    app.run(host="0.0.0.0", port=5000, debug=True)
