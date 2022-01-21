from os.path import exists

from invoke import task


def file_exist(filename, filepath="."):
    return exists(f"{filepath}/{filename}")


@task(name="delete", help={'filename': "Name of file to be deleted",
                           'filepath': "Absolute path of file directory"})
def delete(c, filename, filepath="."):
    """Deletes a file"""
    if filename and file_exist(filename, filepath):
        try:
            c.run(f" rm  {filepath}/{filename}")
            c.run("echo file deleted")
            # click bash command to create file
        except PermissionError:
            print("Access denied.")
    else:
        print("File does not exist")
