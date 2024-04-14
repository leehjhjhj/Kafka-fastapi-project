#!/bin/bash
cd /project/src
uvicorn main:app --host 0.0.0.0 --port 8000 &