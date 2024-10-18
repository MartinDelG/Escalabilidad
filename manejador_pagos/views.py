# views.py
from io import BytesIO
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import InfoPago, Estudiante

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=result)
    if pisa_status.err:
        return None
    return result.getvalue()


def generar_recibo(request, id_estudiante):

    estudiante = get_object_or_404(Estudiante, id=id_estudiante)
    
    info_pago = get_object_or_404(InfoPago, estudiante=estudiante)
    
    deuda = info_pago.cobro_total - info_pago.cantidad_pagada
    
    context = {
        'estudiante': estudiante,
        'info_pago': info_pago,
        'deuda': deuda,
    }
    
    pdf = render_to_pdf('recibo.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = f"Recibo_Estudiante_{estudiante.id}.pdf"
        content = f"inline; filename={filename}"
        response['Content-Disposition'] = content
        return response
    else:
        return HttpResponse("Error al generar el PDF", status=400)


def home (request):
    return render(request, 'home.html')
