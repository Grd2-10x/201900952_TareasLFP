import subprocess


scripts = ("scjson.py", "scxml.py","sccsv")
   
procesos = [subprocess.Popen(["python", script]) for script in scripts]

# Esperamos a que todos los subprocesos terminen.
for proceso in procesos:
    proceso.wait()