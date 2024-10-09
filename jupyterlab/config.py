from jupyter_server.auth.identity import PasswordIdentityProvider

c = get_config()  # noqa
c.ServerApp.ip = "0.0.0.0"
c.ServerApp.port = 8888
c.ServerApp.allow_remote_access = True
c.ServerApp.allow_origin = "*"
c.ServerApp.root_dir = "/home/charles/Workspace/notebooks"
c.ServerApp.open_browser = False
# not for production
# c.ServerApp.token = ""
# c.ServerApp.password = ""

# jupyter extension flags
c.ResourceUseDisplay.track_cpu_percent = True
c.ResourceUseDisplay.track_disk_usage = False

# python3 -c "from jupyter_server.auth import passwd; print(passwd('YOUR_PSWD'))"
PasswordIdentityProvider.hashed_password = "HASHED_PSWD"
