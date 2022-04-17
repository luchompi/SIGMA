from django.urls import path as p
from . import views as v

app_name="bajas"

urlpatterns=[
p('nuevo/',v.BajaIndex.as_view(),name="BajaIndex"),
p('add_plc=<pk>',v.add.as_view(),name="add"),
p('remove_plc=<pk>',v.remove.as_view(),name="remove"),
p('cls_session',v.cls.as_view(),name="cls"),
p('done_success',v.done.as_view(),name="done"),
p('',v.index.as_view(),name="index"),
p('details/<pk>',v.detail.as_view(),name="detail"),
]