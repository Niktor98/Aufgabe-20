import platform

print("SYSTEMBERICHT")
print("==============================")
print()

print("System")
print("------------------------------")
print("Betriebssystem:", platform.system())
print("Systemrelease:", platform.release())
print("Rechnername:", platform.node())
print("Maschinenarchitektur:", platform.machine())
print()

print("Python")
print("------------------------------")
print("Python-Version:", platform.python_version())
print("Python-Implementierung:", platform.python_implementation())
print("==============================")
