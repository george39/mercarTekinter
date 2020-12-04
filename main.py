
from tkinter import *
from tkinter import messagebox as MessageBox


from proveedores import proveedor as modelo_proveedor
from productos import producto as modelo_producto



ventana = Tk()
ventana.title('SUPERMERCADO')
ventana.geometry("{0}x{1}+0+0".format(ventana.winfo_screenwidth(), ventana.winfo_screenheight()))


#DEFINIR CAMPOS DE PANTALLA PARA EL MENU
venta_label = Label(text='Ventas')
producto_label = Label(text='Productos')
proveedor_label = Label(text='Proveedores')


def ventanaProveedores():
    ventana_proveedores = Tk()
    ventana_proveedores.title('PROVEEDORES')
    ventana_proveedores.geometry('300x350')

     
    
    proveedores_box = Frame(ventana_proveedores, width=250)
    proveedores_box.grid(row=1)

    nombre1 = ""
    empresa = ""

    proveedores_lista = []
    provee = modelo_proveedor.Proveedor(nombre1, empresa)
    pro = provee.listar()
    proveedores_lista.append(pro)
    

    for proveedores in pro:                

        Label(proveedores_box, text=(proveedores[1], proveedores[2])).grid()
        #Label(proveedores_box, text=proveedores[2]).grid()
        
        

        














#***************************************************************
# VENTAS
#***************************************************************
venta_name_data = StringVar()
venta_price_data = StringVar()
venta_quantity_data = StringVar()


#Campos del formulario
vent_frame = Frame(ventana)
vent_name_label = Label(vent_frame, text='Nombre')
vent_name_entry = Entry(vent_frame, textvariable=venta_name_data)
vent_price_label = Label(vent_frame, text='Precio')
vent_price_entry = Entry(vent_frame, textvariable=venta_price_data)
vent_quantity_label = Label(vent_frame, text='Cantidad')
vent_quantity_entry = Entry(vent_frame, textvariable=venta_quantity_data)

boton_venta = Button(ventana, text='Guardar', command=ventanaProveedores)



def venta():
    
    venta_label.config(
        fg="white",
        bg="blue",
        font=("Arial", 20),

        padx=650,
        pady=5
    )

    venta_label.grid(row=0, column=0, columnspan=4)


     #***************************************************************
    # CAMPOS DEL FORMULARIO
    #***************************************************************
    vent_frame.grid(row=1)
    vent_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    vent_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    vent_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    vent_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    vent_quantity_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
    vent_quantity_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

    boton_venta.grid(row=5, column=1, sticky=NW)
    boton_venta.config(
        padx=15,
        bg='green',
        fg='white'
    )
    

   
    #Ocultar pantallas
    producto_label.grid_remove()
    proveedor_label.grid_remove()
    proveedor_frame.grid_remove()
    product_frame.grid_remove()
    boton_producto.grid_remove()
    boton_proveedor.grid_remove()
    





#***************************************************************
# PRODUCTOS
#***************************************************************
proveedor_id_data = IntVar()
producto_nombre_data = StringVar()
producto_precio_data = IntVar()
producto_cantidad_data = IntVar()


#Campos del formulario
product_frame = Frame(ventana)
product_id_label = Label(product_frame, text='Proveedor')
product_id_entry = Entry(product_frame, textvariable=proveedor_id_data)
product_name_label = Label(product_frame, text='Nombre')
product_name_entry = Entry(product_frame, textvariable=producto_nombre_data)
product_price_label = Label(product_frame, text='Precio')
product_price_entry = Entry(product_frame, textvariable=producto_precio_data)
product_quantity_label = Label(product_frame, text='Cantidad')
product_quantity_entry = Entry(product_frame, textvariable=producto_cantidad_data)

boton_producto = Button(ventana, text='Guardar', command=ventanaProveedores)


def registroProducto():       

    proveedor_id = product_name_entry
    nombre = product_name_entry
    nombre_empresa = proveedor_nombre_empresa_entry
    
    
    if name_data.get() == "" or nombre_empresa_data.get() == "":         
        MessageBox.showerror(message="El producto no se registro porque tiene un campo vacio" , title="ERROR" )
    else :
        proveedor = modelo_proveedor.Proveedor(nombre.get(), nombre_empresa.get())
        registro = proveedor.registrar()

        if registro[0] >= 1:
            MessageBox.showinfo(message="Has registrado correctamente el producto " + str(registro[1].nombre), title="BIEN HECHO" )

        else:
            MessageBox.showerror(message="El producto no se registro" , title="ERROR" )

        

    name_data.set("")
    nombre_empresa_data.set("")


