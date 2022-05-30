from django.shortcuts import render, HttpResponse
from .models import applicant, meeting

# Create your views here.
def HomePg(request):
	return render(request, 'index.html')

def VerifyParticipant(request):
	phone_no = request.POST["phone_no"]
	rollno = request.POST["rollno"]
	applicants = applicant.objects.all()
	exists = False 
	course = ''
	for i in applicants:
		if i.rollno == int(rollno):
			if i.phone_no == int(phone_no):
				exists = True
				i.no_of_logins+=1
				i.save()
				course = i.course
				break
	if(exists):
		link = meeting.objects.get(name=course).link
		return render(request, 'successpg.html', {'course': course, 'link': link})
	else:
		return HttpResponse("Wrong credentials. Go back and try again")
