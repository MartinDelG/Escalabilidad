from ..models import InfoPago,Estudiante

def get_deuda():
    queryset = InfoPago.objects.get(estudiante_id = 1).cobro_total - InfoPago.objects.get(estudiante_id = 1).cantidad_pagada
    return (queryset)
    