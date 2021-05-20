from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    help = "Commands for building, running, publishing docker image"

    def add_arguments(self, parser):
        cmd = parser.add_mutually_exclusive_group()
        cmd.add_argument('--dev', default=False, action='store_true', help='Start Development Container')
        cmd.add_argument('--build', default=False, action='store_true', help='Build Production Container')
        cmd.add_argument('--start', default=False, action='store_true', help='Start Production Container')
        cmd.add_argument('--stop', default=False, action='store_true', help='Start Production Container')
        cmd.add_argument('--publish', default=False, action='store_true', help='Publish Production Container to Docker Hub')

    def handle(self, *args, **kwargs):
        if kwargs["dev"]: self.__dev()
        elif kwargs["build"]: self.__build()
        elif kwargs["start"]: self.__start()
        elif kwargs["stop"]: self.__stop()
        elif kwargs["publish"]: self.__publish()

    def __dev(self):
        self.stdout.write("Starting Developemnt Container .....")
        os.system('./scripts/dev.sh')
    
    def __build(self):
        self.stdout.write("Building Production Container .....")
        os.system('./scripts/build.sh')
    
    def __start(self):
        self.stdout.write("Starting Production Container .....")
        os.system('./scripts/start.sh')

    def __stop(self):
        self.stdout.write("Stopping Production Container .....")
        os.system('./scripts/stop.sh')
    
    def __publish(self):
        self.stdout.write("Publishing Production Container to Docker Hub .....")
        os.system('./scripts/publish.sh')
    
    
