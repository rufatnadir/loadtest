from locust import HttpLocust, TaskSet, task
import random
import os

class UserBehavior(TaskSet):

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        # self.login()
        self.createfiles()

    def createfiles(self):
        for x in range(0, 500):
            # num=random.randrange(1,500)
            with open("output_file%d.bin" % (x), 'wb') as fout:
                fout.write(os.urandom(1024000))


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
    def upload1(self):
        # post_status = requests.put(url=full_path_in_artifactory, data=file_content)
        for x in range(0, 100):
            with open("/Users/bcourlis/locutus/output_file%d.bin" % (x), mode="rb") as f:
                file_content = f.read()
            # post_status = requests.put(url=full_path_in_artifactory, data=file_content)
                self.client.put("/artifactory/bms-test-snapshot/bens/inputfile1M.%d.jar" % (x), data=file_content)
            # self.client.get("/artifactory/bms-test-snapshot/inputfile1M.1.jar")
            # self.client.get("/artifactory/bms-test-snapshot/inputfile1M.2.jar")
            # self.client.get("/artifactory/bms-test-snapshot/inputfile1M.3.jar")
            # self.client.get("/artifactory/bms-test-snapshot/inputfile1M.4.jar")
            # self.client.get("/artifactory/bms-test-snapshot/inputfile1M.5.jar")
    @task(1)
    def upload2(self):
        for x in range(101, 200):
            with open("/Users/bcourlis/locutus/output_file%d.bin" % (x), mode="rb") as f:
                file_content = f.read()
                self.client.put("/artifactory/bms-test-snapshot/bens/inputfile1M.%d.jar" % (x), data=file_content)

    @task(1)
    def upload3(self):
        for x in range(201, 300):
            with open("/Users/bcourlis/locutus/output_file%d.bin" % (x), mode="rb") as f:
                file_content = f.read()
                self.client.put("/artifactory/bms-test-snapshot/bens/inputfile1M.%d.jar" % (x), data=file_content)

    @task(1)
    def upload4(self):
        for x in range(301, 400):
            with open("/Users/bcourlis/locutus/output_file%d.bin" % (x), mode="rb") as f:
                file_content = f.read()
                self.client.put("/artifactory/bms-test-snapshot/bens/inputfile1M.%d.jar" % (x), data=file_content)

    @task(1)
    def upload5(self):
        for x in range(401, 500):
            with open("/Users/bcourlis/locutus/output_file%d.bin" % (x), mode="rb") as f:
                file_content = f.read()
                self.client.put("/artifactory/bms-test-snapshot/bens/inputfile1M.%d.jar" % (x), data=file_content)


    # @task(10)
    # def dl100K(self):
    #     self.client.get("/artifactory/bms-test-snapshot/inputfile.100K.1.jar")
    #     self.client.get("/artifactory/bms-test-snapshot/inputfile.100K.2.jar")
    #     self.client.get("/artifactory/bms-test-snapshot/inputfile.100K.3.jar")
    #     self.client.get("/artifactory/bms-test-snapshot/inputfile.100K.4.jar")
    #     self.client.get("/artifactory/bms-test-snapshot/inputfile.100K.5.jar")

class UploadUser(HttpLocust):
    task_set = UserBehavior
    # min_wait=5000
    # max_wait=9000

# class DownloadUser(HttpLocust):
