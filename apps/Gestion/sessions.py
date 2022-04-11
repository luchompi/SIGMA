class Asignacion:
    def __init__(self,request):
        self.request=request
        self.session=request.session
        asignacion = self.session.get("asignacion")
        if not asignacion:
            self.session["asignacion"]={}
            self.asignacion=self.session["asignacion"]
        else:
            self.asignacion=asignacion

    def add(self,obj):
        id=str(obj.placa)
        if id not in self.asignacion.keys():
            self.asignacion[id]={
            "elemento_id":obj.placa,
            "modelo":obj.modelo.modelo,
            }
        self.save()

    def save(self):
        self.session["asignacion"]=self.asignacion
        self.session.modified=True

    def remove(self,obj):
        id = str(obj.placa)
        if id in self.asignacion:
            del self.asignacion[id]
            self.save()

    def clear(self):
        self.asignacion={}
        self.save()
