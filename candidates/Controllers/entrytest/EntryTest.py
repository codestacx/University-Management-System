from django.shortcuts import render
from candidates.models.User import User
from candidates.models.Degree import Degree
from candidates.models.CandidateProfile import CandidateProfile
from candidates.models.AppliedTestCandidate import AppliedTestCandidate

import io
from reportlab.pdfgen import canvas
from django.http import FileResponse, HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def entry_test_application(request):
    if request.method == 'POST':
        # only challan copy uploaded
        if request.FILES:
            candidate_application = AppliedTestCandidate.objects.create(
                candidate=User.objects.get(id=request.session['user_id']),
                paid_challan_copy=request.FILES['paid-challan-copy']
            )

            return HttpResponse(candidate_application.pk)
        # form submitted excluding challan copy
        else:
            if request.POST['verification_status'] == 'on':
                candidate_application = AppliedTestCandidate.objects.get(id=request.session['user_id'])
                candidate_application.degree = Degree.objects.get(id=request.POST['degree'])
                candidate_application.save()

                return HttpResponse('success')
            else:
                return HttpResponse('failed')
    else:
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
    template_src = 'pdf_templates/challan.html'

    template = get_template(template_src)
    html  = template.render({'name': name})
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    
    return 'lolz'
