from invoke import Collection, task
from delete import delete


@task(name="hello")
def hello(c):
    """Hello"""
    c.run("Hello World")


# Create a Namespace to load tasks from multiple files into a single namespace
namespace = Collection(delete, hello)
