from django.shortcuts import render
from candidates.models.Degree import Degree
from candidates.models.CandidateProfile import CandidateProfile

import io
from reportlab.pdfgen import canvas
from django.http import FileResponse, HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def entry_test_application(request):
    context = {}
    context['degrees'] = Degree.objects.all()
    context['current_user'] = CandidateProfile.objects.get(id=request.session['user_id'])
    return render(request, "pages/entrytest/entry_test_application.html", context=context)

def registeration_slip(request):
    return render(request, "pages/entrytest/registeration_slip.html")

def adjust_test_schedule(request):
    return render(request, "pages/entrytest/adjust_test_schedule.html")

def entry_test_result(request):
    return render(request, "pages/entrytest/entry_test_result.html")

def get_challan_pdf(request, name):
    template_src = 'challan.html'

    template = get_template(template_src)
    html  = template.render({'name': name})
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    
    return 'lolz'
