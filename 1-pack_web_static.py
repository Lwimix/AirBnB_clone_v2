from datetime import datetime
from fabric.api import local


def do_pack():
    """Create an archive from web_static folder.
    Returns:
        The path of the created archive if successful, None otherwise.
    """
    local("mkdir -p versions")
    time_created = datetime.now().strftime("%Y%m%d%H%M%S")
    archive = f"web_static_{time_created}.tgz"
    try:
        local(f"tar -cfvz versions/{archive} web_static")
        return f"versions/{archive}"
    except Exception as e:
        print(f"Unable to create archive: {e}")
        return None


if __name__ == "__main__":
    do_pack()
