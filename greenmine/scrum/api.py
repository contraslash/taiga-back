from rest_framework import generics

from greenmine.scrum.serializers import *
from greenmine.scrum.models import *
from greenmine.scrum.permissions import *

class SimpleFilterMixin(object):
    filter_fields = []
    filter_special_fields = []

    _special_values_dict = {
        'true': True,
        'false': False,
        'null': None,
    }

    def get_queryset(self):
        queryset = super(SimpleFilterMixin, self).get_queryset()
        query_params = {}

        for field_name in self.filter_fields:
            if field_name in self.request.QUERY_PARAMS:
                field_data = self.request.QUERY_PARAMS[field_name]
                if field_data in self._special_values_dict:
                    query_params[field_name] = self._special_values_dict[field_data]
                else:
                    query_params[field_name] = field_data

        if query_params:
            queryset = queryset.filter(**query_params)

        return queryset


class ProjectList(generics.ListCreateAPIView):
    model = Project
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return self.model.objects.filter(members=self.request.user)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Project
    serializer_class = ProjectSerializer
    permission_classes = (ProjectDetailPermission,)


class MilestoneList(SimpleFilterMixin, generics.ListCreateAPIView):
    model = Milestone
    serializer_class = MilestoneSerializer
    filter_fields = ('project',)

    def get_queryset(self):
        return self.model.objects.filter(project__members=self.request.user)


class MilestoneDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Milestone
    serializer_class = MilestoneSerializer
    permission_classes = (MilestoneDetailPermission,)


class UserStoryList(SimpleFilterMixin, generics.ListCreateAPIView):
    model = UserStory
    serializer_class = UserStorySerializer
    filter_fields = ('project', 'milestone')

    def get_queryset(self):
        return self.model.objects.filter(project__members=self.request.user)


class UserStoryDetail(generics.RetrieveUpdateDestroyAPIView):
    model = UserStory
    serializer_class = UserStorySerializer


class ChangeList(generics.ListCreateAPIView):
    model = Change
    serializer_class = ChangeSerializer

    def get_queryset(self):
        return self.model.objects.filter(project__members=self.request.user)


class ChangeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Change
    serializer_class = ChangeSerializer


class ChangeAttachmentList(generics.ListCreateAPIView):
    model = ChangeAttachment
    serializer_class = ChangeAttachmentSerializer

    def get_queryset(self):
        return self.model.objects.filter(change__project__members=self.request.user)


class ChangeAttachmentDetail(generics.RetrieveUpdateDestroyAPIView):
    model = ChangeAttachment
    serializer_class = ChangeAttachmentSerializer


class IssueList(generics.ListCreateAPIView):
    model = Issue
    serializer_class = IssueSerializer
    filter_fields = ('project',)

    def get_queryset(self):
        return self.model.objects.filter(project__members=self.request.user)


class IssueDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Issue
    serializer_class = IssueSerializer


class TaskList(generics.ListCreateAPIView):
    model = Task
    serializer_class = TaskSerializer
    filter_fields = ('user_story', 'milestone', 'project')

    def get_queryset(self):
        return self.model.objects.filter(project__members=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Task
    serializer_class = TaskSerializer


class SeverityList(generics.ListCreateAPIView):
    model = Severity
    serializer_class = SeveritySerializer
    filter_fields = ('project',)

    def get_queryset(self):
        return self.model.objects.filter(project__members=self.request.user)


class SeverityDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Severity
    serializer_class = SeveritySerializer


class IssueStatusList(generics.ListCreateAPIView):
    model = IssueStatus
    serializer_class = IssueStatusSerializer
    filter_fields = ('project',)

    def get_queryset(self):
        return self.model.objects.filter(project__members=self.request.user)


class IssueStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    model = IssueStatus
    serializer_class = IssueStatusSerializer


class TaskStatusList(SimpleFilterMixin, generics.ListCreateAPIView):
    model = TaskStatus
    serializer_class = TaskStatusSerializer
    filter_fields = ('project',)

    def get_queryset(self):
        return self.model.objects.filter(project__members=self.request.user)


class TaskStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    model = TaskStatus
    serializer_class = TaskStatusSerializer


class UserStoryStatusList(generics.ListCreateAPIView):
    model = UserStoryStatus
    serializer_class = UserStoryStatusSerializer
    filter_fields = ('project',)

    def get_queryset(self):
        return self.model.objects.filter(project__members=self.request.user)


class UserStoryStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    model = UserStoryStatus
    serializer_class = UserStoryStatusSerializer


class PriorityList(generics.ListCreateAPIView):
    model = Priority
    serializer_class = PrioritySerializer
    filter_fields = ('project',)

    def get_queryset(self):
        return self.model.objects.filter(project__members=self.request.user)


class PriorityDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Priority
    serializer_class = PrioritySerializer


class IssueTypeList(generics.ListCreateAPIView):
    model = IssueType
    serializer_class = IssueTypeSerializer
    filter_fields = ('project',)

    def get_queryset(self):
        return self.model.objects.filter(project__members=self.request.user)


class IssueTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = IssueType
    serializer_class = IssueTypeSerializer


class PointsList(generics.ListCreateAPIView):
    model = Points
    serializer_class = PointsSerializer
    filter_fields = ('project',)

    def get_queryset(self):
        return self.model.objects.filter(project__members=self.request.user)


class PointsDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Points
    serializer_class = PointsSerializer