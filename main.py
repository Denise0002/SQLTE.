import orm
from tablas.Productos import Productos
from tablas.Clientes import Clientes

db=orm.SQLiteORM("tiendita")
db.crear_tabla(Productos)
db.crear_tabla(Clientes)

# data={
#     "nombre":"detergente patito",
#     "precio":"2.5",
#     "descripcion":"limpia todo",
#     "cantidad":"10"
# }
# db.insertarUno("Productos",data)
data=[
    {
    "nombre":"chinita",
    "dni":"78374",
    "celular":"92747247",
    "f_nacimiento":"13/06/2004"
    },
    {
    "nombre":"juan",
    "dni":"78289",
    "celular":"934984",
    "f_nacimiento":"07/11/2005"
    }
]
db.insertarVarios("Clientes",data)

# data={"nombre":"maria"}
# db.actualizar("Clientes",data,"dni=78374")
# db.eliminar("Clientes","dni=78289")

# print(db.mostrar("Clientes", type="objeto"))
# print(db.mostrar("Clientes"))
print(db.mostrar("Clientes",where="dni=78289",type="objeto"))
# print(db.mostrar("Clientes",where="nombre LIKKE 'ju%'",type="objeto"))


db.cerrar()