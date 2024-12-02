import subprocess

command = ["uvicorn", "app.main:app", "--reload"]

subprocess.run(command)