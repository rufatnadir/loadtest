from locust import HttpLocust, TaskSet, task
import random
import os

class UserBehavior(TaskSet):

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        # self.login()

        # self.createfiles()

    # def createfiles(self):
        # global num = random.randrange(1,200)
        # print("creating file %d")
        # with open("output_file%d.bin" , 'wb') as fout:
            # fout.write(os.urandom(1024)) # replace 1024 with size_kb if not unreasonably large

    # @task(1)
    # def dl100M(self):
    #     num=random.randrange(1,4)
    #     self.client.get("/artifactory/bms-test-snapshot/inputfile100M.1.jar")
    #     self.client.get("/artifactory/bms-test-snapshot/inputfile100M.2.jar")
    #     self.client.get("/artifactory/bms-test-snapshot/inputfile100M.3.jar")

    # @task(1)
    # def dl10M(self):
    #     num=random.randrange(1,6)
    #     self.client.get("/artifactory/bms-test-snapshot/inputfile10M.1.jar")
    #     self.client.get("/artifactory/bms-test-snapshot/inputfile10M.2.jar")
    #     self.client.get("/artifactory/bms-test-snapshot/inputfile10M.3.jar")
    #     self.client.get("/artifactory/bms-test-snapshot/inputfile10M.4.jar")
    #     self.client.get("/artifactory/bms-test-snapshot/inputfile10M.5.jar")

    @task(1)
    def dl1M(self):
        num=random.randrange(1,6)
        self.client.get("/artifactory/bms-test-snapshot/inputfile1M.1.jar")
        self.client.get("/artifactory/bms-test-snapshot/inputfile1M.2.jar")
        self.client.get("/artifactory/bms-test-snapshot/inputfile1M.3.jar")
        self.client.get("/artifactory/bms-test-snapshot/inputfile1M.4.jar")
        self.client.get("/artifactory/bms-test-snapshot/inputfile1M.5.jar")

    @task(10)
    def dl100K(self):
        num=random.randrange(1,6)
        self.client.get("/artifactory/bms-test-snapshot/inputfile.100K.1.jar")
        self.client.get("/artifactory/bms-test-snapshot/inputfile.100K.2.jar")
        self.client.get("/artifactory/bms-test-snapshot/inputfile.100K.3.jar")
        self.client.get("/artifactory/bms-test-snapshot/inputfile.100K.4.jar")
        self.client.get("/artifactory/bms-test-snapshot/inputfile.100K.5.jar")

class UploadUser(HttpLocust):
    task_set = UserBehavior
    # min_wait=5000
    # max_wait=9000

# class DownloadUser(HttpLocust):
