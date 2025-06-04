from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from database.models import User, UsageHistory, VideoModel
from .serializers import UserSerializer, ChangePasswordSerializer, UsageHistorySerializer, VideoModelSerializer

import os
import uuid

from django.conf import settings
from django.core.files.storage import default_storage
import requests



class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.update(request.user, serializer.validated_data)
            return Response({"message": "Пароль успешно изменён"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Выход выполнен"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class GetUserHistoryView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            user_id = request.query_params.get('user_id')
            if request.user.id != int(user_id):
                return Response({"message": "Доступ к данным другого пользователя запрещен"}, 
                                status=status.HTTP_403_FORBIDDEN)
            user = User.objects.get(id=user_id)
            history = UsageHistory.objects.filter(userID=user)
            serializer = UsageHistorySerializer(history, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"message": "Пользователь не найден"}, status=status.HTTP_404_NOT_FOUND)
        

class UploadVideoView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            user_id = request.data.get('user_id')
            if request.user.id != int(user_id):
                return Response({"message": "Доступ к данным другого пользователя запрещен"}, 
                                status=status.HTTP_403_FORBIDDEN)
            
            if 'video' not in request.FILES:
                return Response({"error": "Видеофайл не предоставлен"},
                                status=status.HTTP_400_BAD_REQUEST)

            video_file = request.FILES['video']
            
            file_ext = os.path.splitext(video_file.name)[1]
            filename = f"{uuid.uuid4()}{file_ext}"
            filepath = f"user_{user_id}/videos/{filename}"

            saved_path = default_storage.save(filepath, video_file)
            video_data = {
                'initialVideoFile': saved_path,
                'resultVideoFile': None
            }

            video_serilizer = VideoModelSerializer(data=video_data)
            video_serilizer.is_valid(raise_exception=True)
            video_instance = video_serilizer.save()

            operation_data = {
                'userID': user_id,
                'videoID': video_instance
            }
            operation_serilizer = UsageHistorySerializer(data=operation_data)
            operation_serilizer.is_valid(raise_exception=True)
            operation_instance = operation_serilizer.save()

            return Response(operation_serilizer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class AnalyzeVideoView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            user_id = request.data.get('user_id')
            if request.user.id != int(user_id):
                return Response({"message": "Доступ к данным другого пользователя запрещен"}, 
                                status=status.HTTP_403_FORBIDDEN)
            
            video_id = request.data.get('video_id')
            operation_id = request.data.get('operation_id')
            

        except Exception as e:
            return Response({"error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)           