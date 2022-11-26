#!/bin/bash
rm -frd ./app/__pycache__/
rm -frd ./app/routes/api/__pycache__/
rm -frd ./app/routes/web/__pycache__/
rm -frd ./app/routes/web/forum/__pycache__/
rm -frd ./app/routes/web/wiki/__pycache__/
rm -frd ./app/routes/web/home/__pycache__/
echo Deleted all __pycache__ folders!
