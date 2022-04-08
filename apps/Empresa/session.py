class sede:
    def __init__(self,request):
        self.request=request
        self.session=request.session
        sede = self.session.get("sede")
        if not sede:
            self.session["sede"]={}
            self.sede=self.session["sede"]
        else:
            self.sede=sede

    def add(self,sede):
        id=str(sede.pk)
        if id not in self.sede.keys():
            self.sede[id]={
            "sede_id":sede.id,
            "sede":sede.sede,
            }
        self.save()

    def save(self):
        self.session["sede"]=self.sede
        self.session.modified=True

    def clear(self):
        self.sede={}
        self.save()




class detalle:
    def __init__(self,request):
        self.request=request
        self.session=request.session
        detalle = self.session.get("detalle")
        if not detalle:
            self.session["detalle"]={}
            self.detalle=self.session["detalle"]
        else:
            self.detalle=detalle

    def add(self,detalle):
        id=str(detalle.pk)
        if id not in self.detalle.keys():
            self.detalle[id]={
            "dependencia_id":detalle.id,
            "dependencia":detalle.dependencia,
            }
        self.save()

    def remove(self,detalle):
        id = str(detalle.id)
        if id in self.detalle:
            del self.detalle[id]
            self.save()

    def save(self):
        self.session["detalle"]=self.detalle
        self.session.modified=True

    def clear(self):
        self.detalle={}
        self.save()
