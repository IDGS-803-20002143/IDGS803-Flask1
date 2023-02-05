from flask import Flask, render_template
from flask import request

app=Flask(__name__)

class variables():
    numeroC = 0
    CostoBo = 12.000
    nombre = ""
    Nboletos = 0
    tarjeta = False

    def verificarcompra(self):
        boletosmaximos = self.numeroC * 7
        print(boletosmaximos)
        if self.Nboletos <= boletosmaximos:
         return boletosmaximos
        else:
            return 0

    def descuentos(self):
        res = self.Nboletos * self.CostoBo
        if self.Nboletos > 5:
            res = res - (res * 0.15)
        elif self.Nboletos >= 3 and self.Nboletos <= 5:
            res = res - (res * 0.10)
        if self.tarjeta == True:
            res = res - (res * 0.10)
        return res

        

@app.route("/")
def index():

    return render_template("actividad2cine-index.html")

@app.route("/res", methods=["POST"])
def res():
        nombre = request.form.get("Nombre")
        numeroC = request.form.get("Ncompradores")
        Nboletos = request.form.get("Nboletos")
        tarjeta = request.form.get("tarjetac")
    
        obj = variables()
        obj.nombre = nombre
        obj.numeroC = int(numeroC)
        obj.Nboletos = int(Nboletos)
        if tarjeta == "1":
            obj.tarjeta = True
        else:
            obj.tarjeta = False
    
        maxPermitidos = obj.verificarcompra()

        if maxPermitidos != 0:
            res = obj.descuentos()
            print(res)
            return render_template("actividad2cine-Resultado.html", nombre=nombre, permitidos=maxPermitidos, pedidos =Nboletos, total=res)    
        else:
            boletosPermitidos = int(numeroC) * 7
            return '''
            <h3> No se puede realizar la operacion por que La cantidad maxima de boletos por persona es 7</h3>
            '''
if __name__=="__main__":
    app.run(debug=True)