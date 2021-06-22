#!/usr/bin/python
from wsgiref.handlers import CGIHandler
from e_commerce import app

CGIHandler().run(app)