def producto():
    #Encabezado    
    producto_label.config(
        fg="white",
        bg="blue",
        font=("Arial", 20),
        padx=650,
        pady=5
    )

    producto_label.grid(row=0, column=0, columnspan=4)

    #***************************************************************
    # CAMPOS DEL FORMULARIO
    #***************************************************************
    product_frame.grid(row=1)
    product_id_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    product_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    product_name_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    product_name_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    product_price_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
    product_price_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

    product_quantity_label.grid(row=4, column=0, padx=5, pady=5, sticky=E)
    product_quantity_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)

    boton_producto.grid(row=5, column=1, sticky=NW)
    boton_producto.config(
        padx=15,
        bg='green',
        fg='white'
    )



    #Ocultar otras pantallas
    venta_label.grid_remove()
    proveedor_label.grid_remove() 
    proveedor_frame.grid_remove()
    vent_frame.grid_remove()
    boton_venta.grid_remove()
    boton_proveedor.grid_remove()
    
    





#***************************************************************
# PROVEEDORES
#***************************************************************
name_data = StringVar()
nombre_empresa_data = StringVar()
    


#Campos del formulario
proveedor_frame = Frame(ventana)
proveedor_name_label = Label(proveedor_frame, text='Nombre proveedor')
proveedor_name_entry = Entry(proveedor_frame, textvariable=name_data)
proveedor_nombre_empresa_label = Label(proveedor_frame, text='Nombre empresa')
proveedor_nombre_empresa_entry = Entry(proveedor_frame, textvariable=nombre_empresa_data)


#***************************************************************
# REGISTRAR UN PROVEEDOR
#***************************************************************
def registroProveedor():      

    nombre = proveedor_name_entry
    nombre_empresa = proveedor_nombre_empresa_entry
    
    
    if name_data.get() == "" or nombre_empresa_data.get() == "":         
        MessageBox.showerror(message="El proveedor no se registro porque tiene un campo vacio" , title="ERROR" )
    else :
        proveedor = modelo_proveedor.Proveedor(nombre.get(), nombre_empresa.get())
        registro = proveedor.registrar()

        if registro[0] >= 1:
            MessageBox.showinfo(message="Has registrado correctamente el proveedor " + str(registro[1].nombre), title="BIEN HECHO" )

        else:
            MessageBox.showerror(message="El proveedor no se registro" , title="ERROR" )

        

    name_data.set("")
    nombre_empresa_data.set("")





#***************************************************************
# MOSTRAR LA LISTA DE LOS PROVEEDORES
#***************************************************************


def mostrarProveedores():
        print(f"\nVale {usuario[1]} Aqui tienes tus notas: ")

        mostrar = proveedor.listar(usuario[0]) 
        mostrar_proveedor = mostrar.listar()

        for proveedor in mostrar:
            print("************************************")
            print(proveedor[2])
            print(proveedor[3])



# Boton para guardar
boton_proveedor = Button(ventana, text='Guardar', command=registroProveedor)
boton_mostrar_proveedor = Button(ventana, text='Listar', command=ventanaProveedores)


def proveedores():   
    
    
    proveedor_label.config(         
        fg="white",
        bg="blue",
        font=("Arial", 20),
        padx=650,
        pady=5
    )
    proveedor_label.grid(row=0, column=0, columnspan=4)


    #***************************************************************
    # CAMPOS DEL FORMULARIO
    #***************************************************************
    proveedor_frame.grid(row=1)
    proveedor_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    proveedor_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    proveedor_nombre_empresa_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    proveedor_nombre_empresa_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    


    boton_proveedor.grid(row=3, column=0)
    boton_proveedor.config(
        padx=15,
        bg='green',
        fg='white'
    )

    boton_mostrar_proveedor.grid(row=3, column=1)
    boton_mostrar_proveedor.config(
        padx=15,
        bg='green',
        fg='white'
    )

    #Ocultar otras pantallas
    venta_label.grid_remove()    
    producto_label.grid_remove()
    product_frame.grid_remove()
    vent_frame.grid_remove()
    boton_venta.grid_remove()
    boton_producto.grid_remove()
   




#***************************************************************************************
#***************************************************************************************        




#***************************************************************
# MENU DE OPCIONES
#***************************************************************
def menu():
    menu_superior = Menu(ventana) 
    menu_superior.add_command(label = 'Ventas', command=venta)   
    menu_superior.add_command(label = 'Productos', command=producto) 
    menu_superior.add_command(label = 'Proveedores', command=proveedores) 


    ventana.config(menu = menu_superior)





menu()
#venta()


ventana.mainloop()





    
        


    


              



