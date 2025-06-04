from rest_framework import serializers
from database.models import User, VideoModel, UsageHistory



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data.pop('password'))
        return super().update(instance, validated_data)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Старый пароль неверен.")
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance


class VideoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoModel
        fields = ['videoID', 'initialVideoFile', 'resultVideoFile']

    def create(self, validated_data):
        video = VideoModel.objects.create(
            initialVideoFile=validated_data.get('initialVideoFile', ''),
            resultVideoFile=validated_data.get('resultVideoFile', '')
        )
        return video

    def update(self, instance, validated_data):
        instance.initialVideoFile = validated_data.get('initialVideoFile', instance.initialVideoFile)
        instance.resultVideoFile = validated_data.get('resultVideoFile', instance.resultVideoFile)
        instance.save()
        return instance


class UsageHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UsageHistory
        fields = ['operationID', 'userID', 'videoID', 'status', 'detectionModel', 'trackingModel', 'analysisModel']

    def create(self, validated_data):
        usage = UsageHistory.objects.create(
            userID=validated_data.get('userID', ''),
            detectionModel=validated_data.get('detectionModel', 'Yolo'),
            trackingModel=validated_data.get('trackingModel', 'ByteTrack'),
            analysisModel=validated_data.get('analysisModel', 'I3D'),
            status=validated_data.get('status', 'pending'),
            videoID=None
        )
        return usage

    def update(self, instance, validated_data):
        instance.detectionModel = validated_data.get('detectionModel', instance.detectionModel)
        instance.trackingModel = validated_data.get('trackingModel', instance.trackingModel)
        instance.analysisModel = validated_data.get('analysisModel', instance.analysisModel)
        instance.status = validated_data.get('status', instance.status)
        instance.videoID = validated_data.get('videoID', instance.videoID)
        instance.save()
        return instance
    
