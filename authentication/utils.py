import requests
from .models import MedicalJournal

# def fetch_medical_journals():
#     url = "https://medical-articles-live.p.rapidapi.com/journals/diabetes"
#     headers = {
#         "X-RapidAPI-Key": "e90b3dbbf2msh550bc8c8beed4c5p18fd23jsnb8325cb6ffbe",
#         "X-RapidAPI-Host": "medical-articles-live.p.rapidapi.com"
#     }
#     try :

#         response = requests.get(url, headers=headers)
#         data = response.json()

#         # Save the data to the model
#         for journal in data.get('journals', []):
#             MedicalJournal.objects.create(
#                 title=journal.get('title', ''),
#                 issn=journal.get('issn', ''),
#                 # Add other fields as needed
#             )
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching medical journals: {e}")
#         raise

#     except ValueError as e:
#         print(f"Error decoding JSON: {e}")
#         raise


from django.http import JsonResponse

def fetch_medical_journals(request):
    url = 'https://medical-articles-live.p.rapidapi.com/journals/diabetes'
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data)

