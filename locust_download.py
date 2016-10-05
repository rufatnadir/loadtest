from locust import HttpLocust, TaskSet, task

class MyTaskSet(TaskSet):

    @task(1)
    def download1(self):
        for x in range(0, 250):
            self.client.get("/artifactory/bms-test-snapshot/bens/inputfile1M.%d.jar" % (x))

    @task(1)
    def download2(self):
        for x in range(251, 500):
            self.client.put("/artifactory/bms-test-snapshot/bens/inputfile1M.%d.jar" % (x))

class DownloadUser(HttpLocust):
    task_set = MyTaskSet
