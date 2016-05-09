import multiprocessing

chdir = '/home/soad/Programming/Projects/web/Django/stepic_web_project'
bind = '0.0.0.0:8080'
workers = multiprocessing.cpu_count() * 2 + 1
