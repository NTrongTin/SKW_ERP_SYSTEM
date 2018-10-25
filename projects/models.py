from django.db import models
from accounts.models import Employee

class ProjectType(models.Model):
    code = models.CharField(max_length=3, unique=True)
    description = models.CharField(max_length=50)
	
	# It will display ProjectType object 0, ProjectType object 1,... if we don't define display string for this object
	# The code below will display "code" for each ProjectType object
    def __str__(self):
        return self.code
		
class ProjectStatus(models.Model):
    status = models.CharField(max_length=3, unique=True)
    description = models.CharField(max_length=20)
    def __str__(self):
        return self.description
		
class Project(models.Model):
    code = models.CharField(max_length=10, unique=True)
    type = models.ForeignKey(ProjectType, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    status = models.ForeignKey(ProjectStatus, on_delete=models.CASCADE, related_name='same_status_projects')
    requester = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='requested_projects')
    task_manager = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='managed_projects')
    task_leader = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leaded_projects')
    estimate = models.IntegerField(default=480)
    worked_time = models.IntegerField(default=0)
    order_date = models.DateField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    completed_date = models.DateField(blank=True, null=True)
    person_in_charge_1 = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.CASCADE, related_name='pic1_projects')
    person_in_charge_2 = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.CASCADE, related_name='pic2_projects')
    person_in_charge_3 = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.CASCADE, related_name='pic3_projects')
    person_in_charge_4 = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.CASCADE, related_name='pic4_projects')
    person_in_charge_5 = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.CASCADE, related_name='pic5_projects')
    tester_1 = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.CASCADE, related_name='tester1_projects')
    tester_2 = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.CASCADE, related_name='tester2_projects')
    tester_3 = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.CASCADE, related_name='tester3_projects')
    tester_4 = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.CASCADE, related_name='tester4_projects')
    tester_5 = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.CASCADE, related_name='tester5_projects')
    def __str__(self):
        return self.title