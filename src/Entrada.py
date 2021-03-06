import gi
import os

from src.Clientes import XestionCli
from src.ProdServ import ProdServi
from src.SqliteBD import MethodsBD

from gi.overrides.Gdk import Gdk

gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class VentanaPrincipal():
    """Interfaz principal del programa.
                **Métodos:**
                - __init__
                - on_btnClientes_clicked
                - on_btnProdutos_clicked
                - on_btnSalir_clicked
            """

    def __init__(self):
        """
        Inicializa la ventana con la interfaz.
        """

        #CSS para las labels y botones
        css = '''
        
                    label {
                    font: 20px Courier-bold;
                    }
                    button { 
                    background:  #ffcc99;
                    padding: 5px 10px;
                    font: 14px Courier-bold;
                    color: #000000;
                    }
                                        '''
        cssProvider = Gtk.CssProvider()
        cssProvider.load_from_data(bytes(css.encode()))
        screen = Gdk.Screen.get_default()
        styleContext = Gtk.StyleContext()
        styleContext.add_provider_for_screen(screen, cssProvider, Gtk.STYLE_PROVIDER_PRIORITY_USER)

        #Creación tablas BD
        MethodsBD.tablas()

        builder = Gtk.Builder()

        #Asignamos a nuestro builder el archivo de nuestro proyecto Glade
        path = os.path.dirname(os.path.realpath(__file__))
        file = os.path.join(path, 'formEntrada.glade')
        builder.add_from_file(file)

        self.vEntrada = builder.get_object("vEntrada")
        self.vEntrada.set_default_size(220, 150)

        self.btnClientes = builder.get_object("btnClientes")
        self.btnProdutos = builder.get_object("btnProdutos")
        self.btnSalir = builder.get_object("btnSalir")

        #Señales
        self.btnClientes.connect("clicked", self.on_btnClientes_clicked)
        self.btnProdutos.connect("clicked", self.on_btnProdutos_clicked)
        self.btnSalir.connect("clicked", self.on_btnSalir_clicked)
        self.vEntrada.connect("destroy", self.on_btnSalir_clicked)

        self.vEntrada.show_all()


    def on_btnClientes_clicked(self, boton):
         """
                  Metodo para entrar al formulario Xestión de Clientes
                  :param boton: boton
                  :return: No devuelve ningún parámetro.
                  """
         XestionCli.Fiestra().show_all()
         self.vEntrada.set_visible(False)

    def on_btnProdutos_clicked(self, boton):
        """
                 Metodo para entrar al formulario Produtos e Servizos
                 :param boton: boton
                 :return: No devuelve ningún parámetro.
                 """
        ProdServi.Fiestra().show_all()
        self.vEntrada.set_visible(False)

    def on_btnSalir_clicked(self, boton):
        """
                 Metodo para cerrar el programa
                 :param boton: boton
                 :return: No devuelve ningún parámetro.
                 """
        exit(0)
