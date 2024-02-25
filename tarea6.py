
[Unit]
Description=Ejecutar tarea5.py cada 10 segundos

[Service]
ExecStart=/usr/bin/python3 /home/alumno/tarea5.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
