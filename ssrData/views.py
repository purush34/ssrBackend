from django.shortcuts import render
from django.http import JsonResponse
from .models import Project,teamDetails,postLikes
from .serializers import projectSerializer,teamDetailsSerializer,postLikesCount
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

# class ssrApiView(APIView):
#     # add permission to check if user is authenticated
#     permission_classes = [permissions.IsAuthenticated]
@api_view(['GET'])
def ssrApiView(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = projectSerializer(projects, many=True)
        return JsonResponse({"Projects":serializer.data})
    elif request.method == 'POST':
        serializer = projectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"Message":"Project posted successfully"})
        return JsonResponse({"Error":serializer.errors})

def ssrYear(request, year):
    projects = Project.objects.filter(year=year)
    serializer = projectSerializer(projects, many=True)
    return JsonResponse({"Projects":serializer.data})

def ssrCategory(request, category):
    projects = Project.objects.filter(category=category)
    serializer = projectSerializer(projects, many=True)
    return JsonResponse({"Projects":serializer.data})

def getCatories(request):
    try:
        categories = Project.objects.values_list('category', flat=True).distinct()
        return JsonResponse({"Categories":list(categories)})
    except:
        return JsonResponse({"Error":"No projects found"})

def getYears(request):
    try:
        years = Project.objects.values_list('year', flat=True).distinct()
        return JsonResponse({"Years":list(years)})
    except:
        return JsonResponse({"Error":"No projects found"})


def ssrProjectId(request, projectId):
    try :
        project = Project.objects.get(projectId=projectId)
        print(project)
    except Project.DoesNotExist:
        return JsonResponse({"Error":"Project not found"})
    serializer = projectSerializer(project)
    return JsonResponse({"Project":serializer.data})

def teamDetailsapi(request, teamId):
    try :
        project = teamDetails.objects.filter(projectId=teamId)
    except teamDetails.DoesNotExist:
        return JsonResponse({"Error":"Team details not found"})
    try:
        serializer = teamDetailsSerializer(project,many=True)
        return JsonResponse({"Team Details":serializer.data})
    except:
        return JsonResponse({"Error":"Team details not found"})

def teams(request):
    try :
        project = teamDetails.objects.all()
        # print teamDetails columns in console
    except teamDetails.DoesNotExist:
        return JsonResponse({"Error":"Team details not found"})
    try:
        serializer = teamDetailsSerializer(project,many=True)
        return JsonResponse({"Team Details":serializer.data})
    except: 
        return JsonResponse({"Error":"Team details not found"})




