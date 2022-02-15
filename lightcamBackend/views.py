from django.http import HttpResponse
import lightcamBackend.external_request as er
import lightcamBackend.email as email


def index(request):
    csv_flag = True
    resource = request.GET.get("resource", "")
    response_content = "Server on"
    if resource == '':
        response_content = "Server onn"
        csv_flag = False
    elif resource == "workflow":
        response_content = er.ExternalRequest.get_workflow()
        csv_flag = False
    elif resource == "timeline":
        response_content = er.ExternalRequest.get_timeline()
    elif resource == "dictionary":
        response_content = er.ExternalRequest.get_dictionary()
    elif resource == "resources":
        response_content = er.ExternalRequest.get_resources()
    elif resource == "email":
        name = request.GET.get("name", "")
        subject = request.GET.get("subject", "")
        email_address = request.GET.get("email", "")
        message = request.GET.get("message", "")
        email.send_feedback(name, subject, email_address, message)
        response_content = "Email sent"
        csv_flag = False
    else:
        csv_flag = False
    response = HttpResponse(response_content)
    response['Access-Control-Allow-Origin'] = '*'
    if csv_flag:
        response['Content-Type'] = "text/csv"
    return response
