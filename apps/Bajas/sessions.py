class baja:
    def __init__(self,request):
        self.request=request
        self.session=request.session
        baja = self.session.get("baja")
        if not baja:
            self.session["baja"]={}
            self.baja=self.session["baja"]
        else:
            self.baja=baja

    def add(self,queryset):
        id=str(queryset.placa)
        if id not in self.baja.keys():
            self.baja[id]={
            "placa":queryset.placa,
            "referencia":str(queryset.modelo),
            "estado":queryset.estado,
            }
        self.save()

    def save(self):
        self.session["baja"]=self.baja
        self.session.modified=True


    def remove(self,queryset):
        print("Remover")
        id = str(queryset.placa)
        print(id)
        if id in self.baja:
            del self.baja[id]
            self.save()

    def clear(self):
        self.baja={}
        self.save()
