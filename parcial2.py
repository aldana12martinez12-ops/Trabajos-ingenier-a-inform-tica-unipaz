import tkinter as tk
from tkinter import messagebox, simpledialog

class InventoryApp:
    def __init__(self, master):
        self.master = master
        master.title("Sistema de Gestión de Inventario (SGI) - CON PRECIOS")

        self.products = []
        self.categories = ["Electrónica", "Ropa", "Alimentos", "Hogar"]

        self.frame_menu = tk.Frame(master)
        self.frame_menu.pack(pady=10)

        self.frame_display = tk.Frame(master)
        self.frame_display.pack(pady=10)

        self.btn_register_product = tk.Button(self.frame_menu, text="Registrar Producto", command=self.open_register_product_window)
        self.btn_register_product.grid(row=0, column=0, padx=5, pady=5)

        self.btn_edit_product = tk.Button(self.frame_menu, text="Editar Producto", command=self.open_edit_product_window)
        self.btn_edit_product.grid(row=0, column=1, padx=5, pady=5)

        self.btn_create_category = tk.Button(self.frame_menu, text="Crear Categoría", command=self.open_create_category_window)
        self.btn_create_category.grid(row=0, column=2, padx=5, pady=5)

        self.btn_generate_invoice = tk.Button(self.frame_menu, text="Generar Factura", command=self.open_generate_invoice_window)
        self.btn_generate_invoice.grid(row=0, column=3, padx=5, pady=5)
      

        self.product_list_label = tk.Label(self.frame_display, text="Productos en Inventario:", font=("Arial", 12, "bold"))
        self.product_list_label.pack()

        self.product_listbox = tk.Listbox(self.frame_display, width=100, height=15)
        self.product_listbox.pack()

        self.display_products() 

    def display_products(self):
        self.product_listbox.delete(0, tk.END)
        if not self.products:
            self.product_listbox.insert(tk.END, "No hay productos registrados.")
        else:
            self.product_listbox.insert(tk.END, "ID | Nombre | Categoría | Cantidad | Precio Unitario")
            self.product_listbox.insert(tk.END, "--------------------------------------------------------------------------------")
            for product in self.products:
                price_str = f"{product['Precio']:.2f}"
                self.product_listbox.insert(tk.END, f"{product['ID']} | {product['Nombre']} | {product['Categoría']} | {product['Cantidad']} | ${price_str}")

    def open_register_product_window(self):
        register_window = tk.Toplevel(self.master)
        register_window.title("Registrar Nuevo Producto")

        tk.Label(register_window, text="ID:").grid(row=0, column=0, padx=5, pady=5)
        id_entry = tk.Entry(register_window)
        id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(register_window, text="Nombre:").grid(row=1, column=0, padx=5, pady=5)
        name_entry = tk.Entry(register_window)
        name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(register_window, text="Categoría:").grid(row=2, column=0, padx=5, pady=5)
        category_var = tk.StringVar(register_window)
        category_var.set(self.categories[0] if self.categories else "")
        category_menu = tk.OptionMenu(register_window, category_var, *self.categories)
        category_menu.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(register_window, text="Cantidad:").grid(row=3, column=0, padx=5, pady=5)
        quantity_entry = tk.Entry(register_window)
        quantity_entry.grid(row=3, column=1, padx=5, pady=5)
        
        tk.Label(register_window, text="Precio individual ($):").grid(row=4, column=0, padx=5, pady=5)
        price_entry = tk.Entry(register_window)
        price_entry.grid(row=4, column=1, padx=5, pady=5)
     

        def register():
            product_id = id_entry.get()
            name = name_entry.get()
            category = category_var.get()
            quantity = quantity_entry.get()
            price = price_entry.get() 

            if not all([product_id, name, category, quantity, price]):
                messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
                return

            try:
                quantity = int(quantity)
                if quantity < 0:
                    raise ValueError
            except ValueError:
                messagebox.showwarning("Advertencia", "La cantidad debe ser un número entero positivo.")
                return
            
            try:
                price = float(price)
                if price <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showwarning("Advertencia", "El precio debe ser un número positivo.")
                return

            if any(p['ID'] == product_id for p in self.products):
                messagebox.showwarning("Advertencia", f"Ya existe un producto con el ID {product_id}.")
                return

            self.products.append({"ID": product_id, "Nombre": name, "Categoría": category, "Cantidad": quantity, "Precio": price})
            
            messagebox.showinfo("Éxito", "Producto registrado correctamente.")
            self.display_products()
            register_window.destroy()

        tk.Button(register_window, text="Registrar", command=register).grid(row=5, column=0, columnspan=2, pady=10)

    def open_edit_product_window(self):
        if not self.products:
            messagebox.showinfo("Información", "No hay productos para editar.")
            return

        edit_window = tk.Toplevel(self.master)
        edit_window.title("Editar Producto")

        tk.Label(edit_window, text="Seleccione el ID del producto a editar:").grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        product_ids = [p['ID'] for p in self.products]
        selected_id_var = tk.StringVar(edit_window)
        selected_id_var.set(product_ids[0] if product_ids else "")
        id_menu = tk.OptionMenu(edit_window, selected_id_var, *product_ids)
        id_menu.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        tk.Label(edit_window, text="Nuevo Nombre:").grid(row=2, column=0, padx=5, pady=5)
        name_entry = tk.Entry(edit_window)
        name_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(edit_window, text="Nueva Categoría:").grid(row=3, column=0, padx=5, pady=5)
        category_var = tk.StringVar(edit_window)
        category_var.set(self.categories[0] if self.categories else "")
        category_menu = tk.OptionMenu(edit_window, category_var, *self.categories)
        category_menu.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(edit_window, text="Nueva Cantidad:").grid(row=4, column=0, padx=5, pady=5)
        quantity_entry = tk.Entry(edit_window)
        quantity_entry.grid(row=4, column=1, padx=5, pady=5)
        
        tk.Label(edit_window, text="Nuevo Precio ($):").grid(row=5, column=0, padx=5, pady=5)
        price_entry = tk.Entry(edit_window)
        price_entry.grid(row=5, column=1, padx=5, pady=5)


        def load_product_data(*args):
            selected_id = selected_id_var.get()
            for product in self.products:
                if product['ID'] == selected_id:
                    name_entry.delete(0, tk.END)
                    name_entry.insert(0, product['Nombre'])
                    category_var.set(product['Categoría'])
                    quantity_entry.delete(0, tk.END)
                    quantity_entry.insert(0, str(product['Cantidad']))
                    price_entry.delete(0, tk.END) 
                    price_entry.insert(0, str(product['Precio']))
                    break
        
        selected_id_var.trace('w', load_product_data)
        load_product_data() 

        def edit():
            product_id = selected_id_var.get()
            new_name = name_entry.get()
            new_category = category_var.get()
            new_quantity = quantity_entry.get()
            new_price = price_entry.get() 

            if not all([product_id, new_name, new_category, new_quantity, new_price]):
                messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
                return

            try:
                new_quantity = int(new_quantity)
                if new_quantity < 0:
                    raise ValueError
            except ValueError:
                messagebox.showwarning("Advertencia", "La cantidad debe ser un número entero positivo.")
                return
            
            try:
                new_price = float(new_price)
                if new_price <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showwarning("Advertencia", "El precio debe ser un número positivo.")
                return

            for product in self.products:
                if product['ID'] == product_id:
                    product['Nombre'] = new_name
                    product['Categoría'] = new_category
                    product['Cantidad'] = new_quantity
                    product['Precio'] = new_price 
                    messagebox.showinfo("Éxito", f"Producto con ID {product_id} actualizado correctamente.")
                    self.display_products()
                    edit_window.destroy()
                    return
            messagebox.showerror("Error", f"No se encontró ningún producto con el ID {product_id}.")

        tk.Button(edit_window, text="Guardar Cambios", command=edit).grid(row=6, column=0, columnspan=2, pady=10)

    def open_create_category_window(self):
        category_window = tk.Toplevel(self.master)
        category_window.title("Crear Nueva Categoría")

        tk.Label(category_window, text="Nombre de la nueva categoría:").grid(row=0, column=0, padx=5, pady=5)
        new_category_entry = tk.Entry(category_window)
        new_category_entry.grid(row=0, column=1, padx=5, pady=5)

        def create_category():
            new_category = new_category_entry.get().strip()
            if not new_category:
                messagebox.showwarning("Advertencia", "El nombre de la categoría no puede estar vacío.")
                return
            if new_category in self.categories:
                messagebox.showwarning("Advertencia", f"La categoría '{new_category}' ya existe.")
                return
            
            self.categories.append(new_category)
            messagebox.showinfo("Éxito", f"Categoría '{new_category}' creada correctamente.")
            category_window.destroy()

        tk.Button(category_window, text="Crear", command=create_category).grid(row=1, column=0, columnspan=2, pady=10)

    def open_generate_invoice_window(self):
        invoice_window = tk.Toplevel(self.master)
        invoice_window.title("Generar Factura")

        tk.Label(invoice_window, text="Seleccione productos para la factura:").grid(row=0, column=0, columnspan=3, padx=5, pady=5)

        invoice_product_listbox = tk.Listbox(invoice_window, selectmode=tk.MULTIPLE, width=80, height=10)
        invoice_product_listbox.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        product_quantities_entries = {} 

        for i, product in enumerate(self.products):
            price_str = f"{product['Precio']:.2f}"
            invoice_product_listbox.insert(tk.END, f"ID: {product['ID']} | Nombre: {product['Nombre']} | Precio: ${price_str} | Cantidad disponible: {product['Cantidad']}")
        
        tk.Label(invoice_window, text="Ingrese la cantidad a comprar para cada producto seleccionado:").grid(row=2, column=0, columnspan=3, padx=5, pady=5)

        def update_quantity_entries():
            for widget in invoice_quantity_frame.winfo_children():
                widget.destroy() 

            selected_indices = invoice_product_listbox.curselection()
            product_quantities_entries.clear()

            for i, index in enumerate(selected_indices):
                product = self.products[index]
                tk.Label(invoice_quantity_frame, text=f"{product['Nombre']} (Cant. Max: {product['Cantidad']}):").grid(row=i, column=0, padx=2, pady=2)
                entry = tk.Entry(invoice_quantity_frame, width=5)
                entry.grid(row=i, column=1, padx=2, pady=2)
                product_quantities_entries[product['ID']] = entry

        invoice_product_listbox.bind('<<ListboxSelect>>', lambda event: update_quantity_entries())
        
        invoice_quantity_frame = tk.Frame(invoice_window)
        invoice_quantity_frame.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

        def generate_invoice():
            selected_indices = invoice_product_listbox.curselection()
            if not selected_indices:
                messagebox.showwarning("Advertencia", "Debe seleccionar al menos un producto para la factura.")
                return

            invoice_items = []
            
            for index in selected_indices:
                product = self.products[index]
                try:
                    quantity_to_buy = int(product_quantities_entries[product['ID']].get())
                    if quantity_to_buy <= 0 or quantity_to_buy > product['Cantidad']:
                        messagebox.showwarning("Advertencia", f"Cantidad inválida para '{product['Nombre']}'. Debe ser entre 1 y {product['Cantidad']}.")
                        return
                    invoice_items.append({"product": product, "quantity": quantity_to_buy})
                except (ValueError, KeyError):
                    messagebox.showwarning("Advertencia", f"Ingrese una cantidad válida para '{product['Nombre']}'.")
                    return

            invoice_text = "--- FACTURA ---\n\n"
            invoice_text += "Producto | Cantidad | Precio Unit. | Subtotal\n"
            invoice_text += "------------------------------------------------\n"
            total = 0.0
            
            for item in invoice_items:
                prod = item["product"]
                qty = item["quantity"]
                price = prod["Precio"]
                subtotal = qty * price
                total += subtotal
                
                price_str = f"${price:.2f}"
                subtotal_str = f"${subtotal:.2f}"
                
                invoice_text += f"{prod['Nombre']} | {qty} | {price_str} | {subtotal_str}\n"
                

                prod['Cantidad'] -= qty 
            
            invoice_text += "\n------------------------------------------------\n"
            invoice_text += f"TOTAL A PAGAR: ${total:.2f}\n"
            invoice_text += "¡Gracias por su compra!\n"

            messagebox.showinfo("Factura Generada", invoice_text)
            self.display_products() 
            invoice_window.destroy()

        tk.Button(invoice_window, text="Generar Factura", command=generate_invoice).grid(row=4, column=0, columnspan=3, pady=10)

root = tk.Tk()
app = InventoryApp(root)
root.mainloop()
