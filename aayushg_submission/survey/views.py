#Importing Libraries

from rest_framework.decorators import api_view
from rest_framework import views
from rest_framework.views import APIView
from django.http import JsonResponse
from django.http import HttpResponse

from .models import *
import random


class Survey(APIView):

	def get(self, request):

		#parameter fetch
		params = request.GET
		survey_id = params.get('id', None)
		
		#print (type(survey_id))

		try:

			if survey_id != None:
				try:
					survey_id = int(survey_id)
				except:
					output = {"code" : 422, "status": "Unprocessable Entity", "type" : "Survey API", "message" : "Make sure that only integers are passed. Example : id = 1"}
					return JsonResponse(output, safe = False)

				temp = list(Relation_Survey_Qn.objects.filter(rel_sid_id = survey_id).filter(rel_last = 1))


				if len(temp): #not first qn
					q_ids = Relation_Survey_Qn.objects.filter(rel_sid_id = survey_id).exclude(rel_last = 1).values_list("rel_qid_id", flat = True)

				else: #first qn
					q_ids = Relation_Survey_Qn.objects.filter(rel_sid_id = survey_id).values_list("rel_qid_id", flat = True)


				if len(q_ids) != 0:
					try:
						q_id = int(random.choice(q_ids))
						Relation_Survey_Qn.objects.filter(rel_sid_id = survey_id).filter(rel_qid_id = q_id).update(rel_last = 1)
						q_text = Question.objects.get(q_id = q_id).q_text
						q_op_ids = Relation_Question_Opn.objects.filter(rel_qid_id = q_id).values_list("rel_opid_id", flat = True)
						op_texts = Options.objects.filter(op_id__in = q_op_ids).values_list("op_text", flat = True)

						data = {"question" : q_text, "options" : list(op_texts)}
						output = {"code" : 200, "status": "OK", "type" : "Survey API", "message" : "Successful", "output" : data}
						return JsonResponse(output, safe = False)


					except:
						output = {"code" : 500, "status": "Internal Server Error", "type" : "Survey API", "message" : "Error with code. Contact Admin"}
						return JsonResponse(output, safe = False)

				else:
					output = {"code" : 200, "status": "OK", "type" : "Survey API", "message" : "No Qns / Survey Over", "output" : None}

					#restoring the column to prev state
					for i in range(1,Relation_Survey_Qn.objects.all().count()+1):
						Relation_Survey_Qn.objects.filter(rel_id = int(i)).update(rel_last = 0)

					return JsonResponse(output, safe = False)


			else:
				output = {"code" : 422, "status": "Unprocessable Entity", "type" : "Survey API", "message" : "No Survey Id's are passed."}
				return JsonResponse(output, safe = False)


		except:
			output = {"code" : 500, "status": "Internal Server Error", "type" : "Survey API", "message" : "Error with code. Contact Admin"}
			return JsonResponse(output, safe = False)

