# import os

# def pre_fork(server, worker):
    
#         print("pre_fork Загрузка переменных выполняется только один раз")
        # os.environ['MY_VARIABLE'] = 'my_value'

# Конфигурация Gunicorn
bind = '0.0.0.0:8000'
workers = 3
worker_class = 'gthread'
worker_tmp_dir = '/dev/shm'
preload_app = True
timeout = 30
loglevel = 'info'
accesslog = '-'
errorlog = '-'
capture_output = True